import json
import re
import networkx as nx

def read_json(file_path):
    """Reads a JSON file and returns its content."""
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_graph_from_firstanswer(firstanswer):
    # 使用正则表达式提取方括号中间的内容
    match = re.search(r'\[(.*?)\]', firstanswer)
    if match is None:
        raise ValueError("The input does not contain a valid edge list format within brackets.")
    edges_str = match.group(1)
    # 使用正则表达式提取每一条边，注意处理边界中的空格
    edge_pattern = re.compile(r'\((\d+),\s*(\d+)\)')
    edges = edge_pattern.findall(edges_str)
    # 创建一个空的Graph对象
    G = nx.Graph()
    # 将所有边添加到图中
    for edge in edges:
        node1, node2 = map(int, edge)
        G.add_edge(node1, node2)
    return G

def extract_node_from_secondanswer(secondanswer):
    """Extracts a single node from the secondanswer string using regex."""
    node_pattern = re.compile(r'\(G,\s*(\d+)\)|\(graph=\s*G?,\s*node\s*=\s*(\d+)\)')
    match = node_pattern.search(secondanswer)
    if match:
        if match.group(1):
            node = int(match.group(1))
        else:
            node = int(match.group(2))
        return node
    raise ValueError("Node not found in secondanswer.")

# File paths
cycle_edge_list_path = '/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/twice/is_node_graphExistance/ans_graph.json'
ans_5ques_path = '/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/twice/is_node_graphExistance/ans_5ques.json'

# Read JSON files
edge_list_data = read_json(cycle_edge_list_path)
ans_5ques_data = read_json(ans_5ques_path)

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
            node = extract_node_from_secondanswer(ans_5ques_obj['secondanswer'])
        except ValueError as e:
            print(f'secondanswer: {ans_5ques_obj["secondanswer"]}')
            print(f"Skipping entry due to error: {e}")
            skipped_entries += 1
            continue
        
        api_name = ans_5ques_obj['api_name']
        real_answer = ans_5ques_obj['answer']
        
        if api_name == "is_node_graphExistance":
            try:
                # Check if the node exists in the graph
                node_exists = graph.has_node(node)
                
                # Compare computed node existence with the provided answer
                is_correct = node_exists == real_answer
                
                if is_correct:
                    matched_entries += 1
                else:
                    # Print the details in case of a mismatch
                    print(f"Unmatched entry:\nPrompt:{ans_5ques_obj['prompt']}\nSecondanswer: {ans_5ques_obj['secondanswer']}\nAnswer: {real_answer}\nEdges: {edge_list_obj['firstanswer']}")
                
                # Print the results
                # print(f"Computed node existence for node {node}: {node_exists}")
                # print(f"Provided answer: {real_answer}")
                # print(f"Is the computed result correct? {'Yes' if is_correct else 'No'}")
                # print("\n")
            except Exception as e:
                error_message = str(e)
                if 'Either source' in error_message or 'target is not in G' in error_message:
                    matched_entries += 1
                else:
                    print(f"Error detecting node existence: {e}")
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
