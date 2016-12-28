#!usr/bin/env python3
# This is a simple cheating program for scrabble written in python
# It is free for use and modification

import argparse

parser = argparse.ArgumentParser(description="Let's cheat together!! yay!!! ;)")
parser.add_argument ("rack", metavar='RACK', help = 'Here goes your rack')
args = parser.parse_args()
rack = args.rack.lower()

def check_intersection ( string_a, string_b):
    """
    Checks if all the character of ``string_a`` are in ``string_b``.

    :param string_a: The string which is checked.
    :param string_b: The string used for the checking.
    :return:         Bool
    """
    _set = list(string_b)
    for ch in string_a:
        try:
            _set.remove(ch)
        except ValueError:
            return False
    return True

def compute_score(scores, string):
    """
    Computes the scrabble scrores for each valid word
    :param scores: The dictionnary used for scoring.
    :param string: The string whose score is to be computed
    """
    score  = 0
    for ch in string:
        score += scores[ch]
    return score
    
all_words = open('sowpods.txt', 'r')
_valid_words = [word.strip().lower() for word in all_words
                if check_intersection(word.strip().lower(), rack)]
all_words.close()
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}
valid_words = [(compute_score(scores, word), word) for word in _valid_words]
valid_words.sort(key=lambda a: a[0], reverse = True )
for e in valid_words[:20]:
    print (str(e[0]) + ': ' + e[1])
