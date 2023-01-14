print('''Fake Fan Question Generator''')
print()
print("Lets see are you One Piece anime fan and also check Big Bang Theory fan")
print()
options = input("Check : One Piece or Big Bang Theory : ")
print()

#One Piece
if options == "One Piece" or options == "one piece":
    favCharacter = input("Oh really?! Name me any of the characters? : ")
    if favCharacter == "Nami":
        print()
        print("You got that by pure chance.") 
        herJob = input("Okay then, what is her job on the ship? :")
        if(herJob == "Navigator"):
            print()
            firstBounty = input("Hmph! What was her first bounty then? : ")
            if(firstBounty == "defeating Kalifa of CP9" or firstBounty == "16,000,000 berry"):
                print("Right Answer")
            else:
                print("See! FAKE One piece fan!")           

                
#Big Bang Theory

elif options == "Big Bang Theory":
    print ("Are you a superfan of 'The Big Bang Theory' or a fake fan?")
    print()
    print("Answer these questions to find out.")
    Glasses = input("Does someone wear glasses?")
    if Glasses == "yes":
        print("Correct!")
    else:
        print("Wrong!")
        WhoGlasses = input("And who wears glasses?")
        if WhoGlasses == "Leonard":
            print("You got it")
        else:
            print("Try again!")
