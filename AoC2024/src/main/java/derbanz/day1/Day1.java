package derbanz.day1;

import derbanz.params.Day;
import derbanz.params.Instructions;
import derbanz.params.Printer;

import java.time.Instant;
import java.util.*;


public class Day1 extends Day {

    @Override
    protected void doExecute(boolean isPartTwo, Instructions instructions, Instant start, boolean isTest) {
        List<Integer> listOne = new ArrayList<>();
        List<Integer> listTwo = new ArrayList<>();
        instructions.getLines().forEach(line -> {
                    try {
                        String[] split = line.split("\\s+");
                        listOne.add(Integer.parseInt(split[0]));
                        listTwo.add(Integer.parseInt(split[1]));
                    } catch (IndexOutOfBoundsException err) {
                        int lineNumber = instructions.getLines().indexOf(line);
                        System.out.printf("Index out of bound for line %s. Line content: %s.", lineNumber, line);
                    } catch (NumberFormatException err) {
                        int lineNumber = instructions.getLines().indexOf(line);
                        System.out.printf("NumberFormatException for line %s. Line content: %s.", lineNumber, line);
                    } catch (Exception err) {
                        int lineNumber = instructions.getLines().indexOf(line);
                        System.out.printf("Exception in line %s. Line content: %s.", lineNumber, line);
                        err.printStackTrace();
                    }
        });
        int distance = 0;
        Collections.sort(listOne);
        Collections.sort(listTwo);
        for(int i = 0; i < instructions.getLines().size(); i++) {
            distance += Math.abs(listOne.get(i) - listTwo.get(i));
        }
        Printer.printResult(String.valueOf(distance), 1, isPartTwo ? 2 : 1, start, isTest);
    }

}