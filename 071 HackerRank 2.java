// 100%

import java.util.Scanner;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int t = 0; t < T; t++) {
            BigInteger a = scanner.nextBigInteger();
            BigInteger b = scanner.nextBigInteger();
            BigInteger N = scanner.nextBigInteger();
            
            BigInteger y0 = modInverse(a, b);
            BigInteger kMax = N.subtract(y0).divide(b);
            BigInteger yMax = y0.add(kMax.multiply(b));
            BigInteger xMax = a.multiply(yMax).subtract(BigInteger.ONE).divide(b);
            
            System.out.println(xMax + " " + yMax);
        }
        scanner.close();
    }
    
    private static BigInteger modInverse(BigInteger a, BigInteger m) {
        BigInteger[] egcd = egcd(a, m);
        if (!egcd[0].equals(BigInteger.ONE)) {
            throw new RuntimeException("Modular inverse does not exist");
        }
        BigInteger x = egcd[1];
        return x.mod(m).add(m).mod(m);
    }
    
    private static BigInteger[] egcd(BigInteger a, BigInteger b) {
        if (a.equals(BigInteger.ZERO)) {
            return new BigInteger[]{b, BigInteger.ZERO, BigInteger.ONE};
        } else {
            BigInteger[] vals = egcd(b.mod(a), a);
            BigInteger gcd = vals[0];
            BigInteger x = vals[1];
            BigInteger y = vals[2];
            BigInteger newX = y.subtract(b.divide(a).multiply(x));
            return new BigInteger[]{gcd, newX, x};
        }
    }
}