def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def pass_wall():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal()==False:
    pass_wall()
    




