package za.co.wethinkcode.toyrobot;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


public class RobotTest {


    @Test
    void initialPosition() {
        Robot robot = new Robot("CrashTestDummy");
        assertEquals(Robot.CENTRE, robot.getPosition());
        assertEquals(Direction.NORTH, robot.getCurrentDirection());
    }


    @Test
    void dump() {
        Robot robot = new Robot("CrashTestDummy");
        assertEquals("[0,0] CrashTestDummy> Ready", robot.toString());
    }


    @Test
    void forward() {
        Robot robot = new Robot("CrashTestDummy");
        ForwardCommand command = new ForwardCommand("10");
        assertTrue(robot.handleCommand(command));
        Position expectedPosition = new Position(Robot.CENTRE.getX(), Robot.CENTRE.getY() + 10);
        assertEquals(expectedPosition, robot.getPosition());
        assertEquals("Moved forward by 10 steps.", robot.getStatus());
    }


    @Test
    public void insideRectangularRegion() {
        Position topLeft = new Position(-20, 20);
        Position bottomRight = new Position(20,-20);
        assertTrue((new Position(10,10)).isIn(topLeft, bottomRight), "should be inside");
        assertFalse((new Position(10,30)).isIn(topLeft, bottomRight), "should be beyond top boundary");
        assertFalse((new Position(10,-30)).isIn(topLeft, bottomRight), "should be beyond bottom boundary");
        assertFalse((new Position(30,10)).isIn(topLeft, bottomRight), "should be beyond right boundary");
        assertFalse((new Position(-30,10)).isIn(topLeft, bottomRight), "should be beyond left boundary");
    }
}



