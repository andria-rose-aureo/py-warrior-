num = int(input("Guess a number between 1 and 10 -  "))
for i in range (1,4):
    if (num == 7):
         print("Congrats! You guessed it right 🎉")
         break
    elif(i!=3):
         print("try again")
         num = int(input("Guess a number again -  "))
else:
         print("Game Over! The number was 7")
