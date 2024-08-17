import networkx as nx
import random
import json
import argparse
import os

def graph_gen(min_nodes, max_nodes): 
    while True:
        G = nx.DiGraph()  # Create a directed graph
        num_nodes = random.randint(min_nodes, max_nodes)
        
        H = nx.path_graph(num_nodes, create_using=nx.DiGraph)  # Initialize a directed path graph
        G.add_nodes_from(H.nodes)  # Add nodes
        G.add_edges_from(H.edges)  # Add edges
        
        # Adjust edge generation probability based on the number of nodes
        if 20 <= num_nodes <= 30:
            p = 0.7 
        elif num_nodes > 30:
            p = 0.8  # Lower probability of edge generation
        else:
            p = 0.5  # Default probability

        # Add random edges
        for node_i in range(num_nodes):
            for node_j in range(num_nodes):
                if node_i != node_j and random.random() > p:
                    G.add_edge(node_i, node_j)
        
        if 0 < len(G.edges) <= 1000:
            break
    return G

def is_node_existence_example_gen(num_samples, output_path, output_dir):
    all_graphs_data = []

    descriptions = [
        "Check if the node exists in the graph.",
        "Verify the existence of a node in the graph.",
        "Determine whether the node is part of the graph.",
        "Confirm if a node can be found in the graph.",
        "Identify whether a certain node exists in the graph."
    ]

    # Divide num_samples into five equal parts
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
            G = graph_gen(min_nodes, max_nodes)
            existing_nodes = list(G.nodes)

            if sample_idx < num_samples // 2:
                # Choose an existing node
                node = random.choice(existing_nodes)
                node_exists = True
            else:
                # Choose a non-existing node
                node = max(existing_nodes) + 1 + sample_idx  # Ensure this node does not exist in the graph
                node_exists = False

            prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph,'
            description = random.choice(descriptions)
            file_name = f"task_{sample_idx}.edgelist"
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, 'w') as f:
                for u, v in G.edges:
                    f.write(f"{u} {v}\n")

            mission = f' the edges are in an edgelist file, the path is "{file_path}". The task is: you need to {description} The node in question is node={node}.'
            prompt_end = '\n\n### Response:'

            prompt = prompt_start + mission + prompt_end

            # Get the nodes and edges of the graph
            graph_data = {
                'id': sample_idx,
                'prompt': prompt,
                'node': node,
                'answer': node_exists,
                'description': description,
                'file_path': file_path
            }
            print(sample_idx)
            all_graphs_data.append(graph_data)
            sample_idx += 1

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save all graph data to a JSON file
    with open(output_path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate examples for checking node existence in directed graphs.")
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated examples.')
    parser.add_argument('--num_examples', type=int, required=True, help='Number of examples to generate.')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the edgelist files.')

    args = parser.parse_args()

    is_node_existence_example_gen(args.num_examples, args.output_path, args.output_dir)

#python Node_E_gen_Di.py --output_path /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Node_Existence/Di/node_e_Di.json --output_dir /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Node_Existence/Di/data --num_examples 500