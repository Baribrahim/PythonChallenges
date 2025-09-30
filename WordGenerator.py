import random

wordbank = [
    "python", "variable", "function", "object", "compile",
    "hangman", "wizard", "jungle", "puzzle", "rocket",
    "galaxy", "nebula", "planet", "asteroid", "comet",
    "castle", "sword", "dragon", "knight", "quest",
    "forest", "ocean", "desert", "island", "mountain",
    "banana", "guitar", "piano", "violin", "trumpet",
    "zebra", "penguin", "giraffe", "dolphin", "kangaroo",
    "mystery", "adventure", "treasure", "pyramid", "labyrinth",
    "shadow", "phantom", "ghost", "skeleton", "zombie",
    "energy", "gravity", "fractal", "quantum", "neutron",
    "coffee", "chocolate", "sandwich", "pancake", "cookie",
    "smile", "friendship", "happiness", "freedom", "courage"
]

class WordGenerator:
    def __init__(self):
        self.random_word = random.choice(wordbank)

    def get_random_word(self):
        return self.random_word

print("\U0001f600 You win!")

print("\U0001F923 You lost! Haha, the word was " + chosenWord)

userinput = userinput.lower()

if livesCounter == 3:
    print("Clue: " + chosenWord[0:1])