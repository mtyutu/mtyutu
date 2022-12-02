# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -----------------------------------------------------------------------------------------

import turtle
from turtle import *
import sys
# import tkinter as TK
# in module obstacles import 
from world.maze.obstacles import *

position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0
blocked = False

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

# turtle
t = turtle.Turtle()
t.color("green")
t.setheading(90)
nm = turtle.Screen()
nm.bgcolor("white")
nm.title("A Maze")
nm.setup(700,700)

# create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)


# Create Level Setup Function
def setup_maze(level):
    # # Create class instances
    pen = Pen()

    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the character at each x,y coordinate
            # NOTE the order of y and x in the next line
            character = level[y][x]
            # Calculate the screen x,y coordinates
            screen_x = -200+(x*16)
            screen_y= 200 - (y*16)

            # Check if it is an X (representing a wall)
            if character=="X":
                pen.goto(screen_x,screen_y)
                pen.stamp()

# Create class instances
# pen = Pen()

def show_constraints():
    "This function use the turtle to draw constraints for the robot"

    t.pencolor("red")
    t.penup()
    t.goto(min_x,min_y)
    t.pendown()
    t.goto(min_x,max_y)
    t.goto(max_x,max_y)
    t.goto(max_x,min_y)
    t.goto(min_x,min_y)
    t.penup()
    t.goto(0,0)
    t.setheading(90)
    

def draw_obstacles(obstacle_list):
    "This fucntion uses turtle to draw obstacles for the robot"
    turtle.tracer(False)
    for i in obstacle_list:
        t.penup()
        t.goto(i)
        t.pendown()
        for j in range(4):
            t.forward(10)
            t.right(90)
    turtle.tracer(True)       
    t.penup()
    t.home()
    t.setheading(90)


def show_position(robot_name):
    """This function prints the current position of the robot
    :param robot_name:
    """
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')
    

def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps,obstacle_list):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y, blocked
    blocked = False
    new_x = position_x
    new_y = position_y
    print(obstacle_list)
    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps
    print(is_position_blocked(new_x,new_y,obstacle_list))
    if is_position_blocked(new_x,new_y,obstacle_list)==True:
        blocked = True
        return False
    elif is_path_blocked(position_x,position_y, new_x, new_y,obstacle_list):
        blocked =True
        return False

    if is_position_allowed(new_x, new_y) and not blocked:
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps,obstacle_list):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps,obstacle_list):
        t.penup()
        t.forward(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    elif blocked:
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps,obstacle_list):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps,obstacle_list):
        t.penup()
        t.backward(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    elif blocked:
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
    t.right(90)
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
    t.left(90)
    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def show_obstacles(obstacles):
    """This function each square obstacle from positions x,y to x+4,y to x+4,y+4 to x,y+4 that are generated
    :param obstacles: the list of obstacles
    """
    if 'maze' in sys.argv:

        if len(obstacles) > 0:
            print("There are some obstacles:")
            for i in obstacles:
                print(f"- At position {i[0]},{i[1]} (to {i[0]+10},{i[1]+10})")

    else:
        if len(obstacles) > 0:
            print("There are some obstacles:")
            for i in obstacles:
                print(f"- At position {i[0]},{i[1]} (to {i[0]+4},{i[1]+4})")            

# show_constraints()
# # 


def setup_world(is_maze):
    if is_maze == False:
        show_constraints()

