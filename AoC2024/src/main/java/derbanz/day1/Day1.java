package derbanz.day1;

import derbanz.params.Day;
import derbanz.params.Instructions;
import derbanz.params.Printer;

import java.time.Instant;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;


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
        int result = isPartTwo ? getSimilarityScore(listOne, listTwo) : getTotalDistance(listOne, listTwo);
        Printer.printResult(String.valueOf(result), 1, isPartTwo ? 2 : 1, start, isTest);
    }

    private int getTotalDistance(List<Integer> listOne, List<Integer> listTwo) {
        int distance = 0;
        Collections.sort(listOne);
        Collections.sort(listTwo);
        for(int i = 0; i < listOne.size(); i++) {
            distance += Math.abs(listOne.get(i) - listTwo.get(i));
        }
        return distance;
    }

    private int getSimilarityScore(List<Integer> listOne, List<Integer> listTwo) {
        AtomicInteger similarityScore = new AtomicInteger();
        listOne.forEach(num -> similarityScore.getAndAdd(num * listTwo.stream().filter(l -> l.equals(num)).toList().size()));
        return similarityScore.get();
    }

}