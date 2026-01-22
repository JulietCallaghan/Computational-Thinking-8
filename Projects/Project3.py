import turtle, time, random
from utils import *

print ("Which Sprite do you think will win?")
print ("You can choose between the sled, snowball, hailey the dog, and lucy the lab")
winner = input ("type in your answer right here >")
time.sleep (3.8)
# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -225
y1 = 215
x2 = -225
y2 = 85
x3 = -190
y3 = -80
x4 = -225
y4 = -200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("Cozy_Mountain")
t1 = create_sprite("Snowvball",x1,y1)
t2 = create_sprite("Lucy_Lab",x2,y2)
t3 = create_sprite("Hailey_Dog",x3,y3)
# Sled
t4 = create_sprite("image",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(30):
    x1 += random.randint (11, 15)
    x2 += 8
    x3 += 5
    x4 += random.randint (9, 20)
# x2 = Lucy the lab. She and x2 = Hailey the dog, will be the slowest. There is no way either of them can win.
# x1 = the snowvball and x2 = the sled, only have a chance of winning because the both range higher than luccy and hailey
# The sled has a low speed of 9 and aa high speed of 20 so there is a big chance that the sled can win
# The snowball also has a chance of winning because can have any speed between 11 and 15.

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
print ()
print (f"You thought that {winner} would win")
print ("lets see if you were right!")
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print ()
    print("The Snowball has won!! If you got it right, this is your sign to have a snowball fight!!!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print ()
    print("Lucy the Lab has won!! If you got it right, this is your sign to get a dog!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print ()
    print ("Hailey the dog has finally won!!! What a close race. If you got it right, this is your chance to brag to your neighbor that you won!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    print ()
    print ("The sled has been the fasted and won! If you go it right, this is a sign to tell your family its time for a ski/snowboard trip!")

turtle.exitonclick()