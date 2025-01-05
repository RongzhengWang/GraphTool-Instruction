# <center> GraphTool-Instruction: Revolutionizing Graph Reasoning in LLMs through Decomposed Subtask Instruction.</center>


This repo contains the code, data, and models for "GraphTool-Instruction: Revolutionizing Graph Reasoning in LLMs through Decomposed Subtask Instruction."


## Brief Introduction 

This project aims to leverage **GraphTool-Instruction**, an innovative instruction-tuning approach that decomposes graph reasoning tasks into three subtasks (*graph extraction*, *tool name identification*, and *tool parameter extraction*) with specialized instructions for each. Using GraphTool-Instruction, we develop **GTools**, a dataset with twenty graph reasoning tasks, and create **GraphForge**, a graph reasoning LLM based on Llama3-8B. Experiments show that GraphTool-Instruction outperforms existing methods, and GraphForge, fine-tuned on GTools, achieves over 30% improvement compared to GPT-3.5-turbo (Function Calling). 

- **GraphTool-Instruction** We summarize LLMs-based graph reasoning methods and propose **GraphTool-Instruction.**, a novel GraphTool level Instruction-tuning method which first decomposes the graph reasoning task into three subtasks *graph extraction*, *tool name identification* and *parameter extraction* with corresponding Graph-Instruction, Task-Instruction and Parameter-Instruction. 
- **GTools and GraphForge.** We develop **GTools**, the first GraphTool-Instruction dataset comprising twenty types of graph reasoning tasks. GTools excels in both the variety of tasks and the scale of graphs, thus posing a greater challenge to LLMs in capturing graph structure information. Furthermore, we develop **GraphForge** based on Llama3-8B fine-tuned with GTools.
- **Improvements.** By incorporating Graph-Instruction and Parameter-Instruction, GraphTool-Instruction significantly improves the accuracy of Tool-Instruction, and achieves state-of-the-art results among all Tool-Instruction methods, except being 1% behind GPT-4o-FC.
- **New metrics.** We have introduced three new evaluation metrics: *Graph*, *Tool Name* and *Tool Parameter* to enhance the reliability of our dataset. Furthermore, we utilize the accuracy rates of these three metrics to deeply analyze the factors that affect the tool execution results.

<div align="center">
<img src="pics\method.png" width="800px">
</div>

**Notice:** For convenience, we have made the following definitions:
- To assess and enhance the capabilities of LLMs in processing graphs of various sizes, we establish a benchmark using the commonly accepted maximum token length of 4096 for current LLMs. This threshold serves to categorize graph sizes into:
  1. **WL-Graph**: *Within Limit Graph* ensures that the entire graph can be directly input into LLMs in textual form.
  2. **EL-Graph**: *Exceeds Limit Graph* accommodates larger graph structures and we store the graph in files with file paths provided to LLMs.
- For twenty graph reasoning tasks, we classify them into two primary categories:
  1. **BGA-Task**: *Basic Graph Analysis Task* which generally requires information on the graph structure and the tool name such as Cycle Detection.
  2. **PGQ-Task**:  *Parametric Graph Query Task* with the necessity for additional parameter inputs, *e.g.*, the Shortest Path necessitates the starting and ending nodes. 

And our entire work flow can be summarized as follows:

<div align="center">
<img src="pics\Flow.png" width="800px">
</div>


### Data Release

Please download our model using the following link: [Huggingface](https://huggingface.co/GraphTool/GraphTool-Instruction/tree/main). 
 

## Getting Started

<span id='all_catelogue'/>

### Table of Contents:
* <a href='#Code Structure'>1. Code Structure</a>
* <a href='#Environment Preparation'>2. Environment Preparation </a>
* <a href='#Graph Reasoning Task Preparation'>3. Graph Reasoning Task Preparation </a>
* <a href='#Evaluating GraphTool-Instruction'>4. Evaluating GraphTool-Instruction</a>
  * <a href='#Task-Instruction Preparation'>4.1. Task-Instruction Preparation</a>
  * <a href='#Reasoning on GraphForge'>4.2. Reasoning on GraphForge</a>
  * <a href='#Running Evaluation'>4.3. Running Evaluation</a>
* <a href='#Training GraphTool-Instruction'>5. Training GraphTool-Instruction </a>
  * <a href='#Prepare Pre-trained Checkpoint'>5.1. Prepare Pre-trained Checkpoint</a>
  * <a href='#LoRA Tuning'>5.2. LoRA Tuning</a>
  * <a href='#Export Model'>5.3. Export Model</a>
* <a href='#Function Calling Reasoning'>6. Function Calling Reasoning </a>
  * <a href='#GPT'>6.1. GPT</a>
  * <a href='#GLM'>6.2. GLM</a>



****



<span id='Code Structure'/>

### 1. Code Structure <a href='#all_catelogue'>[Back to Top]</a>

```
├── README.md
├── GTools
│   ├── Test
│   └── Train
├── GTools_Generation
│   ├── EL
│   ├── EL.bash
│   ├── WL
│   └── WL.bash
├── GraphForge
│   ├── GF_Graph_Instruction.py
│   ├── GF_Task_Instruction.py
│   └── GF_Task_Para_Instruction.py
├── GraphForge_test_WL
│   ├── Cycle_Detection
│   ├── ···
│   └── Triangle
├── Eval
│   ├── Cycle_Detection
│   ├── ···
│   └── Triangle
├── Instruction_template
│   ├── Graph_Instructon_EL.txt
│   ├── Graph_Instructon_WL.txt
│   ├── Para_Instructon.json
│   └── Task_Instructon.txt
├── Train
│   ├── dataset_info.json
│   ├── llama3_lora_sft_merge.yaml
│   └── llama3_lora_sft_train.yaml
├── Llama3
│   ├── Llama3_Graph_Instruction.py
│   ├── Llama3_Task_Instruction.py
│   └── Llama3_Task_Para_Instruction.py
├── Llama3.1
│   ├── Llama3.1_Graph_Instruction.py
│   ├── Llama3.1_Task_Instruction.py
│   └── Llama3.1_Task_Para_Instruction.py
├── GLM4
│   ├── GLM4_Graph_Instruction.py
│   ├── GLM4_Task_Instruction.py
│   └── GLM4_Task_Para_Instruction.py
├── Function_Calling
│   ├── GLM_FC.py
│   └── GPT_FC.py
└── requirements.txt


```


<span id='Environment Preparation'/>


### 2. Environment Preparation  <a href='#all_catelogue'>[Back to Top]</a>
Please first clone the repo and install the required environment, which can be done by running the following commands:
```shell
conda create -n GTI python=3.12

conda activate GTI

# Torch with CUDA 12.3
# Please clone our GraphTool-Instruction first, and switch to the directory.
cd GraphTool-Instruction
# Install required libraries
pip install -r requirements.txt
```

<span id='Graph Reasoning Task Preparation'/>



### 3. Graph Reasoning Task Preparation  <a href='#all_catelogue'>[Back to Top]</a>
We design graph task generation code for eleven categories, comprising a total of twenty tasks. During the generation process, we adhered to the following rules:

- **Diverse sizes**: For WL-Graph, we ensure that graphs cover a node range from 2 to 40 and an edge range for a maximum of 300 to examine the LLMs' capabilities to handle graph information. Additionally, EL-Graph accommodates larger structures, with node counts ranging from 41 to 100 and up to 1,000 edges.
- **Various descriptions**: For each graph reasoning task, we have prepared five different descriptions to evaluate the task identification capabilities of LLMs.
- **Balanced answers**: For graph reasoning tasks that determine truth or falsehood, we ensure an even distribution of answers during the graph generation process. This approach aims to prevent LLMs from developing a bias toward any particular type of result, thereby avoiding artificially high accuracy rates.
- **Unique answer**: For Topological Sorting, which may have multiple valid solutions, we ensure the uniqueness of the answers during the graph generation process. This facilitates the comparison between the LLMs' results and standard labels.

We have implemented graph task generation for WL graphs and EL graphs respectively. The structure of the code is as follows:


```shell

GTools_Generation
├── EL
│   └── ···
├── EL.bash
├── WL
│   ├── Cycle_Detection
│   │   ├── Cycle_gen_Di.py
│   │   └── Cycle_gen_Un.py
│   ├── Degree_Count
│   │   ├── Degree_gen_Di.py
│   │   └── Degree_gen_Un.py
│   ├── Edge_Count
│   │   ├── Edge_C_gen_Di.py
│   │   └── Edge_C_gen_Un.py
│   ├── Edge_Existence
│   │   ├── Edge_E_gen_Di.py
│   │   └── Edge_E_gen_Un.py
│   ├── Flow
│   │   ├── Flow_gen_Di.py
│   │   └── Flow_gen_Un.py
│   ├── Node_Count
│   │   ├── Node_C_gen_Di.py
│   │   └── Node_C_gen_Un.py
│   ├── Node_Existence
│   │   ├── Node_E_gen_Di.py
│   │   └── Node_E_gen_Un.py
│   ├── Path_Existence
│   │   ├── Path_E_gen_Di.py
│   │   └── Path_E_gen_Un.py
│   ├── Shortest_Path
│   │   ├── Shortest_gen_Di.py
│   │   └── Shortest_gen_Un.py
│   ├── Topo
│   │   └── Topo_gen_Di.py
│   └── Triangle
│       └── Triangle_gen.py
└── WL.bash

```
```shell
# To fill in the following path to generate WL size graph task!
output_path= GTools/Test/WL/Cycle_Detection/Di/cycle_Di.json
num_examples= 500

python GTools_Generation/WL/Cycle_Detection/Cycle_gen_Di.py --output_path ${output_path} --num_examples ${num_examples}
```


The code structure for EL graph generation is consistent with that of WL. In the process of generating EL graphs, we have additionally introduced an `output_dir`, a directory to save the edgelist files.

```shell
# To fill in the following path to generate EL size graph task!
output_path= GTools/Test/EL/Cycle_Detection/Di/cycle_Di.json
output_dir= GTools/Test/EL/Cycle_Detection/Di/data
num_examples= 500

python GTools_Generation/EL/Cycle_Detection/Cycle_gen_Di.py --output_path ${output_path} --num_examples ${num_examples} --output_dir ${output_dir}
```

You could also start the task generation by executing the `WL.sh` or `EL.sh` file.


---------


<span id='Evaluating GraphTool-Instruction'/>

## 4. Evaluating GraphTool-Instruction  <a href='#all_catelogue'>[Back to Top]</a>

<span id='Task-Instruction Preparation'/>

**Notice:** Due to the fact that we use 16 T4 GPUs running in parallel during the inference process, our execution script is not suitable for most users. Therefore, we recommend assigning specific tasks to specific GPUs and running each specific task separately.

#### 4.1. Task-Instruction Preparation <a href='#all_catelogue'>[Back to Top]</a>
To construct the Task-Instruction, we manually create a tool set. For each tool, we define four attributes: Tool Name, Tool Description, Tool Parameters and Return type. This set is intended to inform LLMs about the appropriate graph reasoning tasks for each tool. Based on the predefined tool set, we add some general descriptions of the expected format to constrain the output from LLMs. An example of the set of tools and general descriptions is presented as follows:
```shell
{'name': 'shortest_path', 
    'description': 'Given a graph G, a source node and a target node, compute shortest paths in the graph.', 
    'parameters': (graph = G, path_source= , path_target= ),
    'return_type': Int
  },
```

For PGQ-Tasks, we specifically employ Parameter-Instruction to further standardize the format of parameters extracted by Task-Instruction. At first, We propose *Tool Template Retriever*, which identifies the tool name based on previous Task-Instruction and then retrieves the corresponding tool template from the tool set. Second, we combine the searched tool template with Parameter-Instruction as a new input to get highly accurate tool parameters. An example of the Parameter-Instruction is presented as follows:
```shell
"shortest_path": 
    "The answer is correct, keep the original answer and the parameters' order, since I have get the API_Name so I only need you to provide API input strictly following my template definition.\nThe example is as follow:\n###\nAPI_Input: (graph = G, path_source=0 , path_target=1)\n###",
    
```



<span id='Reasoning on GraphForge'/>

#### 4.2. Reasoning on GraphForge<a href='#all_catelogue'>[Back to Top]</a>

Please download our model using the following link: [GraphForge](https://huggingface.co/GraphTool/GraphTool-Instruction/tree/main). And for reasoning on [Llama3](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct/tree/main), [Llama3.1](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct/tree/main) and [GLM4-9B](https://huggingface.co/THUDM/glm-4-9b-chat/tree/main), their models are also available with the corresponding links.

The structure of the GraphForge folder is as follows:
```shell
GraphForge
├── GF_Task_Para_Instruction.py
├── GF_Graph_Instruction.py
└── GF_Task_Instruction.py
```


```shell
# to fill in the following path to extract projector for the second tuning stage!
model_path= GraphForge/model
instruction_path= Instruction_template/Graph_Instructon_WL.txt
input_path= GTools/Test/WL/Cycle_Detection/Di/cycle_Di.json
output_path_graph= GraphForge_test_WL/Cycle_Detection/Di/ans_graph_Di.json
output_path_task= GraphForge_test_WL/Cycle_Detection/Di/ans_Di.json
tool_template= Instruction_template/Para_Instructon.json

# Graph Instruction on WL-Graph
python GraphForge/GF_Graph_Instruction.py --cuda_devices "0,1" \
    --model_path "${model_path}" \
    --instruction_path "${instruction_path}" \
    --output_path "${output_path_graph}" \
    --input_path "${input_path}"
    --max_new_tokens 4096 \
    --temperature 0.7 \
    --top_p 1


# Graph Instruction on EL-Graph, notice the path WL should be change to EL
python GraphForge/GF_Graph_Instruction.py --cuda_devices "2,3" \
    --model_path "${model_path}" \
    --instruction_path "${instruction_path}" \
    --output_path "${output_path_graph}" \
    --input_path "${input_path}"
    --max_new_tokens 4096 \
    --temperature 0.7 \
    --top_p 1


# Task Instruction for BGA-Task
python GraphForge/GF_Task_Instruction.py --cuda_devices "4,5" \
    --model_path "${model_path}" \
    --instruction_path "${instruction_path}" \
    --output_path "${output_path_task}" \
    --input_path "${input_path}" \
    --tool_template "${tool_template}" \
    --max_new_tokens 4096 \
    --temperature 0.7 \
    --top_p 1


# Task and Para Instruction for PGQ-Task
python GraphForge/GF_Task_Para_Instruction.py --cuda_devices "6,7" \
    --model_path "${model_path}" \
    --instruction_path "${instruction_path}" \
    --output_path "${output_path_task}" \
    --input_path "${input_path}" \
    --tool_template "${tool_template}" \
    --max_new_tokens 4096 \
    --temperature 0.7 \
    --top_p 1
```
---------


<span id='Running Evaluation'/>

#### 4.3. Running Evaluation <a href='#all_catelogue'>[Back to Top]</a>

The structure of the Eval folder is as follows:
```shell
Eval
├── Shortest_Path
│   ├── Shortest_eval_Di.py
│   └── Shortest_eval_Un.py
├── Path_Existence
│   ├── Path_E_eval_Un.py
│   └── Path_E_eval_Di.py
├── Edge_Existence
│   ├── Edge_E_eval_Di.py
│   └── Edge_E_eval_Un.py
├── Node_Count
│   ├── Node_C_eval_Di.py
│   └── Node_C_eval_Un.py
├── Topo
│   └── Topo_eval.py
├── Degree_Count
│   ├── Degree_eval_Di.py
│   └── Degree_eval_Un.py
├── Edge_Count
│   ├── Edge_C_eval_Un.py
│   └── Edge_C_eval_Di.py
├── Triangle
│   └── Triangle_eval.py
├── Cycle_Detection
│   ├── Cycle_eval_Un.py
│   └── Cycle_eval_Di.py
├── Flow
│   ├── Flow_eval_Di.py
│   └── Flow_eval_Un.py
└── Node_Existence
    ├── Node_E_eval_Un.py
    └── Node_E_eval_Di.py

```

We have set up individual Eval files for each task to record Total entries, Matched entries, Skipped entries, and Unmatched entries. For the unmatched entries, we will print the reason, which could be due to inaccuracies in graph extraction or parameter extraction. There is an example as below: 
```shell

#graph_path refers to the output_path of Graph Instruction
graph_path= GraphForge_test_WL/Cycle_Detection/Di/ans_graph_Di.json
#ans_path refers to the output_path of Task Instruction
ans_path= GraphForge_test_WL/Cycle_Detection/Di/ans_Di.json

python Eval/Cycle_Detection/Cycle_eval_Di.py  --graph_path ${graph_path} --ans_path ${ans_path} 

```
---------


<span id='Training GraphTool-Instruction'/>

### 5. Training GraphTool-Instruction <a href='#all_catelogue'>[Back to Top]</a>

GraphTool-Instruction tuning paradigm consists of two stages: (1) LLaMA-Factory Installation; (2) LoRA Tuning; (3) Export Model.

<span id='Prepare Pre-trained Checkpoint'/>

#### 5.1. LLaMA-Factory Installation  <a href='#all_catelogue'>[Back to Top]</a>
GraphTool-Instruction is trained based on LLaMA-Factory.
Please follow the instructions to prepare the LLaMA-Factory.

```shell
git clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e ".[torch,metrics]"
```

- `Llama3-8B-Instruction`:
  Prepare our base model Llama3, which is an instruction-tuned chatbot and base model in our implementation. Please download its weights [here](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct/tree/main). We generally use Llama3-8B-Instruction.


- `GTools Data`:
  GTools is a combination of all utilized Instruction-tuning data that contain three subtasks: *graph extraction, tool name identification and tool parameter extraction*. You can download by [Dataset](https://huggingface.co/GraphTool/GraphTool-Instruction/tree/main) and put it at repo path `GTools/Train`.

<span id='LoRA Tuning'/>

#### 5.2. LoRA Tuning  <a href='#all_catelogue'>[Back to Top]</a>

* **Prepare data:** Please download our instruction tuning data first. Our fine-tuning dataset follows the Alpaca format. To use LLaMA-Factory for model fine-tuning, we need to add the following three formats to the LLaMA-Factory/data/dataset_info.json path:


```shell
  "Graph": {
    "file_name": "${GTools/Train/Graph.json}",
    "columns": {
    "prompt": "instruction",
    "query": "input",
    "response": "output",
    "system": "system"
    }
  },
  "BGA": {
    "file_name": "${GTools/Train/BGA.json}",
    "columns": {
    "prompt": "instruction",
    "query": "input",
    "response": "output",
    "system": "system"
    }
  },
  "PGQ": {
    "file_name": "${GTools/Train/PGQ.json}",
    "columns": {
    "prompt": "instruction",
    "query": "input",
    "response": "output",
    "system": "system",
    "history": "history"
    }
  }
```




Use the following command to run LoRA **fine-tuning** of the Llama3-8B-Instruct model under the path: examples/train_lora/llama3_lora_sft.yaml. 

```shell
llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml
```


```shell
# Our fine-tuning parameter settings are as follows.
model_path= Llama3/model
output_model= Llama3/lora_weight

### model
model_name_or_path: ${model_path}

### method
stage: sft
do_train: true
finetuning_type: lora
lora_target: all

### dataset
dataset: Graph, BGA, PGQ
template: llama3
cutoff_len: 4096
max_samples: 100000
overwrite_cache: true
preprocessing_num_workers: 16

### output
output_dir: ${output_model}
logging_steps: 10
save_steps: 500
plot_loss: true
overwrite_output_dir: true

### train
per_device_train_batch_size: 2
gradient_accumulation_steps: 8
learning_rate: 1.0e-5
num_train_epochs: 3
lr_scheduler_type: cosine
warmup_ratio: 0.1
bf16: true
ddp_timeout: 180000000

### eval
val_size: 0.1
per_device_eval_batch_size: 1
eval_strategy: steps
eval_steps: 500

```

<span id='Export Model'/>

#### 5.3. Export Model  <a href='#all_catelogue'>[Back to Top]</a>

We could export model use the following command: 

```shell
llamafactory-cli export examples/merge_lora/llama3_lora_sft.yaml
```
```shell
# Our settings are as follows.
### model
model_name_or_path: Llama3/model
adapter_name_or_path: Llama3/lora_weight
template: llama3
finetuning_type: lora


### export
export_dir: GraphForge/model
export_size: 4
export_device: cpu
export_legacy_format: false

```


<span id='Function Calling Reasoning'/>

### 6. Function Calling Reasoning <a href='#all_catelogue'>[Back to Top]</a>

In order to compare with closed-source large models based on Function-Calling, we implemented `GPT_FC.py` and `GLM_FC.py` based on the Function-Calling tool list template.

<span id='GPT'/>

#### 6.1. GPT <a href='#all_catelogue'>[Back to Top]</a>
In order to run `GPT_FC.py`, you need to fill in the OpenAI API key first:
```shell
client = OpenAI(
   api_key="xxxxxxxxxxxxxxxx",
)
```

```shell
#graph_path refers to the output_path of Graph Instruction
graph_path= GTools/Test/WL/Cycle_Detection/Di/cycle_Di.json
#ans_path refers to the output_path of Task Instruction
ans_path= GPT_test_WL/Cycle_Detection/Di/ans_graph_Di.json

python Function_Calling/GPT_FC.py  --graph_path ${graph_path} --ans_path ${ans_path} 
```

<span id='GLM'/>

#### 6.2. GLM <a href='#all_catelogue'>[Back to Top]</a>
In order to run `GLM_FC.py`, you need to fill in the ZhipuAI key first:
```shell
client = ZhipuAI(api_key="xxxxxxxxxxxxxxxx") 
```

```shell
#graph_path refers to the output_path of Graph Instruction
graph_path= GTools/Test/WL/Cycle_Detection/Di/cycle_Di.json
#ans_path refers to the output_path of Task Instruction
ans_path= GLM_test_WL/Cycle_Detection/Di/ans_graph_Di.json

python Function_Calling/GLM_FC.py  --graph_path ${graph_path} --ans_path ${ans_path} 
```
