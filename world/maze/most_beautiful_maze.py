import turtle
import random
# import obstacles
from collections import deque
from world.maze.obstacles import get_obstacles


# Create levels list


def get_levels():

    # Create levels list
    levels =[""] 

    #Define first level
    # level_12 = [
    #     "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    # ]
    level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X  XXXXXXX  X       XXXXXXXXXXXXXXXXXXXXX",
    "X  XXXXXXX  XXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X       XX  XXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X       XX  XXX        XXXXXXXXXXXXXXXXXX",
    "XXXXXX  XX  XXX        XXXXXXXXXXXXXXXXXX",
    "XXXXXX  XX  XXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "XXXXXX  XX    XXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X  XXX        XXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X                XXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  XXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXX XX  XXXXX  XXXXXXXXXXXXXXXXX",
    "XXX  XXXXXXXXXX         XXXXXXXXXXXXXXXXX",
    "XXX                     XXXXXXXXXXXXXXXXX",
    "XXX         XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXX              XXXXXXXXXXXXXXXXX",
    "XX   XXXXX              XXXXXXXXXXXXXXXXX",
    "XX   XXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXX",
    "XX          XXXX        XXXXXXXXXXXXXXXXX",
    "XXXX                    XXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXX            XXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXX   XXXXXX         XXXXXXXXXXXXXXXX",
    "XXXXXXX   XXXXXXXXXXX    XXXXXXXXXXXXXXXX",
    "XXXXXXX   XXXXXXXXXXX    XXXXXXXXXXXXXXXX",
    "XXXXXXX   XXXXXXXXXXX    XXXXXXXXXXXXXXXX",
    "XY                       XXXXXXXXXXXXXXXX",
    "X                 T        XXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ]

    # Add maze to mazes list
    
    return level_1

def get_obstacles():
    """This function generates obstacles from 1 to 10 for x
    within the range (-100,100) and y within the range (-200,200)
    :return: obstacle_list
    """

    global obstacle_list, path_list, end_edge
    
    path_list = []
    obstacle_list =[]
    end_edge = ()
    level_1 = get_levels()
    for y in range(len(level_1)):
        for x in range(len(level_1[y])):
            x_val = -200 + (x * 10)
            y_val = 200 - (y * 10)
            if level_1 [y][x] == "X" or level_1 [y][x]  == "T" :
                
                obstacle_list.append((x_val,y_val))
            else:
                path_list.append((x_val,y_val))
            if level_1 [y][x]  == "T":
                end_edge = ((x_val, y_val))   
    print(end_edge)                   
    return obstacle_list            

def  is_position_blocked(x,y,obstacles):
    """This function checks if there is an obstacle in the 
    certain position
    :param x:
    :param y:
    :param obstacles:
    :return: True if there's an obstacle in the position else False
    """
    # print(obstacle_list)
    for i in obstacles:
        if x in range(i[0],(i[0])+10) and y in range(i[1],(i[1])+10):
            return True
    return False


def is_path_blocked(x1,y1, x2, y2,obstacles):
    """This function checks if there is an obstacle within a certain path
    from (x1,y1) to (x2,y2)
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param obstacles:
    :return: True if there's an obstacle in the path else False
    """
    for x in range(min(x1,x2),max(x1,x2)):
        if is_position_blocked(x,y1,obstacles):
            return True
    for y in range(min(y1,y2),max(y1,y2)):
        if is_position_blocked(x1,y,obstacles):
            return True
    return False

def set_maze_runner():
        q = deque()
        v = []
        x = 0
        y = 0
        obstacle_list = get_obstacles()
        q.append((x,y))
        current_position = (y,x)
        solution = {}
        solution[current_position] = current_position
        # for t in path_list:
        #     print(t)
        # print(path_list)
        while len(q) > 0:
            x,y = q.popleft()
            
            

            if (x+10,y) in path_list and (x+10,y) not in v:
                q.append((x+10,y))
                v.append((x+10,y))
                solution[(x+10,y)] = x,y

            if (x-10,y) in path_list and (x-10,y) not in v:
                q.append((x-10,y))
                v.append((x-10,y))
                solution[(x-10,y)] = x,y 

            if (x,y+10) in path_list and (x,y+10) not in v:
                q.append((x,y+10))
                v.append((x,y+10))
                solution[(x,y+10)] = x,y    

            if (x,y-10) in path_list and (x,y-10) not in v:
                q.append((x,y-10))
                v.append((x,y-10))
                solution[(x,y-10)] = x,y 
        
        return solution

def back_track():
    solution = set_maze_runner()
    for i in solution:
        print(i)
    p = []
    end_x ,end_y = end_edge
    
    x,y = end_x ,end_y

    start_x, start_y = 0,0

    while (x,y) != (start_x,start_y):
        p.append((x,y))
        x,y = solution[(x,y)]
    # print(p)
    return p    
        

# def create_maze():
#     for y in range(len(level_1))

# Set up the level
# setup_maze(levels[1])

# # Main Gaxme Loop
# while True:
#     pass
    




