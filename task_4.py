#Basic Chatbot 
def chatbot():
    print("Chatbot: Hello! I'm your simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ['hi', 'hello', 'hey']:
            print("Chatbot: Hi!")
        elif user_input in ['how are you?', 'how are you', 'how do you do']:
            print("Chatbot: I'm fine, thanks!")
        elif user_input in ['bye', 'goodbye', 'exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()
