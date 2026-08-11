from datetime import datetime

print("🤖 Chatbot: Hello! I am your AI Chatbot.")
print("Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("🤖 Chatbot: Hello! Nice to meet you.")

    elif user_input == "how are you":
        print("🤖 Chatbot: I'm doing great! How about you?")

    elif user_input == "what is your name":
        print("🤖 Chatbot: My name is CodeAlpha Chatbot.")

    elif user_input == "who made you":
        print("🤖 Chatbot: I was created using Python for the CodeAlpha Internship.")

    elif user_input == "what can you do":
        print("🤖 Chatbot: I can answer simple questions, tell the date and time, and chat with you.")

    elif user_input == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print("🤖 Chatbot: The current time is", current_time)

    elif user_input == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("🤖 Chatbot: Today's date is", current_date)

    elif user_input == "thank you":
        print("🤖 Chatbot: You're welcome!")

    elif user_input == "bye":
        print("🤖 Chatbot: Goodbye! Have a great day!")
        break

    else:
        print("🤖 Chatbot: Sorry, I don't understand that. Please try another question.")