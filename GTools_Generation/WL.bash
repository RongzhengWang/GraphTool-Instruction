#!/bin/bash

# Define the first Python script and its parameters
PYTHON_SCRIPT_CYC_DI="WL/Cycle_Detection/Cycle_gen_Di.py"
OUTPUT_PATH_CYC_DI="../GTools/Test/WL/Cycle_Detection/Di/cycle_Di.json"
NUM_EXAMPLES_CYC_DI=10

# Define the second Python script and its parameters
PYTHON_SCRIPT_CYC_UN="WL/Cycle_Detection/Cycle_gen_Un.py"
OUTPUT_PATH_CYC_UN="../GTools/Test/WL/Cycle_Detection/Un/cycle_Un.json"
NUM_EXAMPLES_CYC_UN=10

# Define the third Python script and its parameters
PYTHON_SCRIPT_DEG_DI="WL/Degree_Count/Degree_gen_Di.py"
OUTPUT_PATH_DEG_DI="../GTools/Test/WL/Degree_Count/Di/degree_Di.json"
NUM_EXAMPLES_DEG_DI=10

# Define the fourth Python script and its parameters
PYTHON_SCRIPT_DEG_UN="WL/Degree_Count/Degree_gen_Un.py"
OUTPUT_PATH_DEG_UN="../GTools/Test/WL/Degree_Count/Un/degree_Un.json"
NUM_EXAMPLES_DEG_UN=10

# Define the fifth Python script and its parameters
PYTHON_SCRIPT_EDGE_C_DI="WL/Edge_Count/Edge_C_gen_Di.py"
OUTPUT_PATH_EDGE_C_DI="../GTools/Test/WL/Edge_Count/Di/edge_c_Di.json"
NUM_EXAMPLES_EDGE_C_DI=10

# Define the sixth Python script and its parameters
PYTHON_SCRIPT_EDGE_C_UN="WL/Edge_Count/Edge_C_gen_Un.py"
OUTPUT_PATH_EDGE_C_UN="../GTools/Test/WL/Edge_Count/Un/edge_c_Un.json"
NUM_EXAMPLES_EDGE_C_UN=10

# Define the seventh Python script and its parameters
PYTHON_SCRIPT_EDGE_E_DI="WL/Edge_Existence/Edge_E_gen_Di.py"
OUTPUT_PATH_EDGE_E_DI="../GTools/Test/WL/Edge_Existence/Di/edge_Di.json"
NUM_EXAMPLES_EDGE_E_DI=10

# Define the eighth Python script and its parameters
PYTHON_SCRIPT_EDGE_E_UN="WL/Edge_Existence/Edge_E_gen_Un.py"
OUTPUT_PATH_EDGE_E_UN="../GTools/Test/WL/Edge_Existence/Un/edge_Un.json"
NUM_EXAMPLES_EDGE_E_UN=10

# Define the ninth Python script and its parameters
PYTHON_SCRIPT_FLOW_DI="WL/Flow/Flow_gen_Di.py"
OUTPUT_PATH_FLOW_DI="../GTools/Test/WL/Flow/Di/flow_Di.json"
NUM_EXAMPLES_FLOW_DI=10

# Define the tenth Python script and its parameters
PYTHON_SCRIPT_FLOW_UN="WL/Flow/Flow_gen_Un.py"
OUTPUT_PATH_FLOW_UN="../GTools/Test/WL/Flow/Un/flow_Un.json"
NUM_EXAMPLES_FLOW_UN=10

# Define the eleventh Python script and its parameters
PYTHON_SCRIPT_NODE_C_DI="WL/Node_Count/Node_C_gen_Di.py"
OUTPUT_PATH_NODE_C_DI="../GTools/Test/WL/Node_Count/Di/node_c_Di.json"
NUM_EXAMPLES_NODE_C_DI=10

# Define the twelfth Python script and its parameters
PYTHON_SCRIPT_NODE_C_UN="WL/Node_Count/Node_C_gen_Un.py"
OUTPUT_PATH_NODE_C_UN="../GTools/Test/WL/Node_Count/Un/node_c_Un.json"
NUM_EXAMPLES_NODE_C_UN=10

# Define the thirteenth Python script and its parameters
PYTHON_SCRIPT_NODE_E_DI="WL/Node_Existence/Node_E_gen_Di.py"
OUTPUT_PATH_NODE_E_DI="../GTools/Test/WL/Node_Existence/Di/node_e_Di.json"
NUM_EXAMPLES_NODE_E_DI=10

# Define the fourteenth Python script and its parameters
PYTHON_SCRIPT_NODE_E_UN="WL/Node_Existence/Node_E_gen_Un.py"
OUTPUT_PATH_NODE_E_UN="../GTools/Test/WL/Node_Existence/Un/node_e_Un.json"
NUM_EXAMPLES_NODE_E_UN=10

# Define the fifteenth Python script and its parameters
PYTHON_SCRIPT_PATH_E_DI="WL/Path_Existence/Path_E_gen_Di.py"
OUTPUT_PATH_PATH_E_DI="../GTools/Test/WL/Path_Existence/Di/path_Di.json"
NUM_EXAMPLES_PATH_E_DI=10

# Define the sixteenth Python script and its parameters
PYTHON_SCRIPT_PATH_E_UN="WL/Path_Existence/Path_E_gen_Un.py"
OUTPUT_PATH_PATH_E_UN="../GTools/Test/WL/Path_Existence/Un/path_Un.json"
NUM_EXAMPLES_PATH_E_UN=10

# Define the seventeenth Python script and its parameters
PYTHON_SCRIPT_SHORTEST_DI="WL/Shortest_Path/Shortest_gen_Di.py"
OUTPUT_PATH_SHORTEST_DI="../GTools/Test/WL/Shortest_Path/Di/shortest_Di.json"
NUM_EXAMPLES_SHORTEST_DI=10

# Define the eighteenth Python script and its parameters
PYTHON_SCRIPT_SHORTEST_UN="WL/Shortest_Path/Shortest_gen_Un.py"
OUTPUT_PATH_SHORTEST_UN="../GTools/Test/WL/Shortest_Path/Un/shortest_Un.json"
NUM_EXAMPLES_SHORTEST_UN=10

# Define the nineteenth Python script and its parameters
PYTHON_SCRIPT_TOPO_DI="WL/Topo/Topo_gen_Di.py"
OUTPUT_PATH_TOPO_DI="../GTools/Test/WL/Topo/topo.json"
NUM_EXAMPLES_TOPO_DI=10

# Define the twentieth Python script and its parameters
PYTHON_SCRIPT_TRIANGLE="WL/Triangle/Triangle_gen.py"
OUTPUT_PATH_TRIANGLE="../GTools/Test/WL/Triangle/triangle.json"
NUM_EXAMPLES_TRIANGLE=10

# Execute the first Python script and pass parameters
python3 $PYTHON_SCRIPT_CYC_DI --output_path $OUTPUT_PATH_CYC_DI --num_examples $NUM_EXAMPLES_CYC_DI

# Execute the second Python script and pass parameters
python3 $PYTHON_SCRIPT_CYC_UN --output_path $OUTPUT_PATH_CYC_UN --num_examples $NUM_EXAMPLES_CYC_UN

# Execute the third Python script and pass parameters
python3 $PYTHON_SCRIPT_DEG_DI --output_path $OUTPUT_PATH_DEG_DI --num_examples $NUM_EXAMPLES_DEG_DI

# Execute the fourth Python script and pass parameters
python3 $PYTHON_SCRIPT_DEG_UN --output_path $OUTPUT_PATH_DEG_UN --num_examples $NUM_EXAMPLES_DEG_UN

# Execute the fifth Python script and pass parameters
python3 $PYTHON_SCRIPT_EDGE_C_DI --output_path $OUTPUT_PATH_EDGE_C_DI --num_examples $NUM_EXAMPLES_EDGE_C_DI

# Execute the sixth Python script and pass parameters
python3 $PYTHON_SCRIPT_EDGE_C_UN --output_path $OUTPUT_PATH_EDGE_C_UN --num_examples $NUM_EXAMPLES_EDGE_C_UN

# Execute the seventh Python script and pass parameters
python3 $PYTHON_SCRIPT_EDGE_E_DI --output_path $OUTPUT_PATH_EDGE_E_DI --num_examples $NUM_EXAMPLES_EDGE_E_DI

# Execute the eighth Python script and pass parameters
python3 $PYTHON_SCRIPT_EDGE_E_UN --output_path $OUTPUT_PATH_EDGE_E_UN --num_examples $NUM_EXAMPLES_EDGE_E_UN

# Execute the ninth Python script and pass parameters
python3 $PYTHON_SCRIPT_FLOW_DI --output_path $OUTPUT_PATH_FLOW_DI --num_examples $NUM_EXAMPLES_FLOW_DI

# Execute the tenth Python script and pass parameters
python3 $PYTHON_SCRIPT_FLOW_UN --output_path $OUTPUT_PATH_FLOW_UN --num_examples $NUM_EXAMPLES_FLOW_UN

# Execute the eleventh Python script and pass parameters
python3 $PYTHON_SCRIPT_NODE_C_DI --output_path $OUTPUT_PATH_NODE_C_DI --num_examples $NUM_EXAMPLES_NODE_C_DI

# Execute the twelfth Python script and pass parameters
python3 $PYTHON_SCRIPT_NODE_C_UN --output_path $OUTPUT_PATH_NODE_C_UN --num_examples $NUM_EXAMPLES_NODE_C_UN

# Execute the thirteenth Python script and pass parameters
python3 $PYTHON_SCRIPT_NODE_E_DI --output_path $OUTPUT_PATH_NODE_E_DI --num_examples $NUM_EXAMPLES_NODE_E_DI

# Execute the fourteenth Python script and pass parameters
python3 $PYTHON_SCRIPT_NODE_E_UN --output_path $OUTPUT_PATH_NODE_E_UN --num_examples $NUM_EXAMPLES_NODE_E_UN

# Execute the fifteenth Python script and pass parameters
python3 $PYTHON_SCRIPT_PATH_E_DI --output_path $OUTPUT_PATH_PATH_E_DI --num_examples $NUM_EXAMPLES_PATH_E_DI

# Execute the sixteenth Python script and pass parameters
python3 $PYTHON_SCRIPT_PATH_E_UN --output_path $OUTPUT_PATH_PATH_E_UN --num_examples $NUM_EXAMPLES_PATH_E_UN

# Execute the seventeenth Python script and pass parameters
python3 $PYTHON_SCRIPT_SHORTEST_DI --output_path $OUTPUT_PATH_SHORTEST_DI --num_examples $NUM_EXAMPLES_SHORTEST_DI

# Execute the eighteenth Python script and pass parameters
python3 $PYTHON_SCRIPT_SHORTEST_UN --output_path $OUTPUT_PATH_SHORTEST_UN --num_examples $NUM_EXAMPLES_SHORTEST_UN

# Execute the nineteenth Python script and pass parameters
python3 $PYTHON_SCRIPT_TOPO_DI --output_path $OUTPUT_PATH_TOPO_DI --num_examples $NUM_EXAMPLES_TOPO_DI

# Execute the twentieth Python script and pass parameters
python3 $PYTHON_SCRIPT_TRIANGLE --output_path $OUTPUT_PATH_TRIANGLE --num_examples $NUM_EXAMPLES_TRIANGLE
