import java.util.*;

public class RomanArabicConverter {
    private static final Map<String, Integer> NUMBERS_MAP = createNumbersMap();
    
    private static Map<String, Integer> createNumbersMap() {
        Map<String, Integer> map = new LinkedHashMap<>();
        map.put("IV", 4);
        map.put("IX", 9);
        map.put("XL", 40);
        map.put("XC", 90);
        map.put("CD", 400);
        map.put("CM", 900);
        map.put("I", 1);
        map.put("V", 5);
        map.put("X", 10);
        map.put("L", 50);
        map.put("C", 100);
        map.put("D", 500);
        map.put("M", 1000);
        return map;
    }
    
    public static String toRoman(int num) {
        StringBuilder roman = new StringBuilder();
        List<Map.Entry<String, Integer>> entries = new ArrayList<>(NUMBERS_MAP.entrySet());
        entries.sort((a, b) -> b.getValue().compareTo(a.getValue()));
        
        for (Map.Entry<String, Integer> entry : entries) {
            String symbol = entry.getKey();
            int value = entry.getValue();
            int count = num / value;
            if (count > 0) {
                roman.append(symbol.repeat(count));
                num -= count * value;
            }
        }
        return roman.toString();
    }
    
    public static int toArabian(String num) {
        int dec = 0;
        String temp = num;
        for (Map.Entry<String, Integer> entry : NUMBERS_MAP.entrySet()) {
            String key = entry.getKey();
            int value = entry.getValue();
            int oldLength = temp.length();
            temp = temp.replace(key, "");
            int occurrences = (oldLength - temp.length()) / key.length();
            dec += occurrences * value;
        }
        return dec;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine(); // consume the newline
        for (int i = 0; i < n; i++) {
            String input = scanner.nextLine();
            int arabic = toArabian(input);
            String roman = toRoman(arabic);
            System.out.println(roman);
        }
    }
}