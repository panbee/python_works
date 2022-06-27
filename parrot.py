# message = input("Tell me something, and I will repeat it back to you:")
# print(message)

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat's your first name?"
# prompt += "\n"

# name = input(prompt)
# print("\nHello, " + name + '!')

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
prompt += "\n"

message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print("\n" + message)