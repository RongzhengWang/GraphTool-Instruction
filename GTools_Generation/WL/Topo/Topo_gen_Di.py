import networkx as nx
import random
import json
import argparse
import os

def graph_gen_topo(min_nodes, max_nodes):
    while True:
        G = nx.DiGraph()  # Create a directed graph
        num_nodes = random.randint(min_nodes, max_nodes)
        nodes = list(range(num_nodes))
        random.shuffle(nodes)
        
        # Initialize the level of each node
        levels = {node: 0 for node in nodes}
        
        # Ensure graph connectivity and build hierarchy
        for i in range(1, num_nodes):
            possible_parents = [n for n in nodes[:i] if levels[n] < levels[nodes[i]] - 1]
            if possible_parents:
                parent = random.choice(possible_parents)
                G.add_edge(parent, nodes[i])
            else:
                levels[nodes[i]] = levels[nodes[i - 1]] + 1
                G.add_edge(nodes[i - 1], nodes[i])
        
        # Add extra edges to increase complexity
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                r = random.random()
                if r > 0.6 and levels[nodes[i]] < levels[nodes[j]] and not G.has_edge(nodes[i], nodes[j]):
                    G.add_edge(nodes[i], nodes[j])
        
        # Ensure the generated graph is a directed acyclic graph (DAG) and the number of edges is less than or equal to 270
        if nx.is_directed_acyclic_graph(G) and len(G.edges) <= 270:
            return G

def topo_sort_example_gen(num_samples, path):
    all_graphs_data = []

    descriptions = [
        "Determine the topological order of the directed graph.",
        "Find the topological sorting of the given graph.",
        "Calculate the topological order of nodes.",
        "Ascertain the topological sequence of the graph.",
        "Identify the topological ordering of the nodes."
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
            G = graph_gen_topo(min_nodes, max_nodes)
            node_cnt = len(G.nodes)
            
            prompt_start = f'Below is an instruction that describes a task. Write a response that determines use which API to complete the task.\n\n### Instruction:\nGiven a directed graph, '
            description = random.choice(descriptions)
            edges_list = str(list(G.edges(data=False)))
            mission = f' The edges are: {edges_list}. The task is: you need to {description}'
            prompt_end = '\n\n### Response:'

            prompt = prompt_start + mission + prompt_end
            #print(prompt)
            print(len(G.edges))
            
            # Use NetworkX to calculate topological sorting
            topo_sort = list(nx.topological_sort(G))
            print(f"Topological sort of the graph: {topo_sort}")

            # Collect graph data
            graph_data = {
                'id': sample_idx,
                'prompt': prompt,
                'topological_sort': str(topo_sort),
                'edges': edges_list,
                'description': description
            }
            all_graphs_data.append(graph_data)
            sample_idx += 1

    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Save all graph data to a JSON file
    with open(path, 'w') as json_file:
        json.dump(all_graphs_data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate examples for finding the topological sort in directed graphs.")
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated examples.')
    parser.add_argument('--num_examples', type=int, required=True, help='Number of examples to generate.')

    args = parser.parse_args()

    topo_sort_example_gen(args.num_examples, args.output_path)
