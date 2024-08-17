import json
import re
import networkx as nx
import argparse
from networkx.algorithms.flow import maximum_flow

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
        edge_pattern = re.compile(r"\((\d+), (\d+), \{'capacity': (\d+)\}\)")
        edges = edge_pattern.findall(graph_data)
        G = nx.Graph()
        for edge in edges:
            u, v, capacity = map(int, edge)
            G.add_edge(u, v, capacity=capacity)
        return G
    else:
        raise ValueError("Graph data not found in firstanswer.")

def extract_nodes_from_secondanswer(secondanswer):
    """Extracts source and sink nodes from the secondanswer string using regex."""
    # Regex pattern to match source and sink nodes in both formats
    node_pattern1 = re.compile(r"source_node\s*=\s*(\d+),\s*sink_node\s*=\s*(\d+)")
    node_pattern2 = re.compile(r"(\d+),\s*(\d+)\s*\)")
    
    match = node_pattern1.search(secondanswer)
    if match:
        source_node = int(match.group(1))
        sink_node = int(match.group(2))
        return source_node, sink_node
    
    match = node_pattern2.search(secondanswer)
    if match:
        source_node = int(match.group(1))
        sink_node = int(match.group(2))
        return source_node, sink_node
    
    print('--------------------------------------')
    print(f'secondanswer: {secondanswer}')
    print('--------------------------------------')
    raise ValueError("Source and sink nodes not found in secondanswer.")

def main(graph_path, ans_path):
    # Read JSON files
    edge_list_data = read_json(graph_path)
    ans_5ques_data = read_json(ans_path)

    # Ensure both JSON files have equal length
    assert len(edge_list_data) == len(ans_5ques_data), "JSON files are not of equal length."

    total_entries = len(edge_list_data)
    matched_entries = 0
    skipped_entries = 0

    # Process and validate each pair of entries
    for edge_list_obj, ans_5ques_obj in zip(edge_list_data, ans_5ques_data):
        try:
            graph = extract_graph_from_firstanswer(edge_list_obj['firstanswer'])
            source_node, sink_node = extract_nodes_from_secondanswer(ans_5ques_obj['secondanswer'])
        except ValueError as e:
            print(f"Skipping entry due to error: {e}")
            skipped_entries += 1
            continue
        
        real_answer = ans_5ques_obj['answer']
        
        try:
            # Compute the maximum flow using NetworkX
            flow_value, flow_dict = nx.maximum_flow(graph, source_node, sink_node, capacity='capacity')
            
            # Compare computed maximum flow with the provided answer
            is_correct = flow_value == real_answer
            
            if is_correct:
                matched_entries += 1
            else:
                # Print the details in case of mismatch
                print(f"Unmatched entry:\nSecondanswer: {ans_5ques_obj['secondanswer']}\nAnswer: {real_answer}\nTool Answer: {flow_value}\nEdges: {edge_list_obj['firstanswer']}")
            
        except Exception as e:
            print(f"Error computing maximum flow: {e}")
            skipped_entries += 1

    # Print summary statistics
    print(f"Total entries: {total_entries}")
    print(f"Matched entries: {matched_entries}")
    print(f"Skipped entries: {skipped_entries}")
    print(f"Unmatched entries: {total_entries - matched_entries - skipped_entries}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check the maximum flow in graphs from JSON files.")
    parser.add_argument("--graph_path", type=str, required=True, help="Path to the graph JSON file.")
    parser.add_argument("--ans_path", type=str, required=True, help="Path to the answers JSON file.")
    args = parser.parse_args()

    main(args.graph_path, args.ans_path)


# python Flow_eval_Un.py --graph_path /home/data2t2/wrz/GraphTool-Instruction/GraphForge_test_WL/Flow/Un/ans_graph_Un.json --ans_path /home/data2t2/wrz/GraphTool-Instruction/GraphForge_test_WL/Flow/Un/ans_Un.json