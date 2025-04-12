import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        Map<Long, Integer> nonLychrel = new HashMap<>();

        for (int i = 10; i <= N; i++) {
            long t = i;
            int j = 0;
            while (j < 60 && !isPalindrome(t)) {
                t = t + reverseNumber(t);
                j++;
            }
            if (isPalindrome(t)) {
                nonLychrel.put(t, nonLychrel.getOrDefault(t, 0) + 1);
            }
        }

        long bestPalindrome = 0;
        int maxCount = 0;
        for (Map.Entry<Long, Integer> entry : nonLychrel.entrySet()) {
            if (entry.getValue() > maxCount || 
                (entry.getValue() == maxCount && entry.getKey() < bestPalindrome)) {
                maxCount = entry.getValue();
                bestPalindrome = entry.getKey();
            }
        }

        System.out.println(bestPalindrome + " " + maxCount);
    }

    private static boolean isPalindrome(long number) {
        String s = Long.toString(number);
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    private static long reverseNumber(long number) {
        long reversed = 0;
        while (number > 0) {
            reversed = reversed * 10 + number % 10;
            number /= 10;
        }
        return reversed;
    }
}