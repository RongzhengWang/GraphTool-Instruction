import json
import re

# 读取JSON文件
file_path = "/home/data2t2/wrz/Graph Tools/GLM_Call/All_type_mission_directed/once/cycle_check_graphExistance/GLM4.json"
with open(file_path, 'r') as file:
    data = json.load(file)

# 正则表达式模式，用于提取prompt中的边列表
edge_pattern = r"The edges are: \[(.*?)\]"

# 遍历JSON文件中的每条数据
results = []
for index, entry in enumerate(data):
    prompt = entry['prompt']
    if 'output' in entry:
        output = entry['output']
        if 'choices' in output:
            choices = output['choices']
            for choice in choices:
                tool_calls = choice['message']['tool_calls']
                for call in tool_calls:
                    # 提取prompt中的边列表
                    match = re.search(edge_pattern, prompt)
                    if match:
                        edges_string_prompt = match.group(1)
                        edges_prompt = eval(f"[{edges_string_prompt}]")  # 将字符串转换为列表
                    else:
                        edges_prompt = []

                    # 提取JSON中的图边列表
                    arguments = json.loads(call['function']['arguments'])
                    edges_string_json = arguments['G']
                    edges_json = eval(edges_string_json)  # 将字符串转换为列表

                    # 比对prompt和JSON中的边列表
                    edges_match = edges_prompt == edges_json
                    results.append(edges_match)

# 输出结果
for index, result in enumerate(results):
    print(f"Graph {index + 1}: {result}")
