import java.math.BigInteger;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int limit = sc.nextInt();

        ArrayList<BigInteger> e = new ArrayList<>();
        e.add(BigInteger.TWO);
        for (int i = 1; e.size() < limit; i++) {
            e.add(BigInteger.ONE);
            e.add(BigInteger.valueOf(2L * i));
            e.add(BigInteger.ONE);
        }

        List<BigInteger> eList = e.subList(0, limit);
        Collections.reverse(eList);

        BigInteger numerator = BigInteger.ONE;
        BigInteger denominator = eList.get(0);

        for (int i = 1; i < eList.size(); i++) {
            BigInteger temp = numerator;
            numerator = denominator;
            denominator = eList.get(i).multiply(denominator).add(temp);
        }

        BigInteger finalNumerator = denominator;
        BigInteger finalDenominator = numerator;

        int digitSum = 0;
        for (char c : finalNumerator.toString().toCharArray()) {
            digitSum += c - '0';
        }

        System.out.println(digitSum);
    }
}
