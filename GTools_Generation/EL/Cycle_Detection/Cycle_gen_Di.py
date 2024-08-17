import networkx as nx  # 导入networkx包
import random  # 导入random包
import json
import argparse
import os
from networkx.exception import NetworkXNoCycle

def graph_gen_cycle(min_nodes, max_nodes, has_cycle=True): 
    while True:
        G = nx.DiGraph()  # 建立有向图
        num_nodes = random.randint(min_nodes, max_nodes)
        
        if has_cycle:
            # 生成一个连通的有向图
            G.add_edges_from((i, i + 1) for i in range(num_nodes - 1))
            
            # 尝试添加额外的边
            def rand_edge(vi, vj, p=0.7):  # 提高概率p=0.7
                probability = random.random()  # 生成随机小数
                if probability > p:  # 如果大于p
                    G.add_edge(vi, vj)  # 连接vi和vj节点
            
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if i != j:
                        rand_edge(i, j)  # 调用rand_edge()
            
            # 尝试添加一个环
            if num_nodes >= 3:
                G.add_edge(0, num_nodes - 1)
            
            if len(G.edges) <= 1000 and nx.is_strongly_connected(G):  # 放宽边数限制到400
                return G
        else:
            # 生成一个有向树结构
            G = nx.random_tree(num_nodes, create_using=nx.DiGraph)
            if len(G.edges) <= 1000:
                return G

def has_cycle_func(G):
    try:
        cycle = nx.find_cycle(G, orientation='original')
        return True
    except nx.exception.NetworkXNoCycle:
        return False

def cycle_check_graphExistance_example_gen(num, output_path, output_dir):
    all_graphs_data = []

    descriptions = [
        "Whether the graph contains a cycle.",
        "Whether there is a loop in the graph.",
        "Whether there is a closed path in the graph.",
        "Whether the graph contains a circuit.",
        "Whether the graph is acyclic."
    ]

    # 将num五等分
    num_per_interval = num // 5
    intervals = [
        (10, 16),
        (17, 23),
        (24, 30),
        (31, 35),
        (36, 100)
    ]

    os.makedirs(output_dir, exist_ok=True)

    # 生成有环和无环图
    for i in range(5):
        min_nodes, max_nodes = intervals[i]
        for j in range(num_per_interval // 2):
            G = graph_gen_cycle(min_nodes, max_nodes, has_cycle=True)
            description = random.choice(descriptions)
            edges_list = list(G.edges)
            file_name = f"task_{i * num_per_interval + j}.edgelist"
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, 'w') as f:
                for edge in edges_list:
                    f.write(f"{edge[0]} {edge[1]}\n")

            prompt = (f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n'
                      f'### Instruction:\nGiven a directed graph,'
                      f'the edges are in an edgelist file, the path is {file_path}. The task is: you need to determine {description}'
                      f'\n\n### Response:')

            graph_data = {
                'id': i * num_per_interval + j,
                'prompt': prompt,
                'answer': has_cycle_func(G),
                'description': description
            }
            print(i * num_per_interval + j)
            all_graphs_data.append(graph_data)

        for j in range(num_per_interval // 2, num_per_interval):
            G = graph_gen_cycle(min_nodes, max_nodes, has_cycle=False)
            description = random.choice(descriptions)
            edges_list = list(G.edges)
            file_name = f"task_{i * num_per_interval + j}.edgelist"
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, 'w') as f:
                for edge in edges_list:
                    f.write(f"{edge[0]} {edge[1]}\n")

            prompt = (f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n'
                      f'### Instruction:\nGiven a directed graph,'
                      f'the edges are in an edgelist file, the path is "{file_path}". The task is: you need to determine {description}'
                      f'\n\n### Response:')

            graph_data = {
                'id': i * num_per_interval + j,
                'prompt': prompt,
                'answer': has_cycle_func(G),
                'description': description
            }
            print(i * num_per_interval + j)
            all_graphs_data.append(graph_data)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate cycle detection examples for directed graphs.")
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated examples.')
    parser.add_argument('--num_examples', type=int, required=True, help='Number of examples to generate.')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the edgelist files.')

    args = parser.parse_args()

    cycle_check_graphExistance_example_gen(args.num_examples, args.output_path, args.output_dir)


#  python Cycle_gen_Di.py --output_path /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Cycle_Detection/Di/cycle_Di.json --output_dir /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Cycle_Detection/Di/data --num_examples 500