print(     '''100 Days of Code QUIZ''')
print()
print("How many can you answer correctly?")
print()
ans1 = input("What language are we writing in? : ")
if ans1 == "python" or ans1 == "Python":
  print("Correct")
else:
  print("Nope")
print()
ans2 = int(input("Which lesson number is this? : "))
if(ans2 > 12):
  print("We're not quite that far yet")
elif(ans2 == 12):
  print("That's right!")
else:
  print("We've gone well past that!")
