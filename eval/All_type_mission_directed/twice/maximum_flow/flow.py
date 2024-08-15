import json
import re
import networkx as nx
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
        G = nx.DiGraph()
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

# File paths
edge_list_path = '/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission_directed/twice/maximum_flow/ans_graph.json'
ans_5ques_path = '/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission_directed/twice/maximum_flow/ans_5ques.json'

# Read JSON files
edge_list_data = read_json(edge_list_path)
ans_5ques_data = read_json(ans_5ques_path)

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
        flow_value, flow_dict = maximum_flow(graph, source_node, sink_node)
        
        # Compare computed maximum flow with the provided answer
        is_correct = flow_value == real_answer
        
        if is_correct:
            matched_entries += 1
        else:
            # Print the details in case of mismatch
            pass
            # print(f"Unmatched entry:\nSecondanswer: {ans_5ques_obj['secondanswer']}\nAnswer: {real_answer}\nEdges: {edge_list_obj['firstanswer']}")
        
        # Print the results
        # print(f"Computed maximum flow from node {source_node} to node {sink_node}: {flow_value}")
        # print(f"Provided answer: {real_answer}")
        # print(f"Is the computed result correct? {'Yes' if is_correct else 'No'}")
        # print("\n")
    except Exception as e:
        print(f"Error computing maximum flow: {e}")
        skipped_entries += 1

# Print summary statistics
print(f"Total entries: {total_entries}")
print(f"Matched entries: {matched_entries}")
print(f"Skipped entries: {skipped_entries}")
print(f"Unmatched entries: {total_entries - matched_entries - skipped_entries}")
