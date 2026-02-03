import turtle, time, random
from utils import *
# The goal of this game is to make the girl not cold nor hot and keep her happiness high. 
# She will start out cold so you will have to press the space bar to make her get warmer
# If she gets too hot than you can feed her ice cream by hitting the "a" key so she will be colder.
# If her happiness gets to low or the temperature is too high or low than she will die. 

# Section 1 - setup
# TODO - set a background using set_background()
set_background("Cozy_Mountain")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
Temperature = 30
Happiness = 35
hot_coco = 0
ice_cream = 0
t1 = create_sprite("cold_girl", -20, 10)
t2 = create_sprite("alien",-350, 150)
t3 = create_sprite ("warm_girl")
t2.hideturtle ()
t3.hideturtle ()
# Section 2 - controls
# TODO - define an action. ex: def my_control()
# for i in range(30):
#     1 += 10
# Hot Coco:
def make_hot_coco ():
    global hot_coco
    hot_coco += 1
    x = random.randint (100,300)
    # Make x value on right
    y = random.randint (-200,200)
    create_sprite("hot_coco",x,y)
    global Temperature
    Temperature += 1
window.onkeypress(make_hot_coco, "space")
# Clicking the space bar will appear a hot coco on the screen and 
# increase the temperature by 1 and depending on your temperature, can either lower or increase her happiness

def make_ice_cream (): 
    global ice_cream
    ice_cream += 1 
    x = random. randint (-190,-100)
    y = random. randint (-200, 50)
    create_sprite ("ice_cream",x,y)
    global Temperature
    Temperature -= 1
window.onkeypress(make_ice_cream, "a")

#  Clicking the "a" key will appear an ice cream on the screen and 
# decrease the temperature by 1 and depending on your temperature can either lower or increase her happiness

    
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control




# Section 3 - game loop
window.listen()
for i in range(1000000000):
    t2.clear()
    t2.write(f"Temperature: {Temperature}\nHappiness: {Happiness}\nHot Coco:{hot_coco}\nIce Cream {ice_cream}",font=("Arial",20,"normal"))
    if Temperature > 45 and Temperature < 75:
        set_image(t1,"normal_girl")
        if i % 20 == 0:
            Happiness += 1
    elif Temperature < 45:
        set_image(t1,"cold_girl")
        if i % 20 == 0:
            Happiness -= 1
       
    elif Temperature > 75:
        set_image(t1,"warm_girl")
        if i % 20 == 0:
            Happiness -= 1

    if Happiness > 100:
        Happiness = 100
    elif Happiness == 0:
        break
        
    
    if i % 80 == 0:
        Temperature -= 1
        if Temperature == 0:
            break
            print ("Game Over")
        elif Temperature >= 100:
            break
            print ("Game Over")
        elif Happiness == 0:
            break
            print ("Game Over")
# Next step is to make the happiness and temperature go up or down depending how many times you click the hot coco or ice cream. Also make sure this works above

    # TODO - put any repeating actions here

    time.sleep(0.01)
    window.update()