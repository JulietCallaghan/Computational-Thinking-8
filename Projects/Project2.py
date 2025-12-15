Cat_points = 0
Dog_points = 0

print ("Hi there!! My name is Chad the Chat and this is a personally quiz!!!")
print ("Do you know yourself very well? Well lets find out!!!")
input ()
print ()
answer = input ("Type 'START' to start the quiz and type 'STOP' to not take the quiz:")
if answer == 'STOP':
    print ("ok! Your lost! Come back anytime to know more about yourself!")
    print ("So long")
    print ("-CHAD THE CHAT (PERSONALLY QUIZ)")
    input ()
    input ()
    input ()
    input ()
    input ()
    input ()
    input ()
    input ()
elif answer == 'START':
    print ("THE QUIZ WILL BEGIN NOW!")
print ()
animal = input ("Are you a dog or cat person? TYPE 'dog' if you like dogs and type 'cat' if you like cats:")
print (f"hmmm. Ok, now since you said you are a {animal} person, lets see if you are right!")
print ()
print (f"For every question you get right you will gain 2 points for {animal} person")
print ("But heres where it gets tricky...")
print (f"For every question you get wrong, you lose a point for {animal} person and gain a point for the other animal!")
print ("Hopefully that makes sense and press enter to start!!!")
input ()
answer = input ("Do you prefer 'A' rock climbing or 'B' swimming:")
if answer == "A" or answer == "a" or answer == " a" or answer == " A":
    if animal == "cat":
        Cat_points += 2
    elif animal == "dog":
        Dog_points -= 1
elif answer == "B" or answer == "b" or answer == " b" or answer == " B": 
    if animal == "dog":
        Dog_points += 2
    elif animal == "cat":
        Cat_points -= 1
print ()
print ("Ok, very interesting")
input ("Now onto question 2!")
print ()
answer1 = input ("Do you prefer 'A' long walks or 'B' power nap instead?:")
if answer1 == "A" or answer1 == "a" or answer1 == " a" or answer1 == " A":
    if animal == "dog":
        Dog_points += 2
    elif animal == "cat":
        Cat_points -= 1
elif answer1 == "B" or answer1 == "b" or answer1 == " b" or answer1 == " B": 
    if animal == "cat":
        Cat_points += 2
    elif animal == "dog": 
        Dog_points -= 1
print ()
print ("Ok, lets move on to the next question!")
answer3 = input ("Do you have 'A' a lot of energy or 'B' not much energy?:")
if answer3 == "A" or answer3 == "a" or answer3 == " a" or answer3 == " A":
    if animal == "dog": 
        Dog_points += 2
    elif animal == "cat": 
        Cat_points -= 3
elif answer3 == "B" or answer3 == "b" or answer3 == " b" or answer3 == " B":
    if animal == "cat":
        Cat_points += 2
    elif animal == "dog":
        Dog_points -= 1
print ()
print ("You are over halfway through the quiz! Two more questions to go!")
print ()
answer4 = input ("Are you 'A' Independent or 'B' Dependent:")
if answer4 == "A" or answer4 == "a" or answer4 == " a" or answer4 == " A": 
    if animal == "cat":
        Cat_points += 2
    elif animal == "dog":
        Dog_points -= 1
elif answer4 == "B" or answer4 == "b" or answer4 == " b" or answer4 == " B":
    if animal == "dog":
        Dog_points += 2
    elif animal == "cat":
        Cat_points -= 1
print ()
print ()
print ("Ok, last question until we will reveal if you are a dog or cat person!")
answer2 = input ("Are you 'A' Extroverted or 'B' Introverted:")
if answer2 == "A" or answer2 == "a" or answer2 == " a" or answer2 == " A":
    if animal == "dog":
        Dog_points += 2
    elif animal == "cat":
        Cat_points -= 1
elif answer2 == "B" or answer2 == "b" or answer2 == " b" or answer2 == " B":
    if animal == "cat":
        Cat_points += 2
    elif animal == "dog":
        Dog_points -= 1
input ("Ok, it is now time to reveal your quiz")
print ("YOUR RESULTS WILL COME OUT SHORTLY, PLEASE WAIT PATIENTLY")
input ()
print (f"You believed that you were a {animal} person")
print ()
print ("After taking our personality quiz, our computer saids:")
if Dog_points > Cat_points:
    if animal == "dog":
        print ("You were right!! Nice job! You are a Dog person!")
    elif animal == "cat":
        print ("You were wrong, your better fit is to be a dog person!")
elif Cat_points > Dog_points:
    if animal == "cat":
        print ("You were right! Nice Job! You are a cat person!")
    elif animal == "dog":
        print ("You are wrong, you are actually a cat person!")
elif Dog_points == Cat_points:
    print ("You got the same amount of points this meaning our computer believes you like them the same amount!")
input ()
print (f"You had a total of {Dog_points} dog points and a total of {Cat_points} cat points.")
print ()
print ("Thank you for playing the personality quiz!")
print ("SO LONG")
print ("-CHAD THE CHAT (PERSONALITY QUIZ)")