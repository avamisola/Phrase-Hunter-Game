# Create your Game class logic in here.


import random

from phrasehunter.phrase import Phrase


class Game():

    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("Hello world"),
            Phrase("How are you"),
            Phrase("Thank you"),
            Phrase("No problem"),
            Phrase("Good luck")
            ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("""\n
========================
Welcome to Phrase Hunter
-Guess the phrase one letter at a time to win.
-If you guess wrong 5 times, you lose.
========================
        """)

    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f"\nNumber missed: {self.missed}\n")
            Phrase.display(self.active_phrase, self.guesses)
            self.user_guess = self.get_guess()
            self.guesses.append(self.user_guess)
            self.active_phrase.check_guess(self.user_guess)
            if self.active_phrase.check_guess(self.user_guess):
                print("\nCorrect!")
            else:
                self.missed += 1
                print("\nNope, try again!")
        self.game_over()

    def get_guess(self):
        return input("\n\nEnter a single letter: ")
    
    def game_over(self):
        if self.missed == 5:
            print("\nYou have made 5 wrong guesses! Sorry, you lose!\n")
        else:
            print("\nYou have guessed the phrase! Congratulations, you win!\n")
