import java.util.*;

public class PentagonalPairs {
    // Method to compute the nth pentagonal number
    static long pentagonal(int n) {
        return (long)n * (3 * n - 1) / 2;
    }

    // Method to check if a number is pentagonal using the inverse formula
    static boolean isPentagonal(long x) {
        long d = 1 + 24 * x;
        long sqrt = (long)Math.sqrt(d);
        if (sqrt * sqrt != d) return false;
        return (1 + sqrt) % 6 == 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();  // Upper bound
        int K = sc.nextInt();  // Difference

        List<Long> result = new ArrayList<>();

        for (int n = K + 1; n < N; n++) {
            long Pn = pentagonal(n);
            long PnK = pentagonal(n - K);

            // Check both sum and difference conditions
            if (isPentagonal(Pn + PnK) || isPentagonal(Pn - PnK)) {
                result.add(Pn);
            }
        }

        // Sort result and print each on a new line
        Collections.sort(result);
        for (long val : result) {
            System.out.println(val);
        }
    }
}
