print("================================")
print("       MY FIRST CHATBOT")
print("================================")
print("Hello! Welcome to my chatbot.")
print("Type 'bye' to exit the chat.")

while True:
    user = input("\nYou: ").lower().strip()

    if user == "hello":
        print("Bot: Hi! Nice to meet you!")

    elif user == "how are you":
        print("Bot: I'm fine, thanks! How are you?")

    elif user == "what is your name":
        print("Bot: My name is PyBot!")

    elif user == "what can you do":
        print("Bot: I can chat with you and answer simple questions!")

    elif user == "who created you":
        print("Bot: I was created using Python!")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")