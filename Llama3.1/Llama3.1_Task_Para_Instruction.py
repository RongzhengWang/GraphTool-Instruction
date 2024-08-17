import transformers
import torch
import os
import json
import re
from tqdm import tqdm
import argparse

def main(args):
    os.environ["CUDA_VISIBLE_DEVICES"] = args.cuda_devices
    model_id = args.model_id

    pipeline = transformers.pipeline(
        "text-generation",
        model=model_id,
        model_kwargs={"torch_dtype": torch.bfloat16},
        device_map="auto",
    )

    with open(args.prompt_path, 'r', encoding='utf-8') as file:
        prompt = file.read()

    if os.path.exists(args.final_answer_file_path):
        with open(args.final_answer_file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    with open(args.files_path, 'r', encoding='utf-8') as file:
        files = json.load(file)

    print(len(files))

    with open(args.api_name_to_template_path, 'r', encoding='utf-8') as file:
        api_name_to_template = json.load(file)

    api_name_list = [
        'is_node_graphExistance', 
        'is_path_graphExistance', 
        'is_edge_graphExistance', 
        'cycle_check_graphExistance', 
        'number_of_edges_graphCount', 
        'degree_graphCount', 
        'number_of_nodes_graphCount', 
        'shortest_path', 
        'maximum_triangle_sum', 
        'maximum_flow', 
        'topological_sort'
    ]

    for obj in tqdm(files):
        message = obj['prompt']
        answer = obj['answer']
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": message}
        ]

        terminators = [
            pipeline.tokenizer.eos_token_id,
            pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        outputs = pipeline(
            messages,
            max_new_tokens=args.max_new_tokens,
            eos_token_id=terminators,
            do_sample=True,
            temperature=args.temperature,
            top_p=args.top_p,
        )
        firstanswer = outputs[0]["generated_text"][-1]['content']
        print(firstanswer)

        api_name_match = re.search(r"API_name:\s*(\w+|\n\s*\w+)", firstanswer)
        if api_name_match:
            api_name = api_name_match.group(1).strip()
        else:
            api_name = None
            for name in api_name_list:
                if name in firstanswer:
                    api_name = name
                    break
            if api_name is None:
                api_name = "unknown"

        prompt2_template = api_name_to_template.get(api_name)

        prompt2 = f"You have chosen an API:{api_name}\n{prompt2_template}"

        messages.append({'role': "assistant", "content": firstanswer})
        messages.append({"role": "user", "content": prompt2})

        outputs = pipeline(
            messages,
            max_new_tokens=args.max_new_tokens,
            eos_token_id=terminators,
            do_sample=True,
            temperature=args.temperature,
            top_p=args.top_p,
        )
        secondanswer = outputs[0]["generated_text"][-1]['content']

        data.append({
            'prompt': message,
            'answer': answer,
            'firstanswer': firstanswer,
            'api_name': api_name,
            'prompt2': prompt2,
            'secondanswer': secondanswer,
            'description': obj['description']
        })

        with open(args.final_answer_file_path, 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate text using a pre-trained model.")
    parser.add_argument('--cuda_devices', type=str, required=True, help='CUDA devices to use.')
    parser.add_argument('--model_id', type=str, required=True, help='Model ID or path to the pre-trained model.')
    parser.add_argument('--prompt_path', type=str, required=True, help='Path to the prompt template file.')
    parser.add_argument('--final_answer_file_path', type=str, required=True, help='Path to the final answer JSON file.')
    parser.add_argument('--files_path', type=str, required=True, help='Path to the input files JSON.')
    parser.add_argument('--api_name_to_template_path', type=str, required=True, help='Path to the API name to template mapping JSON file.')
    parser.add_argument('--max_new_tokens', type=int, required=True, help='Maximum number of new tokens to generate.')
    parser.add_argument('--temperature', type=float, required=True, help='Sampling temperature.')
    parser.add_argument('--top_p', type=float, required=True, help='Nucleus sampling probability.')

    args = parser.parse_args()
    main(args)


