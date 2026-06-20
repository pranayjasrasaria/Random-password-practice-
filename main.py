import random #importing module
playing = True #initialise
password = str(random.randint(1,26)) #random in-built function
 
print("Guess the password! \n")  
while playing:
  guess = input("Give me your best guess! \n")
  if password == guess:
    print("You win the game")
    print("The password was",password)
    break 
    
  else:
    print("Your guess isn't quite right, try again. \n")