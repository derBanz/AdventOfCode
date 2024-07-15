package derbanz.day1.params;

import java.util.ArrayList;
import java.util.List;

public class Instructions {

    private List<String> lines = new ArrayList<>();

    public List<String> getLines() {
        return lines;
    }

    public void setLines(List<String> lines) {
        this.lines = lines;
    }

    public void addLine(String line) {
        this.lines.add(line);
    }
}
