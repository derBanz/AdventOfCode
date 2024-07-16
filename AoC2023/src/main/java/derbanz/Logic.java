package derbanz;

import derbanz.day1.Day1;
import derbanz.day2.Day2;

import java.time.Duration;
import java.time.Instant;

public class Logic {

    public void doDayTwo() {
        Day2 day2 = new Day2();

        Instant start = Instant.now();
        int sumOne = day2.execute("input", false);
        print(String.valueOf(sumOne), 2, 1, start);

//        start = Instant.now();
//        int sumTwo = day2.getSumOfImpossibleIds("input", true);
//        print(String.valueOf(sumTwo), 2, 2, start);

    }

    public void doDayOne() {
        Day1 day1 = new Day1();

        Instant start = Instant.now();
        int sumOne = day1.execute("input", false);
        print(String.valueOf(sumOne), 1, 1, start);

        start = Instant.now();
        int sumTwo = day1.execute("input", true);
        print(String.valueOf(sumTwo), 1, 2, start);
    }

    private void print(String result, int day, int part, Instant instant) {
        System.out.printf("Result for day %s part %s: %s%n", day, part, result);
        Duration between = Duration.between(instant, Instant.now());
        System.out.printf("Calculation took %sd %sh %sm %ss %sms %sns%n", between.toDays(), between.toHours(), between.toMinutes(), between.toSeconds(), between.toMillis(), between.toNanos());
    }
}
