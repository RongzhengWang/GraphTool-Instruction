#!/bin/bash

# Define the first Python script and its parameters
PYTHON_SCRIPT_CYC_DI="EL/Cycle_Detection/Cycle_gen_Di.py"
OUTPUT_PATH_CYC_DI="../GTools/Test/EL/Cycle_Detection/Di/cycle_Di.json"
NUM_EXAMPLES_CYC_DI=10
OUTPUT_DIR_CYC_DI="../GTools/Test/EL/Cycle_Detection/Di/data"

# Define the second Python script and its parameters
PYTHON_SCRIPT_CYC_UN="EL/Cycle_Detection/Cycle_gen_Un.py"
OUTPUT_PATH_CYC_UN="../GTools/Test/EL/Cycle_Detection/Un/cycle_Un.json"
NUM_EXAMPLES_CYC_UN=10
OUTPUT_DIR_CYC_UN="../GTools/Test/EL/Cycle_Detection/Un/data"

# Define the third Python script and its parameters
PYTHON_SCRIPT_DEG_DI="EL/Degree_Count/Degree_gen_Di.py"
OUTPUT_PATH_DEG_DI="../GTools/Test/EL/Degree_Count/Di/degree_Di.json"
NUM_EXAMPLES_DEG_DI=10
OUTPUT_DIR_DEG_DI="../GTools/Test/EL/Degree_Count/Di/data"

# Define the fourth Python script and its parameters
PYTHON_SCRIPT_DEG_UN="EL/Degree_Count/Degree_gen_Un.py"
OUTPUT_PATH_DEG_UN="../GTools/Test/EL/Degree_Count/Un/degree_Un.json"
NUM_EXAMPLES_DEG_UN=10
OUTPUT_DIR_DEG_UN="../GTools/Test/EL/Degree_Count/Un/data"

# Define the fifth Python script and its parameters
PYTHON_SCRIPT_EDGE_C_DI="EL/Edge_Count/Edge_C_gen_Di.py"
OUTPUT_PATH_EDGE_C_DI="../GTools/Test/EL/Edge_Count/Di/edge_c_Di.json"
NUM_EXAMPLES_EDGE_C_DI=10
OUTPUT_DIR_EDGE_C_DI="../GTools/Test/EL/Edge_Count/Di/data"

# Define the sixth Python script and its parameters
PYTHON_SCRIPT_EDGE_C_UN="EL/Edge_Count/Edge_C_gen_Un.py"
OUTPUT_PATH_EDGE_C_UN="../GTools/Test/EL/Edge_Count/Un/edge_c_Un.json"
NUM_EXAMPLES_EDGE_C_UN=10
OUTPUT_DIR_EDGE_C_UN="../GTools/Test/EL/Edge_Count/Un/data"

# Define the seventh Python script and its parameters
PYTHON_SCRIPT_EDGE_E_DI="EL/Edge_Existence/Edge_E_gen_Di.py"
OUTPUT_PATH_EDGE_E_DI="../GTools/Test/EL/Edge_Existence/Di/edge_Di.json"
NUM_EXAMPLES_EDGE_E_DI=10
OUTPUT_DIR_EDGE_E_DI="../GTools/Test/EL/Edge_Existence/Di/data"

# Define the eighth Python script and its parameters
PYTHON_SCRIPT_EDGE_E_UN="EL/Edge_Existence/Edge_E_gen_Un.py"
OUTPUT_PATH_EDGE_E_UN="../GTools/Test/EL/Edge_Existence/Un/edge_Un.json"
NUM_EXAMPLES_EDGE_E_UN=10
OUTPUT_DIR_EDGE_E_UN="../GTools/Test/EL/Edge_Existence/Un/data"

# Define the ninth Python script and its parameters
PYTHON_SCRIPT_FLOW_DI="EL/Flow/Flow_gen_Di.py"
OUTPUT_PATH_FLOW_DI="../GTools/Test/EL/Flow/Di/flow_Di.json"
NUM_EXAMPLES_FLOW_DI=10
OUTPUT_DIR_FLOW_DI="../GTools/Test/EL/Flow/Di/data"

# Define the tenth Python script and its parameters
PYTHON_SCRIPT_FLOW_UN="EL/Flow/Flow_gen_Un.py"
OUTPUT_PATH_FLOW_UN="../GTools/Test/EL/Flow/Un/flow_Un.json"
NUM_EXAMPLES_FLOW_UN=10
OUTPUT_DIR_FLOW_UN="../GTools/Test/EL/Flow/Un/data"

# Define the eleventh Python script and its parameters
PYTHON_SCRIPT_NODE_C_DI="EL/Node_Count/Node_C_gen_Di.py"
OUTPUT_PATH_NODE_C_DI="../GTools/Test/EL/Node_Count/Di/node_c_Di.json"
NUM_EXAMPLES_NODE_C_DI=10
OUTPUT_DIR_NODE_C_DI="../GTools/Test/EL/Node_Count/Di/data"

# Define the twelfth Python script and its parameters
PYTHON_SCRIPT_NODE_C_UN="EL/Node_Count/Node_C_gen_Un.py"
OUTPUT_PATH_NODE_C_UN="../GTools/Test/EL/Node_Count/Un/node_c_Un.json"
NUM_EXAMPLES_NODE_C_UN=10
OUTPUT_DIR_NODE_C_UN="../GTools/Test/EL/Node_Count/Un/data"

# Define the thirteenth Python script and its parameters
PYTHON_SCRIPT_NODE_E_DI="EL/Node_Existence/Node_E_gen_Di.py"
OUTPUT_PATH_NODE_E_DI="../GTools/Test/EL/Node_Existence/Di/node_e_Di.json"
NUM_EXAMPLES_NODE_E_DI=10
OUTPUT_DIR_NODE_E_DI="../GTools/Test/EL/Node_Existence/Di/data"

# Define the fourteenth Python script and its parameters
PYTHON_SCRIPT_NODE_E_UN="EL/Node_Existence/Node_E_gen_Un.py"
OUTPUT_PATH_NODE_E_UN="../GTools/Test/EL/Node_Existence/Un/node_e_Un.json"
NUM_EXAMPLES_NODE_E_UN=10
OUTPUT_DIR_NODE_E_UN="../GTools/Test/EL/Node_Existence/Un/data"

# Define the fifteenth Python script and its parameters
PYTHON_SCRIPT_PATH_E_DI="EL/Path_Existence/Path_E_gen_Di.py"
OUTPUT_PATH_PATH_E_DI="../GTools/Test/EL/Path_Existence/Di/path_Di.json"
NUM_EXAMPLES_PATH_E_DI=10
OUTPUT_DIR_PATH_E_DI="../GTools/Test/EL/Path_Existence/Di/data"

# Define the sixteenth Python script and its parameters
PYTHON_SCRIPT_PATH_E_UN="EL/Path_Existence/Path_E_gen_Un.py"
OUTPUT_PATH_PATH_E_UN="../GTools/Test/EL/Path_Existence/Un/path_Un.json"
NUM_EXAMPLES_PATH_E_UN=10
OUTPUT_DIR_PATH_E_UN="../GTools/Test/EL/Path_Existence/Un/data"

# Define the seventeenth Python script and its parameters
PYTHON_SCRIPT_SHORTEST_DI="EL/Shortest_Path/Shortest_gen_Di.py"
OUTPUT_PATH_SHORTEST_DI="../GTools/Test/EL/Shortest_Path/Di/shortest_Di.json"
NUM_EXAMPLES_SHORTEST_DI=10
OUTPUT_DIR_SHORTEST_DI="../GTools/Test/EL/Shortest_Path/Di/data"

# Define the eighteenth Python script and its parameters
PYTHON_SCRIPT_SHORTEST_UN="EL/Shortest_Path/Shortest_gen_Un.py"
OUTPUT_PATH_SHORTEST_UN="../GTools/Test/EL/Shortest_Path/Un/shortest_Un.json"
NUM_EXAMPLES_SHORTEST_UN=10
OUTPUT_DIR_SHORTEST_UN="../GTools/Test/EL/Shortest_Path/Un/data"

# Define the nineteenth Python script and its parameters
PYTHON_SCRIPT_TOPO_DI="EL/Topo/Topo_gen_Di.py"
OUTPUT_PATH_TOPO_DI="../GTools/Test/EL/Topo/topo.json"
NUM_EXAMPLES_TOPO_DI=10
OUTPUT_DIR_TOPO_DI="../GTools/Test/EL/Topo/data"

# Define the twentieth Python script and its parameters
PYTHON_SCRIPT_TRIANGLE="EL/Triangle/Triangle_gen.py"
OUTPUT_PATH_TRIANGLE="../GTools/Test/EL/Triangle/triangle.json"
NUM_EXAMPLES_TRIANGLE=10
OUTPUT_DIR_TRIANGLE="../GTools/Test/EL/Triangle/data"

# Execute the first Python script and pass parameters
python3 $PYTHON_SCRIPT_CYC_DI --output_path $OUTPUT_PATH_CYC_DI --output_dir $OUTPUT_DIR_CYC_DI --num_examples $NUM_EXAMPLES_CYC_DI

# Execute the second Python script and pass parameters
python3 $PYTHON_SCRIPT_CYC_UN --output_path $OUTPUT_PATH_CYC_UN --output_dir $OUTPUT_DIR_CYC_UN --num_examples $NUM_EXAMPLES_CYC_UN

# Execute the third Python script and pass parameters
python3 $PYTHON_SCRIPT_DEG_DI --output_path $OUTPUT_PATH_DEG_DI --output_dir $OUTPUT_DIR_DEG_DI --num_examples $NUM_EXAMPLES_DEG_DI

# Execute the fourth Python script and pass parameters
python3 $PYTHON_SCRIPT_DEG_UN --output_path $OUTPUT_PATH_DEG_UN --output_dir $OUTPUT_DIR_DEG_UN --num_examples $NUM_EXAMPLES_DEG_UN

# Execute the fifth Python script and pass parameters
python3 $PYTHON_SCRIPT_EDGE_C_DI --output_path $OUTPUT_PATH_EDGE_C_DI --output_dir $OUTPUT_DIR_EDGE_C_DI --num_examples $NUM_EXAMPLES_EDGE_C_DI

# Execute the sixth Python script and pass parameters
python3 $PYTHON_SCRIPT_EDGE_C_UN --output_path $OUTPUT_PATH_EDGE_C_UN --output_dir $OUTPUT_DIR_EDGE_C_UN --num_examples $NUM_EXAMPLES_EDGE_C_UN

# Execute the seventh Python script and pass parameters
python3 $PYTHON_SCRIPT_EDGE_E_DI --output_path $OUTPUT_PATH_EDGE_E_DI --output_dir $OUTPUT_DIR_EDGE_E_DI --num_examples $NUM_EXAMPLES_EDGE_E_DI

# Execute the eighth Python script and pass parameters
python3 $PYTHON_SCRIPT_EDGE_E_UN --output_path $OUTPUT_PATH_EDGE_E_UN --output_dir $OUTPUT_DIR_EDGE_E_UN --num_examples $NUM_EXAMPLES_EDGE_E_UN

# Execute the ninth Python script and pass parameters
python3 $PYTHON_SCRIPT_FLOW_DI --output_path $OUTPUT_PATH_FLOW_DI --output_dir $OUTPUT_DIR_FLOW_DI --num_examples $NUM_EXAMPLES_FLOW_DI

# Execute the tenth Python script and pass parameters
python3 $PYTHON_SCRIPT_FLOW_UN --output_path $OUTPUT_PATH_FLOW_UN --output_dir $OUTPUT_DIR_FLOW_UN --num_examples $NUM_EXAMPLES_FLOW_UN

# Execute the eleventh Python script and pass parameters
python3 $PYTHON_SCRIPT_NODE_C_DI --output_path $OUTPUT_PATH_NODE_C_DI --output_dir $OUTPUT_DIR_NODE_C_DI --num_examples $NUM_EXAMPLES_NODE_C_DI

# Execute the twelfth Python script and pass parameters
python3 $PYTHON_SCRIPT_NODE_C_UN --output_path $OUTPUT_PATH_NODE_C_UN --output_dir $OUTPUT_DIR_NODE_C_UN --num_examples $NUM_EXAMPLES_NODE_C_UN

# Execute the thirteenth Python script and pass parameters
python3 $PYTHON_SCRIPT_NODE_E_DI --output_path $OUTPUT_PATH_NODE_E_DI --output_dir $OUTPUT_DIR_NODE_E_DI --num_examples $NUM_EXAMPLES_NODE_E_DI

# Execute the fourteenth Python script and pass parameters
python3 $PYTHON_SCRIPT_NODE_E_UN --output_path $OUTPUT_PATH_NODE_E_UN --output_dir $OUTPUT_DIR_NODE_E_UN --num_examples $NUM_EXAMPLES_NODE_E_UN

# Execute the fifteenth Python script and pass parameters
python3 $PYTHON_SCRIPT_PATH_E_DI --output_path $OUTPUT_PATH_PATH_E_DI --output_dir $OUTPUT_DIR_PATH_E_DI --num_examples $NUM_EXAMPLES_PATH_E_DI

# Execute the sixteenth Python script and pass parameters
python3 $PYTHON_SCRIPT_PATH_E_UN --output_path $OUTPUT_PATH_PATH_E_UN --output_dir $OUTPUT_DIR_PATH_E_UN --num_examples $NUM_EXAMPLES_PATH_E_UN

# Execute the seventeenth Python script and pass parameters
python3 $PYTHON_SCRIPT_SHORTEST_DI --output_path $OUTPUT_PATH_SHORTEST_DI --output_dir $OUTPUT_DIR_SHORTEST_DI --num_examples $NUM_EXAMPLES_SHORTEST_DI

# Execute the eighteenth Python script and pass parameters
python3 $PYTHON_SCRIPT_SHORTEST_UN --output_path $OUTPUT_PATH_SHORTEST_UN --output_dir $OUTPUT_DIR_SHORTEST_UN --num_examples $NUM_EXAMPLES_SHORTEST_UN

# Execute the nineteenth Python script and pass parameters
python3 $PYTHON_SCRIPT_TOPO_DI --output_path $OUTPUT_PATH_TOPO_DI --output_dir $OUTPUT_DIR_TOPO_DI --num_examples $NUM_EXAMPLES_TOPO_DI

# Execute the twentieth Python script and pass parameters
python3 $PYTHON_SCRIPT_TRIANGLE --output_path $OUTPUT_PATH_TRIANGLE --output_dir $OUTPUT_DIR_TRIANGLE --num_examples $NUM_EXAMPLES_TRIANGLE
