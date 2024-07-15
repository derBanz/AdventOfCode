package derbanz.day2.params;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Instructions {

    private List<String> lines = new ArrayList<>();
    private Map<String, Integer> cubes = new HashMap<>();

    public Instructions(boolean isDayTwo) {
        initialize(isDayTwo);
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

    public Map<String, Integer> getCubes() {
        return cubes;
    }

    public void setCubes(Map<String, Integer> cubes) {
        this.cubes = cubes;
    }

    private void initialize(boolean isPart2) {
        Map<String, Integer> map = new HashMap<>();
        if (isPart2) {
        } else {
            map.put("red", 12);
            map.put("green", 13);
            map.put("blue", 14);
        }
        setCubes(map);
    }
}
