// 33% HackerRank

import java.util.*;

public class Main {
    public static boolean isReversible(long n) {
        String s = Long.toString(n);
        if (s.charAt(s.length() - 1) == '0') {
            return false;
        }
        long reversedN = Long.parseLong(new StringBuilder(s).reverse().toString());
        long total = n + reversedN;
        String totalStr = Long.toString(total);
        for (int i = 0; i < totalStr.length(); i++) {
            if ((totalStr.charAt(i) - '0') % 2 == 0) {
                return false;
            }
        }
        return true;
    }

    public static List<Long> precomputeReversibleNumbers(long limit) {
        List<Long> reversibleNumbers = new ArrayList<>();
        for (long n = 1; n < limit; n++) {
            if (isReversible(n)) {
                reversibleNumbers.add(n);
            }
        }
        return reversibleNumbers;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        long[] queries = new long[T];
        long maxQuery = 0;
        for (int i = 0; i < T; i++) {
            queries[i] = scanner.nextLong();
            if (queries[i] > maxQuery) {
                maxQuery = queries[i];
            }
        }
        List<Long> reversibleNumbers = precomputeReversibleNumbers(maxQuery + 1);
        Collections.sort(reversibleNumbers);
        for (long N : queries) {
            int left = 0;
            int right = reversibleNumbers.size();
            while (left < right) {
                int mid = (left + right) / 2;
                if (reversibleNumbers.get(mid) < N) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            System.out.println(left);
        }
    }
}