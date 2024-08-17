package derbanz.day1;

import derbanz.params.Day;
import derbanz.params.Instructions;
import derbanz.params.Printer;

import java.time.Instant;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;


public class Day1 extends Day {

    @Override
    protected void doExecute(boolean isPartTwo, Instructions instructions, Instant start, boolean isTest) {
        AtomicInteger calibration = new AtomicInteger();
        Map<String, Integer> numbers = initialize(isPartTwo);
        instructions.getLines().forEach(line -> calibration.getAndAdd(getCalibrationValueForLine(numbers, line)));
        Printer.printResult(String.valueOf(calibration.get()), 1, isPartTwo ? 2 : 1, start, isTest);
    }

    private int getCalibrationValueForLine(Map<String, Integer> numbers, String line) {
        String first = numbers.keySet().stream().min(Comparator.comparing(num -> line.contains(num) ? line.indexOf(num) : line.length() + 1)).orElse("0");
        String last = numbers.keySet().stream().max(Comparator.comparing(line::lastIndexOf)).orElse("0");
        return numbers.get(first) * 10 + numbers.get(last);
    }

    private Map<String, Integer> initialize(boolean isPart2) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < 10; i++) {
            map.put(String.valueOf(i), i);
        }
        if (isPart2) {
            map.put("zero", 0);
            map.put("one", 1);
            map.put("two", 2);
            map.put("three", 3);
            map.put("four", 4);
            map.put("five", 5);
            map.put("six", 6);
            map.put("seven", 7);
            map.put("eight", 8);
            map.put("nine", 9);
        }
        return map;
    }

}