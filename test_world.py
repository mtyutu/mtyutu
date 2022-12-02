import unittest
from world.text.world import *
import world.maze.obstacles as obstacles




class MyTestCase(unittest.TestCase):
    def test_do_forward(self):
        robot_name = ""
        steps = 0
        the_obstacle = obstacles.get_obstacles()
        self.assertEqual(do_forward(robot_name,steps, the_obstacle),(True, ' >  moved forward by 0 steps.'))


    def test_do_back(self):
        robot_name = ""
        steps = 0
        the_obstacle = obstacles.get_obstacles()
        self.assertEqual(do_back(robot_name,steps, the_obstacle), (True , ' >  moved back by 0 steps.'))


    def test_update_position(self):
        obstacle_list = obstacles.get_obstacles()
        steps = 0
        self.assertEqual(update_position(steps,obstacle_list), True)


    def test_do_right(self):
        robot_name = ""
        self.assertEqual(do_right_turn(robot_name), (True, ' >  turned right.'))


    def test_do_left(self):
        robot_name = ""
        self.assertEqual(do_left_turn(robot_name),(True, ' >  turned left.'))

    
    def test_position(self):
        new_x = 0
        new_y = 0
        self.assertEqual(is_position_allowed(new_x,new_y),(min_x <= new_x <= max_x and min_y <= new_y <= max_y))




if __name__ == '__main__':
    unittest.main()
