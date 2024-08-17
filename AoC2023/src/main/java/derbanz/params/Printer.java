package derbanz.params;

import derbanz.day1.Day1;
import derbanz.day2.Day2;

import java.time.Duration;
import java.time.Instant;

public class Printer {

    public static void printResult(String result, int day, int part, Instant instant, boolean isTest) {
        System.out.printf("*** Result for day %s part %s%s: %s ***%n", day, part, isTest ? " (test run)" : "", result);
        Duration between = Duration.between(instant, Instant.now());
        System.out.printf("Calculation took %sd %sh %sm %ss %sms %sns%n", between.toDays(), between.toHours(), between.toMinutes(), between.toSeconds(), between.toMillis(), between.toNanos());
    }

    public void doDayTwo(boolean isTest) {
        Day2 day2 = new Day2();

        if (isTest) {
            day2.test(false);
            day2.test(true);
        } else {
            day2.execute(false);
            day2.execute(true);
        }
    }

    public void doDayOne(boolean isTest) {
        Day1 day1 = new Day1();

        if (isTest) {
            day1.test(false);
            day1.test(true);
        } else {
            day1.execute(false);
            day1.execute(true);
        }
    }
}
