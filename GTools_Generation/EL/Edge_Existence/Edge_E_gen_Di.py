import networkx as nx
import random
import json
import argparse
import os

def graph_gen(min_nodes, max_nodes): 
    while True:
        G = nx.DiGraph()  # Create a directed graph
        num_nodes = random.randint(min_nodes, max_nodes)
        
        H = nx.path_graph(num_nodes, create_using=nx.DiGraph())  # Initialize a path graph
        G.add_nodes_from(H.nodes)  # Add nodes
        G.add_edges_from(H.edges)  # Add edges
        
        # Adjust edge generation probability based on the number of nodes
        if min_nodes <= 30 and min_nodes >= 20:
            p = 0.5 
        elif min_nodes > 30:
            p = 0.2
        else:
            p = 0.5  # Default probability

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

def is_edge_existence_example_gen(num_samples, output_path, output_dir):
    all_graphs_data = []

    descriptions = [
        "Check if the specified edge exists in the graph.",
        "Verify the existence of a specific edge in the graph.",
        "Determine whether an edge exists between two specific nodes.",
        "Confirm if an edge can be found between two nodes.",
        "Identify whether an edge exists linking two nodes."
    ]

    # Divide num_samples into five equal parts
    num_per_interval = num_samples // 5
    intervals = [
        (3, 16),
        (17, 23),
        (24, 30),
        (31, 35),
        (36, 100)
    ]

    sample_idx = 0

    os.makedirs(output_dir, exist_ok=True)

    for interval in intervals:
        min_nodes, max_nodes = interval
        true_count = num_per_interval // 2
        false_count = num_per_interval - true_count

        for _ in range(true_count):
            G = graph_gen(min_nodes, max_nodes)
            
            # Try to randomly select two different nodes
            node1 = random.choice(list(G.nodes))
            node2 = random.choice(list(G.nodes))
            while node2 == node1:
                node2 = random.choice(list(G.nodes))

            # Ensure the edge exists
            if not G.has_edge(node1, node2):
                G.add_edge(node1, node2)

            prompt_start = 'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph,'
            description = random.choice(descriptions)
            file_name = f"task_{sample_idx}.edgelist"
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, 'w') as f:
                for edge in G.edges:
                    f.write(f"{edge[0]} {edge[1]}\n")

            mission = f' the edges are in an edgelist file, the path is "{file_path}". The task is: you need to {description} The nodes in question are: edge_source={node1} , edge_target={node2}.'
            prompt_end = '\n\n### Response:'

            prompt = prompt_start + mission + prompt_end

            # Get the nodes and edges of the graph
            graph_data = {
                'id': sample_idx,
                'prompt': prompt,
                'edge': f'({node1}, {node2})',
                'answer': G.has_edge(node1, node2),
                'description': description
            }
            print('id: ', sample_idx)
            print(len(G.edges))
            all_graphs_data.append(graph_data)
            sample_idx += 1

        for _ in range(false_count):
            G = graph_gen(min_nodes, max_nodes)
            
            # Try to randomly select two different nodes
            node1 = random.choice(list(G.nodes))
            node2 = random.choice(list(G.nodes))
            while node2 == node1:
                node2 = random.choice(list(G.nodes))

            # Ensure the edge does not exist
            while len(G.edges) == 0:
                G = graph_gen(min_nodes, max_nodes)
            
            if G.has_edge(node1, node2):
                G.remove_edge(node1, node2)

            prompt_start = 'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph,'
            description = random.choice(descriptions)
            file_name = f"task_{sample_idx}.edgelist"
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, 'w') as f:
                for edge in G.edges:
                    f.write(f"{edge[0]} {edge[1]}\n")

            mission = f' the edges are in an edgelist file, the path is "{file_path}". The task is: you need to {description} The nodes in question are: edge_source={node1} , edge_target={node2}.'
            prompt_end = '\n\n### Response:'

            prompt = prompt_start + mission + prompt_end

            # Get the nodes and edges of the graph
            graph_data = {
                'id': sample_idx,
                'prompt': prompt,
                'edge': f'({node1}, {node2})',
                'answer': G.has_edge(node1, node2),
                'description': description
            }
            print('id: ', sample_idx)
            print(len(G.edges))
            all_graphs_data.append(graph_data)
            sample_idx += 1

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save all graph data to a JSON file
    with open(output_path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate edge existence examples for directed graphs.")
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated examples.')
    parser.add_argument('--num_examples', type=int, required=True, help='Number of examples to generate.')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the edgelist files.')

    args = parser.parse_args()

    is_edge_existence_example_gen(args.num_examples, args.output_path, args.output_dir)

# python Edge_E_gen_Di.py --output_path /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Edge_Existence/Di/edge_Di.json --output_dir /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Edge_Existence/Di/data --num_examples 500
