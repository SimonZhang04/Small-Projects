# Guessing_Game.py
from random import *
import time
import function


print("Epic Guessing Game")
guess_range = 100
function.command_list()
print("The shop and stats page are not available until you start the game.")
start = time.time()
home_command = input()
money = 0
money_earn = 100
lower_range = False
more_money = False
close_up = False
if home_command == "q":
    # game starts
  while True:
    if lower_range:
      guess_range = 80
    if more_money:
      money_earn = 150
    hidden_num = randint(1, guess_range)
    print(f'Range is 1 - {guess_range}')
    while True:
      guess = input()
      try:
        if close_up and hidden_num - 2 < int(guess) < hidden_num + 2:
          print(f'You win! The number was {hidden_num}.')
          print(f'You earned ${money_earn}')
          print("")
          break
        if int(guess) > hidden_num:
          print('Lower')
        elif int(guess) < hidden_num:
          print('Higher')
        else:
          print('You win!')
          print(f'You earned ${money_earn}')
          print("")
          break
      except ValueError:
        print("Please input an integer")
    money += money_earn
    print(f'You now have ${money}.')
    if money >= 500:
      end = time.time()
      print("Congrats you beat the game.")
      print(f'You finished in {round(end - start)} seconds.')
      quit()
    function.command_list()
    next_command = input("What do you want to do next? ")
    if next_command == 'q':
        print("Next game has started")
    elif next_command == 'w':
      while True:
        print('''SHOP
  1. Lower Range - Lower the random number generating range by 10 - $20
  2. Earn More - Earn $50 more after completing one game - $50
  3. Close Complete - If your guess is 2 more or less from the number you win the game" - $50
  4. Leave Shop
  ''')
        shop_command = input("What do you want to do? ")
        if shop_command == '1':
          if money >= 20 and not lower_range:
            print("You bought the 'Lower Range' upgrade!")
            money -= 20
            lower_range = True
            print(f'You have ${money}')
          elif lower_range:
            print("You already bought this upgrade")
          else:
            print("You don't have enough money")
        elif shop_command == '2':
          if money >= 50 and not more_money:
            print("You bought the 'Earn More' upgrade!")
            money -= 50
            more_money = True
          elif more_money:
            print("You already bought this upgrade")
          else:
            print("You don't have enough money")
        elif shop_command == '3':
          if money >= 50 and not close_up:
            print("You bought the 'Close Complete' upgrade!")
            money -= 50
            close_up = True
          elif close_up:
            print("You already bought this upgrade")
          else:
            print("You don't have enough money")
        elif shop_command == '4':
          break
        else:
          print("This is not a command")
    elif next_command == 'e':
      print(f'Lower Range Upgrade = {lower_range}')
      print(f'More Money Upgrade = {more_money}')
      print(f'Close Complete Upgrade = {close_up}')
      print(f'You currently have ${money}.')
    elif next_command == 't':
      print("Quit")
      exit()
      print('')
    elif next_command == 'r':
      print('''
  This is a simple guessing game, except the goal is to reach $500. 
  You will earn $100 after winning one game, and after beating the game you will be given a time. 
  Try to get the lowest time possible. There will be a shop that you can use to buy upgrades to help you.
          ''')
elif home_command == "r":
  print('''
  This is a simple guessing game, except the goal is to reach $500. 
  You will earn $100 after winning one game, and after beating the game you will be given a time. 
  Try to get the lowest time possible. There will be a shop that you can use to buy upgrades to help you.
  ''')
elif home_command == 't':
  print("Quit")
  exit()
else:
  print("This is not a command!")
