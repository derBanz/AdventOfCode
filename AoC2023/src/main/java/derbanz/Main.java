package derbanz;

import derbanz.day1.Day1;
import derbanz.day2.Day2;
import derbanz.day3.Day3;
import derbanz.params.Printer;

public class Main {


    public static void main(String[] args) {
        Printer printer = new Printer();
        printer.doDay(Day1.class, false);
        printer.doDay(Day2.class, false);
        printer.doDay(Day3.class, false);
    }
}