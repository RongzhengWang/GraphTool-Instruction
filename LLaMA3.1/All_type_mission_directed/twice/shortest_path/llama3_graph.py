import transformers
import torch
import os
import json
import re
from tqdm import tqdm

# 设置 CUDA 设备
os.environ["CUDA_VISIBLE_DEVICES"] = "10,11"
model_id = "/home/data2t2/wrz/LLaMA/Llama-3.1-8B-Instruct"

# 初始化生成文本的 pipeline
pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

# 读取 prompt 模板
with open('/home/data2t2/wrz/Graph Tools/prompt_template/prompt_graph3.txt', 'r', encoding='utf-8') as file:
    prompt = file.read()

# 检查并读取现有的 JSON 文件内容
final_answer_file_path = '/home/data2t2/wrz/Graph Tools/1LLaMA3.1/All_type_mission_directed/twice/shortest_path/ans_graph.json'
if os.path.exists(final_answer_file_path):
    with open(final_answer_file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
else:
    data = []

# 读取所有任务文件
with open('/home/data2t2/wrz/Graph Tools/1LLaMA3.1/All_type_mission_directed/twice/is_path_graphExistance/is_path_graphExistance_directed_random100_5ques.json', 'r', encoding='utf-8') as file:
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
        max_new_tokens=4096,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.7,
        top_p=1,
    )
    firstanswer = outputs[0]["generated_text"][-1]['content']
    print(firstanswer)

    
    data.append({
        'prompt': message,
        'firstanswer': firstanswer,
    })

    # 将更新后的内容写回文件
    with open(final_answer_file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    print("JSON 文件已更新。")
