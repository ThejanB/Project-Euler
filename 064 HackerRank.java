// 100% in HackerRank

import java.util.Scanner;

public class Main {
    
    public static int perfArc(int n) {
        int root = (int) Math.sqrt(n);
        if (root * root == n) {
            return 0;
        }
        
        int a = 1;
        int den = n - root * root;
        double firstInvFrac = (Math.sqrt(n) + root) / (double) den;
        double currentInvFrac = firstInvFrac;
        int period = 0;
        
        while (true) {
            int partInt = (int) currentInvFrac;
            root = (den * partInt) / a - root;
            a = den / a;
            den = n - root * root;
            currentInvFrac = a * (Math.sqrt(n) + root) / (double) den;
            period++;
            
            if (Math.abs(currentInvFrac - firstInvFrac) < 1e-9) {
                return period;
            }
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int cntOdd = 0;
        
        for (int k = 2; k <= n; k++) {
            if (perfArc(k) % 2 == 1) {
                cntOdd++;
            }
        }
        
        System.out.println(cntOdd);
        scanner.close();
    }
}
