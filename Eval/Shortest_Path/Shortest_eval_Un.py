import json
import re
import networkx as nx
import argparse

def read_json(file_path):
    """Reads a JSON file and returns its content."""
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_graph_from_firstanswer(firstanswer):
    """Extracts graph G from the firstanswer string using regex."""
    graph_pattern = re.compile(r"\[(.*)\]", re.DOTALL)
    match = graph_pattern.search(firstanswer)
    if match:
        graph_data = match.group(1)
        edge_pattern = re.compile(r"\((\d+), (\d+), \{'weight':\s*(\d+)\}\)")
        edges = edge_pattern.findall(graph_data)
        G = nx.Graph()
        for edge in edges:
            u, v, weight = map(int, edge)
            G.add_edge(u, v, weight=weight)
        return G
    else:
        raise ValueError("Graph data not found in firstanswer.")

def extract_nodes_from_secondanswer(secondanswer):
    """Extracts source and sink nodes from the secondanswer string using regex."""
    node_pattern = re.compile(r'(?:(?:G,\s*(\d+),\s*(\d+))|(?:path_source\s*=\s*(\d+)[,\s]*path_target\s*=\s*(\d+)))')
    match = node_pattern.search(secondanswer)
    if match:
        if match.group(1) and match.group(2):
            path_source = int(match.group(1))
            path_target = int(match.group(2))
        else:
            path_source = int(match.group(3))
            path_target = int(match.group(4))
        return path_source, path_target
    raise ValueError("Source and target nodes not found in secondanswer.")

def main(graph_path, ans_path):
    # Read JSON files
    edge_list_data = read_json(graph_path)
    ans_5ques_data = read_json(ans_path)

    # Ensure the length of edge_list_data is taken into account
    total_entries = len(edge_list_data)
    matched_entries = 0
    skipped_entries = 0

    # Process and validate entries ensuring to use the length of edge_list_data
    for i in range(total_entries):
        edge_list_obj = edge_list_data[i]
        # Ensure the second JSON doesn't go out of index
        if i < len(ans_5ques_data):
            ans_5ques_obj = ans_5ques_data[i]
            
            try:
                graph = extract_graph_from_firstanswer(edge_list_obj['firstanswer'])
                path_source, path_target = extract_nodes_from_secondanswer(ans_5ques_obj['secondanswer'])
            except ValueError as e:
                print(f'secondanswer: {ans_5ques_obj["secondanswer"]}')
                print(f"Skipping entry due to error: {e}")
                skipped_entries += 1
                continue
            
            api_name = ans_5ques_obj['api_name']
            real_answer = ans_5ques_obj['answer']
            
            if api_name == "shortest_path":
                try:
                    # Detect if there is an edge between path_source and path_target
                    is_edge = nx.shortest_path_length(graph, path_source, path_target, weight='weight')
                    
                    # Compare computed edge existence with the provided answer
                    is_correct = is_edge == real_answer
                    
                    if is_correct:
                        matched_entries += 1
                    else:
                        # Print the details in case of a mismatch
                        print(f'path_length: {is_edge} real_answer:{real_answer}')
                    
                except Exception as e:
                    print(f"Error detecting edge existence: {e}")
                    skipped_entries += 1
            else:
                skipped_entries += 1
        else:
            skipped_entries += 1

    # Print summary statistics
    print(f"Total entries: {total_entries}")
    print(f"Matched entries: {matched_entries}")
    print(f"Skipped entries: {skipped_entries}")
    print(f"Unmatched entries: {total_entries - matched_entries - skipped_entries}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check the shortest path in graphs from JSON files.")
    parser.add_argument("--graph_path", type=str, required=True, help="Path to the graph JSON file.")
    parser.add_argument("--ans_path", type=str, required=True, help="Path to the answers JSON file.")
    args = parser.parse_args()

    main(args.graph_path, args.ans_path)

