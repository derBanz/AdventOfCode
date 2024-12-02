package derbanz.day2;

import derbanz.day2.params.Day2Report;
import derbanz.params.Day;
import derbanz.params.Instructions;
import derbanz.params.Printer;

import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;


public class Day2 extends Day {

    private enum ReportStatus {
        NONE,
        ASC,
        DESC;
    }

    @Override
    protected void doExecute(boolean isPartTwo, Instructions instructions, Instant start, boolean isTest) {
        List<Day2Report> reports = instructions.getLines().stream().map(Day2Report::initialize).toList();
        AtomicInteger count = new AtomicInteger();
        countSafeReports(reports, count, isPartTwo);

        Printer.printResult(String.valueOf(count.get()), 2, isPartTwo ? 2 : 1, start, isTest);
    }

    private void countSafeReports(List<Day2Report> reports, AtomicInteger count, boolean isPartTwo) {
        reports.forEach(report -> count.getAndAdd(isSafeReport(report.getLevels(), isPartTwo) ? 1 : 0));
    }

    private boolean isSafeReport(List<Integer> levels, boolean applyProblemDampener) {
        ReportStatus status = ReportStatus.NONE;
        for (int i = 1; i < levels.size(); i++) {
            int diff = levels.get(i) - levels.get(i - 1);
            if (status.equals(ReportStatus.NONE)) {
                // only true for i == 1
                if (diff == 0 && applyProblemDampener) {
                    diff = levels.get(i + 1) - levels.get(i); //drop one of the identical ones as problem dampening
                    status = diff != 0 ? (diff > 0 ? ReportStatus.ASC : ReportStatus.DESC) : ReportStatus.NONE;
                    applyProblemDampener = false;
                } else {
                    status = diff != 0 ? (diff > 0 ? ReportStatus.ASC : ReportStatus.DESC) : ReportStatus.NONE;
                }
            }
            switch (status) {
                case NONE -> {
                    return false;
                }
                case ASC -> {
                    if (diff <= 0 || diff > 3) {
                        return handleProblem(levels, i, applyProblemDampener);
                    }
                }
                case DESC -> {
                    if (diff >= 0 || diff < -3) {
                        return handleProblem(levels, i, applyProblemDampener);
                    }
                }
            }
        }
        return true;
    }

    private boolean handleProblem(List<Integer> levels, int i, boolean applyProblemDampener) {List<Integer> opt1 = new ArrayList<>(List.of(levels.toArray(new Integer[0])));
        opt1.remove(i - 1);
        List<Integer> opt2 = new ArrayList<>(List.of(levels.toArray(new Integer[0])));
        opt2.remove(i);
        List<Integer> opt3 = new ArrayList<>(List.of(levels.toArray(new Integer[0])));
        if (i < levels.size() - 1) {
            opt3.remove(i + 1);
        }
        List<Integer> opt4 = new ArrayList<>(List.of(levels.toArray(new Integer[0])));
        if (i == 2) {
            opt4.removeFirst();
        }
        return applyProblemDampener // f
                && (isSafeReport(opt1, false)
                || isSafeReport(opt2, false)
                || isSafeReport(opt3, false)
                || isSafeReport(opt4, false));
    }

}