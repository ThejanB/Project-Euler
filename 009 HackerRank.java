import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Scanner;

public class Main {
    public static long findPythagoreanTriplet(int n) {
        long maxProduct = -1;
        
        // First implementation (brute force) - 100% in HackerRank
        for (int a = 1; a <= n / 3; a++) {
            for (int b = a + 1; b <= n / 2; b++) {
                int c = n - a - b;
                if (a * a + b * b == c * c) {
                    maxProduct = Math.max(maxProduct, (long)a * b * c);
                }
            }
        }
        
        // Second implementation (optimized)
        /*
        for (int a = 1; a < n / 3; a++) {
            int numerator = n * (n - 2 * a);
            int denominator = 2 * (n - a);
            if (denominator == 0) continue;
            int b = numerator / denominator;
            int c = n - a - b;
            
            if (c <= b) break;
            if (a * a + b * b == c * c) {
                maxProduct = Math.max(maxProduct, (long)a * b * c);
            }
        }
        */
        
        return maxProduct;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            System.out.println(findPythagoreanTriplet(n));
        }
        scanner.close();
    }
}