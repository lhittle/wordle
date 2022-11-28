import random
from colorama import Fore, Back, Style
char_format=Style.BRIGHT + Back.WHITE + Fore.BLACK
correct_format=Style.BRIGHT + Back.GREEN
close_format=Style.BRIGHT + Back.YELLOW
incorrect_format=Style.BRIGHT + Back.RED
reset=Style.RESET_ALL

def five_letter_words():
  with open("five_letter_words.txt", "r") as file:
    all_words=file.read()
    return all_words

def welcome_message(need_rules):
  if need_rules=="Y" or need_rules=="y":
    return "Alrighty!\nThis program will generate a five-letter word.\nYour job is to guess it!\n\nEach guess must be a valid five-letter word\nand you have six tries.\n\nBut not to worry!\nYou'll get a little help depending on which\nwords you guess!\n\nExamples:\n" + correct_format + "W" + char_format + "EARY" + reset + "\nW is in the word and in the correct spot.\n\n" + char_format + "P" + close_format + "I" + char_format + "LLS" + reset + "\nI is in the word but in the wrong spot.\n\n" + char_format + "VAG" + incorrect_format + "U" + char_format + "E" + reset + "\nU is not in the word in any spot.\n\nNow let's get started!"
  elif need_rules=="N" or need_rules=="n":
    return "Perfect! Let's get started."

def pick_answer():
  all_words=five_letter_words()
  word_string=list(map(str,all_words.split()))
  return random.choice(word_string)

def five_letter_guesses():
  with open("five_letter_guesses.txt","r") as file:
    possible_guesses=file.read()
    return possible_guesses

def get_guess(user_input):
  possible_guesses=five_letter_guesses()
  user_input=user_input.upper()
  while len(user_input)!=5 or user_input not in possible_guesses:
    user_input=(input("Invalid guess! Try again!\n")).upper()
  if len(user_input)==5 and user_input in possible_guesses:
    return user_input  

def check_guess(guess, answer):
  wordle_pattern=[]
  for i, letter in enumerate(guess):
    if answer[i]==guess[i]:
      wordle_pattern.append(correct_format+letter)
    elif letter in answer:
      wordle_pattern.append(close_format+letter)
    else:
      wordle_pattern.append(incorrect_format+letter)
  return ''.join(wordle_pattern)+reset

def wordle():
  num_guesses=5
  print(welcome_message(input("Welcome to Wordle!\nDo you need a refresh on the rules? Y/N\n")))
  answer=pick_answer()
  guess=get_guess(input("Make a guess!\n"))
  if guess==answer:
    print(correct_format+guess)
    print(reset+"You got it! It took you one try!")
  if guess!=answer:
    print(check_guess(guess,answer))
    if num_guesses==1:
      print("You have one guess left.")
    else:
      print(f"You have {num_guesses} guesses left.")
  while guess!=answer and num_guesses>0:
    guess=get_guess(input("Make a guess!\n"))
    num_guesses=num_guesses-1
    if guess!=answer:
      print(check_guess(guess,answer))
      if num_guesses==1:
        print("You have 1 guess left.")
      else:
        print(f"You have {num_guesses} guesses left.")
  if guess==answer:
    print(correct_format+guess)
    print(reset+f"You got it! It took you {6-num_guesses} tries.")
  if guess!=answer and num_guesses==0:
    print(reset+f"You're out of guesses! The correct word was {answer}.")
print(wordle())