import unittest
import robot
from robot import *
import world.maze.obstacles as obstacles
import world.text.world as world




class MyTestCase(unittest.TestCase):
    
    # def test_get_robot_name(self):
    #     self.assertEqual(get_robot_name(), ('hal'))


    def test_do_sprint(self):
        world.position_x = 0
        world.position_y = 0
        my_obstacle =obstacles.get_obstacles()
        self.assertEqual(do_sprint('Hal',10,my_obstacle), do_sprint('Hal', (10 -1),my_obstacle))


    def test_is_int(self):
        world.position_x = 0
        world.position_y = 0
        self.assertEqual(is_int(10), True) 


    def test_valid_command(self):
        world.position_x = 0
        world.position_y = 0
        self.assertEqual(valid_command('replay'), True) 


    def test_do_help(self):
        world.position_x = 0
        world.position_y = 0
        self.assertEqual(do_help(),(True , """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
"""))

    

    

   
    # def test_get_commands_history(self):
    #     self.assertEqual(get_commands_history(reverse, relativeStart, relativeEnd))

    # def test_handle_command(self):
    #     self.assertEqual(handle_command('hal',command,obstacles))                   













         

if __name__ == '__main__':
    unittest.main()



