import re, random
from colorama import init, Fore, Style

init(autoreset=True)

destinations = {
    'Beaches': ['Bali', 'Maldives', 'Phuket'],
    'Mountains': ['Swiss Alps', 'Rocky Mountains', 'Himalayas'],
    'Cities': ['Tokyo', 'Paris', 'New York']
}

jokes = [
    "Why don't programmers like nature? Too many bugs!"
    "Why did the computer go to the doctor? Because it had a virus!"
    "Why do travelers always feel warm? Because of their hot spots!"
]

def normalize_input(text):
    return re.sub(r'[^\w\s]', '', text).strip().lower()

def recommand():
    print(Fore.CYAN + "Travelbot: Beaches, Mountains or Cities?")
    preference = input(Fore.YELLOW + 'You: ')
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"Travelbot: What about {suggestion}?")
        print(Fore.CYAN + "Travelbot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + 'You: ').lower()

        if answer == 'yes':
            print(Fore.GREEN + f"Travelbot: Awesome! Enjoy your {suggestion}!")
        elif answer == 'no':
            print(Fore.RED + "Let's try another destination!")
        else:
            print(Fore.RED + "Let's try again")

def packing_tips():
    print(Fore.CYAN + "Travelbot: Where to?")
    location = normalize_input(input(Fore.YELLOW + 'You: '))
    print(Fore.CYAN + "Travelbot: How many days?")
    days = input(Fore.YELLOW + 'You: ')

    print(Fore.GREEN + f"Travelbot: Packing tips for {days} days in {location}")
    print(Fore.GREEN + "- Pack versatile clothes")
    print(Fore.GREEN + "- Bring chargers/adapters")
    print(Fore.GREEN + "- Check weather forecasts")

def tell_joke():
    print(Fore.YELLOW + f"Travelbot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "Travelbot: \nI can")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommenation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'Joke')")
    print(Fore.CYAN + "Type exit or bye to end. \n")

def chat():
    print(Fore.CYAN + "Hello! I'm Travelbot")
    name= input(Fore.YELLOW + "What's your name?")
    print(Fore.GREEN + "Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if 'recommand' in user_input or 'suggest' in user_input:
            recommand()
        elif 'pack' in user_input or 'packing' in user_input:
            packing_tips()
        elif 'joke' in user_input or 'funny' in user_input:
            tell_joke()
        elif 'help' in user_input:
            show_help()
        elif 'exit' in user_input or 'bye' in user_input:
            print(Fore.CYAN + "Travelbot: Safe Travels! Good bye!")
            break
        else:
            print(Fore.RED + "Travelbot: Could you rephrase?")

if __name__ == '__main__':
    chat()