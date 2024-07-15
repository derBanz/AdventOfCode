package derbanz.day1.params;

import java.util.*;

public class Instructions {

    private List<String> lines = new ArrayList<>();
    private Map<String, Integer> numbers = new HashMap<>();

    public Instructions(boolean isPartTwo) {
        initialize(isPartTwo);
    }

    public List<String> getLines() {
        return lines;
    }

    public void setLines(List<String> lines) {
        this.lines = lines;
    }

    public void addLine(String line) {
        this.lines.add(line);
    }

    public Map<String, Integer> getNumbers() {
        return numbers;
    }

    public void setNumbers(Map<String, Integer> numbers) {
        this.numbers = numbers;
    }

    private void initialize(boolean isPart2) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < 10; i++) {
            map.put(String.valueOf(i), i);
        }
        if (isPart2) {
            map.put("zero", 0);
            map.put("one", 1);
            map.put("two", 2);
            map.put("three", 3);
            map.put("four", 4);
            map.put("five", 5);
            map.put("six", 6);
            map.put("seven", 7);
            map.put("eight", 8);
            map.put("nine", 9);
        }
        setNumbers(map);
    }
}
