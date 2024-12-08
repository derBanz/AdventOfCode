package derbanz.day7;

import derbanz.params.Day;
import derbanz.params.Instructions;
import derbanz.params.Printer;

import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicLong;

public class Day7 extends Day {

    @Override
    protected void doExecute(boolean isPartTwo, Instructions instructions, Instant start, boolean isTest) {
        AtomicLong result = new AtomicLong();
        List<Operator> allowedOperators = new ArrayList<>(List.of(Operator.SUM, Operator.MUL));
        if (isPartTwo) {
            allowedOperators.add(Operator.CAT);
        }
        int alOps = allowedOperators.size();
        instructions.getLines().forEach(line -> {
            String[] resultSplit = line.split(": ");
            long res = Long.parseLong(resultSplit[0]);
            String[] argSplit = resultSplit[1].split(" ");
            int args = argSplit.length;
            int ops = args - 1;
            for (int i = 0; i < Math.pow(alOps, ops); i++) {
                long arg1 = Integer.parseInt(argSplit[0]);
                for (int j = 0; j < ops; j++) {
                    long arg2 = Integer.parseInt(argSplit[j + 1]);
                    arg1 = compute(allowedOperators.get((int) (i / Math.pow(alOps, ops - j - 1)) % alOps), arg1, arg2);
                }
                if (arg1 == res) {
                    result.getAndAdd(res);
                    break;
                }
            }
        });
        Printer.printResult(String.valueOf(result.get()), 7, isPartTwo ? 2 : 1, start, isTest);
    }

    private long compute(Operator operator, long arg1, long arg2) {
        return switch (operator) {
            case SUM -> arg1 + arg2;
            case MUL -> arg1 * arg2;
            case CAT -> Long.parseLong(String.valueOf(arg1).concat(String.valueOf(arg2)));
        };
    }

    private enum Operator {
        SUM,
        MUL,
        CAT
    }

}