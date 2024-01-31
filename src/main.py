print("Hello, World!")
print("Welcome to the guessing game")

import random
random_number1=random.randint(1,100)
a = 0
i = random_number1
# print (i)
correct = "Do you want to play again? Type y for yes or n for no: "
for i in range(100):
  start = input("Guess a number between 1 and 100: ")
  print(start)
  a += 1
  b = int(start)
  if b == random_number1 :
    print("You guessed: " + str(b) + " That's it! You guessed the number in " +str(a) +" attempts!")
    print(correct)
    c = input("type y or n:")
    if c == "y":
      random_number1=random.randint(1,100)
      a = 0
      print ("New number has been generated")
      print(i)
    elif c != "y" and c!="n" :
      print("Invalid input, goodbye!")
      break
    else:
      print("are you sure?")
      d = input("type y or n:")
      if d == "y":
        print("are you really sure?")
        e = input("type y or n:")
        if e == "y":
          print("are you really really sure?")
          f = input("type y or n:")
          if f == "y":
            print("Are you really really really sure?")
            g = input("type y or n:")
            if g == "y":
              print("Are you the most sure you have ever been in your lifetime?")
              h = input("type y or n:")
              if h == "y":
                print("goodbye!")
                break
            elif h == "n":
              random_number1=random.randint(1,100)
              a = 0
              print ("New number has been generated")
            elif h!= "y" and h!="n" :
             print("Invalid input, goodbye!")
             break
            
          elif g!= "y" and g!="n" :
            print("Invalid input, goodbye!")
            break
          elif f == "n":
            random_number1=random.randint(1,100)
            a = 0
            print ("New number has been generated")
            print(i)
          elif f!= "y" and f!="n" :
            print("Invalid input, goodbye!")
            break
        if e == "n":
          random_number1=random.randint(1,100)
          a = 0
          print ("New number has been generated")
          print(i)
        elif e!= "y" and e!="n" :
          print("Invalid input, goodbye!")
          break
      if d == "n":
        random_number1=random.randint(1,100)
        a = 0
        print ("New number has been generated")
        print(i)
      elif d!= "y" and d!="n" :
        print("Invalid input, goodbye!")
        break
  elif b > random_number1 and b > 100 or b < 1 :
    print("Your number is out of range. Try again!")
  elif b < random_number1 :
    print("You guessed: " +  str(b) + " Your guess is too low. Try again!")
  elif b > random_number1 :
    print("You guessed: " +  str(b) + " Your guess is too high. Try again!")
  