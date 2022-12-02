import unittest
from world.maze.most_beautiful_maze import *

class test_maze(unittest.TestCase):
    def test_get_levels(self):

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
    
       self.assertEqual(get_levels(), level_1)

def test_get_obstacles(self):
   obstacle_list = get_obstacles()
   self.assertEqual(get_obstacles(), obstacle_list)

def test_is_path_blocked(self):
   x1 =0
   x2 =0
   y1 =0
   y2 =0 

   obstacle_list = []

   self.assertEqual(is_path_blocked(x1,y1,x2,y2,obstacle_list), False)


def test_is_position_blocked(self):
   x=0
   y=0
   obstacle_list=[]
   self.assertEqual(is_position_blocked(x,y,obstacle_list),False) 





if __name__ == '__main__':
        unittest.main()            
 