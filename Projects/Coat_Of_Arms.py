# Section 1 - Your code
from utils import *
set_background("Cozy_Mountain")

s1 = create_sprite("Irish_Flag", -220, 35)
s2 = create_sprite("Hailey_Dog", 150, -120)
s3 = create_sprite("Lucy_Lab", 0, -100)
s4 = create_sprite("Skiing_Poles", -100, -100)

message1 = create_sprite("alien",-210,200)
message1.color("Black")
message1.write("Juliet Callaghan",font = ("Times New Roman", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-330,-250)
message2.color("black")
message2.write("The Master Has Failed More Times Than the Beginner Has Tried",font = ("Times New Roman", 15, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()