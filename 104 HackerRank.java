// 100% in HackerRank

import java.math.BigInteger;
import java.util.Scanner;

public class Main {

    static class Norm {
        long M; // Mantissa (up to 18 digits)
        int E;  // Exponent (power of 10)
        Norm(long M, int E) {
            this.M = M;
            this.E = E;
        }
    }
    
    static long power10(int exp) {
        long res = 1L;
        for (int i = 0; i < exp; i++) {
            res *= 10;
        }
        return res;
    }
    
    static Norm normalize(long M, int E, int p) {
        long lower = power10(p - 1);
        long upper = power10(p);
        while (M >= upper) {
            M /= 10;
            E++;
        }
        while (M < lower) {
            M *= 10;
            E--;
        }
        return new Norm(M, E);
    }
    
    static Norm getNormalized(BigInteger X, int p) {
        String s = X.toString();
        int L = s.length();
        if (L >= p) {
            long M = Long.parseLong(s.substring(0, p));
            int E = L - p;
            return new Norm(M, E);
        } else {
            long M = Long.parseLong(s);
            M *= power10(p - L);
            int E = -(p - L);
            return new Norm(M, E);
        }
    }
    
    static Norm addNormalized(Norm A, Norm B, int p) {
        int E = Math.max(A.E, B.E);
        long shiftA = (E - A.E > 0) ? power10(E - A.E) : 1;
        long shiftB = (E - B.E > 0) ? power10(E - B.E) : 1;
        long MA = A.M;
        long MB = B.M;
        if (shiftA > 1) MA /= shiftA;
        if (shiftB > 1) MB /= shiftB;
        long sum = MA + MB;
        return normalize(sum, E, p);
    }
    
    static boolean isPandigital(long x, int d, long lower, long upper, int targetMask) {
        if (x < lower || x >= upper) return false;
        int mask = 0;
        while (x > 0) {
            int dig = (int)(x % 10);
            if (dig == 0 || dig > d) return false;
            int bit = 1 << dig;
            if ((mask & bit) != 0) return false;
            mask |= bit;
            x /= 10;
        }
        return mask == targetMask;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int d = sc.nextInt();

        long mod = power10(d);
        long lowerBound = power10(d - 1);
        long upperBound = lowerBound * 10;
        int targetMask = 0;
        for (int i = 1; i <= d; i++) {
            targetMask |= (1 << i);
        }
        
        int threshold = 200; // Increased threshold for exact computation
        int MAX_ITER = 2_000_000; // Adjusted to problem's constraint of 2e6
        
        int p = 18; // Use maximum precision for normalized form
        
        BigInteger prevBI = BigInteger.valueOf(a);
        BigInteger currBI = BigInteger.valueOf(b);
        
        long Tprev = a % mod;
        long Tcurr = b % mod;
        
        if (a >= lowerBound) {
            String s = Integer.toString(a);
            if (s.length() >= d) {
                long lead = Long.parseLong(s.substring(0, d));
                if (isPandigital(lead, d, lowerBound, upperBound, targetMask) &&
                    isPandigital(Tprev, d, lowerBound, upperBound, targetMask)) {
                    System.out.println(1);
                    return;
                }
            }
        }
        if (b >= lowerBound) {
            String s = Integer.toString(b);
            if (s.length() >= d) {
                long lead = Long.parseLong(s.substring(0, d));
                if (isPandigital(lead, d, lowerBound, upperBound, targetMask) &&
                    isPandigital(Tcurr, d, lowerBound, upperBound, targetMask)) {
                    System.out.println(2);
                    return;
                }
            }
        }
        
        BigInteger nextBI;
        int n;
        for (n = 3; n <= threshold && n <= MAX_ITER; n++) {
            nextBI = prevBI.add(currBI);
            String s = nextBI.toString();
            long Tnext = (Tprev + Tcurr) % mod;
            if (s.length() >= d) {
                long lead = Long.parseLong(s.substring(0, d));
                if (isPandigital(lead, d, lowerBound, upperBound, targetMask) &&
                    isPandigital(Tnext, d, lowerBound, upperBound, targetMask)) {
                    System.out.println(n);
                    return;
                }
            }
            prevBI = currBI;
            currBI = nextBI;
            Tprev = Tcurr;
            Tcurr = Tnext;
        }
        
        Norm leadPrev = getNormalized(prevBI, p);
        Norm leadCurr = getNormalized(currBI, p);
        
        for (; n <= MAX_ITER; n++) {
            long Tnext = (Tprev + Tcurr) % mod;
            
            Tprev = Tcurr;
            Tcurr = Tnext;
            
            Norm leadNext = addNormalized(leadCurr, leadPrev, p);
            leadPrev = leadCurr;
            leadCurr = leadNext;
            
            long firstDigits = leadCurr.M / power10(p - d);
            if (isPandigital(firstDigits, d, lowerBound, upperBound, targetMask) &&
                isPandigital(Tnext, d, lowerBound, upperBound, targetMask)) {
                System.out.println(n);
                return;
            }
        }
        
        System.out.println("no solution");
    }
}
