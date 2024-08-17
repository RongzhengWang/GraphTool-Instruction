import networkx as nx   
import random 
import matplotlib.pyplot as plt 
import json
import argparse
from networkx.exception import NetworkXNoCycle

def graph_gen_cycle(min_nodes, max_nodes, has_cycle=True): 
    while True:
        G = nx.Graph()  
        num_nodes = random.randint(min_nodes, max_nodes)
        
        if has_cycle:
            
            G = nx.path_graph(num_nodes)
            
            def rand_edge(vi, vj, p=0.5):  
                probability = random.random()  
                if probability > p:  
                    G.add_edge(vi, vj)  
            
            for i in range(num_nodes):
                for j in range(i + 1, num_nodes):
                    rand_edge(i, j)  
            
            if num_nodes >= 3:
                G.add_edge(0, num_nodes - 1)
            
            if len(G.edges) <= 300 and nx.is_connected(G):
                return G
        else:
            G = nx.random_tree(num_nodes)
            if len(G.edges) <= 300:
                return G

def has_cycle_func(G):
    try:
        cycle = nx.find_cycle(G)
        return True
    except nx.exception.NetworkXNoCycle:
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

    num_per_interval = num // 5
    intervals = [
        (10, 16),
        (17, 23),
        (24, 30),
        (31, 35),
        (36, 40)
    ]

    for i in range(5):
        min_nodes, max_nodes = intervals[i]
        for j in range(num_per_interval // 2):
            G = graph_gen_cycle(min_nodes, max_nodes, has_cycle=True)
            description = random.choice(descriptions)
            edges_list = str(list(G.edges))
            prompt = (f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n'
                      f'### Instruction:\nGiven an undirected graph,'
                      f'the edges are: {edges_list}. The task is: you need to determine {description}'
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
            edges_list = str(list(G.edges))
            prompt = (f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n'
                      f'### Instruction:\nGiven an undirected graph,'
                      f'the edges are: {edges_list}. The task is: you need to determine {description}'
                      f'\n\n### Response:')

            graph_data = {
                'id': i * num_per_interval + j,
                'prompt': prompt,
                'answer': has_cycle_func(G),
                'description': description
            }
            print(i * num_per_interval + j)
            all_graphs_data.append(graph_data)

    import os
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate cycle detection examples for directed graphs.")
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated examples.')
    parser.add_argument('--num_examples', type=int, required=True, help='Number of examples to generate.')

    args = parser.parse_args()

    cycle_check_graphExistance_example_gen(args.num_examples, args.output_path)
