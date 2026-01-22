# Section 1 - Your code
from utils import *
set_background("COZYMOUNTAIN")

s1 = create_sprite("present", 100, 100)
s2 = create_sprite("Christmas", -100, 100)
s2 = create_sprite("present", -100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("Red")
message1.write("Happy Holidays!!!",font = ("Oswald", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()