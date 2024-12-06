package derbanz.day5;

import derbanz.params.Day;
import derbanz.params.Instructions;
import derbanz.params.Printer;

import java.time.Instant;
import java.util.*;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;

public class Day5 extends Day {

    @Override
    protected void doExecute(boolean isPartTwo, Instructions instructions, Instant start, boolean isTest) {
        int result = getResult(isPartTwo, instructions);
        Printer.printResult(String.valueOf(result), 5, isPartTwo ? 2 : 1, start, isTest);
    }

    private int getResult(boolean isPartTwo, Instructions instructions) {
        AtomicInteger result = new AtomicInteger();
        Map<Integer, List<Integer>> rules = new HashMap<>();
        List<List<Integer>> updates = new ArrayList<>();
        instructions.getLines().forEach(line -> {
            String[] split = line.split(",");
            if (split.length > 1) {
                updates.add(new ArrayList<>());
                Stream.of(split).forEach(s -> updates.getLast().add(Integer.valueOf(s)));
            } else {
                split = line.split("\\|");
                if (split.length > 1) {
                    List<Integer> rule = rules.computeIfAbsent(Integer.valueOf(split[0]), k -> new ArrayList<>());
                    rule.add(Integer.valueOf(split[1]));
                }
            }
        });
        updates.forEach(update -> {
            AtomicBoolean take = new AtomicBoolean(true);
            List<Integer> computed = new ArrayList<>();
            update.stream().takeWhile(u -> take.get()).forEach(u -> {
                if (rules.get(u) == null || rules.get(u).stream().filter(computed::contains).toList().isEmpty()) {
                    computed.add(u);
                } else {
                    take.set(false);
                }
            });
            if (take.get() && computed.size() % 2 == 1) {
                result.getAndAdd(computed.get(computed.size() / 2));
            }
        });
        return result.get();
    }

}