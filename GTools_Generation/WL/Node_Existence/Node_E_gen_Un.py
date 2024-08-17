import networkx as nx
import random
import json
import argparse
import os

def graph_gen(min_nodes, max_nodes): 
    while True:
        G = nx.Graph()  # Create an undirected graph
        num_nodes = random.randint(min_nodes, max_nodes)
        
        H = nx.path_graph(num_nodes)  # Initialize an undirected path graph
        G.add_nodes_from(H.nodes)  # Add nodes
        G.add_edges_from(H.edges)  # Add edges
        
        # Adjust edge generation probability based on the number of nodes
        if 20 <= num_nodes <= 30:
            p = 0.6 
        elif num_nodes > 30:
            p = 0.7  # Lower probability of edge generation
        else:
            p = 0.5  # Default probability

        # Add random edges
        for node_i in range(num_nodes):
            for node_j in range(node_i + 1, num_nodes):
                if random.random() > p:
                    G.add_edge(node_i, node_j)
        
        if 0 < len(G.edges) <= 300:
            break
    return G

def is_node_existence_example_gen(num_samples, path):
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
        (36, 40)
    ]

    sample_idx = 0

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

            prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven an undirected graph,'
            description = random.choice(descriptions)
            edges_list = str(list(G.edges))
            mission = f'the edges are: {edges_list}. The task is: you need to {description} The node in question is node={node}.'
            prompt_end = '\n\n### Response:'

            prompt = prompt_start + mission + prompt_end

            # Get the nodes and edges of the graph
            graph_data = {
                'id': sample_idx,
                'prompt': prompt,
                'node': node,
                'answer': node_exists,
                'description': description
            }
            print(sample_idx)
            all_graphs_data.append(graph_data)
            sample_idx += 1

    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Save all graph data to a JSON file
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate examples for checking node existence in undirected graphs.")
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated examples.')
    parser.add_argument('--num_examples', type=int, required=True, help='Number of examples to generate.')

    args = parser.parse_args()

    is_node_existence_example_gen(args.num_examples, args.output_path)
