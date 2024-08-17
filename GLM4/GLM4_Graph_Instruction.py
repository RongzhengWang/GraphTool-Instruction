import transformers
import torch
import os
import json
import re
from tqdm import tqdm
import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer

def main(args):
    os.environ["CUDA_VISIBLE_DEVICES"] = args.cuda_devices
    device = "cuda"

    tokenizer = AutoTokenizer.from_pretrained(args.tokenizer_path, trust_remote_code=True)

    # Read the prompt template
    with open(args.instruction_path, 'r', encoding='utf-8') as file:
        prompt = file.read()

    # Check and read the existing JSON file content
    if os.path.exists(args.output_path):
        with open(args.output_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Read all task files
    with open(args.input_path, 'r', encoding='utf-8') as file:
        files = json.load(file)

    print(len(files))

    # Iterate over each object
    for obj in tqdm(files):
        message = obj['prompt']
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": message}
        ]

        inputs = tokenizer.apply_chat_template(messages,
                                               add_generation_prompt=True,
                                               tokenize=True,
                                               return_tensors="pt",
                                               return_dict=True)

        inputs = inputs.to(device)
        model = AutoModelForCausalLM.from_pretrained(
            args.model_path,
            torch_dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
            trust_remote_code=True
        ).to(device).eval()

        gen_kwargs = {"max_length": args.max_new_tokens, "do_sample": True, 'top_k': args.top_k, 'temperature': args.temperature}
        with torch.no_grad():
            outputs = model.generate(**inputs, **gen_kwargs)
            outputs = outputs[:, inputs['input_ids'].shape[1]:]
            firstanswer = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print(firstanswer)

        data.append({
            'prompt': message,
            'firstanswer': firstanswer,
        })

        # Write the updated content back to the file
        with open(args.output_path, 'w') as file:
            json.dump(data, file, indent=4)

        print("JSON file updated.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate text using a pre-trained model.")
    parser.add_argument('--cuda_devices', type=str, required=True, help='CUDA devices to use.')
    parser.add_argument('--model_path', type=str, required=True, help='Model ID or path to the pre-trained model.')
    parser.add_argument('--tokenizer_path', type=str, required=True, help='Path to the tokenizer.')
    parser.add_argument('--instruction_path', type=str, required=True, help='Path to the instruction template file.')
    parser.add_argument('--output_path', type=str, required=True, help='Path to the final answer JSON file.')
    parser.add_argument('--input_path', type=str, required=True, help='Path to the input files JSON.')
    parser.add_argument('--max_new_tokens', type=int, required=True, help='Maximum number of new tokens to generate.')
    parser.add_argument('--temperature', type=float, required=True, help='Sampling temperature.')
    parser.add_argument('--top_k', type=int, required=True, help='Top-k sampling parameter.')

    args = parser.parse_args()
    main(args)
