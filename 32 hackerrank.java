import java.util.*;

public class PandigitalProducts {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();  // Read the number N (number of digits in pandigital)
        System.out.println(findPandigitalProductSum(N));
    }

    static int findPandigitalProductSum(int N) {
        String digits = "";
        for (int i = 1; i <= N; i++) {
            digits += i;
        }

        Set<Integer> products = new HashSet<>();

        // Generate all permutations of digits
        permute(digits.toCharArray(), 0, products, N);

        int sum = 0;
        for (int p : products) {
            sum += p;
        }
        return sum;
    }

    // Backtracking permutation generator
    static void permute(char[] arr, int l, Set<Integer> products, int N) {
        if (l == arr.length) {
            checkCombination(new String(arr), products);
            return;
        }
        for (int i = l; i < arr.length; i++) {
            swap(arr, i, l);
            permute(arr, l + 1, products, N);
            swap(arr, i, l);
        }
    }

    static void checkCombination(String s, Set<Integer> products) {
        int len = s.length();

        // Try every possible split (i for multiplicand, j for multiplier)
        for (int i = 1; i <= len - 2; i++) {
            for (int j = i + 1; j <= len - 1; j++) {
                int a = Integer.parseInt(s.substring(0, i));
                int b = Integer.parseInt(s.substring(i, j));
                int c = Integer.parseInt(s.substring(j));

                if (a * b == c) {
                    products.add(c);  // Add product only once
                }
            }
        }
    }

    static void swap(char[] arr, int i, int j) {
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
