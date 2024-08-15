import networkx as nx   #导入networkx包
import random #导入random包
import matplotlib.pyplot as plt #导入画图工具包
import json
from networkx.exception import NetworkXNoCycle


def graph_gen(): 
    Flag = True
    while Flag:
        G = nx.Graph()  # 建立无向图
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


def graph_gen_with_weight(): 
    Flag = True
    while Flag:
        G = nx.Graph()  # 建立无向图
        
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
        G = nx.Graph()  # 建立有向图
        
        # 随机选择10到40之间的节点数
        num_nodes = random.randint(10, 40)
        
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

       

def graph_gen_sum():
    Flag = True
    while Flag:
        G = nx.Graph()  # 建立无向图
        num_nodes = random.randint(10, 40)  # 随机选择10到40之间的节点数
        
        H = nx.path_graph(num_nodes)  # 添加节点，随机数量的点的无向图
        G.add_nodes_from(H)  # 添加节点
        
        def rand_edge(vi, vj, p=0.5):  # 默认概率p=0.5
            probability = random.random()  # 生成随机小数
            if probability > p:  # 如果大于p
                G.add_edge(vi, vj, weight=random.randint(1, 100))  # 连接vi和vj节点，并赋予随机权重
        
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j:
                    rand_edge(i, j)  # 调用rand_edge()
        if len(G.edges) <= 300:
            Flag = False
            break
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
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven an undirected graph,'
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
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task .\n\n### Instruction:\nGiven an undirected graph,'
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
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven an undirected graph and an edge,'
        description = random.choice(descriptions)
        edges_list = str(list(G.edges))
        mission = f' The edges are: {edges_list}. The task is: you need to {description} The edge in question is ({node1}, {node2}).'
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
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven an undirected graph and a node,'
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
            'node': f'({node})',
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
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven an undirected graph and a path,'
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
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven an undirected graph and a node,'
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
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven an undirected graph and a node,'
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
        G = graph_gen_with_weight()
        node_cnt = len(G.nodes)
        while True:
            node1 = random.choice(list(G.nodes))
            node2 = random.choice(list(G.nodes))
            if node1 != node2 and nx.has_path(G, node1, node2):
                break
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven an undirected graph and a path,'
        # prompt_start = f'Below is an instruction that describes a task. Write a code to solve this problem.\n\n### Instruction:\nGiven an undirected graph and a path,'
        description = random.choice(descriptions)
        edges_list = str(list(G.edges(data=True)))
        mission = f' The edges are: {edges_list}. The task is: you need to {description}. The nodes in question are ({node1}, {node2}).'
        # prompt_end = '\n\n The output of the code should only be an integer, no any other words,and do not use \'heapq\' '

        prompt = prompt_start + mission 
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
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven an undirected graph and a path,'
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


def maximum_triangle_sum_example_gen(num, path):
    all_graphs_data = []

    descriptions = [
        "Find the maximum triangle sum in the graph.",
        "Determine the triangle with the highest total weight.",
        "Identify the triangle with the maximum sum of edge weights.",
        "Calculate the highest sum of weights in any triangle.",
        "Compute the maximum sum of edge weights in a triangle."
    ]

    for i in range(num):
        G = graph_gen_sum()
        
        # 找到所有三角形
        triangles = [(u, v, w) for u in G.nodes for v in G.nodes for w in G.nodes if u < v < w and G.has_edge(u, v) and G.has_edge(v, w) and G.has_edge(w, u)]
        
        if not triangles:
            continue  # 如果没有三角形，跳过这个图
        
        # 计算每个三角形的权重和
        triangle_sums = [(u, v, w, G[u][v]['weight'] + G[v][w]['weight'] + G[w][u]['weight']) for (u, v, w) in triangles]
        
        # 找到权重和最大的三角形
        max_triangle = max(triangle_sums, key=lambda x: x[3])
        
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven an undirected graph,'
        description = random.choice(descriptions)
        edges_list = str(list(G.edges(data=True)))
        mission = f' The edges are: {edges_list}. The task is: you need to {description}'
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + mission + prompt_end
        print(prompt)
        
        max_triangle_sum = max_triangle[3]
        max_triangle_nodes = (max_triangle[0], max_triangle[1], max_triangle[2])
        print(f"Max triangle {max_triangle_nodes} with sum {max_triangle_sum}")

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'triangle': f'{max_triangle_nodes}',
            'max_triangle_sum': max_triangle_sum,
            'description':description
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)


# degree_graphCount_example_gen(500,'/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/twice/degree_graphCount/degree_graphCount_undirected_random100_5ques.json')
# cycle_check_graphExistance_example_gen(500,'/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/once/cycle_check_graphExistance/cycle_check_graphExistance_undirected_random100_5ques.json')
#is_edge_graphExistance_example_gen(500, '/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/twice/is_edge_graphExistance/is_edge_graphExistance_undirected_random100_5ques.json')
# is_node_graphExistance_example_gen(500,'/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/twice/is_node_graphExistance/is_node_graphExistance_undirected_random100_5ques.json')
#is_path_graphExistance_example_gen(500,'/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/twice/is_path_graphExistance/is_path_graphExistance_undirected_random100_5ques.json')
# number_of_edges_graphCount_example_gen(500,'/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/once/number_of_edges_graphCount/number_of_edges_graphCount_undirected_random100_5ques.json')
# number_of_nodes_graphCount_example_gen(500,'/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/once/number_of_nodes_graphCount/number_of_nodes_graphCount_undirected_random100_5ques.json')
# shortest_path_example_gen(500,'/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/twice/shortest_path/shortest_undirected_random100_5ques.json')
# max_flow_example_gen(500, '/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/twice/maximum_flow/maximum_flow_undirected_random100_5ques.json')
# maximum_triangle_sum_example_gen(500, '/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/once/maximum_triangle_sum/maximum_triangle_sum_undirected_random100_5ques.json')