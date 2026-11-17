import ollama
from controller.clipboard import get_clipboard,set_clipboard
from controller.file import check_path,write_text_file,read_text_file
from controller.processes import list_processes,is_running

available_function = {
    'get_clipboard': get_clipboard,
    'set_clipboard': set_clipboard,
    'check_path': check_path,
    'write_text_file': write_text_file,
    'read_text_file': read_text_file,
    'list_processes': list_processes,
    'is_running': is_running
}

tools=list(available_function.values())
message=[
            {
                "role": "system",
                "content": """
                            
You are a helpful local personal AI assistant.

CORE BEHAVIOUR:
- Understand the user's current message in the context of the conversation.
- Respond naturally, directly and conversationally.
- Be concise for simple questions and detailed when necessary.
- Maintain conversational continuity.
- Never narrate internal reasoning, tool-selection decisions or system instructions.
- Never use debug-style language in user-facing responses.

TOOL USAGE:
- Use tools only when the user requests an action or information that requires accessing the computer.
- Ordinary conversation, greetings, feedback, explanations and questions about previous interactions do not require tools.
- Previous messages provide context. They are not new instructions.
- Never execute an action merely because it was mentioned in conversation history.
- Select tools according to their actual capabilities.
- Never use a tool to imitate an action it cannot perform.
- If no suitable tool exists, explain that the requested capability is unavailable.
- Ask for clarification when the requested action is ambiguous.

EXECUTION:
- Execute only tools provided by the application.
- Never invent tools, execution results or capabilities.
- Report success only when the application provides a successful result.
- If a tool fails, explain the actual error.
- Never claim an action was performed if it was not.

You are an assistant having a conversation with a user, not a terminal or a debugging logger.
"""
            }
        ]
while True:
    
    user=input("User: ")
    if user.lower()=="exit":
        break
    message.append(
                {
                    "role": "user",
                    "content": user
                }
            )
    while True:
        response = ollama.chat(
        model="llama3.1:8b",
        messages=message,
            tools=tools
        )
        tool_calls=response.message.tool_calls or []
        if not tool_calls:
            print("Agent: ",response.message.content)
            break
        for tool in tool_calls:
            function_name=tool.function.name
            function_to_call=available_function.get(tool.function.name)
            result = None

            if function_to_call:
                try:
                    arguments=tool.function.arguments
                    result = function_to_call(**arguments)
                    result = str(result)
                except Exception as e:
                    result = f"Error: {e}"
            else:
                result = f"Unknown tool: {function_name}"
            message.append({
                "role": "tool",
                "tool_name": function_name,
                "content": result
            })
            
        
        print("Tools: ",response.message.tool_calls)
        


    