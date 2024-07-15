package derbanz;

import derbanz.day1.Day1;

public class Main {


    public static void main(String[] args) {
        Day1 day1 = new Day1();
        int sum = day1.getSumOfCalibrationValues("input", true);
        System.out.println(sum);
    }
}