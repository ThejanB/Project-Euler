import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int a0 = 0; a0 < t; a0++) {
            int n = scanner.nextInt();
            long x = (n - 1) / 3;
            long tot = 3 * (x * (x + 1)) / 2;
            x = (n - 1) / 5;
            tot += 5 * (x * (x + 1)) / 2;
            x = (n - 1) / 15;
            tot -= 15 * (x * (x + 1)) / 2;
            
            System.out.println(tot);
        }
        scanner.close();
    }
}