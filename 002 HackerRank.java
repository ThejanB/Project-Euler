import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int a0 = 0; a0 < t; a0++) {
            long n = scanner.nextLong();   
            long x = 1;
            long y = 2;
            long tot = 0;
            
            while (y < n) {
                if (y % 2 == 0) {
                    tot += y;
                }
                long next = x + y;
                x = y;
                y = next;
            }
            
            System.out.println(tot);
        }
        scanner.close();
    }
}