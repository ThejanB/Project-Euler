import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int a0 = 0; a0 < t; a0++) {
            int limit = scanner.nextInt();
            int maxProduct = 0;
            int maxX = 0;
            int maxY = 0;

            for (int x = 990; x >= 100; x -= 11) {  // x is divisible by 11
                for (int y = 999; y >= 100; y--) {
                    int product = x * y;
                    if (product < maxProduct && product < limit) {
                        break;  // No need to check smaller y's
                    }
                    if (isPalindrome(product) && product < limit) {
                        if (product > maxProduct) {
                            maxProduct = product;
                            maxX = x;
                            maxY = y;
                        }
                        break;  // Found the largest palindrome for this x
                    }
                }
            }
            System.out.println(maxProduct);
        }
        scanner.close();
    }

    private static boolean isPalindrome(int num) {
        String s = Integer.toString(num);
        return s.equals(new StringBuilder(s).reverse().toString());
    }
}