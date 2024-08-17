#!/bin/bash

# 定义第一个Python脚本及其参数
PYTHON_SCRIPT_CYC_DI="GTools_Generation/WL/Cycle_Detection/Cycle_gen_Di.py"
OUTPUT_PATH_CYC_DI="GTools/Test/WL/Cycle_Detection/Di/cycle_Di.json"
NUM_EXAMPLES_CYC_DI=500

# 定义第二个Python脚本及其参数
PYTHON_SCRIPT_CYC_UN="GTools_Generation/WL/Cycle_Detection/Cycle_gen_Un.py"
OUTPUT_PATH_CYC_UN="GTools/Test/WL/Cycle_Detection/Un/cycle_Un.json"
NUM_EXAMPLES_CYC_UN=500

# 定义第三个Python脚本及其参数
PYTHON_SCRIPT_DEG_DI="GTools_Generation/WL/Degree_Count/Degree_gen_Di.py"
OUTPUT_PATH_DEG_DI="GTools/Test/WL/Degree_Count/Di/degree_Di.json"
NUM_EXAMPLES_DEG_DI=500

# 定义第四个Python脚本及其参数
PYTHON_SCRIPT_DEG_UN="GTools_Generation/WL/Degree_Count/Degree_gen_Un.py"
OUTPUT_PATH_DEG_UN="GTools/Test/WL/Degree_Count/Un/degree_Un.json"
NUM_EXAMPLES_DEG_UN=500

# 定义第五个Python脚本及其参数
PYTHON_SCRIPT_EDGE_C_DI="GTools_Generation/WL/Edge_Count/Edge_C_gen_Di.py"
OUTPUT_PATH_EDGE_C_DI="GTools/Test/WL/Edge_Count/Di/edge_c_Di.json"
NUM_EXAMPLES_EDGE_C_DI=500

# 定义第六个Python脚本及其参数
PYTHON_SCRIPT_EDGE_C_UN="GTools_Generation/WL/Edge_Count/Edge_C_gen_Un.py"
OUTPUT_PATH_EDGE_C_UN="GTools/Test/WL/Edge_Count/Un/edge_c_Un.json"
NUM_EXAMPLES_EDGE_C_UN=500

# 定义第七个Python脚本及其参数
PYTHON_SCRIPT_EDGE_E_DI="GTools_Generation/WL/Edge_Existence/Edge_E_gen_Di.py"
OUTPUT_PATH_EDGE_E_DI="GTools/Test/WL/Edge_Existence/Di/edge_Di.json"
NUM_EXAMPLES_EDGE_E_DI=500

# 定义第八个Python脚本及其参数
PYTHON_SCRIPT_EDGE_E_UN="GTools_Generation/WL/Edge_Existence/Edge_E_gen_Un.py"
OUTPUT_PATH_EDGE_E_UN="GTools/Test/WL/Edge_Existence/Un/edge_Un.json"
NUM_EXAMPLES_EDGE_E_UN=500

# 定义第九个Python脚本及其参数
PYTHON_SCRIPT_FLOW_DI="GTools_Generation/WL/Flow/Flow_gen_Di.py"
OUTPUT_PATH_FLOW_DI="GTools/Test/WL/Flow/Di/flow_Di.json"
NUM_EXAMPLES_FLOW_DI=500

# 定义第十个Python脚本及其参数
PYTHON_SCRIPT_FLOW_UN="GTools_Generation/WL/Flow/Flow_gen_Un.py"
OUTPUT_PATH_FLOW_UN="GTools/Test/WL/Flow/Un/flow_Un.json"
NUM_EXAMPLES_FLOW_UN=500

# 定义第十一个Python脚本及其参数
PYTHON_SCRIPT_NODE_C_DI="GTools_Generation/WL/Node_Count/Node_C_gen_Di.py"
OUTPUT_PATH_NODE_C_DI="GTools/Test/WL/Node_Count/Di/node_c_Di.json"
NUM_EXAMPLES_NODE_C_DI=500

# 定义第十二个Python脚本及其参数
PYTHON_SCRIPT_NODE_C_UN="GTools_Generation/WL/Node_Count/Node_C_gen_Un.py"
OUTPUT_PATH_NODE_C_UN="GTools/Test/WL/Node_Count/Un/node_c_Un.json"
NUM_EXAMPLES_NODE_C_UN=500

# 定义第十三个Python脚本及其参数
PYTHON_SCRIPT_NODE_E_DI="GTools_Generation/WL/Node_Existence/Node_E_gen_Di.py"
OUTPUT_PATH_NODE_E_DI="GTools/Test/WL/Node_Existence/Di/node_e_Di.json"
NUM_EXAMPLES_NODE_E_DI=500

# 定义第十四个Python脚本及其参数
PYTHON_SCRIPT_NODE_E_UN="GTools_Generation/WL/Node_Existence/Node_E_gen_Un.py"
OUTPUT_PATH_NODE_E_UN="GTools/Test/WL/Node_Existence/Un/node_e_Un.json"
NUM_EXAMPLES_NODE_E_UN=500

# 定义第十五个Python脚本及其参数
PYTHON_SCRIPT_PATH_E_DI="GTools_Generation/WL/Path_Existence/Path_E_gen_Di.py"
OUTPUT_PATH_PATH_E_DI="GTools/Test/WL/Path_Existence/Di/path_Di.json"
NUM_EXAMPLES_PATH_E_DI=500

# 定义第十六个Python脚本及其参数
PYTHON_SCRIPT_PATH_E_UN="GTools_Generation/WL/Path_Existence/Path_E_gen_Un.py"
OUTPUT_PATH_PATH_E_UN="GTools/Test/WL/Path_Existence/Un/path_Un.json"
NUM_EXAMPLES_PATH_E_UN=500

# 定义第十七个Python脚本及其参数
PYTHON_SCRIPT_SHORTEST_DI="GTools_Generation/WL/Shortest_Path/Shortest_gen_Di.py"
OUTPUT_PATH_SHORTEST_DI="GTools/Test/WL/Shortest_Path/Di/shortest_Di.json"
NUM_EXAMPLES_SHORTEST_DI=500

# 定义第十八个Python脚本及其参数
PYTHON_SCRIPT_SHORTEST_UN="GTools_Generation/WL/Shortest_Path/Shortest_gen_Un.py"
OUTPUT_PATH_SHORTEST_UN="GTools/Test/WL/Shortest_Path/Un/shortest_Un.json"
NUM_EXAMPLES_SHORTEST_UN=500

# 定义第十九个Python脚本及其参数
PYTHON_SCRIPT_TOPO_DI="GTools_Generation/WL/Topo/Topo_gen_Di.py"
OUTPUT_PATH_TOPO_DI="GTools/Test/WL/Topo/topo.json"
NUM_EXAMPLES_TOPO_DI=500

# 定义第二十个Python脚本及其参数
PYTHON_SCRIPT_TRIANGLE="GTools_Generation/WL/Triangle/Triangle_gen.py"
OUTPUT_PATH_TRIANGLE="GTools/Test/WL/Triangle/triangle.json"
NUM_EXAMPLES_TRIANGLE=500

# 执行第一个Python脚本并传递参数
python3 $PYTHON_SCRIPT_CYC_DI --output_path $OUTPUT_PATH_CYC_DI --num_examples $NUM_EXAMPLES_CYC_DI

# 执行第二个Python脚本并传递参数
python3 $PYTHON_SCRIPT_CYC_UN --output_path $OUTPUT_PATH_CYC_UN --num_examples $NUM_EXAMPLES_CYC_UN

# 执行第三个Python脚本并传递参数
python3 $PYTHON_SCRIPT_DEG_DI --output_path $OUTPUT_PATH_DEG_DI --num_examples $NUM_EXAMPLES_DEG_DI

# 执行第四个Python脚本并传递参数
python3 $PYTHON_SCRIPT_DEG_UN --output_path $OUTPUT_PATH_DEG_UN --num_examples $NUM_EXAMPLES_DEG_UN

# 执行第五个Python脚本并传递参数
python3 $PYTHON_SCRIPT_EDGE_C_DI --output_path $OUTPUT_PATH_EDGE_C_DI --num_examples $NUM_EXAMPLES_EDGE_C_DI

# 执行第六个Python脚本并传递参数
python3 $PYTHON_SCRIPT_EDGE_C_UN --output_path $OUTPUT_PATH_EDGE_C_UN --num_examples $NUM_EXAMPLES_EDGE_C_UN

# 执行第七个Python脚本并传递参数
python3 $PYTHON_SCRIPT_EDGE_E_DI --output_path $OUTPUT_PATH_EDGE_E_DI --num_examples $NUM_EXAMPLES_EDGE_E_DI

# 执行第八个Python脚本并传递参数
python3 $PYTHON_SCRIPT_EDGE_E_UN --output_path $OUTPUT_PATH_EDGE_E_UN --num_examples $NUM_EXAMPLES_EDGE_E_UN

# 执行第九个Python脚本并传递参数
python3 $PYTHON_SCRIPT_FLOW_DI --output_path $OUTPUT_PATH_FLOW_DI --num_examples $NUM_EXAMPLES_FLOW_DI

# 执行第十个Python脚本并传递参数
python3 $PYTHON_SCRIPT_FLOW_UN --output_path $OUTPUT_PATH_FLOW_UN --num_examples $NUM_EXAMPLES_FLOW_UN

# 执行第十一个Python脚本并传递参数
python3 $PYTHON_SCRIPT_NODE_C_DI --output_path $OUTPUT_PATH_NODE_C_DI --num_examples $NUM_EXAMPLES_NODE_C_DI

# 执行第十二个Python脚本并传递参数
python3 $PYTHON_SCRIPT_NODE_C_UN --output_path $OUTPUT_PATH_NODE_C_UN --num_examples $NUM_EXAMPLES_NODE_C_UN

# 执行第十三个Python脚本并传递参数
python3 $PYTHON_SCRIPT_NODE_E_DI --output_path $OUTPUT_PATH_NODE_E_DI --num_examples $NUM_EXAMPLES_NODE_E_DI

# 执行第十四个Python脚本并传递参数
python3 $PYTHON_SCRIPT_NODE_E_UN --output_path $OUTPUT_PATH_NODE_E_UN --num_examples $NUM_EXAMPLES_NODE_E_UN

# 执行第十五个Python脚本并传递参数
python3 $PYTHON_SCRIPT_PATH_E_DI --output_path $OUTPUT_PATH_PATH_E_DI --num_examples $NUM_EXAMPLES_PATH_E_DI

# 执行第十六个Python脚本并传递参数
python3 $PYTHON_SCRIPT_PATH_E_UN --output_path $OUTPUT_PATH_PATH_E_UN --num_examples $NUM_EXAMPLES_PATH_E_UN

# 执行第十七个Python脚本并传递参数
python3 $PYTHON_SCRIPT_SHORTEST_DI --output_path $OUTPUT_PATH_SHORTEST_DI --num_examples $NUM_EXAMPLES_SHORTEST_DI

# 执行第十八个Python脚本并传递参数
python3 $PYTHON_SCRIPT_SHORTEST_UN --output_path $OUTPUT_PATH_SHORTEST_UN --num_examples $NUM_EXAMPLES_SHORTEST_UN

# 执行第十九个Python脚本并传递参数
python3 $PYTHON_SCRIPT_TOPO_DI --output_path $OUTPUT_PATH_TOPO_DI --num_examples $NUM_EXAMPLES_TOPO_DI

# 执行第二十个Python脚本并传递参数
python3 $PYTHON_SCRIPT_TRIANGLE --output_path $OUTPUT_PATH_TRIANGLE --num_examples $NUM_EXAMPLES_TRIANGLE
