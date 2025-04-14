// 100% HackerRank

import java.io.*;
import java.util.*;

public class Main {
    static final int MOD = (int)1e9 + 7;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        List<Integer> inputs = new ArrayList<>();
        int maxN = 0;
        
        for (int i = 0; i < t; i++) {
            int N = sc.nextInt();
            inputs.add(N);
            if (N > maxN) {
                maxN = N;
            }
        }
        
        int[] ans = numberOfWays(maxN);
        
        for (int N : inputs) {
            System.out.println(ans[N]);
        }
    }
    
    public static int[] numberOfWays(int N) {
        int[] dp = new int[N + 1];
        dp[0] = 1;
        
        for (int row = 1; row <= N; row++) {
            for (int col = row; col <= N; col++) {
                dp[col] = (dp[col] + dp[col - row]) % MOD;
            }
        }
        
        return dp;
    }
}