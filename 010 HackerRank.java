// 100%

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static List<Integer> primeList(int n) {
        boolean[] candidates = new boolean[n + 1];
        for (int i = 2; i <= n; i++) {
            candidates[i] = true;
        }
        
        // Mark even numbers > 2 as non-prime
        for (int i = 4; i <= n; i += 2) {
            candidates[i] = false;
        }
        
        for (int i = 3; i * i <= n; i += 2) {
            if (candidates[i]) {
                for (int j = i * i; j <= n; j += i) {
                    candidates[j] = false;
                }
            }
        }
        
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (candidates[i]) {
                primes.add(i);
            }
        }
        return primes;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        int[] inputs = new int[t];
        int maxN = 0;
        
        for (int i = 0; i < t; i++) {
            inputs[i] = scanner.nextInt();
            if (inputs[i] > maxN) {
                maxN = inputs[i];
            }
        }
        
        List<Integer> primes = primeList(maxN);
        
        for (int i = 0; i < t; i++) {
            int n = inputs[i];
            long total = 0;
            for (int p : primes) {
                if (p > n) break;
                total += p;
            }
            System.out.println(total);
        }
        
        scanner.close();
    }
}