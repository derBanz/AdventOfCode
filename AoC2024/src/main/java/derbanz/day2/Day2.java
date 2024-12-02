package derbanz.day2;

import derbanz.day2.params.Day2Report;
import derbanz.params.Day;
import derbanz.params.Instructions;
import derbanz.params.Printer;

import java.time.Instant;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;


public class Day2 extends Day {

    private enum LevelStatus {
        NONE,
        ASC,
        DESC;
    }

    @Override
    protected void doExecute(boolean isPartTwo, Instructions instructions, Instant start, boolean isTest) {
        List<Day2Report> reports = instructions.getLines().stream().map(Day2Report::initialize).toList();
        AtomicInteger count = new AtomicInteger();
        countSafeReports(reports, count);

        Printer.printResult(String.valueOf(count.get()), 1, isPartTwo ? 2 : 1, start, isTest);
    }

    private void countSafeReports(List<Day2Report> reports, AtomicInteger count) {
        reports.forEach(report -> count.getAndAdd(isSafeReport(report.getLevels()) ? 1 : 0));
    }

    private boolean isSafeReport(List<Integer> levels) {
        LevelStatus status = LevelStatus.NONE;
        for (int i = 1; i < levels.size(); i++) {
            int diff = levels.get(i) - levels.get(i - 1);
            if (status.equals(LevelStatus.NONE)) {
                status = diff != 0 ? (diff > 0 ? LevelStatus.ASC : LevelStatus.DESC) : LevelStatus.NONE;
            }
            switch (status) {
                case NONE -> {
                    return false;
                }
                case ASC -> {
                    if (diff <= 0 || diff > 3) {
                        return false;
                    }
                }
                case DESC -> {
                    if (diff >= 0 || diff < -3) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

}