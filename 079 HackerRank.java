// 100% HackerRank

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();

        Set<Character> allChars = new HashSet<>();
        Map<Character, Set<Character>> graph = new HashMap<>();
        Map<Character, Integer> inDegree = new HashMap<>();

        for (int i = 0; i < T; i++) {
            String attempt = sc.nextLine();
            if (attempt.length() != 3) {
                System.out.println("SMTH WRONG");
                return;
            }
            char a = attempt.charAt(0);
            char b = attempt.charAt(1);
            char c = attempt.charAt(2);

            allChars.add(a);
            allChars.add(b);
            allChars.add(c);

            // Add edge a -> b
            if (!graph.containsKey(a)) {
                graph.put(a, new HashSet<>());
            }
            if (!graph.get(a).contains(b)) {
                graph.get(a).add(b);
                inDegree.put(b, inDegree.getOrDefault(b, 0) + 1);
            }

            // Add edge b -> c
            if (!graph.containsKey(b)) {
                graph.put(b, new HashSet<>());
            }
            if (!graph.get(b).contains(c)) {
                graph.get(b).add(c);
                inDegree.put(c, inDegree.getOrDefault(c, 0) + 1);
            }

            // Ensure all characters are in inDegree
            inDegree.putIfAbsent(a, 0);
            inDegree.putIfAbsent(b, 0);
            inDegree.putIfAbsent(c, 0);
        }

        // Prepare for topological sort using a min-heap for lex order
        PriorityQueue<Character> queue = new PriorityQueue<>();
        for (char ch : allChars) {
            if ((inDegree.getOrDefault(ch, 0) == 0) && graph.containsKey(ch)) {
                queue.offer(ch);
            }
        }

        StringBuilder passcode = new StringBuilder();
        while (!queue.isEmpty()) {
            if (queue.size() > 1) {
                // Multiple choices, pick lex smallest
            }
            char u = queue.poll();
            passcode.append(u);

            if (graph.containsKey(u)) {
                for (char v : graph.get(u)) {
                    inDegree.put(v, inDegree.get(v) - 1);
                    if (inDegree.get(v) == 0) {
                        queue.offer(v);
                    }
                }
            }
        }

        if (passcode.length() != allChars.size()) {
            System.out.println("SMTH WRONG");
        } else {
            System.out.println(passcode.toString());
        }
    }
}