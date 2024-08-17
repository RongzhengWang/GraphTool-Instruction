import networkx as nx
import random
import json
import argparse
import os

def graph_gen_with_weight(min_nodes, max_nodes): 
    while True:
        G = nx.Graph()  # Create an undirected graph
        
        num_nodes = random.randint(min_nodes, max_nodes)
        
        H = nx.path_graph(num_nodes)  # Initialize an undirected path graph
        G.add_nodes_from(H)  # Add nodes
        
        if 20 <= num_nodes <= 30:
            p = 0.8 
        elif num_nodes > 30:
            p = 0.9  # Lower the edge generation probability
        else:
            p = 0.5  # Default probability

        def rand_edge(vi, vj, p):  
            probability = random.random()  # Generate a random decimal
            if probability > p:  # If greater than p
                weight = random.randint(1, 100)  # Generate the edge weight, range can be adjusted as needed
                G.add_edge(vi, vj, weight=weight)  # Connect vi and vj nodes, and set the edge weight
        
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j:
                    rand_edge(i, j, p)  # Call rand_edge()
        if len(G.edges) <= 1000:  # Relax the edge limit to 150
            break
    
    return G

def shortest_path_example_gen(num_samples, output_path, output_dir):
    all_graphs_data = []

    descriptions = [
        "Determine the shortest path between two specific nodes in the graph.",
        "Find the minimum distance between a given pair of nodes.",
        "Calculate the shortest route from one node to another.",
        "Ascertain the shortest path length between two nodes.",
        "Identify the shortest connection between two nodes in the graph."
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
        for _ in range(num_per_interval):
            G = graph_gen_with_weight(min_nodes, max_nodes)
            node_cnt = len(G.nodes)
            attempts = 0
            while attempts < 100:  # Attempt limit to avoid infinite loop
                node1 = random.choice(list(G.nodes))
                node2 = random.choice(list(G.nodes))
                if node1 != node2 and nx.has_path(G, node1, node2):
                    break
                attempts += 1
            if attempts == 100:
                continue  # If attempts reach 100, regenerate the graph

            prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven an undirected graph,'
            description = random.choice(descriptions)
            file_name = f"task_{sample_idx}.edgelist"
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, 'w') as f:
                for u, v, data in G.edges(data=True):
                    f.write(f"{u} {v} {data['weight']}\n")

            mission = f' the edges are in an edgelist file, the path is "{file_path}". The task is: you need to {description} The nodes in question are: path_source={node1} , path_target={node2}.'
            prompt_end = '\n\n### Response:'

            prompt = prompt_start + mission + prompt_end
            print(prompt)

            shortest_path = nx.shortest_path(G, source=node1, target=node2, weight='weight')
            print(f"Shortest path between {node1} and {node2}: {shortest_path}")

            shortest_path_length = nx.shortest_path_length(G, source=node1, target=node2, weight='weight')
            print(f"Shortest path length between {node1} and {node2}: {shortest_path_length}")

            graph_data = {
                'id': sample_idx,
                'prompt': prompt,
                'path': f'({node1},{node2})',
                'shortest_path': shortest_path,
                'answer': shortest_path_length,
                'description': description,
                'file_path': file_path
            }
            all_graphs_data.append(graph_data)
            sample_idx += 1

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate examples for finding the shortest path in undirected graphs.")
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated examples.')
    parser.add_argument('--num_examples', type=int, required=True, help='Number of examples to generate.')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the edgelist files.')

    args = parser.parse_args()

    shortest_path_example_gen(args.num_examples, args.output_path, args.output_dir)


#python Shortest_gen_Un.py --output_path /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Shortest_Path/Un/shortest_Un.json --output_dir /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Shortest_Path/Un/data --num_examples 500