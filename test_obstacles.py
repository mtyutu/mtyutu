from random import randint
import unittest
from  world.maze.obstacles import *
import world.text.world as world

# from obstacles import *



class MyTestCase(unittest.TestCase):
    def test_obstacle(self):
        world.position_x = 0
        world.position_y = 0
        random.randint = lambda a,b: 1
        # obstacle_list = [(-25, -11), (-17, 113), (20, -169)]
        obstacle_list = [(1,1)]
        self.assertEqual(get_obstacles(),obstacle_list)


    def test_is_position_blocked(self):
        world.position_x = 0
        world.position_y = 0
        x =0
        y=0 
        obstacle_list = [(1,1)]
        self.assertEqual(is_position_blocked(x,y,obstacle_list), False)


    def test_is_path_blocked(self):
        world.position_x = 0
        world.position_y = 0
        
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        obstacle_list = [(1,1)] 
        self.assertEqual(is_path_blocked(x1,y1,x2,y2,obstacle_list), False)

  
        







if __name__ == '__main__':

    unittest.main()        
