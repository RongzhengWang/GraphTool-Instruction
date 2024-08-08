import json
import os
import re

# 定义用于匹配所有形如 (a, b, {'weight': c}) 的正则表达式
edge_pattern = re.compile(r'\((\d+),\s*(\d+),\s*\{\'weight\':\s*(\d+)\}\)')

# 定义用于匹配[]内的内容的正则表达式
brackets_pattern = re.compile(r'\[(.*?)\]')

def extract_edges_and_prompts_from_json(file_path):
    # 初始化一个空列表，用于存储每个图对象的边和提示中的边列表
    graph_data = []

    # 检查文件是否存在
    if os.path.exists(file_path):
        # 打开文件并读取内容
        with open(file_path, 'r') as file:
            # 加载整个JSON文件内容到数据变量中
            data = json.load(file)
            
            # 遍历每个JSON对象
            for item in data:
                # 初始化一个字典存储当前对象的边和提示中的边列表
                graph_item = {
                    "edges": [],
                    "prompt_list": []
                }

                # 提取每个对象中的firstanswer键
                first_answer_data = item.get("firstanswer", None)
                if first_answer_data:
                    # 找到所有匹配的边
                    matches = edge_pattern.findall(first_answer_data)
                    # 将找到的边添加到边列表中
                    for match in matches:
                        # 转换为整数并作为元组加入边列表
                        graph_item["edges"].append((int(match[0]), int(match[1]), int(match[2])))

                # 提取每个对象的prompt键
                prompt_data = item.get("prompt", None)
                if prompt_data:
                    # 找出prompt中的[]中内容
                    bracket_content = brackets_pattern.findall(prompt_data)
                    for content in bracket_content:
                        # 找到[]中的匹配的所有边
                        matches = edge_pattern.findall(content)
                        if matches:
                            # 将找到的边添加到prompt_list
                            for match in matches:
                                # 转换为整数并作为元组加入prompt_list
                                graph_item["prompt_list"].append((int(match[0]), int(match[1]), int(match[2])))
                
                # 将当前图对象数据加入到总列表中
                graph_data.append(graph_item)
    else:
        print(f"File {file_path} does not exist.")

    return graph_data

# 比较两个列表并判定是否相同
def are_lists_equal(list1, list2):
    return sorted(list1) == sorted(list2)

# 调用函数并传入文件路径
file_path = "/home/data2t2/wrz/Graph Tools/Graph_LLaMA_test/All_type_mission/once/maximum_triangle_sum/ans_graph.json"
graph_data_list = extract_edges_and_prompts_from_json(file_path)

# 初始化一个用于记录匹配的计数器
matching_count = 0
total_count = len(graph_data_list)

# 比较每个图对象中的两个列表是否相同
for graph_data in graph_data_list:
    if are_lists_equal(graph_data['edges'], graph_data['prompt_list']):
        matching_count += 1

# 输出匹配的个数以及总数
print(f"Total Graphs: {total_count}")
print(f"Matching Graphs: {matching_count}")
print(f"Non-Matching Graphs: {total_count - matching_count}")
