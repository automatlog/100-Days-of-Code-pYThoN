print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()

counter = 1
while True:
  lyrics = input('''Blinded by the _______
Revved up like a deuce
Another runner in the night \n''')
    
  if lyrics == "light" or lyrics == "Light":
    print("You got it!")
  else:
    print("Nope! Try again!")
    counter +=1
  if lyrics == "light":
    break
print("Thanks for playing!")

print("You got the correct lyrics in", counter, "attempt(s).")
