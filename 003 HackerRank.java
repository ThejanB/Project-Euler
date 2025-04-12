import java.util.Scanner;

public class Main {
    // Function to check if a number is prime (i > 2 and odd)
    private static boolean isPrime(long i) {
        for (long j = 3; j * j <= i; j += 2) {
            if (i % j == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int a0 = 0; a0 < t; a0++) {
            long x = scanner.nextLong();
            long maxPrime = 0;

            // Handle even factors
            while (x % 2 == 0) {
                maxPrime = 2;
                x /= 2;
            }

            // Handle odd factors
            while (true) {
                boolean foundFactor = false;
                for (long i = 1; i * i <= x; i += 2) {
                    if (x % i == 0) {
                        if (i > maxPrime && isPrime(i)) {
                            maxPrime = i;
                        }
                        long counterpart = x / i;
                        if (counterpart > maxPrime && isPrime(counterpart)) {
                            maxPrime = counterpart;
                        }
                        if (i != 1) {
                            x /= i;
                            foundFactor = true;
                            break;
                        }
                    }
                }
                if (!foundFactor) {
                    break;
                }
            }

            // If remaining x is a prime greater than maxPrime
            if (x > maxPrime && isPrime(x)) {
                maxPrime = x;
            }

            System.out.println(maxPrime);
        }
        scanner.close();
    }
}