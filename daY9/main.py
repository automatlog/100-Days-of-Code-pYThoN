print(''' 
     Generation Generator''')
myName = input("What's Your Name? : ")
print()
birthYear = int(input("What year were you born? : "))
print()
print("[Generation Name] : ")
if birthYear <= 1946:
    print("You are a Traditionalists.")
elif birthYear >= 1947 and birthYear <=1964:
    print("You are a Baby Boomers.")
elif birthYear >= 1965 and birthYear <=1981:
    print("You are a Generation X.")
elif birthYear >= 1982 and birthYear <=1995:
    print("You are a Millenials.")
elif birthYear >= 1996:
    print("You are a Generation Z.")
else:
    print("Try Again...!")
