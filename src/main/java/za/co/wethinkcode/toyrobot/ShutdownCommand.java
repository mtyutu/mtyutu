package za.co.wethinkcode.toyrobot;

public class ShutdownCommand extends Command {
    public ShutdownCommand(String name) {
        super(name);
    }

    public ShutdownCommand() {
        super("off");
    }

    public String getName() {
        return "off";
    }

    @Override
    public boolean execute(Robot target) {
        target.setStatus("Shutting down...");
        return true;
    }

}

