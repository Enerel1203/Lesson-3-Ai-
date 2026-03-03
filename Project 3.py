import re
import random
from colorama import init, Fore, Style
from datetime import datetime

init(autoreset=True)

destinations = {
    'beaches': ['Bali', 'Maldives', 'Phuket'],
    'mountains': ['Swiss Alps', 'Rocky Mountains', 'Himalayas'],
    'cities': ['Tokyo', 'Paris', 'New York']
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of their hot spots!"
]

def normalize_input(text):
    return re.sub(r'[^\w\s]', '', text).strip().lower()

def recommand():
    print(Fore.CYAN + "Travelbot: Do you prefer Beaches, Mountains or Cities?")
    preference = normalize_input(input(Fore.YELLOW + 'You: '))
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"Travelbot: What about {suggestion}?")
        answer = input(Fore.CYAN + "Do you like it? (yes/no): ").lower()
        if answer == 'yes':
            print(Fore.GREEN + f"Travelbot: Awesome! Enjoy your {suggestion}!")
        else:
            print(Fore.RED + "Travelbot: Let's try another destination next time!")

def packing_tips():
    print(Fore.CYAN + "Travelbot: Where are you going?")
    location = normalize_input(input(Fore.YELLOW + 'You: '))
    print(Fore.CYAN + "Travelbot: How many days will you stay?")
    days = input(Fore.YELLOW + 'You: ')
    print(Fore.GREEN + f"Travelbot: Packing tips for {days} days in {location.capitalize()}:")
    print(Fore.GREEN + "- Pack versatile clothes")
    print(Fore.GREEN + "- Bring chargers/adapters")
    print(Fore.GREEN + "- Check weather forecasts")

def tell_joke():
    print(Fore.YELLOW + f"Travelbot: {random.choice(jokes)}")

def show_weather():
    cities = ['Tokyo', 'Paris', 'New York', 'Bali', 'Swiss Alps']
    city = random.choice(cities)
    temp = random.randint(15, 35)
    print(Fore.CYAN + f"Travelbot: The current weather in {city} is {temp}°C and sunny!")

def show_news():
    headlines = [
        "Travel restrictions are easing in many countries.",
        "New tropical resort opens in Maldives.",
        "Tech conferences are back in-person this year."
    ]
    print(Fore.CYAN + f"Travelbot: News Update: {random.choice(headlines)}")

def show_time():
    city_times = {
        'Tokyo': 9,
        'Paris': 1,
        'New York': -4
    }
    city = random.choice(list(city_times.keys()))
    hour = (datetime.utcnow().hour + city_times[city]) % 24
    print(Fore.CYAN + f"Travelbot: Current local time in {city} is {hour}:00 hours")

def show_help():
    print(Fore.MAGENTA + "Travelbot: I can help you with:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommend')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.GREEN + "- Show weather info (say 'weather')")
    print(Fore.GREEN + "- Show news updates (say 'news')")
    print(Fore.GREEN + "- Show local time (say 'time')")
    print(Fore.CYAN + "Type exit or bye to end the chat.\n")

def chat():
    print(Fore.CYAN + "Hello! I'm Travelbot")
    name = input(Fore.YELLOW + "What's your name? ").strip()
    if not name:
        name = "Traveler"
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = normalize_input(input(Fore.YELLOW + f"{name}: "))
        if 'recommend' in user_input or 'suggest' in user_input:
            recommand()
        elif 'pack' in user_input or 'packing' in user_input:
            packing_tips()
        elif 'joke' in user_input or 'funny' in user_input:
            tell_joke()
        elif 'weather' in user_input:
            show_weather()
        elif 'news' in user_input:
            show_news()
        elif 'time' in user_input:
            show_time()
        elif 'help' in user_input:
            show_help()
        elif 'exit' in user_input or 'bye' in user_input:
            print(Fore.CYAN + "Travelbot: Safe Travels! Goodbye!")
            break
        else:
            print(Fore.RED + "Travelbot: Could you rephrase that?")

if __name__ == "__main__":
    chat()