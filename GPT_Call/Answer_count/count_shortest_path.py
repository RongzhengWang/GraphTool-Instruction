import json
import networkx as nx

# 读取JSON文件
# /home/data2t2/wrz/Graph Tools/GPT_Call/old/apicall_gpt4o_shortest.json
with open('/home/data2t2/wrz/Graph Tools/GPT_Call/All_type_mission_directed/twice/shortest_path/apicall_gpt3.5.json', 'r') as file:
    data = json.load(file)

total_count = 0
correct_count = 0

# 遍历JSON对象
for item in data:
    prompt = item.get('prompt')
    output = item.get('output')
    answer = item.get('answer')
    
    # 检查是否存在 'output' 键
    if not output:
        print("Missing 'output' key in item:", item)
        continue
    
    # 提取图数据和路径信息
    for choice in output['choices']:
        tool_call = choice['message']['tool_calls'][0]
        arguments = json.loads(tool_call['function']['arguments'])
        
        try:
            edges = eval(arguments['G'])
        except Exception as e:
            print(f"Error evaluating edges: {e}")
            print(f"arguments['G']: {arguments['G']}")
            continue
        
        path_source = arguments['path_source']
        path_target = arguments['path_target']
        
        # 创建无向图
        G = nx.DiGraph()
        G.add_edges_from(edges)
        
        # 计算最短路径
        try:
            shortest_path_length = nx.shortest_path_length(G, source=path_source, target=path_target, weight='weight')
        except nx.NetworkXNoPath:
            print(f"No path between {path_source} and {path_target}")
            continue
        
        total_count += 1
        
        # 比对结果
        if shortest_path_length == answer:
            correct_count += 1
        else:
            print(f"Incorrect: {shortest_path_length} != {answer}")
            print(f"Item: {item}")

print(f"Correct results: {correct_count} out of {total_count}")


# import json
# import networkx as nx
# import re

# # 读取 JSON 文件
# with open('/home/data2t2/wrz/Graph Tools/GPT_Call/All_type_mission_directed/twice/shortest_path/apicall_gpt3.5.json', 'r') as file:
#     data = json.load(file)

# total_count = 0
# correct_count = 0
# mismatch_count = 0

# # 正则表达式模式，用于提取边信息
# edges_pattern = r"The edges are: (\[\(.*?\{.*?\}\)\])"

# # 遍历 JSON 对象
# for item in data:
#     prompt = item.get('prompt')
#     output = item.get('output')
#     answer = item.get('answer')
    
#     # 检查是否存在 'output' 键
#     if not output:
#         print("Missing 'output' key in item:", item)
#         continue
    
#     # 提取 prompt 中的图数据
#     prompt_match = re.search(edges_pattern, prompt)
#     if not prompt_match:
#         print(f"Could not extract edges from prompt: {prompt}")
#         continue

#     try:
#         edges_from_prompt = eval(prompt_match.group(1))
#     except Exception as e:
#         # print(f"Error processing edges from prompt: {e}")
#         continue

#     # 提取 output 中的图数据和路径信息
#     for choice in output['choices']:
#         tool_call = choice['message']['tool_calls'][0]
#         arguments = json.loads(tool_call['function']['arguments'])
        
#         try:
#             edges_from_output = eval(arguments['G'])
#         except Exception as e:
#             # print(f"Error evaluating edges: {e}")
#             # print(f"arguments['G']: {arguments['G']}")
#             continue
        
#         path_source_output = arguments['path_source']
#         path_target_output = arguments['path_target']
        
#         # 比较 prompt 和 output 中的图信息是否一致
#         if edges_from_prompt != edges_from_output:
#             mismatch_count += 1
#             print(f"Mismatch {mismatch_count}:")
#             print(f"edges_from_prompt: {edges_from_prompt}")
#             print(f"edges_from_output: {edges_from_output}")
#             continue

#         # 创建有向图
#         G = nx.DiGraph()
#         G.add_edges_from(edges_from_output)
        
#         # 计算最短路径
#         try:
#             shortest_path_length = nx.shortest_path_length(G, source=path_source_output, target=path_target_output, weight='weight')
#         except nx.NetworkXNoPath:
#             print(f"No path between {path_source_output} and {path_target_output}")
#             continue
        
#         total_count += 1
        
#         # 比对结果
#         if shortest_path_length == answer:
#             correct_count += 1
#         else:
#             print(f"Incorrect: {shortest_path_length} != {answer}")
#             print(f"Item: {item}")

# print(f"Correct results: {correct_count} out of {total_count}")
# print(f"Total mismatches: {mismatch_count}")
