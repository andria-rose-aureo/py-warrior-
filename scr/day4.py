num = int(input("Guess a number between 1 and 10 -  "))
for i in range (1,3):
    if (num == 7):
         print("Congrats! You guessed it right 🎉")
         break
    else:
         print("try again")
         num = int(input("Guess a number again -  "))
print("Game Over! The number was 7")