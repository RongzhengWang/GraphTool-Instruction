import networkx as nx
import random
import json
import argparse
import os

def graph_gen(min_nodes, max_nodes, ensure_connected=True):
    while True:
        G = nx.DiGraph() 
        num_nodes = random.randint(min_nodes, max_nodes)
        
        H = nx.path_graph(num_nodes, create_using=nx.DiGraph)  
        G.add_nodes_from(H.nodes)  
        G.add_edges_from(H.edges)  
        
        if min_nodes <= 30 and min_nodes >= 20:
            p = 0.2 
        elif min_nodes > 30:
            p = 0.2
        else:
            p = 0.2 

        def rand_edge(node_i, node_j, p):  
            probability = random.random()
            if probability < p:
                G.add_edge(node_i, node_j)
        
        for node_i in range(num_nodes):
            for node_j in range(num_nodes):
                if node_i != node_j:
                    rand_edge(node_i, node_j, p)
        
        if 0 < len(G.edges) <= 1000:
            break
    return G

def is_path_graph_existence_example_gen(num_samples, output_path, output_dir):
    all_graphs_data = []

    descriptions = [
        "Check if there is a path between two nodes in the graph.",
        "Verify the existence of a path from one node to another.",
        "Determine whether a route exists between two specific nodes.",
        "Confirm if a path can be found between two nodes.",
        "Identify whether a path exists linking two nodes."
    ]

    num_per_interval = num_samples // 5
    intervals = [
        (10, 20),
        (21, 25),
        (26, 30),
        (31, 35),
        (36, 100)
    ]

    sample_idx = 0

    os.makedirs(output_dir, exist_ok=True)

    for interval in intervals:
        min_nodes, max_nodes = interval
        true_count = num_per_interval // 2
        false_count = num_per_interval // 2

        for _ in range(true_count):
            G = graph_gen(min_nodes, max_nodes)
            node1 = random.choice(list(G.nodes))
            node2 = random.choice(list(G.nodes))
            while node2 == node1:
                node2 = random.choice(list(G.nodes))

            while not nx.has_path(G, node1, node2):
                G = graph_gen(min_nodes, max_nodes)
                node1 = random.choice(list(G.nodes))
                node2 = random.choice(list(G.nodes))
                while node2 == node1:
                    node2 = random.choice(list(G.nodes))

            prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph,'
            description = random.choice(descriptions)
            file_name = f"task_{sample_idx}.edgelist"
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, 'w') as f:
                for u, v in G.edges:
                    f.write(f"{u} {v}\n")

            mission = f' the edges are in an edgelist file, the path is "{file_path}". The task is: you need to {description} The nodes in question are: path_source={node1} , path_target={node2}.'
            prompt_end = '\n\n### Response:'

            prompt = prompt_start + mission + prompt_end

            graph_data = {
                'id': sample_idx,
                'prompt': prompt,
                'path': f'({node1}, {node2})',
                'answer': nx.has_path(G, node1, node2),
                'description': description,
                'file_path': file_path
            }
            print(f'True: {sample_idx}')
            print(len(G.edges))
            all_graphs_data.append(graph_data)
            sample_idx += 1

        if min_nodes <= 30 and min_nodes >= 20:
            p = 0.2 
        elif min_nodes > 30:
            p = 0.2
        else:
            p = 0.2  

        for _ in range(false_count):
            G = nx.DiGraph()
            num_nodes = random.randint(min_nodes, max_nodes)
            nodes = list(range(num_nodes))
            random.shuffle(nodes)
            split_point = num_nodes // 2

            part1 = nodes[:split_point]
            part2 = nodes[split_point:]

            G.add_nodes_from(part1)
            G.add_nodes_from(part2)

            def rand_edge(node_i, node_j, p):
                probability = random.random()
                if probability < p:
                    G.add_edge(node_i, node_j)
                    
            for part in [part1, part2]:
                H = nx.path_graph(part, create_using=nx.DiGraph)
                G.add_edges_from(H.edges)
                for node_i in part:
                    for node_j in part:
                        if node_i != node_j:
                            rand_edge(node_i, node_j, p)

            for node_i in part1:
                for node_j in part2:
                    if G.has_edge(node_i, node_j):
                        G.remove_edge(node_i, node_j)

            node1 = random.choice(part1)
            node2 = random.choice(part2)

            prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph,'
            description = random.choice(descriptions)
            file_name = f"task_{sample_idx}.edgelist"
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, 'w') as f:
                for u, v in G.edges:
                    f.write(f"{u} {v}\n")

            mission = f' the edges are in an edgelist file, the path is "{file_path}". The task is: you need to {description} The nodes in question are: path_source={node1} , path_target={node2}.'
            prompt_end = '\n\n### Response:'

            prompt = prompt_start + mission + prompt_end

            graph_data = {
                'id': sample_idx,
                'prompt': prompt,
                'path': f'({node1}, {node2})',
                'answer': nx.has_path(G, node1, node2),
                'description': description,
                'file_path': file_path
            }
            print(f'False: {sample_idx}')
            print(len(G.edges))
            all_graphs_data.append(graph_data)
            sample_idx += 1

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate examples for checking path existence in directed graphs.")
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated examples.')
    parser.add_argument('--num_examples', type=int, required=True, help='Number of examples to generate.')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the edgelist files.')

    args = parser.parse_args()

    is_path_graph_existence_example_gen(args.num_examples, args.output_path, args.output_dir)


# python Path_E_gen_Di.py --output_path /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Path_Existence/Di/path_Di.json --output_dir /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Path_Existence/Di/data --num_examples 500