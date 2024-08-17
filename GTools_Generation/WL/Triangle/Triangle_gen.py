import networkx as nx
import random
import json
import argparse
import os

def graph_gen_sum(min_nodes, max_nodes):
    while True:
        G = nx.Graph()  # Create an undirected graph
        num_nodes = random.randint(min_nodes, max_nodes)  # Randomly select the number of nodes between min_nodes and max_nodes
        
        H = nx.path_graph(num_nodes)  # Initialize an undirected path graph
        G.add_nodes_from(H.nodes)  # Add nodes
        
        # Adjust edge generation probability based on the number of nodes
        if num_nodes > 30:
            p = 0.8  # Lower the edge generation probability
        else:
            p = 0.5  # Default probability

        def rand_edge(vi, vj, p):  # Default probability p=0.5
            probability = random.random()  # Generate a random decimal
            if probability > p:  # If greater than p
                G.add_edge(vi, vj, weight=random.randint(1, 100))  # Connect vi and vj nodes and assign a random weight
        
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                rand_edge(i, j, p)  # Call rand_edge()
        
        if len(G.edges) <= 150:  # Adjust the edge limit
            break
    return G

def maximum_triangle_sum_example_gen(num_samples, path):
    all_graphs_data = []

    descriptions = [
        "Find the maximum triangle sum in the graph.",
        "Determine the triangle with the highest total weight.",
        "Identify the triangle with the maximum sum of edge weights.",
        "Calculate the highest sum of weights in any triangle.",
        "Compute the maximum sum of edge weights in a triangle."
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
            G = graph_gen_sum(min_nodes, max_nodes)
            
            # Find all triangles
            triangles = [(u, v, w) for u in G.nodes for v in G.nodes for w in G.nodes if u < v < w and G.has_edge(u, v) and G.has_edge(v, w) and G.has_edge(w, u)]
            
            if not triangles:
                continue  # If no triangles, skip this graph
            
            # Calculate the sum of weights for each triangle
            triangle_sums = [(u, v, w, G[u][v]['weight'] + G[v][w]['weight'] + G[w][u]['weight']) for (u, v, w) in triangles]
            
            # Find the triangle with the maximum sum of weights
            max_triangle = max(triangle_sums, key=lambda x: x[3])
            
            prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven an undirected graph,'
            description = random.choice(descriptions)
            edges_list = str(list(G.edges(data=True)))
            mission = f' The edges are: {edges_list}. The task is: you need to {description}'
            prompt_end = '\n\n### Response:'

            prompt = prompt_start + mission + prompt_end
            print(prompt)
            
            max_triangle_sum = max_triangle[3]
            max_triangle_nodes = (max_triangle[0], max_triangle[1], max_triangle[2])
            print(f"Max triangle {max_triangle_nodes} with sum {max_triangle_sum}")

            # Collect graph data
            graph_data = {
                'id': sample_idx,
                'prompt': prompt,
                'triangle': f'{max_triangle_nodes}',
                'max_triangle_sum': max_triangle_sum,
                'description': description
            }
            print(len(G.edges(data=True)))
            all_graphs_data.append(graph_data)
            sample_idx += 1

    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Save all graph data to a JSON file
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate examples for finding the maximum triangle sum in undirected graphs.")
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated examples.')
    parser.add_argument('--num_examples', type=int, required=True, help='Number of examples to generate.')

    args = parser.parse_args()

    maximum_triangle_sum_example_gen(args.num_examples, args.output_path)
