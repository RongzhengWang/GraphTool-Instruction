import networkx as nx
import random
import json
import argparse

def graph_gen(min_nodes, max_nodes): 
    Flag = True
    while Flag:
        G = nx.DiGraph()  # Create a directed graph
        num_nodes = random.randint(min_nodes, max_nodes)
        
        H = nx.path_graph(num_nodes, create_using=nx.DiGraph)  # Initialize a path graph
        G.add_nodes_from(H.nodes)  # Add nodes
        G.add_edges_from(H.edges)  # Add edges
        
        # Adjust edge generation probability based on the number of nodes
        if num_nodes <= 30 and num_nodes >= 20:
            p = 0.7 
        elif num_nodes > 30:
            p = 0.85  # Increase the probability of edge generation
        else:
            p = 0.5  # Default probability

        def rand_edge(node_i, node_j, p):  
            probability = random.random()
            if probability > p:
                G.add_edge(node_i, node_j)
        
        for node_i in range(num_nodes):
            for node_j in range(num_nodes):
                if node_i != node_j:
                    rand_edge(node_i, node_j, p)
        
        if len(G.edges) <= 280:
            Flag = False
            break
    return G

def node_degree_example_gen(num_samples, path):
    all_graphs_data = []

    descriptions = [
        "Determine the degree of a specific node in the graph.",
        "Find out the number of edges connected to a particular node.",
        "Calculate the degree of a given vertex.",
        "Ascertain the number of connections for a specific node.",
        "Identify the degree of a certain vertex in the graph."
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

            # Select an existing node
            node = random.choice(existing_nodes)
            node_degree = G.degree[node]

            prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph,'
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
                'answer': node_degree,
                'description': description
            }
            print('id', sample_idx)
            print(len(G.edges))
            all_graphs_data.append(graph_data)
            sample_idx += 1
    import os
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Save all graph data to a JSON file
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate degree examples for directed graphs.")
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated examples.')
    parser.add_argument('--num_examples', type=int, required=True, help='Number of examples to generate.')

    args = parser.parse_args()

    node_degree_example_gen(args.num_examples, args.output_path)
