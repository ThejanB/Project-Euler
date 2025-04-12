// 100% in HackerRank

import java.util.*;

public class MonopolySimulation {
    // Constants for the board
    private static final int BOARD_SIZE = 40;
    private static final int GO_TO_JAIL = 30; // G2J position (30th square, index position)
    private static final int JAIL = 10;
    private static final int GO = 0;
    
    // Community Chest and Chance card positions
    private static final int[] CC_POSITIONS = {2, 17, 33}; // CC1, CC2, CC3
    private static final int[] CH_POSITIONS = {7, 22, 36}; // CH1, CH2, CH3
    
    // Railway company positions
    private static final int[] RAILWAY_POSITIONS = {5, 15, 25, 35}; // R1, R2, R3, R4
    
    // Utility company positions
    private static final int[] UTILITY_POSITIONS = {12, 28}; // U1, U2
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt(); // Number of sides on each die
        int K = scanner.nextInt(); // Number of most popular squares to find
        scanner.close();
        
        // Calculate long-term probabilities of landing on each square
        double[] squareProbabilities = calculateLongTermProbabilities(N);
        
        // Find K most popular squares
        List<String> topSquares = findTopKSquares(squareProbabilities, K);
        
        // Print the results
        for (int i = 0; i < topSquares.size(); i++) {
            System.out.print(topSquares.get(i));
            if (i < topSquares.size() - 1) {
                System.out.print(" ");
            }
        }
        System.out.println();
    }
    
    private static double[] calculateLongTermProbabilities(int diceSides) {
        // Create transition matrix
        double[][] transitionMatrix = new double[BOARD_SIZE][BOARD_SIZE];
        
        // Calculate dice roll probabilities for N-sided dice
        double[][] diceProbs = new double[BOARD_SIZE][BOARD_SIZE];
        
        // Calculate basic dice roll probabilities (without special rules)
        for (int from = 0; from < BOARD_SIZE; from++) {
            for (int d1 = 1; d1 <= diceSides; d1++) {
                for (int d2 = 1; d2 <= diceSides; d2++) {
                    int steps = d1 + d2;
                    int to = (from + steps) % BOARD_SIZE;
                    diceProbs[from][to] += 1.0 / (diceSides * diceSides);
                }
            }
        }
        
        // Apply special rules
        for (int from = 0; from < BOARD_SIZE; from++) {
            for (int to = 0; to < BOARD_SIZE; to++) {
                // If there's a probability to move from 'from' to 'to'
                if (diceProbs[from][to] > 0) {
                    if (to == GO_TO_JAIL) {
                        // G2J: Go directly to jail
                        transitionMatrix[from][JAIL] += diceProbs[from][to];
                    } 
                    else if (isCC(to)) {
                        // Community Chest: 2/16 cards cause movement
                        // 1/16 to GO
                        transitionMatrix[from][GO] += diceProbs[from][to] * (1.0/16);
                        // 1/16 to JAIL
                        transitionMatrix[from][JAIL] += diceProbs[from][to] * (1.0/16);
                        // 14/16 stay where you are
                        transitionMatrix[from][to] += diceProbs[from][to] * (14.0/16);
                    } 
                    else if (isCH(to)) {
                        // Chance: 10/16 cards cause movement
                        // 1. Advance to GO
                        transitionMatrix[from][GO] += diceProbs[from][to] * (1.0/16);
                        // 2. Go to JAIL
                        transitionMatrix[from][JAIL] += diceProbs[from][to] * (1.0/16);
                        // 3. Go to C1 (11)
                        transitionMatrix[from][11] += diceProbs[from][to] * (1.0/16);
                        // 4. Go to E3 (24)
                        transitionMatrix[from][24] += diceProbs[from][to] * (1.0/16);
                        // 5. Go to H2 (39)
                        transitionMatrix[from][39] += diceProbs[from][to] * (1.0/16);
                        // 6. Go to R1 (5)
                        transitionMatrix[from][5] += diceProbs[from][to] * (1.0/16);
                        // 7. Go to next R (railway)
                        transitionMatrix[from][getNextRailway(to)] += diceProbs[from][to] * (1.0/16);
                        // 8. Go to next R (railway) - same as above
                        transitionMatrix[from][getNextRailway(to)] += diceProbs[from][to] * (1.0/16);
                        // 9. Go to next U (utility)
                        transitionMatrix[from][getNextUtility(to)] += diceProbs[from][to] * (1.0/16);
                        // 10. Go back 3 squares
                        int backThree = (to - 3 + BOARD_SIZE) % BOARD_SIZE;
                        
                        // Special processing for "go back 3 squares"
                        if (backThree == GO_TO_JAIL) {
                            // If going back 3 lands on G2J, go to JAIL
                            transitionMatrix[from][JAIL] += diceProbs[from][to] * (1.0/16);
                        } else if (isCC(backThree)) {
                            // If going back 3 lands on a CC, apply CC rules
                            transitionMatrix[from][GO] += diceProbs[from][to] * (1.0/16) * (1.0/16);
                            transitionMatrix[from][JAIL] += diceProbs[from][to] * (1.0/16) * (1.0/16);
                            transitionMatrix[from][backThree] += diceProbs[from][to] * (1.0/16) * (14.0/16);
                        } else {
                            // Normal "go back 3"
                            transitionMatrix[from][backThree] += diceProbs[from][to] * (1.0/16);
                        }
                        
                        // Remaining 6/16 cards: stay on the CH square
                        transitionMatrix[from][to] += diceProbs[from][to] * (6.0/16);
                    } 
                    else {
                        // Normal movement - no special rules
                        transitionMatrix[from][to] += diceProbs[from][to];
                    }
                }
            }
        }
        
        // Calculate steady state using power iteration
        double[] steadyState = new double[BOARD_SIZE];
        steadyState[0] = 1.0; // Start at GO
        
        double[] newState = new double[BOARD_SIZE];
        for (int iter = 0; iter < 1000; iter++) {
            Arrays.fill(newState, 0.0);
            
            // Apply transition matrix
            for (int i = 0; i < BOARD_SIZE; i++) {
                for (int j = 0; j < BOARD_SIZE; j++) {
                    newState[j] += steadyState[i] * transitionMatrix[i][j];
                }
            }
            
            // Check convergence
            double diff = 0.0;
            for (int i = 0; i < BOARD_SIZE; i++) {
                diff += Math.abs(newState[i] - steadyState[i]);
            }
            
            // Copy new state to steady state
            System.arraycopy(newState, 0, steadyState, 0, BOARD_SIZE);
            
            if (diff < 1e-10) break;
        }
        
        return steadyState;
    }
    
    // Check if position is a Community Chest square
    private static boolean isCC(int position) {
        for (int cc : CC_POSITIONS) {
            if (position == cc) return true;
        }
        return false;
    }
    
    // Check if position is a Chance square
    private static boolean isCH(int position) {
        for (int ch : CH_POSITIONS) {
            if (position == ch) return true;
        }
        return false;
    }
    
    // Get next railway company from current position
    private static int getNextRailway(int position) {
        for (int r : RAILWAY_POSITIONS) {
            if (r > position) return r;
        }
        // Wrap around to first railway if past last one
        return RAILWAY_POSITIONS[0];
    }
    
    // Get next utility company from current position
    private static int getNextUtility(int position) {
        for (int u : UTILITY_POSITIONS) {
            if (u > position) return u;
        }
        // Wrap around to first utility if past last one
        return UTILITY_POSITIONS[0];
    }
    
    // Find the top K squares with highest probabilities
    private static List<String> findTopKSquares(double[] probabilities, int k) {
        // Create pairs of (index, probability)
        List<Map.Entry<Integer, Double>> indexProbPairs = new ArrayList<>();
        for (int i = 0; i < probabilities.length; i++) {
            indexProbPairs.add(new AbstractMap.SimpleEntry<>(i, probabilities[i]));
        }
        
        // Sort by probability (descending)
        indexProbPairs.sort((a, b) -> Double.compare(b.getValue(), a.getValue()));
        
        // Extract top K indices and convert to square names
        List<String> result = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            result.add(getSquareName(indexProbPairs.get(i).getKey()));
        }
        
        return result;
    }
    
    // Convert position index to square name
    private static String getSquareName(int position) {
        String[] squares = {
            "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
            "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
            "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
            "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"
        };
        return squares[position];
    }
}