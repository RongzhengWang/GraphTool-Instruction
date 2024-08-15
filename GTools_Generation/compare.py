import json
import re

def extract_path_info(api_input):
    # 第一种形式: "(G, 17, 19)"
    pattern1 = r'\(G,\s*(\d+),\s*(\d+)\)'
    
    # 第二种形式: "(graph=G, path_source=0, path_target=13)"
    pattern2 = r'edge_source=(\d+),\s*edge_target=(\d+)'

    # 第二种形式: "(graph=G, path_source=0, path_target=13)"
    pattern3 = r'edge_source= (\d+),\s*edge_target= (\d+)'
    
    match1 = re.search(pattern1, api_input)
    match2 = re.search(pattern2, api_input)
    match3 = re.search(pattern3, api_input)
    
    if match1:
        return int(match1.group(1)), int(match1.group(2))
    elif match2:
        return int(match2.group(1)), int(match2.group(2))
    elif match3:
        return int(match3.group(1)), int(match3.group(2))
    else:
        raise ValueError("Invalid api_input format")

# 读取JSON文件
# 指定compute的输出文件extracted
with open('/home/data2t2/wrz/Graph Tools/All_type_mission_directed/is_edge_graphExistance/extracted_ans_5ques_5k_lora.json', 'r') as file:
    ext_datas = json.load(file)
with open('/home/data2t2/wrz/Graph Tools/prompt_template/prompt3.txt', 'r', encoding='utf-8') as file:
    prompt = file.read()

list1 = []
for item in ext_datas:
    try:
        api_input = item.get('api_input', '')
        path_source, path_target = extract_path_info(api_input)
        list1.append([path_source, path_target])
    except ValueError as e:
        list1.append([-1, -1])
        print(f"Error processing item: {e}")
        continue

list2 = []
# 读取JSON文件
# 指定graph_genernate生成的原数据文件
with open('/home/data2t2/wrz/Graph Tools/All_type_mission_directed/is_edge_graphExistance/is_edge_graphExistance_direted_random40_5ques_5k.json', 'r') as file:
    datas = json.load(file)
for data in datas:
    # 提取path字段
    path = data['edge']

    # 去除括号并分割数字
    numbers = path.strip('()').split(',')
    list2.append([int(numbers[0]), int(numbers[1])])

def compare_and_save(list1, list2, data):
    # 以list1的长度为准进行比较
    length = len(list1)
    if length > len(list2):
        print("List1 is longer than List2. Using List1 length for comparison.")
    
    matched_items = []
    mismatched_items = []  # Initialize a list to store mismatched items

    for i in range(length):
        item1 = list1[i]
        item2 = list2[i] if i < len(list2) else None  # Handle case where list2 is shorter
        if item1 == item2:
            # Save matched items
            matched_item = {
                "system": prompt,
                "instruction": data[i]["prompt2"],
                "input": "",
                "output": data[i]["secondanswer_content"],
                "history": [
                    [data[i]["prompt"], data[i]["firstanswer_content"]]
                ]
            }
            matched_items.append(matched_item)
        else:
            # Save mismatched items
            mismatched_item = {
                "item1": item1,
                "item2": item2
            }
            mismatched_items.append(mismatched_item)

    # Print the mismatched items
    print("Mismatched items:")
    for mismatched_item in mismatched_items:
        print(f"Item1: {mismatched_item['item1']}, Item2: {mismatched_item['item2']}")

    # Print the count of mismatched items
    print(f"Number of mismatched items: {len(mismatched_items)}")

    # Save matched items to a new JSON file
    with open('matched_items_path.json', 'w', encoding='utf-8') as f:
        json.dump(matched_items, f, ensure_ascii=False, indent=4)

# 使用函数
compare_and_save(list1, list2, ext_datas)
