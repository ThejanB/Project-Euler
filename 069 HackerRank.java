import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Long> primorials = precomputePrimorials();
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int i = 0; i < T; i++) {
            long N = scanner.nextLong();
            int left = 0;
            int right = primorials.size() - 1;
            long best = 2; // default answer for N >=3 is at least 2
            while (left <= right) {
                int mid = (left + right) / 2;
                if (primorials.get(mid) < N) {
                    best = primorials.get(mid);
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            System.out.println(best);
        }
    }

    private static List<Long> precomputePrimorials() {
        List<Integer> primes = new ArrayList<>();
        boolean[] isPrime = new boolean[100];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i < 100; i++) {
            if (isPrime[i]) {
                primes.add(i);
                for (int j = i * i; j < 100; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        List<Long> primorials = new ArrayList<>();
        long product = 1;
        for (int p : primes) {
            if (product > Long.MAX_VALUE / p) {
                break;
            }
            product *= p;
            primorials.add(product);
        }
        return primorials;
    }
}