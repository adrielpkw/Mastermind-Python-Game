import random
#This is the menu for the user to interact
#Used function for menu
def menu():
  select = input("Would you like to start? \n(1)Start \n(2)Exit\n")
  while select not in["1","2"]:
    print("Invalid option")
    select = input("Would you like to start? \n(1)Start \n(2)Exit\n")
  return select

while True:
  print ("Welcome to MASTERMIND! \nGuess the colour pattern with 6 tries only.")
  select = menu()
  if select == "2":
      print("Exiting....")
      exit()
      
  #Game start with guide given
  #Randomisation starts here
  print("You can use Purple(P), Green(G), Black(B), Orange(O) and Magenta(M) only!\n")
  print("You are required to guess a colour pattern that has 4 colours \nbased on the given colours above inside it.\n")
  print("No hints will be given! Good luck!\n")
  pattern = []
  for i in range(4):
    pattern.append("PGBOM"[random.randrange(0,5)])
    
    
    
  #Allow user to input their guess
  attempts = 0
  while attempts<6:
    guess = list(input("Please enter your colour pattern: \n").upper())
    
    #Validity check
    if len(guess)!=4:
      print("Please enter 4 characters only!")
      continue
    
    if not all(c in "PGBOM" for c in guess):
      print("See what colours you can use and try again!")
      continue
    
    #When user input their guess
    attempts += 1
    if guess==pattern:
      print("Congratulations! The correct colour pattern is", "".join(pattern))
      print("You need ", attempts, "attempts to guess it correctly!")
      break #User won the game

    print("\nYour colour pattern is", "".join(guess))

    #Check correct colour in correct position
    correct = 0
    tmpPattern = []
    tmpGuess = []

    for i in range(4):
      if guess[i]==pattern[i]:
        correct += 1
      else:
        tmpPattern.append(pattern[i])
        tmpGuess.append(guess[i])
    
    #Check correct colour in wrong position:
    wrongPo = 0
    for c in tmpPattern:
      if c in tmpGuess:
        wrongPo += 1
        tmpGuess.remove(c)
    
    print("\nCorrect colour and Correct Position: ", correct)
    print("Correct colour but Wrong Position: ", wrongPo, "\n")

  #When user used 6 attempts
  if attempts==6 and guess != pattern:
    print("Max attempts reached, the colour pattern is", "".join(pattern))
    
  #Asks user if want to continue or exit
  select = input("Would you like to try again? \n(1)Yes \n(2)No\n")
  while select not in["1","2"]:
    print("Invalid option")
    select = input("Would you like to try again? \n(1)Yes \n(2)No\n")
  if select == "2":
    print("Exiting....")
    exit()
  


