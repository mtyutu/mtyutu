package za.co.wethinkcode.toyrobot;

import java.util.Arrays;
import java.util.List;



public class Robot {
    private static final List<String> VALID_COMMANDS = Arrays.asList("off", "help", "forward");

    private static final int MIN_Y = -200;
    private static final int MAX_Y = 200;
    private static final int MIN_X = -100;
    private static final int MAX_X = 100;

    public static final Position CENTRE = new Position(0, 0);

    private Position position;
    private final Direction currentDirection;
    private String status;
    private final String name;
    private Position TOP_LEFT = new Position(-100,100);
    private Position BOTTOM_RIGHT= new Position(100,-200);

    public Robot(String name) {
        this.name = name;
        this.status = "Ready";
        this.position = CENTRE;
        this.currentDirection = Direction.NORTH;
    }

    public String getStatus() {                                                                         //<5>
        return this.status;
    }

    public int getPositionX() {                                                                         //<6>
        return this.position.getY();
    }

    public int getPositionY() {                                                                         //<7>
        return this.position.getX();
    }
    public Position getPosition() {
        return this.position;
    }


    public Direction getCurrentDirection() {                                                               //<8>
        return this.currentDirection;
    }

    public boolean isValidCommand(String commandInput){
        String[] args = commandInput.strip().split(" ");
        String command = args[0].trim().toLowerCase();
        return VALID_COMMANDS.contains(command);
    }

    public boolean handleCommand(Command command){
//        if (!isValidCommand(commandInput)) {
//           this.status = "I am not programmed to: " + commandInput;
//           return false;
//        }
//
//        String[] args = commandInput.strip().split(" ");
//        String command = args[0].trim().toLowerCase();

//        switch (command){
//            case "off":
//                this.status = "Shutting down";
//                break;
//            case "help":
//                this.status = doHelp();
//                break;
//            case "forward":
//                this.status = doForward(Integer.parseInt(args[1]));
//                break;
//            default:
//                this.status = "I am not programmed for: " + command;
//        }
        return command.execute(this);
    }

    String doHelp() {
        return "I can understand these commands:\n" +
                "OFF  - Shut down robot\n" +
                "HELP - provide information about commands\n" +
                "FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'";
    }


    private boolean isPositionAllowed(int newX, int newY){
        return MIN_X <= newX && newX <= MAX_X
                && MIN_Y <= newY && newY <= MAX_Y;
    }

    boolean updatePosition(int nrSteps){
        int newY = this.position.getX();
        int newX = this.position.getY();

        if (Direction.NORTH.equals(this.currentDirection)) {
            newY = newY + nrSteps;
        }

        Position newPosition = new Position(newX, newY);
        if (newPosition.isIn(TOP_LEFT,BOTTOM_RIGHT)){
            this.position = newPosition;
            return true;
        }
        return false;
    }


    public String doForward(int nrSteps){
        if (updatePosition(nrSteps)){
            return "Moved forward by "+nrSteps+" steps.";
        } else {
            return "Sorry, I cannot go outside my safe zone.";
        }
    }

    @Override
    public String toString() {
       return "[" + this.position.getX() + "," + this.position.getY() + "] "
//               + "{" + this.currentDirection + "} "
               + this.name + "> " + this.status;
    }

    public void setStatus(String s) {
        this.status = s;
    }
}
