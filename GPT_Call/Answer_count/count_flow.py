import json
import networkx as nx

# 读取JSON文件
with open('/home/data2t2/wrz/Graph Tools/GPT_Call/All_type_mission_directed/twice/maximum_flow/apicall_gpt3.5.json', 'r') as file:
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
        
        path_source = arguments['source_node']
        path_target = arguments['sink_node']
        
        # 创建有向图，使用最大流问题需要有向图
        G = nx.DiGraph()
        for u, v, data in edges:
            G.add_edge(u, v, capacity=data.get('capacity', 1))  # 假设边有权重，如果没有默认权重为1
        
        # 计算最大流
        try:
            flow_value, flow_dict = nx.maximum_flow(G, path_source, path_target)
        except nx.NetworkXError as e:
            print(f"NetworkX Error: {e}")
            continue
        
        total_count += 1
        
        # 比对结果，假定 answer 存储的是最大流值
        if flow_value == answer:
            correct_count += 1
        else:
            print(f"Incorrect: {flow_value} != {answer}")
            print(f"Item: {item}")

print(f"Correct results: {correct_count} out of {total_count}")
