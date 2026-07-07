# Task 2: FAQ Chatbot
# CodeAlpha AI Internship - June 2026

print("=== CodeAlpha FAQ Bot ===")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()
    
    if user == "bye":
        print("Bot: Goodbye!")
        break
    elif "internship" in user:
        print("Bot: CodeAlpha AI Internship duration is 1 month")
    elif "certificate" in user:
        print("Bot: Yes, you get certificate after completion")
    elif "task" in user:
        print("Bot: Complete 3 tasks and submit GitHub repo link")
    else:
        print("Bot: Sorry, I don't understand")