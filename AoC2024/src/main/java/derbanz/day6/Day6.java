package derbanz.day6;

import derbanz.day6.params.Direction;
import derbanz.day6.params.Plan;
import derbanz.day6.params.GuardStatus;
import derbanz.params.Day;
import derbanz.params.Instructions;
import derbanz.params.Printer;

import java.time.Instant;
import java.util.*;

public class Day6 extends Day {

    @Override
    protected void doExecute(boolean isPartTwo, Instructions instructions, Instant start, boolean isTest) {
        Plan plan = createPlan(instructions);
        int result;
        if (isPartTwo) {
            result = 0;
            while (true) {
                Plan planCopy = setObstacle(plan);
                if (planCopy == null) {
                    break;
                }
                GuardStatus status = getResult(planCopy);
                if (status.equals(GuardStatus.LOOP)) {
                    result++;
                }
                status = move(plan);
                if (status.equals(GuardStatus.OFFMAP)) {
                    break;
                }
            }
        } else {
            getResult(plan);
            result = plan.getMap().stream().flatMap(Collection::stream).map(v -> v > 0 ? 1 : 0).reduce(0, Integer::sum);
        }
        Printer.printResult(String.valueOf(result), 6, isPartTwo ? 2 : 1, start, isTest);
    }

    private Plan setObstacle(Plan plan) {
        Plan planCopy = copyPlan(plan);
        switch (planCopy.getFacingDirection()) {
            case NORTH -> {
                if (planCopy.getPositionY() == 0) {
                    return null;
                }
                if (planCopy.getMap().get(planCopy.getPositionY() - 1).get(planCopy.getPositionX()).equals(-1)) {
                    planCopy.setFacingDirection(Direction.EAST);
                    return setObstacle(planCopy);
                }
                if (planCopy.getMap().get(planCopy.getPositionY() - 1).get(planCopy.getPositionX()) == 0) {
                    planCopy.getMap().get(planCopy.getPositionY() - 1).set(planCopy.getPositionX(), -1);
                }
            }
            case EAST -> {
                if (planCopy.getPositionX() == plan.getMaxX()) {
                    return null;
                }
                if (planCopy.getMap().get(planCopy.getPositionY()).get(planCopy.getPositionX() + 1).equals(-1)) {
                    planCopy.setFacingDirection(Direction.SOUTH);
                    return setObstacle(planCopy);
                }
                if (planCopy.getMap().get(planCopy.getPositionY()).get(planCopy.getPositionX() + 1) == 0) {
                    planCopy.getMap().get(planCopy.getPositionY()).set(planCopy.getPositionX() + 1, -1);
                }
            }
            case SOUTH -> {
                if (planCopy.getPositionY() == planCopy.getMaxY()) {
                    return null;
                }
                if (planCopy.getMap().get(planCopy.getPositionY() + 1).get(planCopy.getPositionX()).equals(-1)) {
                    planCopy.setFacingDirection(Direction.WEST);
                    return setObstacle(planCopy);
                }
                if (planCopy.getMap().get(planCopy.getPositionY() + 1).get(planCopy.getPositionX()) == 0) {
                    planCopy.getMap().get(planCopy.getPositionY() + 1).set(planCopy.getPositionX(), -1);
                }
            }
            case WEST -> {
                if (planCopy.getPositionX() == 0) {
                    return null;
                }
                if (planCopy.getMap().get(planCopy.getPositionY()).get(planCopy.getPositionX() - 1).equals(-1)) {
                    planCopy.setFacingDirection(Direction.NORTH);
                    return setObstacle(planCopy);
                }
                if (planCopy.getMap().get(planCopy.getPositionY()).get(planCopy.getPositionX() - 1) == 0) {
                    planCopy.getMap().get(planCopy.getPositionY()).set(planCopy.getPositionX() - 1, -1);
                }
            }
        }
        return planCopy;
    }

    private Plan copyPlan(Plan plan) {
        Plan planCopy = new Plan();
        planCopy.setPositionX(plan.getPositionX());
        planCopy.setPositionY(plan.getPositionY());
        planCopy.setMaxX(plan.getMaxX());
        planCopy.setMaxY(plan.getMaxY());
        planCopy.setFacingDirection(plan.getFacingDirection());
        planCopy.setMap(new ArrayList<>());
        plan.getMap().forEach(line -> planCopy.getMap().add(new ArrayList<>(line)));
        return planCopy;
    }

    private GuardStatus getResult(Plan plan) {
        GuardStatus status = GuardStatus.WALKING;
        while (status.equals(GuardStatus.WALKING)) {
            status = move(plan);
        }
        return status;
    }

    private GuardStatus move(Plan plan) {
        int x = plan.getPositionX();
        int y = plan.getPositionY();
        switch (plan.getFacingDirection()) {
            case NORTH -> {
                if (y == 0) {
                    return GuardStatus.OFFMAP;
                }
                if (plan.getMap().get(--y).get(x).equals(-1)) {
                    plan.setFacingDirection(Direction.EAST);
                    return move(plan);
                }
                plan.setPositionY(y);

            }
            case EAST -> {
                if (x == plan.getMaxX()) {
                    return GuardStatus.OFFMAP;
                }
                if (plan.getMap().get(y).get(++x).equals(-1)) {
                    plan.setFacingDirection(Direction.SOUTH);
                    return move(plan);
                }
                plan.setPositionX(x);
            }
            case SOUTH -> {
                if (y == plan.getMaxY()) {
                    return GuardStatus.OFFMAP;
                }
                if (plan.getMap().get(++y).get(x).equals(-1)) {
                    plan.setFacingDirection(Direction.WEST);
                    return move(plan);
                }
                plan.setPositionY(y);
            }
            case WEST -> {
                if (x == 0) {
                    return GuardStatus.OFFMAP;
                }
                if (plan.getMap().get(y).get(--x).equals(-1)) {
                    plan.setFacingDirection(Direction.NORTH);
                    return move(plan);
                }
                plan.setPositionX(x);
            }
        }
        int visits = plan.getMap().get(y).get(x);
        if (visits < 5) {
            plan.getMap().get(y).set(x, ++visits);
            return GuardStatus.WALKING;
        }
        return GuardStatus.LOOP;
    }

    private Plan createPlan(Instructions instructions) {
        Plan plan = new Plan();
        List<List<Integer>> map = new ArrayList<>();
        plan.setMaxY(instructions.getLines().size() - 1);
        plan.setMaxX(plan.getMaxY() > 0 ? instructions.getLines().getFirst().length() - 1 : 0);
        for (int y = 0; y <= plan.getMaxY(); y++) {
            String line = instructions.getLines().get(y);
            List<Integer> l = new ArrayList<>();
            for (int x = 0; x <= line.length() - 1; x++) {
                char c = line.charAt(x);
                switch (Character.toString(c)) {
                    case "^" -> {
                        setOriginalPosition(plan, x, y, Direction.NORTH);
                        l.add(1);
                    }
                    case "v" -> {
                        setOriginalPosition(plan, x, y, Direction.SOUTH);
                        l.add(1);
                    }
                    case ">" -> {
                        setOriginalPosition(plan, x, y, Direction.EAST);
                        l.add(1);
                    }
                    case "<" -> {
                        setOriginalPosition(plan, x, y, Direction.WEST);
                        l.add(1);
                    }
                    case "#" -> {
                        l.add(-1);
                    }
                    default -> {
                        l.add(0);
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

    private void printPlan(Plan plan) {
        if (plan == null) return;
        plan.getMap().forEach(planLine -> {
            planLine.forEach(p -> System.out.print(p + "\t"));
            System.out.println();
        });
            System.out.println();
    }

}