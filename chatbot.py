# Rule-Based AI Chatbot

print("🤖 AI Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    # Greetings
    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    # Asking name
    elif "your name" in user:
        print("Bot: I am DecodeLabs AI Chatbot.")

    # Asking about AI
    elif "what is ai" in user:
        print("Bot: AI stands for Artificial Intelligence.")

    # Asking about internship
    elif "internship" in user:
        print("Bot: DecodeLabs provides AI industrial training.")

    # Help command
    elif "help" in user:
        print("Bot: You can ask me about AI, internship, or greetings.")

    # Exit condition
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day 🚀")
        break

    # Default response
    else:
        print("Bot: Sorry, I don't understand that.")