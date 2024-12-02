package derbanz;

import derbanz.day1.Day1;
import derbanz.params.Printer;

public class Main {


    public static void main(String[] args) {
        Printer printer = new Printer();
        printer.doDay(Day1.class, true);
    }
}