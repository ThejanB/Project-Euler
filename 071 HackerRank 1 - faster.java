// 100%
// directly used modInverse in BigInteger - Ez

import java.util.Scanner;
import java.math.BigInteger;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            BigInteger a = sc.nextBigInteger();
            BigInteger b = sc.nextBigInteger();
            BigInteger n = sc.nextBigInteger();
            BigInteger invA = a.modInverse(b);
            BigInteger r = n.mod(b);
            BigInteger d = r.subtract(invA);
            if (d.compareTo(BigInteger.ZERO) < 0)
                d = d.add(b);
            BigInteger den = n.subtract(d);
            BigInteger num = (den.multiply(a).subtract(BigInteger.ONE)).divide(b);
            System.out.println(num + " " + den);
        }
    }
}
