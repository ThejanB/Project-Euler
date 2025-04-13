// 100% HackerRank

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.*;
import java.util.PriorityQueue;
import java.util.Collections;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        
        int[][] arr = new int[N][];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = new int[i + 1];
            for (int j = 0; j < i + 1; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        int[][] partialSum = new int[N][];
        for (int i = 0; i < N; i++) {
            partialSum[i] = new int[i + 1];
            partialSum[i][0] = arr[i][0];
            for (int j = 1; j < i + 1; j++) {
                partialSum[i][j] = partialSum[i][j - 1] + arr[i][j];
            }
        }
        
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int r = 0; r < N; r++) {
            for (int c = 0; c <= r; c++) {
                int currentSum = 0;
                int maxSize = N - r;
                for (int s = 1; s <= maxSize; s++) {
                    int rowIndex = r + s - 1;
                    int colStart = c;
                    int colEnd = c + s - 1;
                    
                    int rowSegment = partialSum[rowIndex][colEnd];
                    if (colStart > 0) {
                        rowSegment -= partialSum[rowIndex][colStart - 1];
                    }
                    
                    currentSum += rowSegment;
                    
                    if (heap.size() < K) {
                        heap.offer(currentSum);
                    } else if (currentSum < heap.peek()) {
                        heap.poll();
                        heap.offer(currentSum);
                    }
                }
            }
        }
        
        ArrayList<Integer> result = new ArrayList<>();
        while (!heap.isEmpty()) {
            result.add(heap.poll());
        }
        Collections.sort(result);
        
        for (int sum : result) {
            System.out.println(sum);
        }
    }
}
