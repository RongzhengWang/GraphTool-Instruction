import json
import networkx as nx

# 读取JSON文件
file_path = "/home/data2t2/wrz/Graph Tools/GLM_Call/All_type_mission_directed/once/cycle_check_graphExistance/GLM4.json"
with open(file_path, 'r') as file:
    data = json.load(file)

# 遍历JSON文件中的每条数据
results = []
for index, entry in enumerate(data):
    if 'output' in entry:
        output = entry['output']
        if 'choices' in output:
            choices = output['choices']
            for choice in choices:
                tool_calls = choice['message']['tool_calls']
                for call in tool_calls:
                    arguments = json.loads(call['function']['arguments'])
                    edges_string = arguments['G']
                    edges = eval(edges_string)  # 将字符串转换为列表
                    
                    # 创建有向图并添加边
                    G = nx.DiGraph()
                    G.add_edges_from(edges)

                    # 检查图中是否存在环，仅返回True或False
                    has_cycle = nx.is_directed_acyclic_graph(G) == False
                    results.append(has_cycle)

# 输出结果
for index, result in enumerate(results):
    print(f"Graph {index + 1}: {result}")

