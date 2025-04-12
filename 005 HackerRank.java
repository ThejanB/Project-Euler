import java.util.Scanner;

public class Main {
    private static long findLCM(long x, long y) {
        if (x > y) {
            long temp = x;
            x = y;
            y = temp;
        }
        
        for (long i = y; i <= x * y; i += y) {
            if (i % x == 0) {
                return i;
            }
        }
        return x * y;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int a0 = 0; a0 < t; a0++) {
            int n = scanner.nextInt();
            
            long lcm = 1;
            for (int num = 2; num <= n; num++) {
                lcm = findLCM(lcm, num);
            }
            System.out.println(lcm);
        }
        scanner.close();
    }
}