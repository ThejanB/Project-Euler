// 100%

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

 
    private static boolean isPermutation(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        char[] a = s.toCharArray();
        char[] b = t.toCharArray();
        Arrays.sort(a);
        Arrays.sort(b);
        return Arrays.equals(a, b);
    }

 
    private static int[] computeTotients(int limit) {
        int[] phi = new int[limit];
        for (int i = 0; i < limit; i++) {
            phi[i] = i;
        }
        for (int i = 2; i < limit; i++) {
            if (phi[i] == i) {  // i is prime
                for (int j = i; j < limit; j += i) {
                    phi[j] -= phi[j] / i;
                }
            }
        }
        return phi;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int limit = Integer.parseInt(reader.readLine().trim());

        if (limit <= 3) {
            System.out.println(limit);
            return;
        }

        int[] phi = computeTotients(limit);

        double bestRatio = Double.MAX_VALUE;
        int bestN = 0;

        for (int n = 2; n < limit; n++) {
            int totient = phi[n];
            if (isPermutation(Integer.toString(n), Integer.toString(totient))) {
                double ratio = (double) n / totient;
                if (ratio < bestRatio) {
                    bestRatio = ratio;
                    bestN = n;
                }
            }
        }

        System.out.println(bestN);
    }
}
