package derbanz.params;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.Instant;
import java.util.Arrays;
import java.util.stream.Stream;

public abstract class Day {

    protected final String PATH = "D:\\Documents\\Programming\\Java\\AdventOfCode\\AoC2023\\src\\main\\resources";

    public void execute(boolean isPartTwo) {
        Instant start = Instant.now();
        Instructions instructions = readInputFile("input");
        doExecute(isPartTwo, instructions, start, false);
    }

    public void test(boolean isPartTwo) {
        Instant start = Instant.now();
        Instructions instructions = readInputFile("input_part" + (isPartTwo ? 2 : 1) + "_test");
        doExecute(isPartTwo, instructions, start, true);
    }

    protected abstract void doExecute(boolean isPartTwo, Instructions instructions, Instant start,  boolean isTest);

    private Instructions readInputFile(String file) {
        Instructions instructions = new Instructions();
        String[] packageName = this.getClass().getPackageName().split("\\.");
        String path = String.format("%s\\%s\\", PATH, packageName[packageName.length - 1]);
        try (Stream<String> stream = Files.lines(Path.of(path + file))) {
            stream.forEach(instructions::addLine);
        } catch (IOException e) {
            System.out.println(Arrays.stream(e.getStackTrace()).map(StackTraceElement::toString));
        }
        return instructions;
    }
}
