import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call a fish wearing a crown? King Neptune!",
    "Why don't eggs tell jokes? Because they might crack up!",
    "How do you organize a space party? You planet!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why did the tomato turn red? Because it saw the salad dressing!"
]

def tell_joke():
    if not jokes:
        print("No more jokes to tell!")
        return
    random_joke = random.choice(jokes)
    jokes.remove(random_joke)
    print(random_joke)

def ask_for_another_joke():
    answer = input("Do you want to hear another joke? (yes/no): ")
    if answer.lower() == "yes" or answer.lower() == "y":
        tell_joke()
        ask_for_another_joke()
    elif answer.lower() == "no" or answer.lower() == "n":
        print("Ok, grumpy pants")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        ask_for_another_joke()

tell_joke()
ask_for_another_joke()