# The basic premise of the game Gallows is to follow two rules:
#
# First character of next word must match last character of previous word.
# The word must not have already been said.
# Below is an example of a Gallows game:
#
# ['word', 'dowry', 'yodel', 'leader', 'righteous', 'serpent']  #valid!
#
# ['motive', 'beach']  # invalid! - beach should start with "e"
#
# ['hive', 'eh', 'hive']  # invalid! - "hive" has already been said
# Write a Gallows class that has two instance variables:
#
# words: a list of words already said.
# game_over: a boolean that is true if the game is over.
# and two instance methods:
#
# play: a method that takes in a word as an argument and checks if it is valid
# (the word should follow rules #1 and #2 above).
#
# If it is valid, it adds the word to the words list, and returns the words list.
# If it is invalid (either rule is broken), it returns "game over" and sets the game_over boolean to true.
# restart: a method that sets the words list to an empty one [] and sets the game_over boolean to false.
#     It should return "game restarted".

class Gallows:
    last_word = ''
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, new_word):
        if new_word not in self.words and new_word[:1] == self.last_word[-1:] or self.last_word == '':
            self.words.append(new_word)
            self.last_word = new_word
            return self.words
        self.game_over = True
        return "game over"

    def restart(self):
        self.__init__()
        return "game restarted"

my_gallows = Gallows()
print(my_gallows.game_over)
print(my_gallows.play('apple'))
print(my_gallows.words)
print(my_gallows.play('ear'))
print(my_gallows.play('rhino'))
print(my_gallows.play('ocelot'))
print(my_gallows.game_over)
print(my_gallows.play('oops'))
print(my_gallows.game_over)
print(my_gallows.words)