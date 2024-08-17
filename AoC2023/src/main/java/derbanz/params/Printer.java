package derbanz.params;

import java.time.Duration;
import java.time.Instant;

public class Printer {

    public static void printResult(String result, int day, int part, Instant instant, boolean isTest) {
        System.out.printf("*** Result for day %s part %s%s: %s ***%n", day, part, isTest ? " (test run)" : "", result);
        Duration between = Duration.between(instant, Instant.now());
        System.out.printf("Calculation took %sd %sh %sm %ss %sms %sns%n", between.toDays(), between.toHours(), between.toMinutes(), between.toSeconds(), between.toMillis(), between.toNanos());
    }

    public void doDay(Class<? extends Day> d, boolean isTest) {
        try {
            Day day = d.getDeclaredConstructor().newInstance();

            if (isTest) {
                day.test(false);
                day.test(true);
            } else {
                day.execute(false);
                day.execute(true);
            }
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }
}
