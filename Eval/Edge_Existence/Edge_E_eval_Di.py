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
    # Use regex to extract the content within square brackets
    match = re.search(r'\[(.*?)\]', firstanswer)
    if match is None:
        raise ValueError("The input does not contain a valid edge list format within brackets.")
    edges_str = match.group(1)
    # Use regex to extract each edge, paying attention to spaces within the edges
    edge_pattern = re.compile(r'\((\d+),\s*(\d+)\)')
    edges = edge_pattern.findall(edges_str)
    # Create an empty DiGraph object
    G = nx.DiGraph()
    # Add all edges to the graph
    for edge in edges:
        node1, node2 = map(int, edge)
        G.add_edge(node1, node2)
    return G

def extract_nodes_from_secondanswer(secondanswer):
    """Extracts source and sink nodes from the secondanswer string using regex."""
    node_pattern = re.compile(r'(?:(?:G,\s*(\d+),\s*(\d+))|(?:edge_source\s*=\s*(\d+)[,\s]*edge_target\s*=\s*(\d+)))')
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
            
            if api_name == "is_edge_graphExistance":
                try:
                    # Detect if there is an edge between path_source and path_target
                    is_edge = graph.has_edge(path_source, path_target)
                    
                    # Compare computed edge existence with the provided answer
                    is_correct = is_edge == real_answer
                    
                    if is_correct:
                        matched_entries += 1
                    else:
                        # Print the details in case of a mismatch
                        print(f"Unmatched entry:\nPrompt:{ans_5ques_obj['prompt']}\nSecondanswer: {ans_5ques_obj['secondanswer']}\nAnswer: {real_answer}\nEdges: {edge_list_obj['firstanswer']}")
                    
                except Exception as e:
                    error_message = str(e)
                    if 'Either source' in error_message or 'target is not in G' in error_message:
                        matched_entries += 1
                    else:
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
    parser = argparse.ArgumentParser(description="Check the existence of edges in graphs from JSON files.")
    parser.add_argument("--graph_path", type=str, required=True, help="Path to the graph JSON file.")
    parser.add_argument("--ans_path", type=str, required=True, help="Path to the answers JSON file.")
    args = parser.parse_args()

    main(args.graph_path, args.ans_path)


# python Edge_E_eval_Di.py --graph_path /home/data2t2/wrz/GraphTool-Instruction/GraphForge_test_WL/Edge_Existence/Di/ans_graph_Di.json --ans_path /home/data2t2/wrz/GraphTool-Instruction/GraphForge_test_WL/Edge_Existence/Di/ans_Di.json