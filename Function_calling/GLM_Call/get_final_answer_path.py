import json
import re
import networkx as nx

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_data(json_object):
    try:
        function_name = json_object["output"]["choices"][0]["message"]["tool_calls"][0]["function"]["name"]
        print(function_name)
        if function_name == "is_path_graphExistance":
            arguments = json_object["output"]["choices"][0]["message"]["tool_calls"][0]["function"]["arguments"]
            graph_string = re.search(r'"G":"(.*?)"', arguments).group(1)
            path_source = int(re.search(r'"path_source":(\d+)', arguments).group(1))
            path_target = int(re.search(r'"path_target":(\d+)', arguments).group(1))
            expected_answer = json_object["answer"]
            return graph_string, path_source, path_target, expected_answer
    except KeyError as e:
        print(f"KeyError: {e} in JSON object: {json_object}")
    except AttributeError as e:
        print(f"AttributeError: {e} - Some structure might be None in JSON object: {json_object}")
    except Exception as e:
        print(f"Unexpected error: {e} in JSON object: {json_object}")
    return None

def build_graph(graph_string):
    G = nx.Graph()
    edges = graph_string.split()
    for edge in edges:
        try:
            nodes = edge.strip('()').split(',')
            G.add_edge(int(nodes[0]), int(nodes[1]))
        except ValueError as e:
            print(f"ValueError: {e} for edge: {edge}")
    return G

def main(json_file_path):
    json_data = load_json(json_file_path)
    total_count = 0
    equal_count = 0
    for idx, json_object in enumerate(json_data):
        data = extract_data(json_object)
        if data:
            total_count += 1
            graph_string, path_source, path_target, expected_answer = data
            G = build_graph(graph_string)
            # 检查 source 和 target 是否在图 G 中
            if G.has_node(path_source) and G.has_node(path_target):
                path_exists = nx.has_path(G, path_source, path_target)
                if path_exists == expected_answer:
                    equal_count += 1
                else:
                    pass
                    #print(f"Test case {idx}: Expected {expected_answer}, but got {path_exists}")
            else:
                print(f"Test case {idx}: Either source {path_source} or target {path_target} is not in the graph")
    print(f"Number of equal cases: {equal_count} Total test cases: {total_count}")

# 调用main函数并传入json文件路径
main('/home/data2t2/wrz/Graph Tools/API_Call/NLgraph_GLM4.json')
