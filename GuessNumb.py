import random
top_of_range= input("Put number:")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range <= 0 :
        print("Next time input a number that is above o")
        quit()
else:
    print("Put an integer next time")

random_no=random.randint(0,top_of_range)

gusses=0
while True:
    gusses += 1
    gussed_no= input("Guess the number: ")
    if gussed_no == random_no:
        print("U got it")
        break
    else:
        print("Try again")

print("You got it after ",gusses," gusses")