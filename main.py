import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)

word_list = []
word_file = open("words.txt")

for word in word_file:
  word_list.append(word.strip())


word = random.choice(word_list)

guess = 6
correct = False

while guess != 0 and not correct:
  user = input("Enter a word: ")

  while len(user) != 5:
    print("It has to be 5 characters.")
    user = input("Enter a word: ")

  # First letter
  if user.lower()[0] == word[0]:
    print(Fore.GREEN + word[0], end = " ")
  elif user.lower()[0] in word:
    print(Fore.YELLOW + user.lower()[0], end = " ")
  else:
    print(user.lower()[0], end = " ")

  # Second letter
  if user.lower()[1] == word[1]:
    print(Fore.GREEN + word[1], end = " ")
  elif user.lower()[1] in word:
    print(Fore.YELLOW + user.lower()[1], end = " ")
  else:
    print(user.lower()[1], end = " ")

  # Third letter
  if user.lower()[2] == word[2]:
    print(Fore.GREEN + word[2], end = " ")
  elif user.lower()[2] in word:
    print(Fore.YELLOW + user.lower()[2], end = " ")
  else:
    print(user.lower()[2], end = " ")

  # Fourth letter
  if user.lower()[3] == word[3]:
    print(Fore.GREEN + word[3], end = " ")
  elif user.lower()[3] in word:
    print(Fore.YELLOW + user.lower()[3], end = " ")
  else:
    print(user.lower()[3], end = " ")

  # Fifth letter
  if user.lower()[4] == word[4]:
    print(Fore.GREEN + word[4])
  elif user.lower()[4] in word:
    print(Fore.YELLOW + user.lower()[4])
  else:
    print(user.lower()[4])

    
  guess -= 1
  print("You have", guess, "guesses left")

  if user == word:
    correct = True
    print("You won")
  elif guess == 0:
    print("You lost. The word is", word)