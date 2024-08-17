import networkx as nx
import random
import json
import argparse
import os

def graph_gen_with_capacity(min_nodes, max_nodes): 
    while True:
        G = nx.DiGraph()  # Create a directed graph
        
        # Randomly select the number of nodes between min_nodes and max_nodes
        num_nodes = random.randint(min_nodes, max_nodes)
        
        H = nx.path_graph(num_nodes)  # Add nodes, undirected graph with a random number of nodes
        G.add_nodes_from(H)  # Add nodes
        
        # Adjust edge generation probability based on the number of nodes
        if num_nodes <= 30 and num_nodes >= 20:
            p = 0.5 
        elif num_nodes > 30:
            p = 0.7  # Lower the probability of edge generation
        else:
            p = 0.5  # Default probability

        def rand_edge(vi, vj, p):  
            probability = random.random()  # Generate a random float
            if probability > p:  # If greater than p
                weight = random.randint(1, 100)  # Generate edge weight, range can be adjusted as needed
                G.add_edge(vi, vj, capacity=weight)  # Connect nodes vi and vj, and set edge weight
        
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j:
                    rand_edge(i, j, p)  # Call rand_edge()
        if len(G.edges) <= 1000:
            break
    
    return G

def max_flow_example_gen(num_samples, output_path, output_dir):
    all_graphs_data = []

    descriptions = [
        "Determine the maximum flow between two specific nodes in the graph.",
        "Calculate the maximum flow from one node to another.",
        "Ascertain the maximum flow value between two nodes.",
        "Compute the maximum flow from one specific node to another.",
        "Get the maximum flow between two given vertices."
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
            G = graph_gen_with_capacity(min_nodes, max_nodes)
            node_cnt = len(G.nodes)
            while True:
                node1 = random.choice(list(G.nodes))
                node2 = random.choice(list(G.nodes))
                if node1 != node2 and nx.has_path(G, node1, node2):
                    break
            prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph,'
            description = random.choice(descriptions)
            file_name = f"task_{sample_idx}.edgelist"
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, 'w') as f:
                for u, v, data in G.edges(data=True):
                    f.write(f"{u} {v} {data['capacity']}\n")

            mission = f' the edges are in an edgelist file, the path is "{file_path}". The task is: you need to {description} The nodes in question are: source_node={node1} , sink_node={node2}.'
            prompt_end = '\n\n### Response:'

            prompt = prompt_start + mission + prompt_end
            print(prompt)
            if node1 == node2:
                print('error')
                break
            # Use NetworkX to calculate maximum flow
            flow_value, flow_dict = nx.maximum_flow(G, node1, node2)
            print(f"Maximum flow between {node1} and {node2}: {flow_value}")

            # Get the nodes and edges of the graph
            graph_data = {
                'id': sample_idx,
                'prompt': prompt,
                'path': f'({node1},{node2})',
                'answer': flow_value,
                'description': description,
                'file_path': file_path
            }
            print(sample_idx)
            print(len(G.edges))
            all_graphs_data.append(graph_data)
            sample_idx += 1

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save all graph data to a JSON file
    with open(output_path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate maximum flow examples for directed graphs.")
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated examples.')
    parser.add_argument('--num_examples', type=int, required=True, help='Number of examples to generate.')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the edgelist files.')

    args = parser.parse_args()

    max_flow_example_gen(args.num_examples, args.output_path, args.output_dir)

# python Flow_gen_Di.py --output_path /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Flow/Di/flow_Di.json --output_dir /home/data2t2/wrz/GraphTool-Instruction/GTools/Test/EL/Flow/Di/data --num_examples 500

