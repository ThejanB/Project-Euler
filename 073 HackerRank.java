// 100% HackerRank

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Solution {

    private static Map<Long, List<Long>> primeFactorsCache = new HashMap<>();

    private static List<Long> getPrimeFactors(long num) {
        if (primeFactorsCache.containsKey(num)) {
            return primeFactorsCache.get(num);
        }
        List<Long> factors = new ArrayList<>();
        long tempNum = num;
        for (long i = 2; i * i <= tempNum; ++i) {
            if (tempNum % i == 0) {
                factors.add(i);
                while (tempNum % i == 0) {
                    tempNum /= i;
                }
            }
        }
        if (tempNum > 1) {
            factors.add(tempNum);
        }
        Set<Long> distinctFactors = new HashSet<>(factors);
        List<Long> result = new ArrayList<>(distinctFactors);
        result.sort(Long::compareTo);
        primeFactorsCache.put(num, result);
        return result;
    }

    private static long countCoprime(long l, long r, long num) {
        if (l > r) {
            return 0;
        }
        List<Long> primeFactors = getPrimeFactors(num);
        long count = 0;
        int m = primeFactors.size();
        for (int i = 0; i < (1 << m); ++i) {
            long product = 1;
            int setBits = 0;
            for (int j = 0; j < m; ++j) {
                if ((i >> j) % 2 == 1) {
                    product *= primeFactors.get(j);
                    setBits++;
                }
            }
            long termCount = (r / product) - ((l - 1) / product);
            if (setBits % 2 == 0) {
                count += termCount;
            } else {
                count -= termCount;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long a = scanner.nextLong();
        long dLimit = scanner.nextLong();
        long totalCount = 0;
        for (long d = 1; d <= dLimit; ++d) {
            long lowerN = d / (a + 1) + 1;
            long upperN = (long) Math.ceil((double) d / a) - 1;
            totalCount += countCoprime(lowerN, upperN, d);
        }
        System.out.println(totalCount);
        scanner.close();
    }
}