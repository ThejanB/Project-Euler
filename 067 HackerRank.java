// 100%

import java.io.*;
import java.util.*;

public class Main {
    public static int helper(int rows, int[][] triangle) {
        for (int row = rows - 2; row >= 0; row--) {
            for (int col = 0; col < triangle[row].length; col++) {
                triangle[row][col] += Math.max(triangle[row + 1][col], triangle[row + 1][col + 1]);
            }
        }
        return triangle[0][0];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testCases = scanner.nextInt();
        
        for (int i = 0; i < testCases; i++) {
            int rows = scanner.nextInt();
            int[][] triangle = new int[rows][];
            
            for (int j = 0; j < rows; j++) {
                String[] rowInput = scanner.nextLine().split(" ");
                while (rowInput.length == 0 || rowInput[0].isEmpty()) {
                    rowInput = scanner.nextLine().split(" ");
                }
                int[] row = new int[rowInput.length];
                for (int k = 0; k < rowInput.length; k++) {
                    row[k] = Integer.parseInt(rowInput[k]);
                }
                triangle[j] = row;
            }
            
            int result = helper(rows, triangle);
            System.out.println(result);
        }
        scanner.close();
    }
}