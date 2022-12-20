import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Bin_Packing_Problem {
    private int best;

    private void place(int[] bins, int used, int[] items, int index, int capacity) {
        if(used >= best) return;
        if(index < 0) {
            best = used;
            return;
        }

        Set<Integer> set = new HashSet<>();

        for(int i = 0; i < used; i++) {
            if (!set.add(bins[i])) continue;
            if(bins[i] + items[index] <= capacity) {
                bins[i] += items[index];
                place(bins, used, items, index - 1, capacity);
                bins[i] -= items[index];
            }
        }
        bins[used] = items[index];
        place(bins, used + 1, items, index - 1, capacity);
        bins[used] = 0;
    }

    public int minSessions(int[] tasks, int sessionTime) {
        Arrays.sort(tasks);
        best = tasks.length;
        place(new int[tasks.length], 0, tasks, tasks.length - 1, sessionTime);
        return best;
    }
}
