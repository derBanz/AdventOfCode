package derbanz.day3;

import derbanz.params.Day;
import derbanz.params.Instructions;
import derbanz.params.Printer;

import java.time.Instant;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;


public class Day3 extends Day {

    @Override
    protected void doExecute(boolean isPartTwo, Instructions instructions, Instant start, boolean isTest) {
        int result = getMultiplicationResult(instructions.getLines());
        Printer.printResult(String.valueOf(result), 3, isPartTwo ? 2 : 1, start, isTest);
    }

    private int getMultiplicationResult(List<String> lines) {
        String line = lines.stream().reduce("", String::concat);
        return Pattern.compile("mul\\(\\d+,\\d+\\)").matcher(line).results()
                .map(result -> Pattern.compile("\\d+").matcher(result.group()).results()
                        .map(r -> Integer.valueOf(r.group()))
                        .reduce(1, (a, b) -> a * b))
                .reduce(0, Integer::sum);
    }

}