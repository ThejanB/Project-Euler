// 31.5%
// 46 cases passed, others timelimit exceeded
//
// converted to Haskell and got 33.9% 
// 49 cases passed, others timelimit exceeded

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static BigInteger sqrtFloor(BigInteger x) {
        if (x.compareTo(BigInteger.ZERO) < 0)
            throw new ArithmeticException("Negative argument");
        if (x.equals(BigInteger.ZERO) || x.equals(BigInteger.ONE))
            return x;
        BigInteger two = BigInteger.valueOf(2);
        BigInteger y = x.shiftRight(x.bitLength() / 2);
        while (true) {
            BigInteger z = y.add(x.divide(y)).divide(two);
            if (z.equals(y) || z.equals(y.subtract(BigInteger.ONE))) {
                while (z.multiply(z).compareTo(x) > 0)
                    z = z.subtract(BigInteger.ONE);
                return z;
            }
            y = z;
        }
    }

    static BigInteger sqrtCeil(BigInteger x) {
        BigInteger floor = sqrtFloor(x);
        return floor.multiply(floor).equals(x) ? floor : floor.add(BigInteger.ONE);
    }

    static boolean fullMatch(BigInteger S, String pat, int len) {
        String s = S.toString();
        if (s.length() < len) {
            StringBuilder pad = new StringBuilder();
            for (int i = 0; i < len - s.length(); i++) pad.append('0');
            pad.append(s);
            s = pad.toString();
        }
        if (s.length() != len)
            return false;
        StringBuilder ext = new StringBuilder();
        for (int i = 0; i < s.length(); i += 2)
            ext.append(s.charAt(i));
        return ext.toString().equals(pat);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        StringBuilder patB = new StringBuilder();
        for (int i = 0; i < n; i++)
            patB.append(sc.next());
        String pattern = patB.toString();
        int L = 2 * n - 1;

        StringBuilder minSB = new StringBuilder();
        StringBuilder maxSB = new StringBuilder();
        for (int i = 0; i < n; i++) {
            minSB.append(pattern.charAt(i));
            if (i < n - 1)
                minSB.append('0');
        }
        for (int i = 0; i < n; i++) {
            maxSB.append(pattern.charAt(i));
            if (i < n - 1)
                maxSB.append('9');
        }
        BigInteger minS = new BigInteger(minSB.toString());
        BigInteger maxS = new BigInteger(maxSB.toString());
        BigInteger lowX = sqrtCeil(minS);
        BigInteger highX = sqrtFloor(maxS);

        int d = (n >= 2) ? Math.min(n, 3) : 1;
        int m = 2 * d - 1;
        int modInt = (int) Math.pow(10, m);
        BigInteger modVal = BigInteger.valueOf(modInt);

        ArrayList<Integer> validResidues = new ArrayList<>();
        for (int r = 0; r < modInt; r++) {
            long sq = (long) r * r;
            boolean valid = true;
            for (int j = n - d; j < n; j++) {
                int p = 2 * (n - 1 - j);
                int dig = (int) ((sq / (long) Math.pow(10, p)) % 10);
                int req = pattern.charAt(j) - '0';
                if (dig != req) {
                    valid = false;
                    break;
                }
            }
            if (valid)
                validResidues.add(r);
        }

        BigInteger ans = null;
        for (int residue : validResidues) {
            BigInteger rBI = BigInteger.valueOf(residue);
            BigInteger rem = lowX.mod(modVal);
            BigInteger candidate = (rem.compareTo(rBI) <= 0) ? lowX.subtract(rem).add(rBI)
                    : lowX.subtract(rem).add(modVal).add(rBI);
            for (; candidate.compareTo(highX) <= 0; candidate = candidate.add(modVal)) {
                BigInteger candidateSq = candidate.multiply(candidate);
                if (fullMatch(candidateSq, pattern, L)) {
                    ans = candidate;
                    break;
                }
            }
            if (ans != null)
                break;
        }
        System.out.println(ans == null ? "No solution found" : ans);
    }
}
