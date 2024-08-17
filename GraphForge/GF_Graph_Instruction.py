import transformers
import torch
import os
import json
import re
from tqdm import tqdm
import argparse

def main(args):
    # 设置 CUDA 设备
    os.environ["CUDA_VISIBLE_DEVICES"] = args.cuda_devices
    model_path = args.model_path

    # 初始化生成文本的 pipeline
    pipeline = transformers.pipeline(
        "text-generation",
        model=model_path,
        model_kwargs={"torch_dtype": torch.bfloat16},
        device_map="auto",
    )

    # 读取 prompt 模板
    with open(args.instruction_path, 'r', encoding='utf-8') as file:
        prompt = file.read()

    # 检查并读取现有的 JSON 文件内容
    if os.path.exists(args.output_path):
        with open(args.output_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # 读取所有任务文件
    with open(args.input_path, 'r', encoding='utf-8') as file:
        files = json.load(file)

    print(len(files))

    # 遍历每个对象
    for obj in tqdm(files):
        message = obj['prompt']
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

        data.append({
            'prompt': message,
            'firstanswer': firstanswer,
        })

        # 将更新后的内容写回文件
        with open(args.output_path, 'w') as file:
            json.dump(data, file, indent=4)

        print("JSON 文件已更新。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate text using a pre-trained model.")
    parser.add_argument('--cuda_devices', type=str, required=True, help='CUDA devices to use.')
    parser.add_argument('--model_path', type=str, required=True, help='Model ID or path to the pre-trained model.')
    parser.add_argument('--instruction_path', type=str, required=True, help='Path to the instruction template file.')
    parser.add_argument('--output_path', type=str, required=True, help='Path to the final answer JSON file.')
    parser.add_argument('--input_path', type=str, required=True, help='Path to the input files JSON.')
    parser.add_argument('--max_new_tokens', type=int, required=True, help='Maximum number of new tokens to generate.')
    parser.add_argument('--temperature', type=float, required=True, help='Sampling temperature.')
    parser.add_argument('--top_p', type=float, required=True, help='Nucleus sampling probability.')

    args = parser.parse_args()
    main(args)



#python generate_text.py --cuda_devices "6,7" --model_path "/home/data2t2/wrz/LLaMA/llama3_GLandEX" --instruction_path "/home/data2t2/wrz/Graph Tools/prompt_template/prompt_graph3.txt" --output_path "/home/data2t2/wrz/GraphTool-Instruction/GraphForge_test_WL/Cycle_Detection/Di/ans_graph_Di.json" --input_path "/home/data2t2/wrz/GraphTool-Instruction/GraphForge_test_WL/Cycle_Detection/Di/cycle_Di.json" --max_new_tokens 4096 --temperature 0.7 --top_p 1
