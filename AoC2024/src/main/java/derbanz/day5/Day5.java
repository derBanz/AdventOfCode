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
        List<List<Integer>> correctUpdates = new ArrayList<>();
        List<List<Integer>> erroneousUpdates = new ArrayList<>();
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
            if (take.get()) {
                correctUpdates.add(update);
            } else {
                erroneousUpdates.add(update);
            }
        });
        if (!isPartTwo) {
            correctUpdates.forEach(update -> {
                if (update.size() % 2 == 1) {
                    result.getAndAdd(update.get(update.size() / 2));
                }
            });
        } else {
            erroneousUpdates.forEach(update -> result.getAndAdd(fixUpdate(rules, update)));
        }
        return result.get();
    }

    private int fixUpdate(Map<Integer, List<Integer>> rules, List<Integer> update) {
        update.sort((a, b) -> {
            List<Integer> aRule = rules.get(a);
            List<Integer> bRule = rules.get(b);
            if (aRule != null && aRule.contains(b)) {
                return -1;
            } else if (bRule != null && bRule.contains(a)) {
                return 1;
            } else {
                return 0;
            }
        });
        return update.size() % 2 == 1 ? update.get(update.size() / 2) : 0;
    }

}