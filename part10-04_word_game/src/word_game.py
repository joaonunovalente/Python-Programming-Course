# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return 0

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word, player2_word):
        vowels: str = "aeiou"
        number_of_vowels1 = 0
        number_of_vowels2 = 0

        for vowel in vowels:
            print(vowel)
            number_of_vowels1 += player1_word.count(vowel)
            number_of_vowels2 += player2_word.count(vowel)

        if number_of_vowels1 > number_of_vowels2:
            return 1
        elif number_of_vowels1 < number_of_vowels2:
            return 2
        else:
            return 0

class RockPaperScissors(WordGame):
    def __ini__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word, player2_word):
        valid_answers = ["rock", "paper", "scissors"]


        # Incorrect words
        if player1_word not in valid_answers and player2_word not in valid_answers:
            return 0
        elif player1_word not in valid_answers:
            return 2
        elif player2_word not in valid_answers:
            return 1
        
        # Same word: Tie
        if player1_word == player2_word:
            return 0
        
        if player1_word == "rock" and player2_word == "scissors":
            return 1
        elif player2_word == "rock" and player1_word == "scissors":
            return 2
        elif player1_word == "paper" and player2_word == "scissors":
            return 2
        elif player2_word == "paper" and player1_word == "scissors":
            return 1
        elif player1_word == "rock" and player2_word == "paper":
            return 2    
        elif player2_word == "rock" and player1_word == "paper":
            return 1           

if __name__ == "__main__":
    p = RockPaperScissors(3)
    p.play()  