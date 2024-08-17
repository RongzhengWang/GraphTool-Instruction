import networkx as nx
import random
import json
import argparse
import os
from networkx.exception import NetworkXNoCycle

def graph_gen_cycle(min_nodes, max_nodes, has_cycle=True): 
    while True:
        G = nx.Graph()  
        num_nodes = random.randint(min_nodes, max_nodes)
        
        if has_cycle:
            G = nx.path_graph(num_nodes)
            
            def rand_edge(vi, vj, p=0.3):  
                probability = random.random()  
                if probability > p:  
                    G.add_edge(vi, vj)  
            
            for i in range(num_nodes):
                for j in range(i + 1, num_nodes):
                    rand_edge(i, j)  
            
            if num_nodes >= 3:
                G.add_edge(0, num_nodes - 1)
            
            if len(G.edges) <= 1000 and nx.is_connected(G):
                return G
        else:
            G = nx.random_tree(num_nodes)
            if len(G.edges) <= 1000:
                return G

def has_cycle_func(G):
    try:
        cycle = nx.find_cycle(G)
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

    num_per_interval = num // 5
    intervals = [
        (10, 16),
        (17, 23),
        (24, 30),
        (31, 35),
        (36, 100)
    ]

    os.makedirs(output_dir, exist_ok=True)

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
                      f'### Instruction:\nGiven an undirected graph,'
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
                      f'### Instruction:\nGiven an undirected graph,'
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
    parser = argparse.ArgumentParser(description="Generate cycle detection examples for undirected graphs.")
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated examples.')
    parser.add_argument('--num_examples', type=int, required=True, help='Number of examples to generate.')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the edgelist files.')

    args = parser.parse_args()

    cycle_check_graphExistance_example_gen(args.num_examples, args.output_path, args.output_dir)


# python Cycle_gen_Un.py --output_path /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Cycle_Detection/Un/cycle_Un.json --output_dir /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Cycle_Detection/Un/data --num_examples 500