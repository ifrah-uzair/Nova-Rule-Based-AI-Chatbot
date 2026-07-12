from responses import greeting, joke, unknown_response
from utils import show_banner, show_help, current_time, current_date


def start_chat():

    # Welcome Banner
    show_banner()

    # User Name
    user_name = input("Enter your name: ").strip()

    print("\n" + "=" * 50)
    print(f"Hello, {user_name}! 👋")
    print("I'm Nova, your Rule-Based AI Assistant.")
    print("Type 'help' to see all available commands.")
    print("Type 'bye' anytime to exit.")
    print("=" * 50)

    # Count commands
    commands_used = 0

    # Chat Loop
    while True:

        user_input = input("\nYou : ").lower().strip()

        commands_used += 1

        # Exit
        if user_input == "bye" or user_input == "exit" or user_input == "quit":

            print("\n" + "=" * 50)
            print("           SESSION ENDED")
            print("=" * 50)
            print(f"Goodbye, {user_name}! 👋")
            print("Thank you for using Nova.")
            print(f"Total Commands Used : {commands_used}")
            print("Have a wonderful day!")
            print("=" * 50)
            break

        # Greetings
        elif user_input == "hello" or user_input == "hi" or user_input == "hey":

           print("\n🤖 Nova")
           print("-" * 35)
           print(greeting())

        # Small Talk
        elif user_input == "how are you":

            print("\n🤖 Nova")
            print("-" * 35)
            print("I'm doing great! 😄")
            print("Thanks for asking.")

        # Bot Name
        elif user_input == "what is your name":

            print("\n🤖 Nova")
            print("-" * 35)
            print("My name is Nova.")
            print("I'm a Rule-Based AI Assistant built with Python.")

        elif user_input == "my name":

            print("\n🤖 Nova")
            print("-" * 35)
            print(f"Your name is {user_name}.")

        # Creator
        elif user_input == "who made you":

            print("\n🤖 Nova")
            print("-" * 35)
            print("I was developed by Ifrah Uzair.")
            print("This project is built using Python..")

        # Capabilities
        elif user_input == "what can you do":

            print("\n🤖 Nova")
            print("-" * 35)
            print("I can perform the following tasks:\n")
            print("• Greet you")
            print("• Tell the current time")
            print("• Tell today's date")
            print("• Tell random programming jokes")
            print("• Show the help menu")
            print("• Count commands used")
            print("• Exit politely")

        # Current Time
        elif user_input == "current time":

            print("\n🤖 Nova")
            print("-" * 35)
            print("Current Time :", current_time())

        # Current Date
        elif user_input == "current date":

            print("\n🤖 Nova")
            print("-" * 35)
            print("Today's Date :", current_date())

        # Joke
        elif user_input == "tell me a joke":

            print("\n🤖 Nova")
            print("-" * 35)
            print(joke())

        # Commands Used
        elif user_input == "commands":

            print("\n🤖 Nova")
            print("-" * 35)
            print(f"You have used {commands_used} commands.")

        # Thank You
        elif user_input == "thank you" or user_input == "thanks":

            print("\n🤖 Nova")
            print("-" * 35)
            print("You're welcome! 😊")
            print("Happy to help.")

        # Help
        elif user_input == "help":

            show_help()

        # Unknown Command
        else:

            print("\n🤖 Nova")
            print("-" * 35)
            print(unknown_response())
            print("Type 'help' to see the available commands.")