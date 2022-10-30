print("Welcome to my computer quiz!")

playing=input("Do you want to play? Type Y for yes and N for no. ")



print(playing)

if playing == "Y":
    print("Okay! Let's play :)")
else:
    print("Aww! I guess I'll see you next time!")
    quit()
    
score=0 

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")


answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/3)*100) + "%!")


