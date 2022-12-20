import java.util.Arrays;

public class LeetCode393_UTF8_Validation {

    public static void main(String[] args) {
        LeetCode393_UTF8_Validation solution = new LeetCode393_UTF8_Validation();
        System.out.println(solution.validUtf8(new int[]{197}));
    }

    private boolean validUtf8(int[] data) {
        int bytes = 0;
        for (int seq : data) {
            String oct = String.format("%08d", Integer.parseInt(Integer.toBinaryString(seq)));
            if (bytes != 0) {
                if (oct.startsWith("10")) {
                    bytes--;
                } else {
                    return false;
                }
            } else {
                if (oct.startsWith("11110")) {
                    bytes += 3;
                } else if (oct.startsWith("1110")) {
                    bytes += 2;
                } else if (oct.startsWith("110")) {
                    bytes += 1;
                } else if (oct.startsWith("0")){
                    continue;
                } else {
                    return false;
                }
            }
        }
        return bytes == 0;
    }

}
