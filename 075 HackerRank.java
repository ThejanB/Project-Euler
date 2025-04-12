// 100%

import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        final int MAX = 5_000_000;
        int[] lookup = new int[MAX + 1];
        
        for (int u = 1; u <= Math.sqrt(MAX); u += 2) {
            for (int v = 1; v < u; v += 2) {
                if (BigInteger.valueOf(u).gcd(BigInteger.valueOf(v)).intValue() == 1) {
                    int s = u*u + u*v;
                    for (int i = s; i <= MAX; i += s) {
                        lookup[i]++;
                    }
                }
            }
        }
        
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i <= MAX; i++) {
            if (lookup[i] == 1) {
                ans.add(i);
            }
        }
        
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            int left = 0, right = ans.size();
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (ans.get(mid) <= n) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            System.out.println(left);
        }
    }
}