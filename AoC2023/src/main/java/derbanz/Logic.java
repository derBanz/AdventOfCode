package derbanz;

import derbanz.day1.Day1;
import derbanz.day2.Day2;

import java.time.Duration;
import java.time.Instant;

public class Logic {

    public void doDayTwo() {
        Day2 day2 = new Day2();
        Instant start = Instant.now();
        int sumOne = day2.getSumOfImpossibleIds("input", false);
        print(String.valueOf(sumOne), 2, 1, start);
    }

    public void doDayOne() {
        Day1 day1 = new Day1();
        Instant start = Instant.now();
        int sumOne = day1.getSumOfCalibrationValues("input", false);
        print(String.valueOf(sumOne), 1, 1, start);
        start = Instant.now();
        int sumTwo = day1.getSumOfCalibrationValues("input", true);
        print(String.valueOf(sumTwo), 1, 2, start);
    }

    private void print(String result, int day, int part, Instant instant) {
        System.out.println(String.format("Result for day %s part %s: %s", day, part, result));
        Duration between = Duration.between(instant, Instant.now());
        System.out.println(String.format("Calculation took %sd %sh %sm %ss %sms %sns", between.toDays(), between.toHours(), between.toMinutes(), between.toSeconds(), between.toMillis(), between.toNanos()));
    }
}
