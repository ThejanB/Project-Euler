import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int a0 = 0; a0 < t; a0++) {
            long n = scanner.nextLong();
            
            long sq1 = (n * (n + 1) / 2) * (n * (n + 1) / 2);
            
            long sq2 = n * (n + 1) * (2 * n + 1) / 6;
            
            System.out.println(sq1 - sq2);
        }
        scanner.close();
    }
}