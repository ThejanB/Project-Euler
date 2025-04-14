// 100% HackerRank

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BigInteger limit = scanner.nextBigInteger();
        BigInteger four = BigInteger.valueOf(4);
        BigInteger tiles = limit.divide(four);
        BigInteger sum = BigInteger.ZERO;
        BigInteger i = BigInteger.ONE;

        while (i.multiply(i).compareTo(tiles) <= 0) {
            sum = sum.add(tiles.divide(i).subtract(i));
            i = i.add(BigInteger.ONE);
        }

        System.out.println(sum);
        scanner.close();
    }
}


// -This question is about a square.
//  So we can consider only one side of the sqrare.

