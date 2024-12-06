package derbanz.day4;

import derbanz.day4.params.DirectionEnum;
import derbanz.params.Day;
import derbanz.params.Instructions;
import derbanz.params.Printer;

import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;


public class Day4 extends Day {

    public final String XMAS = "XMAS";
    public final String MAS = "MAS";

    @Override
    protected void doExecute(boolean isPartTwo, Instructions instructions, Instant start, boolean isTest) {
        int result = countXMAS(instructions.getLines(), isPartTwo);
        Printer.printResult(String.valueOf(result), 4, isPartTwo ? 2 : 1, start, isTest);
    }

    private int countXMAS(List<String> lines, boolean isPartTwo) {
        AtomicInteger counter = new AtomicInteger();
        for (int y = 0; y < lines.size(); y++) {
            String line = lines.get(y);
            for (int x = 0; x < line.length(); x++) {
                char character = line.charAt(x);
                if (!isPartTwo && character == 'X') {
                    lookForGroups(lines, counter, x, y);
                } else if (isPartTwo && character == 'A') {
                    lookForMAS(lines, counter, x, y);
                }
            }
        }
        return counter.get();
    }

    private void lookForMAS(List<String> lines, AtomicInteger counter, int x, int y) {
        int maxX = lines.getFirst().length();
        int maxY = lines.size();
        if (x > 0 && x < maxX - 1 && y > 0 && y < maxY - 1) {
            boolean masOne = MAS.equals(Character.toString(lines.get(y - 1).charAt(x - 1))
                    + lines.get(y).charAt(x)
                    + lines.get(y + 1).charAt(x + 1));
            boolean masTwo = MAS.equals(Character.toString(lines.get(y + 1).charAt(x - 1))
                    + lines.get(y).charAt(x)
                    + lines.get(y - 1).charAt(x + 1));
            boolean masThree = MAS.equals(Character.toString(lines.get(y - 1).charAt(x + 1))
                    + lines.get(y).charAt(x)
                    + lines.get(y + 1).charAt(x - 1));
            boolean masFour = MAS.equals(Character.toString(lines.get(y + 1).charAt(x + 1))
                    + lines.get(y).charAt(x)
                    + lines.get(y - 1).charAt(x - 1));
            counter.getAndAdd((masOne || masFour) && (masTwo || masThree) ? 1 : 0);
        }
    }

    private void lookForGroups(List<String> lines, AtomicInteger counter, int x, int y) {
        int maxX = lines.getFirst().length();
        int maxY = lines.size();
        List<DirectionEnum> directions = new ArrayList<>(List.of(DirectionEnum.HORIZONTAL, DirectionEnum.VERTICAL,
                DirectionEnum.HORIZONTAL_BACK, DirectionEnum.VERTICAL_BACK, DirectionEnum.BOTTOM_RIGHT,
                DirectionEnum.BOTTOM_LEFT, DirectionEnum.TOP_RIGHT, DirectionEnum.TOP_LEFT));
        if (x < 3) {
            directions.removeAll(List.of(DirectionEnum.HORIZONTAL_BACK, DirectionEnum.TOP_LEFT, DirectionEnum.BOTTOM_LEFT));
        }
        if (x >= maxX - 3) {
            directions.removeAll(List.of(DirectionEnum.HORIZONTAL, DirectionEnum.TOP_RIGHT, DirectionEnum.BOTTOM_RIGHT));
        }
        if (y < 3) {
            directions.removeAll(List.of(DirectionEnum.VERTICAL_BACK, DirectionEnum.TOP_LEFT, DirectionEnum.TOP_RIGHT));
        }
        if (y >= maxY - 3) {
            directions.removeAll(List.of(DirectionEnum.VERTICAL, DirectionEnum.BOTTOM_LEFT, DirectionEnum.BOTTOM_RIGHT));
        }
        directions.forEach(direction -> {
            String xmas = switch (direction) {
                case HORIZONTAL -> lines.get(y).substring(x, x + 4);
                case VERTICAL -> Character.toString(lines.get(y).charAt(x))
                                + lines.get(y + 1).charAt(x)
                                + lines.get(y + 2).charAt(x)
                                + lines.get(y + 3).charAt(x);
                case HORIZONTAL_BACK -> Character.toString(lines.get(y).charAt(x))
                        + lines.get(y).charAt(x - 1)
                        + lines.get(y).charAt(x - 2)
                        + lines.get(y).charAt(x - 3);
                case VERTICAL_BACK -> Character.toString(lines.get(y).charAt(x))
                                + lines.get(y - 1).charAt(x)
                                + lines.get(y - 2).charAt(x)
                                + lines.get(y - 3).charAt(x);
                case TOP_LEFT -> Character.toString(lines.get(y).charAt(x))
                        + lines.get(y - 1).charAt(x - 1)
                        + lines.get(y - 2).charAt(x - 2)
                        + lines.get(y - 3).charAt(x - 3);
                case TOP_RIGHT -> Character.toString(lines.get(y).charAt(x))
                        + lines.get(y - 1).charAt(x + 1)
                        + lines.get(y - 2).charAt(x + 2)
                        + lines.get(y - 3).charAt(x + 3);
                case BOTTOM_LEFT -> Character.toString(lines.get(y).charAt(x))
                        + lines.get(y + 1).charAt(x - 1)
                        + lines.get(y + 2).charAt(x - 2)
                        + lines.get(y + 3).charAt(x - 3);
                case BOTTOM_RIGHT -> Character.toString(lines.get(y).charAt(x))
                        + lines.get(y + 1).charAt(x + 1)
                        + lines.get(y + 2).charAt(x + 2)
                        + lines.get(y + 3).charAt(x + 3);
            };
            counter.getAndAdd(xmas.equals(XMAS) ? 1 : 0);
        });
    }

}