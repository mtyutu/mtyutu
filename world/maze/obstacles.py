import random

def get_obstacles():
    """This function generates obstacles from 1 to 10 for x
    within the range (-100,100) and y within the range (-200,200)
    :return: obstacle_list
    """

    global obstacle_list
    obstacle_list =[]
    for i in range(random.randint(1,10)):
        x = random.randint(-100,100)
        y= random.randint(-200,200)
        obstacle_list.append((x,y))
    return obstacle_list


def  is_position_blocked(x,y,obstacles):
    """This function checks if there is an obstacle in the 
    certain position
    :param x:
    :param y:
    :param obstacles:
    :return: True if there's an obstacle in the position else False
    """
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