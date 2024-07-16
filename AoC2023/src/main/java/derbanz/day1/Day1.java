package derbanz.day1;

import derbanz.day1.params.Instructions;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;


public class Day1 {

    private final String path = "D:\\Documents\\Programming\\Java\\AdventOfCode\\AoC2023\\src\\main\\resources\\day1\\";

    public int execute(String file, boolean isPartTwo) {
        Instructions instructions = readInputFile(file, isPartTwo);
        AtomicInteger calibration = new AtomicInteger();
        instructions.getLines().forEach(line -> calibration.getAndAdd(getCalibrationValueForLine(instructions.getNumbers(), line)));
        return calibration.get();
    }

    private Instructions readInputFile(String file, boolean isPartTwo) {
        Instructions instructions = new Instructions(isPartTwo);
        try (Stream<String> stream = Files.lines(Path.of(path + file))) {
            stream.forEach(instructions::addLine);
        } catch (IOException e) {
            System.out.println(Arrays.stream(e.getStackTrace()).map(StackTraceElement::toString));
        }
        return instructions;
    }

    private int getCalibrationValueForLine(Map<String, Integer> numbers, String line) {
        String first = numbers.keySet().stream().min(Comparator.comparing(num -> line.contains(num) ? line.indexOf(num) : line.length() + 1)).orElse("0");
        String last = numbers.keySet().stream().max(Comparator.comparing(line::lastIndexOf)).orElse("0");
        int result = numbers.get(first) * 10 + numbers.get(last);
        return result;
    }
}