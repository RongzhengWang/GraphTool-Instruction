import json
import os

# 文件路径列表
file_paths = [
    '/home/data2t2/wrz/Graph Tools/All_type_mission_directed/shortest_path/ans_5ques.json',
    '/home/data2t2/wrz/Graph Tools/All_type_mission_directed/is_edge_graphExistance/ans_5ques.json',
    '/home/data2t2/wrz/Graph Tools/All_type_mission_directed/is_edge_graphExistance/ans_5ques_5k.json',
    '/home/data2t2/wrz/Graph Tools/All_type_mission_directed/is_path_graphExistance/ans_5ques_5k.json',
    # 添加其他文件路径
]



# 循环处理每个文件
for file_path in file_paths:
    # 初始化计数器
    total_count = 0
    # 提取文件路径中 "All_type_mission_directed" 和 "ans_5ques.json" 之间的部分
    parts = file_path.split('/')
    if 'All_type_mission_directed' in parts:
        index = parts.index('All_type_mission_directed')
        api_name = parts[index + 1]
    else:
        continue  # 如果路径中没有 "All_type_mission_directed"，则跳过

    # 从文件中读取JSON数据
    with open(file_path, 'r', encoding='utf-8') as file:
        data_list = json.load(file)

    # 循环读取每个JSON对象
    for data in data_list:
        # 提取 "output" 中 "content" 的内容
        firstanswer_content = data["firstanswer"]["content"]
        count = 0

        # 计数 "API_name: <api_name>" 或 "API_name:\n<api_name>" 的出现次数
        if(firstanswer_content.count(f"API_name: {api_name}") >= 1 or firstanswer_content.count(f"API_name:\n{api_name}") >= 1):
            count = 1

        # 累加计数结果
        total_count += count

    # 输出总计数结果
    print(f"API_name: {api_name}出现的总次数:", total_count)
