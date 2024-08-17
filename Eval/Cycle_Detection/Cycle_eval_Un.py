import json
import re
import networkx as nx
import argparse

def read_json(file_path):
    """Reads a JSON file and returns its content."""
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_graph_from_firstanswer(firstanswer):
    """Extracts graph G from the firstanswer string."""
    graph_pattern = re.compile(r"G:\s*\[(.*)\]", re.DOTALL)
    match = graph_pattern.search(firstanswer)
    if match:
        graph_data = match.group(1)
        edge_pattern = re.compile(r"\((\d+),\s*(\d+)\)")
        edges = edge_pattern.findall(graph_data)
        G = nx.Graph()
        for edge in edges:
            u, v = map(int, edge)
            G.add_edge(u, v)
        return G
    else:
        print('-------------------')
        print(f'firstanswer: {firstanswer}')
        print('-------------------')
        raise ValueError("Graph data not found in firstanswer.")

def main(graph_path, ans_path):
    # Read JSON files
    edge_list_data = read_json(graph_path)
    ans_5ques_data = read_json(ans_path)

    # Process and validate each pair of entries
    total_entries = len(edge_list_data)
    matched_entries = 0
    skipped_entries = 0

    # Use the length of edge_list_data as the limit
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
        expected_answer = ans_5ques_obj['answer']  # Directly use the boolean value
        
        if api_name == "cycle_check_graphExistance":
            try:
                try:
                    # Check for cycles using NetworkX
                    nx.find_cycle(graph, orientation='original')
                    cycle_exists = True
                except nx.NetworkXNoCycle:
                    cycle_exists = False
            
                # Compare detected cycle existence with the provided answer
                is_correct = cycle_exists == expected_answer
                
                if is_correct:
                    matched_entries += 1
                else:
                    # Print the details in case of a mismatch
                    print(f"Unmatched entry:\nAPI Name: {api_name}\nProvided Answer: {expected_answer}\nGraph: {edge_list_obj['firstanswer']}")
                
            except Exception as e:
                print(f"Error detecting cycle: {e}")
                skipped_entries += 1

    # Print summary statistics
    print(f"Total entries: {total_entries}")
    print(f"Matched entries: {matched_entries}")
    print(f"Skipped entries: {skipped_entries}")
    print(f"Unmatched entries: {total_entries - matched_entries - skipped_entries}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check for cycles in graphs from JSON files.")
    parser.add_argument("--graph_path", type=str, required=True, help="Path to the graph JSON file.")
    parser.add_argument("--ans_path", type=str, required=True, help="Path to the answers JSON file.")
    args = parser.parse_args()

    main(args.graph_path, args.ans_path)

#python Cycle_eval_Un.py  --graph_path /home/data2t2/wrz/GraphTool-Instruction/GraphForge_test_WL/Cycle_Detection/Un/ans_graph_Un.json --ans_path /home/data2t2/wrz/GraphTool-Instruction/GraphForge_test_WL/Cycle_Detection/Un/ans_Un.json