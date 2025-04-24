import java.io.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws Exception {
        int m = 100;
        final int MOD = 100000;
        
        BigInteger[] pow10 = new BigInteger[m+1];
        pow10[0] = BigInteger.ONE;
        for (int i = 1; i <= m; i++) {
            pow10[i] = pow10[i-1].multiply(BigInteger.TEN);
        }

        int sumMod = 0;
        for (int k = 1; k <= 9; k++) {
            int denom = 10*k - 1;                  // 10k - 1
            BigInteger Bden = BigInteger.valueOf(denom);
            BigInteger Bk   = BigInteger.valueOf(k);
            
            for (int d = 2; d <= m; d++) {
                BigInteger tenPow   = pow10[d-1];       // 10^(d-1)
                BigInteger lowerA   = pow10[d-2];       // 10^(d-2)
                BigInteger upperA   = pow10[d-1];       // 10^(d-1)
                
                for (int b = 1; b <= 9; b++) {
                    BigInteger num = BigInteger.valueOf(b)
                                        .multiply(tenPow.subtract(Bk));
                    if (!num.mod(Bden).equals(BigInteger.ZERO)) continue;
                    BigInteger a = num.divide(Bden);
                    if (a.compareTo(lowerA) < 0 || a.compareTo(upperA) >= 0)
                        continue;
                    BigInteger n = a.multiply(BigInteger.TEN)
                                     .add(BigInteger.valueOf(b));
                    int nmod = n.mod(BigInteger.valueOf(MOD)).intValue();
                    sumMod = (sumMod + nmod) % MOD;
                }
            }
        }

        System.out.println(sumMod);
    }
}
