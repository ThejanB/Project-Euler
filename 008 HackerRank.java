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
        scanner.nextLine(); 
        
        for (int a0 = 0; a0 < t; a0++) {
            String[] nk = scanner.nextLine().split(" ");
            int n = Integer.parseInt(nk[0]);
            int k = Integer.parseInt(nk[1]);
            
            String no = scanner.nextLine();
            long maxProduct = 0;
            
            for (int x = 0; x <= n - k; x++) {
                long product = 1;
                for (int y = x; y < x + k; y++) {
                    product *= Character.getNumericValue(no.charAt(y));
                }
                maxProduct = Math.max(maxProduct, product);
            }
            
            System.out.println(maxProduct);
        }
        scanner.close();
    }
}