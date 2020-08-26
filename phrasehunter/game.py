# Create your Game class logic in here.

import random

from phrasehunter.phrase import Phrase


class Game():

    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase('Hello world'),
            Phrase('How are you'),
            Phrase('Thank you'),
            Phrase('No problem'),
            Phrase('Good luck')
            ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def get_random_phrase(self):
        return random.choice(self.phrases)
