// 100% in HackerRank

import java.util.Scanner;
import java.math.BigInteger;

public class Main {
    
    static final int MAX_DIGITS = 17;
    static long[] fac = new long[MAX_DIGITS];
    static long[] fac1 = new long[MAX_DIGITS];  // cumulative sum
    
    static {
        for (int i = 0; i < MAX_DIGITS; i++) {
            fac[i] = (i + 1) * 9L * pow10(i);
        }
        fac1[0] = fac[0];
        for (int i = 1; i < MAX_DIGITS; i++) {
            fac1[i] = fac[i] + fac1[i - 1];
        }
    }
    
    public static long pow10(int p) {
        long result = 1;
        for (int i = 0; i < p; i++) {
            result *= 10;
        }
        return result;
    }
    
 
    public static int findDigit(long n) {
        if (n < 9) {
            return (int) n;
        }
        
        int j = 0;
        for (; j < fac1.length; j++) {
            if (n == fac1[j]) {
                return 9;  // if exactly at the end of a block, the digit is always 9.
            }
            if (n < fac1[j]) {
                break;
            }
        }
        
        long prev = (j == 0) ? 0 : fac1[j - 1];
        long diff = n - prev;
        int digitsInBlock = j + 1;
        long quotient = diff / digitsInBlock;
        long remainder = diff % digitsInBlock;
        
        if (remainder == 0) {
            quotient = quotient - 1;
        }
        
        long number = pow10(j) + quotient;
        String numberStr = Long.toString(number);
        int index = (remainder == 0) ? j : (int) (remainder - 1);
        return numberStr.charAt(index) - '0';
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        scanner.nextLine();
        
        for (int a0 = 0; a0 < t; a0++) {
            String line = scanner.nextLine().trim();
            if (line.isEmpty()) {
                System.out.println(1);
                continue;
            }
            String[] parts = line.split("\\s+");
            
            BigInteger prod = BigInteger.ONE;
            for (String part : parts) {
                long position = Long.parseLong(part);
                int digit = findDigit(position);
                prod = prod.multiply(BigInteger.valueOf(digit));
            }
            System.out.println(prod);
        }
        scanner.close();
    }
}
