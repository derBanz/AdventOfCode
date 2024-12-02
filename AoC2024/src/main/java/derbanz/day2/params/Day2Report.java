package derbanz.day2.params;

import java.util.Arrays;
import java.util.List;

public class Day2Report {
    private List<Integer> levels;

    public List<Integer> getLevels() {
        return levels;
    }

    public void setLevels(List<Integer> levels) {
        this.levels = levels;
    }

    public static Day2Report initialize(String levels) {
        Day2Report report = new Day2Report();
        report.setLevels(Arrays.stream(levels.split("\\s+")).map(Integer::valueOf).toList());
        return report;
    }
}
