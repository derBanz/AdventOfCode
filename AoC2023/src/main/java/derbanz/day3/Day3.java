package derbanz.day3;

import derbanz.params.Day;
import derbanz.params.Instructions;
import derbanz.params.Printer;

import java.time.Instant;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;

public class Day3 extends Day {

    @Override
    protected void doExecute(boolean isPartTwo, Instructions instructions, Instant start, boolean isTest) {
        int sum = 0;
        if (!isPartTwo) {
            sum = addPartNumbers(instructions);
        }
        Printer.printResult(String.valueOf(sum), 3, isPartTwo ? 2 : 1, start, isTest);
    }

    private int addPartNumbers(Instructions instructions) {
        AtomicInteger sum = new AtomicInteger();
        List<String> lines = instructions.getLines();
        final int maxY = lines.size() - 1;
        final int maxX = lines.getFirst().length() - 1;
        IntStream.range(0, maxY + 1).forEachOrdered(y -> {
            String line = lines.get(y);
            Map<Integer, Integer> currNum = new HashMap<>();
            IntStream.range(0, maxX + 1).forEachOrdered(x -> {
                int num = Character.getNumericValue(line.charAt(x)); // equals -1 for non-numericals

                if (num >= 0) {
                    currNum.put(x, num);
                }

                if (!currNum.isEmpty() && (num < 0 || x == maxX)) {
                    AtomicBoolean isPart = new AtomicBoolean(false);
                    IntStream.range(Math.max(0, currNum.keySet().stream().reduce(Integer::min).get() - 1), Math.min(maxX, x + 1) + 1).takeWhile(xi -> !isPart.get()).forEach(xi -> {
                        IntStream.range(Math.max(0, y - 1), Math.min(maxY, y + 1) + 1).takeWhile(yi -> !isPart.get()).forEach(yi -> {
                            char partNum = lines.get(yi).charAt(xi);
                            isPart.set(Character.getNumericValue(partNum) == -1 && partNum != '.');
                        });
                    });
                    if (isPart.get()) {
                        AtomicInteger number = new AtomicInteger();
                        currNum.values().forEach(c -> number.set(number.get() * 10 + c));
                        sum.getAndAdd(number.get());
                    }
                    currNum.clear();
                }
            });
        });
        return sum.get();
    }
}
