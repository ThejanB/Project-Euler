import java.util.*;

public class MonopolySimulation {
    // Board constants
    private static final int BOARD_SIZE = 40;
    private static final int GO = 0;
    private static final int JAIL = 10;
    private static final int GO_TO_JAIL = 30;
    
    // Special square positions
    private static final int[] CC_POSITIONS = {2, 17, 33}; // Community Chest positions
    private static final int[] CH_POSITIONS = {7, 22, 36}; // Chance positions
    private static final int[] RAILWAY_POSITIONS = {5, 15, 25, 35}; // R1, R2, R3, R4
    private static final int[] UTILITY_POSITIONS = {12, 28}; // U1, U2
    
    // Markov chain state space: 
    // (position, consecutive doubles count) -> 40 positions x 3 doubles states = 120 states
    private static final int NUM_STATES = BOARD_SIZE * 3;
    
    public static void main(String[] args) {
        // Use 4-sided dice for this problem
        int sides = 4;
        
        // Compute the steady-state probabilities
        double[] steadyState = computeSteadyState(sides);
        
        // Combine the position probabilities (summing over all doubles states)
        double[] squareProbabilities = new double[BOARD_SIZE];
        for (int pos = 0; pos < BOARD_SIZE; pos++) {
            for (int doubles = 0; doubles < 3; doubles++) {
                squareProbabilities[pos] += steadyState[getStateIndex(pos, doubles)];
            }
        }
        
        // Find the three most popular squares
        int[] topSquares = findTopThreeSquares(squareProbabilities);
        
        // Format and print the modal string
        String modalString = String.format("%02d%02d%02d", topSquares[0], topSquares[1], topSquares[2]);
        System.out.println(modalString);
    }
    
    private static double[] computeSteadyState(int diceSides) {
        // Transition matrix for the Markov chain
        double[][] transitionMatrix = buildTransitionMatrix(diceSides);
        
        // Initialize steady state with all probability at GO, 0 doubles
        double[] steadyState = new double[NUM_STATES];
        steadyState[getStateIndex(GO, 0)] = 1.0;
        
        // Power iteration to find steady state
        double[] newState = new double[NUM_STATES];
        for (int iter = 0; iter < 1000; iter++) {
            // Apply transition matrix
            for (int i = 0; i < NUM_STATES; i++) {
                newState[i] = 0.0;
                for (int j = 0; j < NUM_STATES; j++) {
                    newState[i] += steadyState[j] * transitionMatrix[j][i];
                }
            }
            
            // Check for convergence
            double maxDiff = 0.0;
            for (int i = 0; i < NUM_STATES; i++) {
                maxDiff = Math.max(maxDiff, Math.abs(newState[i] - steadyState[i]));
            }
            
            // Update steady state
            System.arraycopy(newState, 0, steadyState, 0, NUM_STATES);
            
            if (maxDiff < 1e-10) {
                break;
            }
        }
        
        return steadyState;
    }
    
    private static double[][] buildTransitionMatrix(int diceSides) {
        double[][] matrix = new double[NUM_STATES][NUM_STATES];
        
        // For each state (position, doubles count)
        for (int position = 0; position < BOARD_SIZE; position++) {
            for (int doubles = 0; doubles < 3; doubles++) {
                int fromState = getStateIndex(position, doubles);
                
                // Roll two dice
                for (int dice1 = 1; dice1 <= diceSides; dice1++) {
                    for (int dice2 = 1; dice2 <= diceSides; dice2++) {
                        boolean isDouble = (dice1 == dice2);
                        int steps = dice1 + dice2;
                        double rollProb = 1.0 / (diceSides * diceSides);
                        
                        // Handle three consecutive doubles
                        if (isDouble && doubles == 2) {
                            // Three consecutive doubles: go to jail with 0 doubles
                            matrix[fromState][getStateIndex(JAIL, 0)] += rollProb;
                        } else {
                            // Normal movement
                            int newPosition = (position + steps) % BOARD_SIZE;
                            int newDoubles = isDouble ? doubles + 1 : 0;
                            
                            // Process landing on special squares
                            processLanding(fromState, newPosition, newDoubles, rollProb, matrix);
                        }
                    }
                }
            }
        }
        
        return matrix;
    }
    
    private static void processLanding(int fromState, int position, int doubles, double probability, double[][] matrix) {
        // Go To Jail square
        if (position == GO_TO_JAIL) {
            matrix[fromState][getStateIndex(JAIL, 0)] += probability;
            return;
        }
        
        // Community Chest
        if (isInArray(position, CC_POSITIONS)) {
            // 1/16 to GO
            matrix[fromState][getStateIndex(GO, 0)] += probability * (1.0/16);
            // 1/16 to JAIL
            matrix[fromState][getStateIndex(JAIL, 0)] += probability * (1.0/16);
            // 14/16 stay here
            matrix[fromState][getStateIndex(position, doubles)] += probability * (14.0/16);
            return;
        }
        
        // Chance
        if (isInArray(position, CH_POSITIONS)) {
            // 1. Advance to GO (1/16)
            matrix[fromState][getStateIndex(GO, 0)] += probability * (1.0/16);
            
            // 2. Go to JAIL (1/16)
            matrix[fromState][getStateIndex(JAIL, 0)] += probability * (1.0/16);
            
            // 3. Go to C1 (1/16) - position 11
            matrix[fromState][getStateIndex(11, 0)] += probability * (1.0/16);
            
            // 4. Go to E3 (1/16) - position 24
            matrix[fromState][getStateIndex(24, 0)] += probability * (1.0/16);
            
            // 5. Go to H2 (1/16) - position 39
            matrix[fromState][getStateIndex(39, 0)] += probability * (1.0/16);
            
            // 6. Go to R1 (1/16) - position 5
            matrix[fromState][getStateIndex(5, 0)] += probability * (1.0/16);
            
            // 7 & 8. Go to next R (2/16)
            int nextR = getNextInArray(position, RAILWAY_POSITIONS);
            matrix[fromState][getStateIndex(nextR, 0)] += probability * (2.0/16);
            
            // 9. Go to next U (1/16)
            int nextU = getNextInArray(position, UTILITY_POSITIONS);
            matrix[fromState][getStateIndex(nextU, 0)] += probability * (1.0/16);
            
            // 10. Go back 3 squares (1/16)
            int back3 = (position - 3 + BOARD_SIZE) % BOARD_SIZE;
            if (back3 == GO_TO_JAIL) {
                matrix[fromState][getStateIndex(JAIL, 0)] += probability * (1.0/16);
            } else if (isInArray(back3, CC_POSITIONS)) {
                // Back 3 lands on CC, apply CC rules
                matrix[fromState][getStateIndex(GO, 0)] += probability * (1.0/16) * (1.0/16);
                matrix[fromState][getStateIndex(JAIL, 0)] += probability * (1.0/16) * (1.0/16);
                matrix[fromState][getStateIndex(back3, 0)] += probability * (1.0/16) * (14.0/16);
            } else {
                matrix[fromState][getStateIndex(back3, 0)] += probability * (1.0/16);
            }
            
            // Remaining 6/16 cards: stay on Chance
            matrix[fromState][getStateIndex(position, doubles)] += probability * (6.0/16);
            return;
        }
        
        // Normal square
        matrix[fromState][getStateIndex(position, doubles)] += probability;
    }
    
    // Helper method to get state index from position and doubles count
    private static int getStateIndex(int position, int doublesCount) {
        return position * 3 + doublesCount;
    }
    
    // Check if a value is in an array
    private static boolean isInArray(int value, int[] array) {
        for (int i : array) {
            if (i == value) return true;
        }
        return false;
    }
    
    // Find next position in array after current position (with wrap-around)
    private static int getNextInArray(int current, int[] array) {
        for (int pos : array) {
            if (pos > current) return pos;
        }
        return array[0]; // Wrap around to first element
    }
    
    // Find the three most popular squares
    private static int[] findTopThreeSquares(double[] probabilities) {
        int[] topThree = new int[3];
        
        // Create list of index-probability pairs
        List<Map.Entry<Integer, Double>> pairs = new ArrayList<>();
        for (int i = 0; i < probabilities.length; i++) {
            pairs.add(new AbstractMap.SimpleEntry<>(i, probabilities[i]));
        }
        
        // Sort by probability (descending)
        pairs.sort((a, b) -> Double.compare(b.getValue(), a.getValue()));
        
        // Get the top three
        for (int i = 0; i < 3; i++) {
            topThree[i] = pairs.get(i).getKey();
        }
        
        return topThree;
    }
}