package derbanz.day6;

import derbanz.day6.params.Direction;
import derbanz.day6.params.Plan;
import derbanz.params.Day;
import derbanz.params.Instructions;
import derbanz.params.Printer;

import java.time.Instant;
import java.util.*;

public class Day6 extends Day {

    @Override
    protected void doExecute(boolean isPartTwo, Instructions instructions, Instant start, boolean isTest) {
        Plan plan = createPlan(instructions);
        boolean onTheMap = plan.getFacingDirection() != null;
        while (onTheMap) {
            onTheMap = move(plan);
        }
        int result = plan.getMap().stream().flatMap(Collection::stream).map(v -> (v.equals(".") || v.equals("#")) ? 0 : 1).reduce(0, Integer::sum);
        Printer.printResult(String.valueOf(result), 5, isPartTwo ? 2 : 1, start, isTest);
    }

    private Plan createPlan(Instructions instructions) {
        Plan plan = new Plan();
        List<List<String>> map = new ArrayList<>();
        plan.setMaxY(instructions.getLines().size() - 1);
        plan.setMaxX(plan.getMaxY() > 0 ? instructions.getLines().getFirst().length() - 1 : 0);
        for (int y = 0; y <= plan.getMaxY(); y++) {
            String line = instructions.getLines().get(y);
            List<String> l = new ArrayList<>();
            for (int x = 0; x <= line.length() - 1; x++) {
                char c = line.charAt(x);
                switch (Character.toString(c)) {
                    case "^" -> {
                        setOriginalPosition(plan, x, y, Direction.NORTH);
                        l.add("^");
                    }
                    case "v" -> {
                        setOriginalPosition(plan, x, y, Direction.SOUTH);
                        l.add("v");
                    }
                    case ">" -> {
                        setOriginalPosition(plan, x, y, Direction.EAST);
                        l.add(">");
                    }
                    case "<" -> {
                        setOriginalPosition(plan, x, y, Direction.WEST);
                        l.add("<");
                    }
                    case "#" -> {
                        l.add("#");
                    }
                    default -> {
                        l.add(".");
                    }
                }
            }
            map.add(l);
        }
        plan.setMap(map);
        return plan;
    }

    private void setOriginalPosition(Plan plan, int x, int y, Direction direction) {
        plan.setPositionX(x);
        plan.setPositionY(y);
        plan.setFacingDirection(direction);
    }

    private boolean move(Plan plan) {
        int x = plan.getPositionX();
        int y = plan.getPositionY();
        switch (plan.getFacingDirection()) {
            case NORTH -> {
                if (y == 0) {
                    return false;
                }
                if (plan.getMap().get(--y).get(x).equals("#")) {
                    plan.setFacingDirection(Direction.EAST);
                    plan.getMap().get(++y).set(x,">");
                    return move(plan);
                }
                plan.setPositionY(y);
                plan.getMap().get(y).set(x,"^");

            }
            case EAST -> {
                if (x == plan.getMaxX()) {
                    return false;
                }
                if (plan.getMap().get(y).get(++x).equals("#")) {
                    plan.setFacingDirection(Direction.SOUTH);
                    plan.getMap().get(y).set(--x,"v");
                    return move(plan);
                }
                plan.setPositionX(x);
                plan.getMap().get(y).set(x,">");
            }
            case SOUTH -> {
                if (y == plan.getMaxY()) {
                    return false;
                }
                if (plan.getMap().get(++y).get(x).equals("#")) {
                    plan.setFacingDirection(Direction.WEST);
                    plan.getMap().get(--y).set(x,"<");
                    return move(plan);
                }
                plan.setPositionY(y);
                plan.getMap().get(y).set(x,"v");
            }
            case WEST -> {
                if (x == 0) {
                    return false;
                }
                if (plan.getMap().get(y).get(--x).equals("#")) {
                    plan.setFacingDirection(Direction.NORTH);
                    plan.getMap().get(y).set(++x,"^");
                    return move(plan);
                }
                plan.setPositionX(x);
                plan.getMap().get(y).set(x,"<");
            }
        }
        return true;
    }

    private void printPlan(Plan plan) {
        plan.getMap().forEach(planLine -> {
            planLine.forEach(p -> System.out.print(p + "\t"));
            System.out.println();
        });
            System.out.println();
    }

}