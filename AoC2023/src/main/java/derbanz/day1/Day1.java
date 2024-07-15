package derbanz.day1;

import derbanz.day1.params.Instructions;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;
import java.util.stream.Stream;


public class Day1 {

    private String path = "D:\\Documents\\Programming\\Java\\AdventOfCode\\AoC2023\\src\\main\\resources\\day1\\";

    public int getSumOfCalibrationValues (String file) {
        Instructions instructions = readInputFile(file);
        AtomicInteger calibration = new AtomicInteger();
        instructions.getLines().forEach(line -> {
            calibration.getAndAdd(getCalibrationValueForLine(line));
        });
        return calibration.get();
    }

    private Instructions readInputFile(String file) {
        Instructions instructions = new Instructions();
        try (Stream<String> stream = Files.lines(Path.of(path + file))) {
            stream.forEach(instructions::addLine);
        } catch (IOException e) {
            System.out.println(Arrays.stream(e.getStackTrace()).map(StackTraceElement::toString));
        }
        return instructions;
    }

    private int getCalibrationValueForLine(String line) {
        List<Character> numbers = line.chars().filter(Character::isDigit).mapToObj(ch -> (char) ch).toList();
        int size = numbers.size();
        int number = 0;
        if (size > 0) {
            number += Character.getNumericValue(numbers.getFirst()) * 10;
            number += Character.getNumericValue(numbers.get(size - 1));
        }
        return number;
    }
}