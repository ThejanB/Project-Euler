import java.util.*;

public class Main {

    private static final double EPSILON = 1e-10;

    public static void main(String[] args) {
        int maxSequenceLength = 0;
        String bestCombination = "";

        // Iterate through all possible combinations of four distinct digits in ascending order
        for (int a = 1; a <= 6; a++) {
            for (int b = a + 1; b <= 7; b++) {
                for (int c = b + 1; c <= 8; c++) {
                    for (int d = c + 1; d <= 9; d++) {
                        List<Double> digits = new ArrayList<>();
                        digits.add((double) a);
                        digits.add((double) b);
                        digits.add((double) c);
                        digits.add((double) d);

                        Set<Integer> results = evaluateAllExpressions(digits);
                        int sequenceLength = getConsecutiveSequenceLength(results);

                        if (sequenceLength > maxSequenceLength) {
                            maxSequenceLength = sequenceLength;
                            bestCombination = String.format("%d%d%d%d", a, b, c, d);
                        } else if (sequenceLength == maxSequenceLength) {
                            String currentCombination = String.format("%d%d%d%d", a, b, c, d);
                            if (currentCombination.compareTo(bestCombination) < 0) {
                                bestCombination = currentCombination;
                            }
                        }
                    }
                }
            }
        }

        System.out.println("Best combination: " + bestCombination);
        System.out.println("Longest consecutive sequence: 1 to " + maxSequenceLength);
    }

    private static Set<Integer> evaluateAllExpressions(List<Double> digits) {
        Set<Integer> results = new HashSet<>();
        evaluate(digits, results);
        return results;
    }

    private static void evaluate(List<Double> digits, Set<Integer> results) {
        if (digits.size() == 1) {
            double value = digits.get(0);
            if (value > EPSILON && Math.abs(value - Math.round(value)) < EPSILON) {
                results.add((int) Math.round(value));
            }
            return;
        }

        for (int i = 0; i < digits.size(); i++) {
            for (int j = 0; j < digits.size(); j++) {
                if (i == j) continue;

                double a = digits.get(i);
                double b = digits.get(j);

                List<Double> nextDigits = new ArrayList<>();
                for (int k = 0; k < digits.size(); k++) {
                    if (k != i && k != j) {
                        nextDigits.add(digits.get(k));
                    }
                }

                // Addition
                nextDigits.add(a + b);
                evaluate(nextDigits, results);
                nextDigits.remove(nextDigits.size() - 1);

                // Subtraction
                nextDigits.add(a - b);
                evaluate(nextDigits, results);
                nextDigits.remove(nextDigits.size() - 1);

                // Multiplication
                nextDigits.add(a * b);
                evaluate(nextDigits, results);
                nextDigits.remove(nextDigits.size() - 1);

                // Division
                if (Math.abs(b) > EPSILON) {
                    nextDigits.add(a / b);
                    evaluate(nextDigits, results);
                    nextDigits.remove(nextDigits.size() - 1);
                }
            }
        }
    }

    private static int getConsecutiveSequenceLength(Set<Integer> results) {
        int n = 1;
        while (results.contains(n)) {
            n++;
        }
        return n - 1;
    }
}

// Output:
//      Best combination: 1258
//      Longest consecutive sequence: 1 to 51