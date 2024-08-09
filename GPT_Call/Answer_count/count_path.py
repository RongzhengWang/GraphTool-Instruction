import json
import networkx as nx

# 读取JSON文件
with open('/home/data2t2/wrz/Graph Tools/GPT_Call/All_type_mission_directed/twice/is_path_graphExistance/apicall_gpt3.5.json', 'r') as file:
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
        
        try:
            arguments = json.loads(tool_call['function']['arguments'])
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            print(f"Tool Call arguments: {tool_call['function']['arguments']}")
            continue
        
        try:
            edges = eval(arguments['G'])
        except Exception as e:
            print(f"Error evaluating edges: {e}")
            print(f"arguments['G']: {arguments['G']}")
            continue
        
        path_source = arguments.get('path_source')
        path_target = arguments.get('path_target')
        
        if path_source is None or path_target is None:
            print(f"Missing path_source or path_target in arguments: {arguments}")
            continue
        
        # 创建无向图
        G = nx.DiGraph()
        
        try:
            G.add_edges_from(edges)
        except nx.NetworkXError as e:
            print(f"NetworkX Error: {e}")
            continue
        
        # 检查两个节点之间是否存在路径
        path_exists = nx.has_path(G, source=path_source, target=path_target)
        
        total_count += 1
        
        # 比对结果，假定 answer存储的是布尔值，表示是否存在路径
        if path_exists == answer:
            correct_count += 1
        else:
            print(f"Incorrect: {path_exists} != {answer}")
            print(f"Item: {item}")

print(f"Correct results: {correct_count} out of {total_count}")