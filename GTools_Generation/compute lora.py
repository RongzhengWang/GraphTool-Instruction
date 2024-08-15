# import json
# import re

# def extract_api_input(json_file_path):
#     # 读取 JSON 文件
#     with open(json_file_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)

#     # 如果数据是列表,遍历每个项目;如果是单个对象,将其放入列表中
#     if isinstance(data, list):
#         json_objects = data
#     else:
#         json_objects = [data]

#     prompt_api_pairs = []

#     for obj in json_objects:
#         prompt = obj.get('prompt', 'No prompt found')
        
#         if 'secondanswer' in obj and 'content' in obj['secondanswer']:
#             content = obj['secondanswer']['content']
#             # 使用正则表达式查找 API_Input，只提取括号内的内容
#             match = re.search(r'API_Input:\s*(\([^)]+\))', content)
#             if match:
#                 api_input = match.group(1).strip()
#                 prompt_api_pairs.append({"prompt": prompt, "api_input": api_input})
#             else:
#                 prompt_api_pairs.append({"prompt": prompt, "api_input": 'No API_Input found'})
#         else:
#             prompt_api_pairs.append({"prompt": prompt, "api_input": 'No API_Input found'})

#     return prompt_api_pairs

# # 使用函数
# input_json_file_path = '/home/data2t2/wrz/Graph Tools/All_type_mission_directed/is_path_graphExistance/ans_5ques_5k.json'
# output_json_file_path = '/home/data2t2/wrz/Graph Tools/All_type_mission_directed/is_path_graphExistance/extracted_ans_5ques_5k.json'

# extracted_pairs = extract_api_input(input_json_file_path)

# # 将结果保存到新的 JSON 文件
# with open(output_json_file_path, 'w', encoding='utf-8') as outfile:
#     json.dump(extracted_pairs, outfile, ensure_ascii=False, indent=2)

# print(f"Results have been saved to {output_json_file_path}")

# # 打印提取的 prompt 和 API_Input 对（可选，用于验证）
# for i, pair in enumerate(extracted_pairs, 1):
#     print(f"Pair {i}:")
#     print(f"Prompt: {pair['prompt']}")
#     print(f"API_Input: {pair['api_input']}")
#     print()  # 添加一个空行以提高可读性

import json
import re

def extract_api_input(json_file_path):
    # 读取 JSON 文件
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 如果数据是列表,遍历每个项目;如果是单个对象,将其放入列表中
    if isinstance(data, list):
        json_objects = data
    else:
        json_objects = [data]

    prompt_api_pairs = []

    for obj in json_objects:
        prompt = obj.get('prompt', 'No prompt found')
        prompt2 = obj.get('prompt2', 'No prompt2 found')
        firstanswer_content = obj.get('firstanswer', 'No firstanswer content found')
        secondanswer_content = obj.get('secondanswer', 'No secondanswer content found')
        content = obj['secondanswer']
        # 使用正则表达式查找 API_Input，只提取括号内的内容
        match = re.search(r'API_Input:\s*(\([^)]+\))', content)
        if match:
            api_input = match.group(1).strip()
            prompt_api_pairs.append({
                "prompt": prompt,
                "api_input": api_input,
                "firstanswer_content": firstanswer_content,
                "secondanswer_content": secondanswer_content,
                "prompt2": prompt2
            })
        else:
            prompt_api_pairs.append({
                "prompt": prompt,
                "api_input": 'No API_Input found',
                "firstanswer_content": firstanswer_content,
                "secondanswer_content": secondanswer_content,
                "prompt2": prompt2
            })

    return prompt_api_pairs

# 使用函数
# compute 先使用，指定ans文件以及输出文件
input_json_file_path = '/home/data2t2/wrz/Graph Tools/All_type_mission_directed/is_edge_graphExistance/ans_5ques_5k_lora.json'
output_json_file_path = '/home/data2t2/wrz/Graph Tools/All_type_mission_directed/is_edge_graphExistance/extracted_ans_5ques_5k_lora.json'

extracted_pairs = extract_api_input(input_json_file_path)

# 将结果保存到新的 JSON 文件
with open(output_json_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(extracted_pairs, outfile, ensure_ascii=False, indent=2)

print(f"Results have been saved to {output_json_file_path}")

# 打印提取的 prompt 和 API_Input 对（可选，用于验证）
for i, pair in enumerate(extracted_pairs, 1):
    print(f"Pair {i}:")
    print(f"Prompt: {pair['prompt']}")
    print(f"API_Input: {pair['api_input']}")
    print(f"First Answer Content: {pair['firstanswer_content']}")
    print(f"Second Answer Content: {pair['secondanswer_content']}")
    print(f"Prompt2: {pair['prompt2']}")
    print()  # 添加一个空行以提高可读性
