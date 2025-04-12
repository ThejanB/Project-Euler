// 100%

import java.util.*;

public class Main {
    private static Map<String, Set<Double>> memo = new HashMap<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        List<Integer> digits = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            digits.add(scanner.nextInt());
        }
        scanner.close();

        Set<Double> allValues = computePossibleValues(digits);
        Set<Integer> possibleIntegers = new HashSet<>();

        for (double val : allValues) {
            if (val > 0 && Math.abs(val - Math.round(val)) < 1e-9) {
                possibleIntegers.add((int) Math.round(val));
            }
        }

        int maxN = 0;
        if (possibleIntegers.contains(1)) {
            int current = 1;
            while (possibleIntegers.contains(current)) {
                maxN = current;
                current++;
            }
        }

        System.out.println(maxN);
    }

    private static Set<Double> computePossibleValues(List<Integer> digits) {
        Collections.sort(digits);
        String key = digits.toString();
        if (memo.containsKey(key)) {
            return new HashSet<>(memo.get(key));
        }

        Set<Double> results = new HashSet<>();
        if (digits.size() == 1) {
            double value = digits.get(0);
            results.add(value);
            memo.put(key, new HashSet<>(results));
            return results;
        }

        int n = digits.size();
        for (int mask = 1; mask < (1 << n) - 1; mask++) {
            List<Integer> left = new ArrayList<>();
            List<Integer> right = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    left.add(digits.get(i));
                } else {
                    right.add(digits.get(i));
                }
            }

            Set<Double> leftValues = computePossibleValues(left);
            Set<Double> rightValues = computePossibleValues(right);

            for (double l : leftValues) {
                for (double r : rightValues) {
                    results.add(l + r);
                    results.add(l - r);
                    results.add(r - l);
                    results.add(l * r);
                    if (r != 0) {
                        results.add(l / r);
                    }
                    if (l != 0) {
                        results.add(r / l);
                    }
                }
            }
        }

        memo.put(key, new HashSet<>(results));
        return results;
    }
}