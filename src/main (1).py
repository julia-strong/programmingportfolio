print ("Hello, World")

import time 
time1=2

# create user input for a word
word = input("Type a lowercase word that you would like to have converted into pig latin: ")

# find the number of letters in the word
word_length = len(word)
# turn the word into a string
word1 = str(word)
# isolate the first character of the string
firstLetter = word1[0]
# check if the first letter is a vowel


if firstLetter == "a" or firstLetter == "e" or firstLetter == "i" or firstLetter == "o" or firstLetter == "u":
    # if it is, add "ay" to the end of the word
  print("Converting " + word + " to pig latin ... ")
  print("Please have patience while your request is processsed")
    # wait for 10 seconds
  time.sleep(time1)
  print(word + "ay")
# if it is not, check if the second letter is a vowel and if it is, move the first letter to the end of the word and add "ay"
elif word1[1] == "a" or word1[1] == "e" or word1 == "i" or word1[1] == "o" or word1[1] == "u":
  print("Converting " + word + " to pig latin... ")
  print("Please have patience while your request is processsed")
  time.sleep(time1)
  print(word1[1:] + firstLetter + "ay")
# if it is not, check if the third letter is a vowel and if it is, move the first two letters to the end of the word and add "ay"
elif word1[2] == "a" or word1[2] == "e" or word1[2] == "i" or word1[2] == "o" or word1[2] == "u":
  print("Converting  " + word + " to pig latin... ")
  print("Please have patience while your request is processsed")
  time.sleep(time1)
  print(word1[2:] + firstLetter + word1[1] + "ay")
# if it is not, check if the fourth letter is a vowel and if it is, move the first three letters to the end of the word and add "ay"
elif word1[3] == "a" or word1[3] == "e" or word1[3] == "i" or word1[3] == "o" or word1[3] == "u":
  print("Converting  " + word + " to pig latin... ")
  print("Please have patience while your request is processsed")
  time.sleep(time1)
  print(word1[3:] + firstLetter +  word1[1] + word1[2] + "ay")
else:
  print("Are you sure " + word + " is a real word?")
  


