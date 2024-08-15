import transformers
import torch
import os
import json
import re
from tqdm import tqdm

# 设置 CUDA 设备
os.environ["CUDA_VISIBLE_DEVICES"] = "8,9"
model_id = "/home/data2t2/wrz/LLaMA/llama3_Graph_LLaMA"

# 初始化生成文本的 pipeline
pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

# 读取 prompt 模板
with open('/home/data2t2/wrz/Graph Tools/prompt_template/prompt3.txt', 'r', encoding='utf-8') as file:
    prompt = file.read()

# 检查并读取现有的 JSON 文件内容
final_answer_file_path = '/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/twice/degree_graphCount/ans_5ques.json'
if os.path.exists(final_answer_file_path):
    with open(final_answer_file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
else:
    data = []

# 读取所有任务文件
with open('/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/twice/degree_graphCount/degree_graphCount_undirected_random100_5ques.json', 'r', encoding='utf-8') as file:
    files = json.load(file)

print(len(files))

# 读取 API_name 到模板内容的映射
with open('/home/data2t2/wrz/Graph Tools/prompt_template/api_name_to_template.json', 'r', encoding='utf-8') as file:
    api_name_to_template = json.load(file)

# 定义 API_name 列表
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

# 遍历每个对象
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
        max_new_tokens=4096,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.7,
        top_p=1,
    )
    firstanswer = outputs[0]["generated_text"][-1]['content']
    print(firstanswer)

    # 尝试提取 API_name 的值，兼容两种形式
    api_name_match = re.search(r"API_name:\s*(\w+|\n\s*\w+)", firstanswer)
    if api_name_match:
        api_name = api_name_match.group(1).strip()
    else:
        # 如果正则表达式匹配失败，则在列表中查找
        api_name = None
        for name in api_name_list:
            if name in firstanswer:
                api_name = name
                break
        if api_name is None:
            api_name = "unknown"

    # 根据 API_name 获取对应的 prompt2_template
    prompt2_template = api_name_to_template.get(api_name)

    # 构建新的 prompt2
    prompt2 = f"You have chosen an API:{api_name}\n{prompt2_template}"

    messages.append({'role': "assistant", "content": firstanswer})
    messages.append({"role": "user", "content": prompt2})

    outputs = pipeline(
        messages,
        max_new_tokens=4096,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.7,
        top_p=1,
    )
    secondanswer = outputs[0]["generated_text"][-1]['content']

    data.append({
        'prompt': message,
        'answer': answer,
        'firstanswer': firstanswer,
        'api_name':api_name,
        'prompt2': prompt2,
        'secondanswer': secondanswer,
        'description':obj['description']
    })

    # 将更新后的内容写回文件
    with open(final_answer_file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    print("JSON 文件已更新。")
