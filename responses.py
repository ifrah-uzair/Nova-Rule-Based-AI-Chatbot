import random

greetings = [
    "Hello! Nice to meet you. 😊",
    "Hi! How can I help you today?",
    "Hey! Welcome back.",
    "Hello! Hope you're having a great day.",
    "Hi there! 😊"
]

jokes = [
    "Why do programmers prefer Python? Because it's simple and powerful!",
    "Why did the computer go to the doctor? It caught a virus!",
    "Why don't programmers like nature? Because it has too many bugs!",
    "Debugging is like being a detective in a crime movie where you are also the criminal.",
    "Why did the programmer quit his job? Because he didn't get arrays."
]

unknown = [
    "Sorry! I don't understand that.",
    "I'm still learning. Please try another command.",
    "Oops! I don't have an answer for that yet.",
    "Please type 'help' to see the available commands."
]


def greeting():
    return random.choice(greetings)


def joke():
    return random.choice(jokes)


def unknown_response():
    return random.choice(unknown)