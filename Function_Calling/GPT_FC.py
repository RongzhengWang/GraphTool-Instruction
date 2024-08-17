import json
from openai import OpenAI
from tqdm import tqdm
import os
import argparse

#GPT_MODEL = 'gpt-4o-2024-05-13'
GPT_MODEL = "gpt-3.5-turbo-0125"

client = OpenAI(
   api_key="",
)

def chat_completion_request(messages, tools=None, model=GPT_MODEL):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            max_tokens=8192,
            tool_choice='required',
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e

tools = [ 
    {
        "type": "function",
        "function": {
            "name": "cycle_check_graphExistance",
            "description": "Given a graph G, returns whether a graph G contains a cycle.",
            "parameters": {
                "type": "object",
                "properties": {
                    "G": {
                        "type": "string",
                        "description": "The graph G is the graph object specified in the problem, where the graph object is a list. For example:[(0, 1), (0, 2), (0, 5), (0, 6), (0, 8), (0, 10)]",
                    },
                },
                "required": ["G"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "number_of_edges_graphCount",
            "description": "Given a graph G, returns the whole number of all edges.",
            "parameters": {
                "type": "object",
                "properties": {
                    "G": {
                        "type": "string",
                        "description": "The graph G is the graph object specified in the problem, where the graph object is a list. For example:[(0, 1), (0, 2), (0, 5), (0, 6), (0, 8), (0, 10)]",
                    },
                },
                "required": ["G"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "number_of_nodes_graphCount",
            "description": "Given a graph G, returns the number of nodes in the graph.",
            "parameters": {
                "type": "object",
                "properties": {
                    "G": {
                        "type": "string",
                        "description": "The graph G is the graph object specified in the problem, where the graph object is a list. For example:[(0, 1), (0, 2), (0, 5), (0, 6), (0, 8), (0, 10)]",
                    },
                },
                "required": ["G"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "maximum_triangle_sum",
            "description": "Given a graph G, find the maximum sum of weights for any connected triplet of nodes.",
            "parameters": {
                "type": "object",
                "properties": {
                    "G": {
                        "type": "string",
                        "description": "The graph G is the graph object specified in the problem, where the graph object is a list. For example:[(0, 1, {'weight': 1}), (0, 5, {'weight': 9}), (0, 6, {'weight': 6}), (0, 7, {'weight': 2}), (0, 8, {'weight': 2}), (0, 9, {'weight': 9}), (0, 10, {'weight': 5}), (0, 2, {'weight': 9})]",
                    },
                },
                "required": ["G"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "topological_sort",
            "description": "Given a graph G, find a topological ordering of nodes in a directed acyclic graph G.",
            "parameters": {
                "type": "object",
                "properties": {
                    "G": {
                        "type": "string",
                        "description": "The graph G is the graph object specified in the problem, where the graph object is a list. For example:[(0, 1), (0, 2), (0, 5), (0, 6), (0, 8), (0, 10)]",
                    },
                },
                "required": ["G"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "is_path_graphExistance",
            "description": "Given a graph G and an path, returns whether or not the specified path exists.",
            "parameters": {
                "type": "object",
                "properties": {
                    "G": {
                        "type": "string",
                        "description": "The graph G is the graph object specified in the problem, where the graph object is a list. For example:[(0, 1), (0, 2), (0, 5), (0, 6), (0, 8), (0, 10)]",
                    },
                    "path_source": {
                        "type": "integer", 
                        "description": "The source node of the path.",
                    },
                    "path_target": {
                        "type": "integer", 
                        "description": "The target node of the path.",
                    },
                },
                "required": ["G","path_source","path_target"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "is_edge_graphExistance",
            "description": "Given a graph G and an edge, returns whether or not the specified edge exists.",
            "parameters": {
                "type": "object",
                "properties": {
                    "G": {
                        "type": "string",
                        "description": "The graph G is the graph object specified in the problem, where the graph object is a list. For example:[(0, 1), (0, 2), (0, 5), (0, 6), (0, 8), (0, 10)]",
                    },
                    "edge_source": {
                        "type": "integer", 
                        "description": "The source node of the edge.",
                    },
                    "edge_target": {
                        "type": "integer", 
                        "description": "The target node of the edge.",
                    },
                },
                "required": ["G","edge_source","edge_target"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "shortest_path",
            "description": "Given a graph G, a source node and a target node, compute shortest paths in the graph.",
            "parameters": {
                "type": "object",
                "properties": {
                    "G": {
                        "type": "string",
                        "description": "The graph G is the graph object specified in the problem, where the graph object is a list. For example:[(0, 1, {'weight': 1}), (0, 5, {'weight': 9}), (0, 6, {'weight': 6}), (0, 7, {'weight': 2}), (0, 8, {'weight': 2}), (0, 9, {'weight': 9}), (0, 10, {'weight': 5}), (0, 2, {'weight': 9})]",
                    },
                    "path_source": {
                        "type": "integer", 
                        "description": "The source node of the path.",
                    },
                    "path_target": {
                        "type": "integer", 
                        "description": "The target node of the path.",
                    },
                },
                "required": ["G","path_source","path_target"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "maximum_flow",
            "description": "Given a graph G, a source node and a sink node, compute the maximum flow from the source node to the sink node in the graph.",
            "parameters": {
                "type": "object",
                "properties": {
                    "G": {
                        "type": "string",
                        "description": "The graph G is the graph object specified in the problem, where the graph object is a list. For example:[(0, 1, {'capacity': 59}), (0, 4, {'capacity': 91}), (0, 5, {'capacity': 13}), (0, 6, {'capacity': 88}), (0, 7, {'capacity': 60})]",
                    },
                    "source_node": {
                        "type": "integer", 
                        "description": "The source node of the path.",
                    },
                    "sink_node": {
                        "type": "integer", 
                        "description": "The target node of the path.",
                    },
                },
                "required": ["G","source_node","sink_node"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "degree_graphCount",
            "description": "Given a graph G and a single node, returns a degree view of single node.",
            "parameters": {
                "type": "object",
                "properties": {
                    "G": {
                        "type": "string",
                        "description": "The graph G is the graph object specified in the problem, where the graph object is a list. For example:[(0, 1), (0, 2), (0, 5), (0, 6), (0, 8), (0, 10)]",
                    },
                    "node": {
                        "type": "integer", 
                        "description": "The single node of which need to be count.",
                    }
                },
                "required": ["G","node"],
            },
        }
    },
]

def main(input_path, output_path):
    data = []
    if os.path.exists(output_path):
        with open(output_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []

    with open(input_path, 'r', encoding='utf-8') as file:
        files = json.load(file)

    cnt = 0

    for obj in tqdm(files):
        cnt += 1
        message = obj['prompt']
        answer = obj['answer']
        messages = []
        messages.append({"role": "system", "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous. You should give me the full Graph, with the list format. For example:[(0, 1, {'weight': 1}), (0, 5, {'weight': 9}), (0, 6, {'weight': 6}), (0, 7, {'weight': 2}), (0, 8, {'weight': 2}), (0, 9, {'weight': 9}), (0, 10, {'weight': 5}), (0, 2, {'weight': 9})]"})
        messages.append({"role": "user", "content": message})
        chat_response = chat_completion_request(messages, tools=tools)
        print(chat_response)

        if isinstance(chat_response, Exception):
            # Skip the current iteration if an error occurred
            continue

        assistant_message = chat_response.choices[0].message

        # Convert the response to a serializable format
        chat_response_serializable = {
            "id": chat_response.id,
            "choices": [{
                "message": {
                    "role": assistant_message.role,
                    "content": assistant_message.content,
                    "function_call": {
                        "name": assistant_message.function_call.name,
                        "arguments": assistant_message.function_call.arguments
                    } if assistant_message.function_call else None,
                    "tool_calls": [{
                        "id": tool_call.id,
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments
                        }
                    } for tool_call in assistant_message.tool_calls] if assistant_message.tool_calls else []
                }
            }],
            "created": chat_response.created,
            "model": chat_response.model,
            "object": chat_response.object
        }

        data.append({
            'prompt': message,
            'output': chat_response_serializable,
            'answer': answer,
        })

        with open(output_path, 'w') as file:
            json.dump(data, file, indent=4)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate chat completions for graph problems.")
    parser.add_argument('--input_path', type=str, required=True, help='Path to the input JSON file with graph problems.')
    parser.add_argument('--output_path', type=str, required=True, help='Path to save the generated chat completions.')

    args = parser.parse_args()

    main(args.input_path, args.output_path)
