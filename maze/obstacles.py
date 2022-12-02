# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------
import random
 



def get_obstacles():
    """we are keeping a list of obstacles"""
    global obstacle_list
    obstacle_list = [] 

    random_num = random.randint(1,10)
    
    for e in range(random_num):
        x = random.randint(-100, 100)
        y = random.randint(-200, 200)
        coordinates = x,y
        obstacle_list.append(coordinates)
    return obstacle_list


def is_position_blocked(x,y,obstacle_list):
    """We are checking if position (x,y) falls inside an obstacle"""


    for i in obstacle_list:
        if x in range(i[0], i[0]+10) and y in range(i[1],i[1]+10):
            return True
    return False
    

def is_path_blocked(x1,y1,x2,y2,obstacle_list):
    """we are checking if there is an obstacle in the line between the coordinates (x1, y1) and (x2, y2)"""
    for x in range(x1,x2+1):
        if is_position_blocked(x,y1, obstacle_list): 
            return True 
    for y in range(y1,y2+1):
        if is_position_blocked(x2,y, obstacle_list):
            return True
    
    for x in range(x2,x1+1):
        if is_position_blocked(x,y1, obstacle_list): 
            return True 
    for y in range(y2,y1+1):
        if is_position_blocked(x2,y, obstacle_list):
            return True
    return False







# def create_random_obstacles():
#     pass


# def is_position_blocked(x, y):
#     pass


# def is_path_blocked(x1, y1, x2, y2):
#     pass

# def get_obstacles():
#     pass
