// java 8 - 100%
// java 15 - 83.33% - 1 case timeout

import java.util.*;
import java.io.*;

public class Main {

    static final long[] code_p = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};

    public static long rootval(long n) {
        long product = 1;
        while (n > 0) {
            int d = (int)(n % 10);
            product *= code_p[d];
            n /= 10;
        }
        return product;
    }

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        
        long N = sc.nextLong();
        int K = sc.nextInt();
        
        long orig = N;
        
        if (N == 1000 || N == 10000 || N == 100000 || N == 1000000) {
            N = N - 1;
        }
        
        int digits = Long.toString(N).length();
        int sieveLimit = (int) (Math.pow(10, digits) - 1);
        
        boolean[] isComposite = new boolean[sieveLimit];
        for (int i = 2; i < sieveLimit; i++) {
            if (!isComposite[i]) {
                for (int j = i * 2; j < sieveLimit; j += i) {
                    isComposite[j] = true;
                }
            }
        }
        
        LinkedHashMap<Long, ArrayList<Integer>> primes_d = new LinkedHashMap<>();
        
        LinkedHashMap<Integer, LinkedHashMap<Integer, ArrayList<Integer>>> k_vals = new LinkedHashMap<>();
        
        for (int j = 2; j < sieveLimit; j++) {
            if (!isComposite[j] && j >= 1487) {
                if (j < orig) {
                    k_vals.put(j, new LinkedHashMap<>());
                }
                
                long val = rootval(j);
                
                if (!primes_d.containsKey(val)) {
                    ArrayList<Integer> list = new ArrayList<>();
                    list.add(j);
                    primes_d.put(val, list);
                } else {
                    ArrayList<Integer> primeList = primes_d.get(val);
                    for (int k : primeList) {
                        if (k_vals.containsKey(k)) {
                            LinkedHashMap<Integer, ArrayList<Integer>> diffMap = k_vals.get(k);
                            for (int d : new ArrayList<>(diffMap.keySet())) {
                                if ((j - k) % d == 0) {
                                    diffMap.get(d).add((j - k) / d);
                                }
                            }
                            if (!diffMap.containsKey(j - k)) {
                                ArrayList<Integer> arr = new ArrayList<>();
                                arr.add(1); // The first multiplier is 1.
                                diffMap.put(j - k, arr);
                            }
                        }
                    }
                    primeList.add(j);
                }
            }
        }
        
        for (Map.Entry<Integer, LinkedHashMap<Integer, ArrayList<Integer>>> entry : k_vals.entrySet()) {
            int start = entry.getKey();
            LinkedHashMap<Integer, ArrayList<Integer>> diffMap = entry.getValue();
            if (diffMap.size() < K - 1) {
                continue;
            }
            ArrayList<Integer> diffs = new ArrayList<>(diffMap.keySet());
            Collections.sort(diffs);
            for (int d : diffs) {
                ArrayList<Integer> progression = diffMap.get(d);
                if (progression.size() >= K - 1 && progression.get(K - 2) == K - 1) {
                    StringBuilder sb = new StringBuilder();
                    for (int x = 0; x < K; x++) {
                        sb.append(start + x * d);
                    }
                    System.out.println(sb.toString());
                }
            }
        }
    }
}