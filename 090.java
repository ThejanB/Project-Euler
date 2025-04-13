import java.util.*;

public class Main {
    static List<Integer> allSubsets = new ArrayList<>();  

    public static void main(String[] args) {
        int N = 9; 
        int M = 2;

        List<String> squares = buildSquares(N,M);
        if (squares == null) {
            System.out.println(0);
            return;
        }
        if (squares.isEmpty()) {
            System.out.println(0);
            return;
        }

        precomputeAll6digitSubsets();

        if (M == 1) {
            long ans = 0;
            for (int mask : allSubsets) {
                if (canFormAllSingleDigitSquares(mask,squares)) {
                    ans++;
                }
            }
            System.out.println(ans);
            return;
        }


        int[] subsetArray = new int[allSubsets.size()];
        for (int i = 0; i < allSubsets.size(); i++) {
            subsetArray[i] = allSubsets.get(i);
        }


        long count = 0;
        count = countCombinations(subsetArray,0, new int[M], 0, M, squares);

        System.out.println(count);
    }

    private static List<String> buildSquares(int N, int M) {
        int maxSquare = N*N;
        String maxStr = String.valueOf(maxSquare);
        if (maxStr.length() > M) {
            return null;
        }
        List<String> ans = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            int sq = i*i;
            String s = String.valueOf(sq);
            if (s.length() <= M) {
                s = String.format("%0"  + M + "d", sq);
                ans.add(s);
            }
        }
        return ans;
    }

    private static void precomputeAll6digitSubsets() {
        if (!allSubsets.isEmpty()) return;
        for (int mask = 0; mask < (1 << 10); mask++) {
            if (Integer.bitCount(mask) == 6) {
                allSubsets.add(mask);
            }
        }
    }

    private static boolean canFormAllSingleDigitSquares(int mask, List<String> squares) {
        for (String sq : squares) {
            int d = sq.charAt(0) - '0';
            if (!canRepresentDigit(d, mask)) {
                return  false;
            } 
        }
        return true;
    }

    private static boolean canRepresentDigit(int d, int mask) {
        if (d == 6 || d == 9) {
            return ((mask & (1 << 6)) != 0) || ((mask & (1 << 9)) != 0);
        } else {
            return ((mask & (1 << d)) != 0);
        }
    }

    private static long countCombinations(int[] subsetArray, int startIndex,
                                          int[] chosen, int depth, int M,
                                          List<String> squares) {
        long total = 0;
        if (depth == M) {
            if (canFormAllSquares(chosen, subsetArray, squares)) {
                return 1;
            } else {
                return  0;
            }
        }
        for (int i = startIndex; i < subsetArray.length; i++) {
            chosen[depth] = i;
            total += countCombinations(subsetArray, i, chosen, depth+1, M, squares);
        }
        return total;
    }

    private static boolean canFormAllSquares(int[] chosen, int[] subsetArray, List<String> squares) {
        for (String sq : squares) {
            if (!canFormThisSquare(sq, chosen, subsetArray)) {
                return false;
            }
        }
        return true;
    }

    private static boolean canFormThisSquare(String sq, int[] chosen, int[] subsetArray) {
        int M = sq.length();
        boolean[][] adj = new boolean[M][M];
        for (int i = 0; i < M; i++) {
            int d = sq.charAt(i) - '0';
            for (int j = 0; j < M; j++) {
                int mask = subsetArray[ chosen[j] ];
                if (canRepresentDigit(d, mask)) {
                    adj[i][j] = true;
                }
            }
        }
        int[] matchR = new int[M];  // matchR[j] = which digit i is matched to j, or -1 if none
        Arrays.fill(matchR, -1);
        for (int i = 0; i < M; i++) {
            boolean[] used = new boolean[M];
            if (!tryMatch(i, adj, matchR, used)) {
                return false;
            }
        }
        return true;
    }

    private static boolean tryMatch(int u, boolean[][] adj, int[] matchR, boolean[] used) {
        int M = adj[u].length;
        for (int v = 0; v < M; v++) {
            if (adj[u][v] &&  !used[v]) {
                used[v] = true;
                if (matchR[v] < 0 || tryMatch(matchR[v], adj, matchR, used)) {
                    matchR[v] = u;
                    return true;
                }
            }
        }
        return false;
    }
}
