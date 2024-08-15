# 随机生成10个节点的图
import networkx as nx   #导入networkx包
import random #导入random包
import matplotlib.pyplot as plt #导入画图工具包
import json
from networkx.exception import NetworkXNoCycle


# def graph_gen(): 
#     Flag = True
#     while Flag:
#         G = nx.Graph()  # 建立无向图
#         # 随机选择10到100之间的节点数
#         num_nodes = random.randint(10, 40)
        
#         H = nx.path_graph(num_nodes)  # 添加节点，随机数量的点的无向图
#         G.add_nodes_from(H)  # 添加节点
        
#         def rand_edge(vi, vj, p=0.5):  # 默认概率p=0.5
#             probability = random.random()  # 生成随机小数
#             if probability > p:  # 如果大于p
#                 G.add_edge(vi, vj)  # 连接vi和vj节点
        
#         for i in range(num_nodes):
#             for j in range(i):
#                 rand_edge(i, j)  # 调用rand_edge()
#         if len(G.edges)<=300:
#             Flag = False
#             break
        
#     # print(G.nodes)
#     # print(G.edges)
    
#     return G

def graph_gen(): 
    Flag = True
    while Flag:
        G = nx.DiGraph()  # 建立有向图
        # 随机选择10到40之间的节点数
        num_nodes = random.randint(10, 100)
        
        H = nx.path_graph(num_nodes)  # 添加节点，随机数量的点的无向图
        G.add_nodes_from(H)  # 添加节点
        
        def rand_edge(vi, vj, p=0.5):  # 默认概率p=0.5
            probability = random.random()  # 生成随机小数
            if probability > p:  # 如果大于p
                G.add_edge(vi, vj)  # 连接vi和vj节点
        
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j:
                    rand_edge(i, j)  # 调用rand_edge()
        if len(G.edges) <= 300:
            Flag = False
            break
    return G



# def graph_gen_with_weight(): 
#     Flag = True
#     while Flag:
#         G = nx.Graph()  # 建立无向图
        
#         # 随机选择10到100之间的节点数
#         num_nodes = random.randint(10, 40)
        
#         H = nx.path_graph(num_nodes)  # 添加节点，随机数量的点的无向图
#         G.add_nodes_from(H)  # 添加节点
        
#         def rand_edge(vi, vj, p=0.5):  # 默认概率p=0.5
#             probability = random.random()  # 生成随机小数
#             if probability > p:  # 如果大于p
#                 weight = random.randint(1, 100)  # 生成边的权重，范围可以根据需要调整
#                 G.add_edge(vi, vj, weight=weight)  # 连接vi和vj节点，并设置边的权重
        
#         for i in range(num_nodes):
#             for j in range(i):
#                 rand_edge(i, j)  # 调用rand_edge()
#         if len(G.edges)<=200:
#             Flag = False
#             break
    
#     return G

def graph_gen_with_weight(): 
    Flag = True
    while Flag:
        G = nx.DiGraph()  # 建立有向图
        
        # 随机选择10到40之间的节点数
        num_nodes = random.randint(10, 100)
        
        H = nx.path_graph(num_nodes)  # 添加节点，随机数量的点的无向图
        G.add_nodes_from(H)  # 添加节点
        
        def rand_edge(vi, vj, p=0.5):  # 默认概率p=0.5
            probability = random.random()  # 生成随机小数
            if probability > p:  # 如果大于p
                weight = random.randint(1, 100)  # 生成边的权重，范围可以根据需要调整
                G.add_edge(vi, vj, weight=weight)  # 连接vi和vj节点，并设置边的权重
        
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j:
                    rand_edge(i, j)  # 调用rand_edge()
        if len(G.edges) <= 200:
            Flag = False
            break
    
    return G

def graph_gen_with_capacity(): 
    Flag = True
    while Flag:
        G = nx.DiGraph()  # 建立有向图
        
        # 随机选择10到40之间的节点数
        num_nodes = random.randint(10, 100)
        
        H = nx.path_graph(num_nodes)  # 添加节点，随机数量的点的无向图
        G.add_nodes_from(H)  # 添加节点
        
        def rand_edge(vi, vj, p=0.5):  # 默认概率p=0.5
            probability = random.random()  # 生成随机小数
            if probability > p:  # 如果大于p
                weight = random.randint(1, 100)  # 生成边的权重，范围可以根据需要调整
                G.add_edge(vi, vj, capacity=weight)  # 连接vi和vj节点，并设置边的权重
        
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j:
                    rand_edge(i, j)  # 调用rand_edge()
        if len(G.edges) <= 200:
            Flag = False
            break
    
    return G

def graph_gen_topo():
    while True:
        G = nx.DiGraph()  # 建立有向图
        num_nodes = random.randint(10, 100)  # 随机选择10到40之间的节点数
        nodes = list(range(num_nodes))
        random.shuffle(nodes)  # 随机打乱节点顺序
        
        # 确保图是连通的有向无环图（DAG）
        for i in range(num_nodes - 1):
            G.add_edge(nodes[i], nodes[i + 1])
        
        # 添加额外的随机边
        def rand_edge(vi, vj, p=0.5):  # 默认概率p=0.5
            probability = random.random()  # 生成随机小数
            if probability > p and not G.has_edge(vi, vj) and vi != vj and nx.has_path(G, vi, vj):
                G.add_edge(vi, vj)  # 连接vi和vj节点
        
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                rand_edge(nodes[i], nodes[j])
        
        if nx.is_directed_acyclic_graph(G) and len(G.edges) <= 300:
            return G
        

def degree_graphCount_example_gen(num, path):
    all_graphs_data = []

    descriptions = [
        "Determine the degree of a specific node in the graph.",
        "Find out the number of edges connected to a particular node.",
        "Calculate the degree of a given vertex.",
        "Ascertain the number of connections for a specific node.",
        "Identify the degree of a certain vertex in the graph."
    ]

    for i in range(num):
        G = graph_gen()
        node = random.choice(list(G.nodes))
        node_cnt = len(G.nodes)
        print(node)
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph, '
        description = random.choice(descriptions)
        edges_list = str(list(G.edges))
        mission = f' The edges are: {edges_list}. The task is: you need to {description} The node in question is {node}.'
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'node': node,
            'answer': G.degree(node),
            'description':description
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)




def has_cycle(G):
    try:
        cycle = nx.find_cycle(G)
        return True
    except NetworkXNoCycle:
        return False


def cycle_check_graphExistance_example_gen(num, path):
    all_graphs_data = []

    descriptions = [
        "Whether the graph contains a cycle.",
        "Whether there is a loop in the graph.",
        "Whether there is a closed path in the graph.",
        "Whether the graph contains a circuit.",
        "Whether the graph is acyclic."
    ]

    for i in range(num):
        G = graph_gen()
        node = random.choice(list(G.nodes))
        node_cnt = len(G.nodes)
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task .\n\n### Instruction:\nGiven a directed graph, '
        description = random.choice(descriptions)
        edges_list = str(list(G.edges))
        mission = f' The edges are: {edges_list}. The task is: you need to determine {description}'
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'answer': has_cycle(G),
            'description':description
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)




def is_edge_graphExistance_example_gen(num, path):
    all_graphs_data = []

    descriptions = [
        "Check if there is an edge between two nodes in the graph.",
        "Verify the existence of an edge connecting two specific nodes.",
        "Determine whether there is a direct link between two nodes.",
        "See if an edge exists from one node to another in the graph.",
        "Ascertain if an edge is present between two particular nodes."
    ]

    for i in range(num):
        G = graph_gen()
        while True:
            node1 = random.choice(list(G.nodes))
            node2 = random.choice(list(G.nodes))
            if node1 != node2 and nx.has_path(G, node1, node2):
                break
        node_cnt = len(G.nodes)
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph and an edge, '
        description = random.choice(descriptions)
        edges_list = str(list(G.edges))
        mission = f' The edges are: {edges_list}. The task is: you need to {description} The edge in question is edge_source= {node1}, edge_target= {node2}.'
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'edge': f'({node1}, {node2})',
            'answer': G.has_edge(node1, node2),
            'description':description
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)




def is_node_graphExistance_example_gen(num, path):
    all_graphs_data = []

    descriptions = [
        "Check if a node exists in the graph.",
        "Verify the presence of a specific node in the graph.",
        "Determine whether a particular node is in the graph.",
        "Confirm the existence of a node within the graph.",
        "Ascertain if a certain node is contained in the graph."
    ]

    for i in range(num):
        G = graph_gen()
        node = random.choice(list(G.nodes))
        node_cnt = len(G.nodes)
        print(node)
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph and a node, '
        description = random.choice(descriptions)
        edges_list = str(list(G.edges))
        mission = f' The edges are: {edges_list}. The task is: you need to {description} The node in question is {node}.'
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'node': f'{node}',
            'answer': G.has_node(node),
            'description':description
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)




def is_path_graphExistance_example_gen(num, path):
    all_graphs_data = []

    descriptions = [
        "Check if there is a path between two nodes in the graph.",
        "Verify the existence of a path from one node to another.",
        "Determine whether a route exists between two specific nodes.",
        "Confirm if a path can be found between two nodes.",
        "Identify whether a path exists linking two nodes."
    ]

    for i in range(num):
        G = graph_gen()
        node1 = random.choice(list(G.nodes))
        node2 = random.choice(list(G.nodes))
        node_cnt = len(G.nodes)
        while node2 == node1:
            node2 = random.choice(list(G.nodes))
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph and a path, '
        description = random.choice(descriptions)
        edges_list = str(list(G.edges))
        mission = f' The edges are: {edges_list}. The task is: you need to {description} The nodes in question are ({node1}, {node2}).'
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'path': f'({node1}, {node2})',
            'answer': nx.has_path(G, node1, node2),
            'description':description
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)



def number_of_edges_graphCount_example_gen(num, path):
    all_graphs_data = []

    descriptions = [
        "Determine the number of edges in the graph.",
        "Find out how many edges the graph has.",
        "Count the total number of edges in the graph.",
        "Ascertain the number of edges present in the graph.",
        "Calculate the number of edges in the graph."
    ]

    for i in range(num):
        G = graph_gen()
        node_cnt = len(G.nodes)
        node = random.choice(list(G.nodes))
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph and a node, '
        description = random.choice(descriptions)
        edges_list = str(list(G.edges))
        mission = f' The edges are: {edges_list}. The task is: you need to {description}'
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'answer': len(G.edges),
            'description':description
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)


def number_of_nodes_graphCount_example_gen(num, path):
    all_graphs_data = []

    descriptions = [
        "Determine the number of nodes in the graph.",
        "Find out how many vertices the graph has.",
        "Count the total number of nodes in the graph.",
        "Ascertain the number of vertices in the graph.",
        "Calculate the number of nodes present in the graph."
    ]

    for i in range(num):
        G = graph_gen()
        node = random.choice(list(G.nodes))
        node_cnt = len(G.nodes)
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph and a node, '
        description = random.choice(descriptions)
        edges_list = str(list(G.edges))
        mission = f' The edges are: {edges_list}. The task is: you need to {description}'
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'answer': len(G.nodes),
            'description':description
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)




def shortest_path_example_gen(num, path):
    all_graphs_data = []

    descriptions = [
        "Determine the shortest path between two specific nodes in the graph.",
        "Find the minimum distance between a given pair of nodes.",
        "Calculate the shortest route from one node to another.",
        "Ascertain the shortest path length between two nodes.",
        "Identify the shortest connection between two nodes in the graph."
    ]

    for i in range(num):
        edge_list_path = f'/home/data2t2/wrz/Graph Tools/1EL_graph/All_type_mission_directed/twice/data/shortest{i}.edgelist'
        G = graph_gen_with_weight()
        node_cnt = len(G.nodes)
        while True:
            node1 = random.choice(list(G.nodes))
            node2 = random.choice(list(G.nodes))
            if node1 != node2 and nx.has_path(G, node1, node2):
                break
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph and a path, '
        description = random.choice(descriptions)
        edges_list = str(list(G.edges(data=True)))
        mission = f' The edges are in the egdelist file, the path is: {edge_list_path}. The task is: you need to {description}. The nodes in question are ({node1}, {node2}).'
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + mission + prompt_end
        print(prompt)
        if node1 == node2:
            print('error')
            break
        # 使用 NetworkX 计算最短路径
        shortest_path = nx.shortest_path(G, source=node1, target=node2, weight='weight')
        print(f"Shortest path between {node1} and {node2}: {shortest_path}")

        # 计算最短路径的长度
        shortest_path_length = nx.shortest_path_length(G, source=node1, target=node2, weight='weight')
        print(f"Shortest path length between {node1} and {node2}: {shortest_path_length}")

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'path': f'({node1},{node2})',
            'shortest_path': shortest_path,
            'answer': shortest_path_length,
            'description':description
        }
        all_graphs_data.append(graph_data)

        # 保存图到指定路径
        
        nx.write_edgelist(G, edge_list_path, data=True)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)

def max_flow_example_gen(num, path):
    all_graphs_data = []

    descriptions = [
        "Determine the maximum flow between two specific nodes in the graph.",
        "Calculate the maximum flow from one node to another.",
        "Ascertain the maximum flow value between two nodes.",
        "Compute the maximum flow from one specific node to another.",
        "Get the maximum flow between two given vertices."
    ]

    for i in range(num):
        G = graph_gen_with_capacity()
        node_cnt = len(G.nodes)
        while True:
            node1 = random.choice(list(G.nodes))
            node2 = random.choice(list(G.nodes))
            if node1 != node2 and nx.has_path(G, node1, node2):
                break
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph and a path, '
        description = random.choice(descriptions)
        edges_list = str(list(G.edges(data=True)))
        mission = f' The edges are: {edges_list}. The task is: you need to {description}. The nodes in question are ({node1}, {node2}).'
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + mission + prompt_end
        print(prompt)
        if node1 == node2:
            print('error')
            break
        # 使用 NetworkX 计算最大流
        flow_value, flow_dict = nx.maximum_flow(G, node1, node2)
        print(f"Maximum flow between {node1} and {node2}: {flow_value}")

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'path': f'({node1},{node2})',
            'answer': flow_value,
            'description':description
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)


def topo_sort_example_gen(num, path):
    all_graphs_data = []

    descriptions = [
        "Determine the topological order of the directed graph.",
        "Find the topological sorting of the given graph.",
        "Calculate the topological order of nodes.",
        "Ascertain the topological sequence of the graph.",
        "Identify the topological ordering of the nodes."
    ]

    for i in range(num):
        G = graph_gen_topo()
        node_cnt = len(G.nodes)
        
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph, '
        description = random.choice(descriptions)
        edges_list = str(list(G.edges(data=False)))
        mission = f' The edges are: {edges_list}. The task is: you need to {description}'
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + mission + prompt_end
        print(prompt)
        
        # 使用 NetworkX 计算拓扑排序
        topo_sort = list(nx.topological_sort(G))
        print(f"Topological sort of the graph: {topo_sort}")

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'topological_sort': topo_sort,
            'edges': edges_list,
            'description':description
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)




# degree_graphCount_example_gen(500,'/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission_directed/twice/degree_graphCount/degree_graphCount_directed_random100_5ques.json')
# cycle_check_graphExistance_example_gen(500,'/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission_directed/once/cycle_check_graphExistance/cycle_check_graphExistance_directed_random100_5ques.json')
# is_edge_graphExistance_example_gen(500, '/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission_directed/twice/is_edge_graphExistance/is_edge_graphExistance_directed_random100_5ques.json')
# is_node_graphExistance_example_gen(500,'/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission_directed/twice/is_node_graphExistance/is_node_graphExistance_directed_random100_5ques.json')
# is_path_graphExistance_example_gen(500,'/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission_directed/twice/is_path_graphExistance/is_path_graphExistance_directed_random100_5ques.json')
# number_of_edges_graphCount_example_gen(500,'/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission_directed/once/number_of_edges_graphCount/number_of_edges_graphCount_directed_random100_5ques.json')
# number_of_nodes_graphCount_example_gen(500,'/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission_directed/once/number_of_nodes_graphCount/number_of_nodes_graphCount_directed_random100_5ques.json')
shortest_path_example_gen(500,'/home/data2t2/wrz/Graph Tools/1EL_graph/All_type_mission_directed/twice/shortest_path/shortest_directed_random100_5ques.json')
# max_flow_example_gen(500, '/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission_directed/twice/maximum_flow/maximum_flow_directed_random100_5ques.json')
# topo_sort_example_gen(500, '/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission_directed/once/topological_sort/topological_sort_directed_random100_5ques.json')