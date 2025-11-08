
# Step1: Create a prompt for "mood checker game" in which include all types of mood & this game will be created in python.
# (it will generate mood checker prompt for python code)
# Step2: Use this prompt and create mood checker game by asking mood from user in python.git.
# (Results are below)

import sys

def get_mood_response(mood):
    """
    Determines the appropriate response based on the user's mood.
    """
    mood = mood.lower()
    
    happy_moods = ["happy", "joyful", "excited", "great", "good", "cheerful"]
    sad_moods = ["sad", "unhappy", "down", "blue", "gloomy"]
    angry_moods = ["angry", "mad", "furious", "irritated", "annoyed"]
    anxious_moods = ["anxious", "worried", "stressed", "nervous"]
    tired_moods = ["tired", "sleepy", "exhausted", "drained"]
    bored_moods = ["bored", "uninterested", "dull"]
    calm_moods = ["calm", "relaxed", "peaceful", "content"]

    if mood in happy_moods:
        return "That's wonderful to hear! Keep that positive energy going. Here's a fun fact: A group of flamingos is called a 'flamboyance'!"
    elif mood in sad_moods:
        return "I'm sorry you're feeling this way. Remember that tough times don't last, but tough people do. Maybe listening to your favorite song could help lift your spirits."
    elif mood in angry_moods:
        return "It's okay to feel angry sometimes. Take a few deep breaths and try to focus on something that calms you down. Maybe step away from the situation for a moment."
    elif mood in anxious_moods:
        return "I understand that feeling. Try this simple grounding exercise: name 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste."
    elif mood in tired_moods:
        return "It sounds like you need some rest. Your body and mind deserve a break. A short nap or a good night's sleep can make a world of difference."
    elif mood in bored_moods:
        return "Boredom is a canvas for creativity! Why not try learning a new 5-minute recipe, sketching something, or planning a fun future activity?"
    elif mood in calm_moods:
        return "It's great that you're feeling calm and at peace. Enjoy this moment of tranquility and let it recharge you."
    else:
        return "I don't recognize that feeling, but I hope you have a good day nonetheless!"

def mood_checker_game():
    """
    Main function to run the mood checker game.
    """
    print("--- Welcome to the Mood Checker Game! ---")
    print("You can enter your mood to get a response, or type 'quit' or 'exit' to end the game.")
    
    while True:
        user_input = input("\nHow are you feeling today? ")
        
        if user_input.lower() in ["quit", "exit"]:
            print("Thank you for playing. Goodbye!")
            sys.exit()
            
        response = get_mood_response(user_input)
        print(response)

if __name__ == "__main__":
    mood_checker_game()
