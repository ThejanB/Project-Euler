//  88.24% Hackerrank
//  2 cases time limit exceeded


import java.util.*;

class Solution {
    public static long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public static class Pair {
        long num;
        long den;

        public Pair(long num, long den) {
            this.num = num;
            this.den = den;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Pair other = (Pair) obj;
            return num == other.num && den == other.den;
        }

        @Override
        public int hashCode() {
            return Objects.hash(num, den);
        }

        @Override
        public String toString() {
            return "(" + num + ", " + den + ")";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        if (n == 0) {
            System.out.println(0);
        } else {
            List<Set<Pair>> dp = new ArrayList<>(n + 1);
            for (int i = 0; i <= n; i++) {
                dp.add(new HashSet<>());
            }
            dp.get(1).add(new Pair(1, 1));

            for (int k = 2; k <= n; k++) {
                for (int i = 1; i <= k / 2; i++) {
                    int j = k - i;
                    for (Pair a : dp.get(i)) {
                        for (Pair b : dp.get(j)) {
                            long sum_num = a.num * b.den + b.num * a.den;
                            long sum_den = a.den * b.den;
                            long gcd_val_sum = gcd(sum_num, sum_den);
                            dp.get(k).add(new Pair(sum_num / gcd_val_sum, sum_den / gcd_val_sum));

                            long series_num = a.num * b.num;
                            long series_den = a.num * b.den + b.num * a.den;
                            if (series_den != 0) {
                                long gcd_val_series = gcd(series_num, series_den);
                                dp.get(k).add(new Pair(series_num / gcd_val_series, series_den / gcd_val_series));
                            }
                        }
                    }
                }
            }

            Set<Pair> total = new HashSet<>();
            for (int k = 1; k <= n; k++) {
                total.addAll(dp.get(k));
            }

            System.out.println(total.size());
        }
        scanner.close();
    }
}
