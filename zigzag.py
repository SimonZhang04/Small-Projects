import time, sys
import random
import string
from termcolor import cprint 

# global variables
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.
lineLength = 8 # How many characters in one line
lineIncreasing = False # Whether the line length is increasing or not.
character = "*" # What character is being printed
pause = 0.1 # The length (secs) between each line
windingLength = False
colour = "white"
colours = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
speeds = { # pre-set speeds for pause times
  0.02 : "very fast",
  0.05 : "fast",
  0.1 : "normal",
  0.15: "slow",
  0.2: "very slow"
}

# introduction
print("Zigzag Program\n")
print("This program displays a moving zigzag. Use Ctrl-C to stop the zigzag and open the menu once the it has started. Edit the zigzag using the menu to make it appear differently.")

while True: # loops the zigzag with the menu
  while True: # menu loop
    print("\nMENU\nA. Start the Zigzag\nB. Change Character(s)\nC. Change Colour\nD. Change Speed\nE. Winding Length\nF. Randomize!\nG. Show Set Options\nQ. Quit the program")
    choice = input().upper()

    if choice == "A": 
      break # break out of menu loop and starts the zigzag

    elif choice == "B": # Change character
      print("What would you like to change the character to?")
      while True:
        character = input("Enter up to 3 characters: ")
        if not character or " " in character or "\t" in character: # cases for spaces, entering nothing, tabs
          print("Please do not enter empty spaces.")
        elif len(character) <= 3:
          print("The character(s) has been changed to:", character)
          break
        else:
          print("Enter only up to 3 characters. ")
        
    elif choice == "C": # Change the colour
      print("What would you like to change the colour to be?")
      print("Options: ", end="")
      for x in range(len(colours)-1): # print the list of colours
        print(colours[x] + ", ", end="")
      print("and white")
      while True:
        colour = input().lower()
        if colour not in colours: 
          print("That is not an valid option. ")
        else:
          print("The colour has been changed to", colour + "!")
          break

    elif choice == "D": # Change speed
      print("What would you like to change the speed to?")
      print("A. Very Fast\nB. Fast\nC. Normal\nD. Slow\nE. Very Slow")
      while True:
        userInput = input().upper()
        if userInput == "A": # very fast
          pause = 0.02
          break
        elif userInput == "B": # fast
          pause = 0.05
          break
        elif userInput == "C": # normal
          pause = 0.1
          break
        elif userInput == "D": # slow
          pause = 0.15
          break
        elif userInput == "E": # very slow
          pause = 0.2
          break
        else:
          print("That is not a valid option.")
      print("The speed has been set to", str(speeds[pause]) + ".")

    elif choice == "E": # Enable/Disable winding length
      while True:
        print("Enter Y to turn on Winding Length and N to turn off Winding Length.")
        userInput = input().upper()
        if userInput == "Y":
          print("Winding length is on!")
          windingLength = True
          break
        elif userInput == "N":
          windingLength = False
          print("Winding length is off!")
          break
        else:
          print("Enter Y or N.")
    
    elif choice == "F": # Randomized options
      print("The options have been randomized!\nGo to 'Show Set Options' to see what changes have been made.")
      character = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 3))) # random string of characters at a length of 1-3
      colour = colours[random.randint(0, 7)]
      pause = list(speeds.keys())[random.randint(0,4)]
      windingLength = bool(random.getrandbits(1))

    elif choice == "G": # Show set options
      print("\nHere is the current set options:")
      print("Character(s):", character)
      print("Colour:", colour)
      print("Speed:", speeds[pause])
      print("Winding length is ", end="")
      if windingLength:
        print("on")
      else:
        print("off")
    
    elif choice == "Q": # Quit the program
      print("Thank for you using the Zigzag program.")
      sys.exit()
  
    else: 
      print("That is not a valid option.")

  print("\nZigzag Start!\n")

  while True: # Zig zag loop
    try: 
      print(' ' * indent, end='')
      cprint((character * lineLength), colour)
      time.sleep(pause) # Pause for 1/10 of a second.
     
      if windingLength:
        if lineIncreasing: # Increase the number of characters
          lineLength += 1
          if lineLength == 10: # stop increasing length
            lineIncreasing = False

        else:
          lineLength -= 1 # Decrease the number of characters
          if lineLength == 2: # start increasing length
            lineIncreasing = True
      
      if indentIncreasing:
        # Increase the number of spaces:
        indent += 1
        if indent == 20:
            # Change direction:
          indentIncreasing = False
    
      else:
        # Decrease the number of spaces:
        indent -= 1
        if indent == 0:
            # Change direction:
          indentIncreasing = True
    
    except KeyboardInterrupt: # If the user does Ctrl-C
      print("\nZigzag Stop!")
      break # Goes back to the menu
