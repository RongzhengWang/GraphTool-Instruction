import networkx as nx
import random
import json
import argparse
import os

def graph_gen(min_nodes, max_nodes): 
    Flag = True
    while Flag:
        G = nx.Graph()  # Create an undirected graph
        num_nodes = random.randint(min_nodes, max_nodes)
        
        H = nx.path_graph(num_nodes)  # Initialize a path graph
        G.add_nodes_from(H.nodes)  # Add nodes
        G.add_edges_from(H.edges)  # Add edges
        
        # Adjust edge generation probability based on the number of nodes
        if num_nodes <= 30 and num_nodes >= 20:
            p = 0.5 
        elif num_nodes > 30:
            p = 0.65  # Higher probability of edge generation
        else:
            p = 0.5  # Default probability

        def rand_edge(node_i, node_j, p):  
            probability = random.random()
            if probability > p:
                G.add_edge(node_i, node_j)
        
        for node_i in range(num_nodes):
            for node_j in range(node_i + 1, num_nodes):  # Only consider upper triangle for undirected graph
                rand_edge(node_i, node_j, p)
        
        if len(G.edges) <= 280:
            Flag = False
            break
    return G

def number_of_nodes_graphCount_example_gen(num_samples, path):
    all_graphs_data = []

    descriptions = [
        "Determine the number of nodes in the graph.",
        "Find out how many vertices the graph has.",
        "Count the total number of nodes in the graph.",
        "Ascertain the number of vertices in the graph.",
        "Calculate the number of nodes present in the graph."
    ]

    # Divide num_samples into five equal parts
    num_per_interval = num_samples // 5
    intervals = [
        (4, 20),
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
            node_cnt = len(G.nodes)
            node = random.choice(list(G.nodes))
            prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven an undirected graph,'
            description = random.choice(descriptions)
            edges_list = str(list(G.edges))
            mission = f' The edges are: {edges_list}. The task is: you need to {description}'
            prompt_end = '\n\n### Response:'

            prompt = prompt_start + mission + prompt_end
            #print(prompt)

            # Get the nodes and edges of the graph
            graph_data = {
                'id': sample_idx,
                'prompt': prompt,
                'answer': len(G.nodes),
                'description': description
            }
            print('id: ', sample_idx)
            #print(len(G.nodes))
            print(len(G.edges))
            all_graphs_data.append(graph_data)
            sample_idx += 1

    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Save all graph data to a JSON file
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate examples for counting the number of nodes in undirected graphs.")
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated examples.')
    parser.add_argument('--num_examples', type=int, required=True, help='Number of examples to generate.')

    args = parser.parse_args()

    number_of_nodes_graphCount_example_gen(args.num_examples, args.output_path)
