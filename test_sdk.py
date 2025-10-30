from litellm import completion
import litellm


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
    }
]

messages = [{"role": "user", "content": "What's the weather like in Boston today?"}]


response = completion(
    model="ollama_chat/gemma3n:e2b", messages=messages, tools=tools, stream=True
)
print(response)

for chunk in response:
    print(chunk["choices"][0]["delta"].content, end="", flush=True)
print()
