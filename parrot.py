# message = raw_input("tell me something and I will repeat it back to you: ")
# print(message)

message = input("Tell me something and I will repeat it back to you: ")
print(message)

# for some reason this only works in the terminal with python3  cannot be python parrot.py


prompt = "if you tell us who you are we can personalize your message"
prompt += "\nWhat is your name?"

name = input(prompt)
print("\nHello "+ name)


# for python2.7 you use raw_input instead of input...
