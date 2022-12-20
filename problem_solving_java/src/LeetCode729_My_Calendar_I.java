import java.util.TreeMap;

public class LeetCode729_My_Calendar_I {

    public static void main(String[] args) {
        LeetCode729_My_Calendar_I solution = new LeetCode729_My_Calendar_I();
        MyCalendar obj = solution.new MyCalendar();
        boolean param_1 = obj.book(1,100);
        boolean param_2 = obj.book(120,130);
        boolean param_3 = obj.book(10,30);
    }

    private class MyCalendar {

        private TreeMap<Integer, Integer> calendar;

        private MyCalendar() {
            calendar = new TreeMap();
        }

        private boolean book(int start, int end) {
            Integer prev = calendar.floorKey(start),
                    next = calendar.ceilingKey(start);
            if ((prev == null || calendar.get(prev) <= start) &&
                    (next == null || end <= next)) {
                calendar.put(start, end);
                return true;
            }
            return false;
        }
    }

}
