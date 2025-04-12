// 52.7%
// 63 cases passed, others timelimit exceeded


import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        StringBuilder patternBuilder = new StringBuilder();
        for (int i = 0; i < n; i++) {
            patternBuilder.append(sc.next());
        }
        String pattern = patternBuilder.toString();
        int L = 2 * n - 1;
        
        BigInteger result = solve(pattern, n, L);
        System.out.println(result);
    }
    
    private static BigInteger solve(String pattern, int n, int L) {
        StringBuilder minSqBuilder = new StringBuilder();
        StringBuilder maxSqBuilder = new StringBuilder();
        
        for (int i = 0; i < n; i++) {
            minSqBuilder.append(pattern.charAt(i));
            if (i < n - 1) {
                minSqBuilder.append('0');
            }
            
            maxSqBuilder.append(pattern.charAt(i));
            if (i < n - 1) {
                maxSqBuilder.append('9');
            }
        }
        
        BigInteger minSquare = new BigInteger(minSqBuilder.toString());
        BigInteger maxSquare = new BigInteger(maxSqBuilder.toString());
        
        BigInteger lowerBound = sqrtCeil(minSquare);
        BigInteger upperBound = sqrtFloor(maxSquare);
        
        int d = Math.min(n, (n >= 8) ? 4 : 3);
        if (n <= 2) d = 1;
        
        int m = 2 * d - 1;
        int modInt = (int) Math.pow(10, m);
        BigInteger modulus = BigInteger.valueOf(modInt);
        
        ArrayList<Integer> validResidues = new ArrayList<>();
        for (int r = 0; r < modInt; r++) {
            long square = (long) r * r;
            boolean isValid = true;
            
            for (int j = n - d; j < n; j++) {
                if (j < 0) continue;
                
                int position = 2 * (n - 1 - j);
                int digit = (int) ((square / (long) Math.pow(10, position)) % 10);
                int expected = pattern.charAt(j) - '0';
                
                if (digit != expected) {
                    isValid = false;
                    break;
                }
            }
            
            if (isValid) {
                validResidues.add(r);
            }
        }
        
        for (int residue : validResidues) {
            BigInteger rBig = BigInteger.valueOf(residue);
            BigInteger remainder = lowerBound.mod(modulus);
            
            BigInteger candidate;
            if (remainder.compareTo(rBig) <= 0) {
                candidate = lowerBound.subtract(remainder).add(rBig);
            } else {
                candidate = lowerBound.subtract(remainder).add(modulus).add(rBig);
            }
            
            while (candidate.compareTo(upperBound) <= 0) {
                BigInteger square = candidate.multiply(candidate);
                
                if (matches(square, pattern, L)) {
                    return candidate;
                }
                
                candidate = candidate.add(modulus);
            }
        }
        
        return BigInteger.ZERO; // Shouldn't reach here if problem has guaranteed solution
    }
    
    private static boolean matches(BigInteger square, String pattern, int expectedLength) {
        String squareStr = square.toString();
        
        if (squareStr.length() < expectedLength) {
            StringBuilder padded = new StringBuilder();
            for (int i = 0; i < expectedLength - squareStr.length(); i++) {
                padded.append('0');
            }
            padded.append(squareStr);
            squareStr = padded.toString();
        }
        
        if (squareStr.length() != expectedLength) {
            return false;
        }
        
        StringBuilder extracted = new StringBuilder();
        for (int i = 0; i < squareStr.length(); i += 2) {
            extracted.append(squareStr.charAt(i));
        }
        
        return extracted.toString().equals(pattern);
    }
    
    private static BigInteger sqrtCeil(BigInteger x) {
        BigInteger floor = sqrtFloor(x);
        return floor.multiply(floor).equals(x) ? floor : floor.add(BigInteger.ONE);
    }
    
    private static BigInteger sqrtFloor(BigInteger x) {
        if (x.compareTo(BigInteger.ZERO) < 0) {
            throw new ArithmeticException("Negative argument");
        }
        if (x.equals(BigInteger.ZERO) || x.equals(BigInteger.ONE)) {
            return x;
        }
        
        BigInteger two = BigInteger.valueOf(2);
        BigInteger y = x.shiftRight(x.bitLength() / 2);
        
        while (true) {
            BigInteger z = y.add(x.divide(y)).divide(two);
            if (z.equals(y) || z.equals(y.subtract(BigInteger.ONE))) {
                while (z.multiply(z).compareTo(x) > 0) {
                    z = z.subtract(BigInteger.ONE);
                }
                return z;
            }
            y = z;
        }
    }
}
