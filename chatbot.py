import nltk
from nltk.chat.util import Chat, reflections

# Pairs of patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello! How can I assist you today?"]],
    [r"what is your name\??", ["I'm Chatbot! What's your name?"]],
    [r"my name is (.*)", ["Nice to meet you, %1! How can I help you?"]],
    [r"how are you\??", ["I'm just a program, but I'm doing great! How about you?"]],
    [r"sorry (.*)", ["No problem at all. How can I assist you?"]],
    [r"I am (.*)", ["Why do you say you are %1?"]],
    [r"bye|goodbye", ["Goodbye! Have a great day!"]],
    [r"(.*)", ["I'm not sure I understand that. Can you rephrase?"]]
]

# Initialize Chatbot
def basic_chatbot():
    print("Chatbot: Hi! I'm a basic chatbot. Type 'bye' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    basic_chatbot()

