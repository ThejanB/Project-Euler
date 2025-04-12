import java.util.*;

public class Main {
    static int N, S;
    
    // Global list for storing solution strings.
    static List<String> solutions = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();  // e.g. 3 or 5
        S = sc.nextInt();  // the magic sum, e.g., 9 for 3-gon, 14 for 5-gon

        int totalNumbers = 2 * N;
        int requiredOuterSum = N * (4 * N + 2 - S);
        List<Set<Integer>> outerCandidates = getOuterCandidates(totalNumbers, N, requiredOuterSum);

        for (Set<Integer> candidate : outerCandidates) {
            Set<Integer> outers = new HashSet<>(candidate);
            Set<Integer> allNumbers = new HashSet<>();
            for (int i = 1; i <= totalNumbers; i++) {
                allNumbers.add(i);
            }
            Set<Integer> inners = new HashSet<>(allNumbers);
            inners.removeAll(outers);
            
            int a = Collections.min(outers);
            outers.remove(a);
            
            for (int b : new HashSet<>(inners)) {
                Set<Integer> newInners = new HashSet<>(inners);
                newInners.remove(b);
                int c = S - a - b;
                if (newInners.contains(c)) {
                    newInners.remove(c);
                    List<Integer> solOuters = new ArrayList<>();
                    solOuters.add(a);
                    List<Integer> solInners = new ArrayList<>();
                    solInners.add(b);
                    solInners.add(c);
                    complete(solOuters, solInners, new HashSet<>(outers), newInners);
                }
            }
        }
        
        Collections.sort(solutions);
        for (String sol : solutions) {
            System.out.println(sol);
        }
    }
    
    static void complete(List<Integer> solOuters, List<Integer> solInners, Set<Integer> outers, Set<Integer> inners) {
        if (inners.isEmpty() && outers.size() == 1) {
            List<Integer> solO = new ArrayList<>(solOuters);
            solO.add(outers.iterator().next());
            if (checkSolution(solO, solInners)) {
                solutions.add(formatSolution(solO, solInners));
            }
            return;
        }
        for (int newOuter : new HashSet<>(outers)) {
            List<Integer> newSolOuters = new ArrayList<>(solOuters);
            newSolOuters.add(newOuter);
            Set<Integer> newOuters = new HashSet<>(outers);
            newOuters.remove(newOuter);
            
            int lastInner = solInners.get(solInners.size() - 1);
            int newInner = S - newOuter - lastInner;
            if (inners.contains(newInner)) {
                List<Integer> newSolInners = new ArrayList<>(solInners);
                newSolInners.add(newInner);
                Set<Integer> newInners = new HashSet<>(inners);
                newInners.remove(newInner);
                
                if (newInners.isEmpty() && newOuters.size() == 1) {
                    newSolOuters.add(newOuters.iterator().next());
                    if (checkSolution(newSolOuters, newSolInners)) {
                        solutions.add(formatSolution(newSolOuters, newSolInners));
                        return;
                    }
                }
                complete(newSolOuters, newSolInners, newOuters, newInners);
            }
        }
    }
    
    static boolean checkSolution(List<Integer> outers, List<Integer> inners) {
        int n = outers.size();
        for (int i = 0; i < n; i++) {
            int sum = outers.get(i) + inners.get(i) + inners.get((i + 1) % n);
            if (sum != S) {
                return false;
            }
        }
        return true;
    }
    
    static String formatSolution(List<Integer> outers, List<Integer> inners) {
        StringBuilder sb = new StringBuilder();
        int n = outers.size();
        for (int i = 0; i < n; i++) {
            sb.append(outers.get(i));
            sb.append(inners.get(i));
            sb.append(inners.get((i + 1) % n));
        }
        return sb.toString();
    }
    
    static List<Set<Integer>> getOuterCandidates(int total, int choose, int targetSum) {
        List<Set<Integer>> res = new ArrayList<>();
        combinationHelper(1, total, choose, 0, targetSum, new ArrayList<>(), res);
        return res;
    }
    

    static void combinationHelper(int start, int total, int choose, int currentSum, int target,
                                  List<Integer> curr, List<Set<Integer>> res) {
        if (curr.size() == choose) {
            if (currentSum == target) {
                res.add(new HashSet<>(curr));
            }
            return;
        }
        for (int i = start; i <= total; i++) {
            curr.add(i);
            combinationHelper(i + 1, total, choose, currentSum + i, target, curr, res);
            curr.remove(curr.size() - 1);
        }
    }
}
