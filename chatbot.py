from matcher import get_best_answer

class Chatbot:
    def __init__(self, name="AIBot"):
        self.name = name

    def greet(self):
        return (
            f"👋 Hi! I'm {self.name}, your Artificial Intelligence FAQ assistant!\n"
            "Ask me anything about AI, Machine Learning, Deep Learning, and more.\n"
            "Type 'bye' or 'exit' to end the chat."
        )

    def farewell(self):
        return "👋 Goodbye! Hope I was helpful. Keep learning about AI! 🚀"

    def is_farewell(self, user_input):
        farewell_triggers = ["bye", "goodbye", "exit", "quit", "see you", "cya"]
        return user_input.lower().strip() in farewell_triggers

    def is_greeting(self, user_input):
        greeting_triggers = ["hi", "hello", "hey", "howdy", "what's up", "sup"]
        return user_input.lower().strip() in greeting_triggers

    def respond(self, user_input):
        if not user_input.strip():
            return "Please type a question! I'm here to help. 😊"
        if self.is_farewell(user_input):
            return self.farewell()
        if self.is_greeting(user_input):
            return "Hello! 😊 Feel free to ask me anything about Artificial Intelligence!"
        return get_best_answer(user_input)

if __name__ == "__main__":
    bot = Chatbot(name="AIBot")
    print(bot.greet())
    while True:
        user_input = input("You: ").strip()
        response = bot.respond(user_input)
        print(f"{bot.name}: {response}")
        if bot.is_farewell(user_input):
            break