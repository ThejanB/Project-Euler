// 100% 

import java.io.*;
import java.util.*;

public class Main {
    
    private static final double EPSILON = 0.00001;
    
    private static Set<Double> evaluate(List<Double> numbers) {
        Set<Double> results = new HashSet<>();
        if (numbers.size() == 1) {
            results.add(numbers.get(0));
            return results;
        }
        
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double a = numbers.get(i);
                double b = numbers.get(j);
                
                List<Double> remaining = new ArrayList<>(numbers);
                remaining.remove(j); // remove b first (higher index)
                remaining.remove(i); // then remove a
                
                for (double val : evaluateOperation(a, b)) {
                    remaining.add(val);
                    results.addAll(evaluate(remaining));
                    remaining.remove(remaining.size() - 1);
                }
            }
        }
        return results;
    }
    
    private static List<Double> evaluateOperation(double a, double b) {
        List<Double> operations = new ArrayList<>();
        operations.add(a + b);
        operations.add(a - b);
        operations.add(b - a);
        operations.add(a * b);
        if (Math.abs(b) > EPSILON) operations.add(a / b);
        if (Math.abs(a) > EPSILON) operations.add(b / a);
        return operations;
    }
    
    private static int getSequenceLength(List<Double> numbers) {
        Set<Double> allResults = evaluate(numbers);
        boolean[] used = new boolean[1000];
        
        for (double result : allResults) {
            double rounded = result + EPSILON;
            int index = (int) rounded;
            if (index >= 0 && index < used.length && Math.abs(rounded - index) <= 10 * EPSILON) {
                used[index] = true;
            }
        }
        
        int maxLength = 0;
        while (maxLength + 1 < used.length && used[maxLength + 1]) {
            maxLength++;
        }
        return maxLength;
    }
    
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int N = sc.nextInt();
            List<Double> numbers = new ArrayList<>();
            while (N-- > 0) {
                numbers.add(sc.nextDouble());
            }
            System.out.println(getSequenceLength(numbers));
        }
    }
}
