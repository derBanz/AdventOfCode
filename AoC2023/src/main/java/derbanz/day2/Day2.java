package derbanz.day2;

import derbanz.day2.params.Instructions;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;

public class Day2 {

    private final String path = "D:\\Documents\\Programming\\Java\\AdventOfCode\\AoC2023\\src\\main\\resources\\day2\\";

    public int execute(String file, boolean isPartTwo) {
        Instructions instructions = readInputFile(file, isPartTwo);
        int sum = 0;
        if (!isPartTwo) {
            sum = getSumOfPossibleIds(instructions);
        }
        return sum;
    }

    private Instructions readInputFile(String file, boolean isPartTwo) {
        Instructions instructions = new Instructions();
        try (Stream<String> stream = Files.lines(Path.of(path + file))) {
            stream.forEach(instructions::addLine);
        } catch (IOException e) {
            System.out.println(Arrays.stream(e.getStackTrace()).map(StackTraceElement::toString));
        }
        return instructions;
    }

    private int getSumOfPossibleIds(Instructions instructions) {
        Map<String, Integer> maxAmounts = Map.of("red", 12, "green", 13, "blue", 14);
        AtomicInteger sum = new AtomicInteger();
        instructions.getLines().forEach(line -> {
            boolean loop = true;
            String[] split = line.split(": ");
            String id = split[0].split(" ")[1];
            String[] sets = split[1].split("; ");
            int i = 0;
            while (loop) {
                String[] cubes = sets[i].split(", ");
                int j = 0;
                while (loop) {
                    String[] cube = cubes[j].split(" ");
                    if (Integer.parseInt(cube[0]) > maxAmounts.get(cube[1])) {
                        loop = false;
                    }
                    if (++j >= cubes.length) {
                        break;
                    }
                }
                if (loop && ++i >= sets.length) {
                    sum.getAndAdd(Integer.parseInt(id));
                    break;
                }
            }
        });
        return sum.get();
    }
}
