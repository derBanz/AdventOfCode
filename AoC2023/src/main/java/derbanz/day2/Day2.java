package derbanz.day2;

import derbanz.params.Day;
import derbanz.params.Instructions;
import derbanz.params.Printer;
import java.time.Instant;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;

public class Day2 extends Day {

    @Override
    protected void doExecute(boolean isPartTwo, Instructions instructions, Instant start, boolean isTest) {
        int sum = 0;
        if (!isPartTwo) {
            sum = getSumOfPossibleIds(instructions);
        }
        Printer.printResult(String.valueOf(sum), 1, isPartTwo ? 2 : 1, start, isTest);
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
