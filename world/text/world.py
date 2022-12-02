# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------


# def setup_world():
#     pass

from world.maze.obstacles import *

min_y, max_y = -200, 200
min_x, max_x = -100, 100

position_x = 0
position_y = 0
# variables tracking position and direction

directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

blocked = False


def show_obstacles(obstacle_list2):
    """We are showing obstacles and checking if the path is blocked"""
    if len(obstacle_list2) != 0:
        print("There are some obstacles:")
        for i in obstacle_list2:
            print(f"- At position {i[0]},{i[1]} (to {i[0]+4},{i[1]+4})")


def show_position(robot_name):
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

    global position_x, position_y,blocked
    new_x = position_x
    new_y = position_y
    blocked = False

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_blocked(new_x,new_y,obstacle_list):
        blocked = True
        return False
    elif is_path_blocked(position_x,position_y,new_x,new_y,obstacle_list):
        blocked =True
        return False
    if is_position_allowed(new_x, new_y) and not blocked:
        position_x = new_x
        position_y = new_y
        return True

    return False


def do_forward(robot_name, steps, obstacle_list):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps, obstacle_list):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps, obstacle_list):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps, obstacle_list):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
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
    
    return True, ' > '+robot_name+' turned left.'


