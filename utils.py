from datetime import datetime


def show_banner():
    print("=" * 60)
    print("            RULE-BASED AI CHATBOT")
    print("=" * 60)
    print("Welcome!")
    print("A console-based Rule-Based AI Chatbot built with Python.")
    print("Type 'help' to view all supported commands.")
    print("=" * 60)


def show_help():

    def show_help():

     print("\n" + "=" * 60)
     print("                    HELP MENU")
     print("=" * 60)

    print("\n👋 Greeting Commands")
    print("  hello")
    print("  hi")
    print("  hey")

    print("\n💬 Conversation")
    print("  how are you")
    print("  what is your name")
    print("  my name")
    print("  who made you")
    print("  what can you do")

    print("\n🛠️ Utilities")
    print("  current time")
    print("  current date")
    print("  tell me a joke")
    print("  commands")

    print("\n📌 Other Commands")
    print("  thank you")
    print("  help")
    print("  bye")
    print("  exit")
    print("  quit")

    print("=" * 60)

def current_time():
    return datetime.now().strftime("%I:%M:%S %p")


def current_date():
    return datetime.now().strftime("%d %B %Y")