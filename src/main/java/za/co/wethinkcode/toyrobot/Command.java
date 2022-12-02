package za.co.wethinkcode.toyrobot;

public  abstract class Command {
    private final String name;
    private String argument;

    public Command(String name){
        String[] args = name.strip().split(" ");
        name = args[0].trim().toLowerCase();
        this.name = name;
    }

    public String getName() {
        return name;
    }
    public Command(String name, String argument) {
        this(name);
        this.argument = argument.trim();
    }
    public String getArgument() {
        return this.argument;
    }
    public static Command create(String instruction) {
        String[] args = instruction.toLowerCase().trim().split(" ");
        switch (args[0]){
            case "shutdown":
                return new ShutdownCommand();
            case "help":
                return new HelpCommand();
            case "forward":
                return new ForwardCommand(args[1]);
            default:
                throw new IllegalArgumentException("Unsupported command: " + instruction);
        }
    }

    public abstract boolean execute(Robot target);

}

