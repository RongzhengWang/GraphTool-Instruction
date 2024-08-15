import json
import re
import networkx as nx

def read_json(file_path):
    """Reads a JSON file and returns its content."""
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_graph_from_firstanswer(firstanswer):
    """Extracts graph G from the firstanswer string."""
    # 正则表达式以匹配包含权重的边："G: [(0, 1, {'weight': 45}), (0, 2, {'weight': 95})]"
    graph_pattern = re.compile(r"G:\s*\[(.*)\]", re.DOTALL)
    match = graph_pattern.search(firstanswer)
    if match:
        graph_data = match.group(1)
        # 匹配包含权重的边
        edge_pattern = re.compile(r"\((\d+),\s*(\d+)\)")
        nodes = edge_pattern.findall(graph_data)
        G = nx.Graph()
        for edge in nodes:
            u, v = map(int, edge)
            G.add_edge(u, v)
        return G
    else:
        print('-------------------')
        print(f'firstanswer: {firstanswer}')
        print('-------------------')
        raise ValueError("Graph data not found in firstanswer.")

def calculate_number_of_nodes(graph):
    """Calculates the number of nodes in the graph."""
    return graph.number_of_nodes()

# File paths
edge_list_path = '/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/once/number_of_nodes_graphCount/ans_graph.json'
ans_5ques_path = '/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/once/number_of_nodes_graphCount/ans_5ques.json'

# Read JSON files
edge_list_data = read_json(edge_list_path)
ans_5ques_data = read_json(ans_5ques_path)

# Process and validate each pair of entries
total_entries = len(edge_list_data)
matched_entries = 0
skipped_entries = 0

for i in range(total_entries):
    edge_list_obj = edge_list_data[i]
    if i < len(ans_5ques_data):
        ans_5ques_obj = ans_5ques_data[i]
    else:
        print(f"No corresponding ans_5ques entry for edge_list entry at index {i}. Skipping this entry.")
        skipped_entries += 1
        continue

    try:
        graph = extract_graph_from_firstanswer(edge_list_obj['firstanswer'])
    except ValueError as e:
        print(f"Skipping entry due to error: {e}")
        skipped_entries += 1
        continue
    
    api_name = ans_5ques_obj['api_name']
    expected_answer = ans_5ques_obj['answer']
    
    if api_name == "number_of_nodes_graphCount":
        try:
            # Calculate the number of nodes in the graph
            num_nodes = calculate_number_of_nodes(graph)
            print(f'num_nodes: {num_nodes}')
        
            # Compare calculated number of nodes with the provided answer
            is_correct = num_nodes == expected_answer
            
            if is_correct:
                matched_entries += 1
            else:
                # Print the details in case of a mismatch
                print(f"Unmatched entry:\nAPI Name: {api_name}\nProvided Answer: {expected_answer}\nCalculated Number of Nodes: {num_nodes}\nGraph: {edge_list_obj['firstanswer']}")
            
        except Exception as e:
            print(f"Error calculating number of nodes: {e}")
            skipped_entries += 1

# Print summary statistics
print(f"Total entries: {total_entries}")
print(f"Matched entries: {matched_entries}")
print(f"Skipped entries: {skipped_entries}")
print(f"Unmatched entries: {total_entries - matched_entries - skipped_entries}")
