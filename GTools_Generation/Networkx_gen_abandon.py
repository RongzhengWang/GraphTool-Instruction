# 随机生成10个节点的图
import networkx as nx   #导入networkx包
import random #导入random包
import matplotlib.pyplot as plt #导入画图工具包
import json
from networkx.exception import NetworkXNoCycle


def graph_gen(): 
    Flag = True
    while Flag:
        G = nx.Graph()  # 建立无向图
        # 随机选择10到100之间的节点数
        num_nodes = random.randint(10, 40)
        
        H = nx.path_graph(num_nodes)  # 添加节点，随机数量的点的无向图
        G.add_nodes_from(H)  # 添加节点
        
        def rand_edge(vi, vj, p=0.5):  # 默认概率p=0.5
            probability = random.random()  # 生成随机小数
            if probability > p:  # 如果大于p
                G.add_edge(vi, vj)  # 连接vi和vj节点
        
        for i in range(num_nodes):
            for j in range(i):
                rand_edge(i, j)  # 调用rand_edge()
        if len(G.edges)<=300:
            Flag = False
            break
        
    # print(G.nodes)
    # print(G.edges)
    
    return G


def graph_gen_with_weight(): 
    Flag = True
    while Flag:
        G = nx.Graph()  # 建立无向图
        
        # 随机选择10到100之间的节点数
        num_nodes = random.randint(10, 40)
        
        H = nx.path_graph(num_nodes)  # 添加节点，随机数量的点的无向图
        G.add_nodes_from(H)  # 添加节点
        
        def rand_edge(vi, vj, p=0.5):  # 默认概率p=0.5
            probability = random.random()  # 生成随机小数
            if probability > p:  # 如果大于p
                weight = random.randint(1, 100)  # 生成边的权重，范围可以根据需要调整
                G.add_edge(vi, vj, weight=weight)  # 连接vi和vj节点，并设置边的权重
        
        for i in range(num_nodes):
            for j in range(i):
                rand_edge(i, j)  # 调用rand_edge()
        if len(G.edges)<=200:
            Flag = False
            break
    
    return G




def degree_graphCount_example_gen(num, path):
    all_graphs_data = []

    for i in range(num):
        G = graph_gen()
        node = random.choice(list(G.nodes))
        node_cnt = len(G.nodes)
        print(node)
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task .\n\n### Instruction:\nGiven a graph, you need to count the degree of the given node. \n\Q: The nodes are numbered from 0 to {node_cnt-1}, and the edges are: '
        edges_list = str(G.edges)
        mission = f'. The task is: you need to count the degree of node {node} '
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + edges_list + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'answer': G.degree(node)
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


def cycle_check_graphExistance_example_gen(num,path):
    all_graphs_data = []

    for i in range(num):
        G = graph_gen()
        node = random.choice(list(G.nodes))
        node_cnt = len(G.nodes)
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task .\n\n### Instruction:\nGiven a graph, you need to determine whether the graph contains a cycle . \n\Q: The nodes are numbered from 0 to {node_cnt}, and the edges are: '
        edges_list = str(G.edges)
        mission = f'. The task is: you need to determine whether the graph contains a cycle '
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + edges_list + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'answer': has_cycle(G)
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)




def is_edge_graphExistance_example_gen(num, path):
    all_graphs_data = []

    for i in range(num):
        G = graph_gen()
        while True:
            node1 = random.choice(list(G.nodes))
            node2 = random.choice(list(G.nodes))
            if node1 != node2 and nx.has_path(G, node1, node2):
                break
        node_cnt = len(G.nodes)
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task .\n\n### Instruction:\nGiven a graph and an edge, you need to determine whether this edge exist in this graph. \n\Q: The nodes are numbered from 0 to {node_cnt}, and the edges are: '
        edges_list = str(G.edges)
        mission = f'. The task is: you need to find if the edge ({node1},{node2}) exists '
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + edges_list + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'edge': f'({node1},{node2})',
            'answer': G.has_edge(node1,node2)
        }
        if node1 == node2:
            print('error')
            break
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)




def is_node_graphExistance_example_gen(num, path):
    all_graphs_data = []

    for i in range(num):
        G = graph_gen()
        node = random.choice(list(G.nodes))
        node_cnt = len(G.nodes)
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task .\n\n### Instruction:\nGiven a graph and a node, you need to determine whether this node exist in this graph. \n\Q: The nodes are numbered from 0 to {node_cnt}, and the edges are: '
        edges_list = str(G.edges)
        mission = f'. The task is: you need to find if the node {node} exists '
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + edges_list + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'node': f'({node})',
            'answer': G.has_node(node)
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)




def is_path_graphExistance_example_gen(num, path):
    all_graphs_data = []

    for i in range(num):
        G = graph_gen()
        node1 = random.choice(list(G.nodes))
        node2 = random.choice(list(G.nodes))
        node_cnt = len(G.nodes)
        while node2 == node1:
            node2 = random.choice(list(G.nodes))
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task .\n\n### Instruction:\nGiven a graph and an path, you need to determine whether there is a path between the two nodes. \n\Q: The nodes are numbered from 0 to {node_cnt}, and the edges are: '
        edges_list = str(G.edges)
        mission = f'. The task is: you need to find if there is a path between ({node1},{node2}) '
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + edges_list + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'path': f'({node1},{node2})',
            'answer': nx.has_path(G,node1,node2)
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)



def number_of_edges_graphCount_example_gen(num, path):
    all_graphs_data = []

    for i in range(num):
        G = graph_gen()
        node_cnt = len(G.nodes)
        node = random.choice(list(G.nodes))
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task .\n\n### Instruction:\nGiven a graph and a node, you need to count the edge numbers in this graph. \n\Q: The nodes are numbered from 0 to {node_cnt}, and the edges are: '
        edges_list = str(G.edges)
        mission = f'. The task is: you need to count the total number of the edges'
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + edges_list + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'answer': len(G.edges)
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)



def number_of_nodes_graphCount_example_gen(num, path):
    all_graphs_data = []

    for i in range(num):
        G = graph_gen()
        node = random.choice(list(G.nodes))
        node_cnt = len(G.nodes)
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task .\n\n### Instruction:\nGiven a graph and a node,  you need to count the node numbers in this graph. \n\Q: The nodes are numbered from 0 to {node_cnt}, and the edges are: '
        edges_list = str(G.edges)
        mission = f'. The task is: you need to count the total number of the nodes'
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + edges_list + mission + prompt_end
        print(prompt)

        # 获取图的节点和边
        graph_data = {
            'id': i,
            'prompt': prompt,
            'answer': len(G.nodes)
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)





def shortest_path_example_gen(num, path):
    all_graphs_data = []

    for i in range(num):
        G = graph_gen_with_weight()
        node_cnt = len(G.nodes)
        while True:
            node1 = random.choice(list(G.nodes))
            node2 = random.choice(list(G.nodes))
            if node1 != node2 and nx.has_path(G, node1, node2):
                break
        prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task .\n\n### Instruction:\nGiven a graph and an path, you need to find the shortest path between the two nodes. \n\Q: The nodes are numbered from 0 to {node_cnt}, and the edges are: '
        edges_list = str(G.edges(data=True))
        mission = f'. The task is: you need to find the shortest path between ({node1},{node2}) '
        prompt_end = '\n\n### Response:'

        prompt = prompt_start + edges_list + mission + prompt_end
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
            'shortest_path':shortest_path,
            'answer': shortest_path_length
        }
        all_graphs_data.append(graph_data)

    # 将所有图的数据保存到 JSON 文件中
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)




degree_graphCount_example_gen(1000,'/home/data2t2/wrz/Graph Tools/All_type_mission/degree_graphCount/degree_graphCount_data_undirected_random40_10000.json')
cycle_check_graphExistance_example_gen(1000,'/home/data2t2/wrz/Graph Tools/All_type_mission/cycle_basis_graphExistance/cycle_basis_graphExistance_undirected_random40_10000.json')
is_edge_graphExistance_example_gen(1000, '/home/data2t2/wrz/Graph Tools/All_type_mission/is_edge_graphExistance/is_edge_graphExistance_undirected_random40_10000.json')
is_node_graphExistance_example_gen(1000,'/home/data2t2/wrz/Graph Tools/All_type_mission/is_node_graphExistance/is_node_graphExistance_undirected_random40_10000.json')
is_path_graphExistance_example_gen(1000,'/home/data2t2/wrz/Graph Tools/All_type_mission/is_path_graphExistance/is_path_graphExistance_undirected_random40_10000.json')
number_of_edges_graphCount_example_gen(1000,'/home/data2t2/wrz/Graph Tools/All_type_mission/number_of_edges_graphCount/number_of_edges_graphCount_undirected_random40.json')
number_of_nodes_graphCount_example_gen(1000,'/home/data2t2/wrz/Graph Tools/All_type_mission/number_of_nodes_graphCount/number_of_nodes_graphCount_undirected_random40.json')
shortest_path_example_gen(1000,'/home/data2t2/wrz/Graph Tools/All_type_mission/shortest_path/shortest_path_undirected_random40_10000.json')