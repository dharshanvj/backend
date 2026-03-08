import re

def update_recursion_java():
    with open('main.py', 'r', encoding='utf-8') as f:
        text = f.read()

    # Find the bounds of the "Recursion" module
    start_idx = text.find('"Recursion": {')
    if start_idx == -1: return
    end_idx = text.find('},', text.find('"Advanced":', start_idx) + 10) # rough end
    end_idx = text.find('"Backtracking": {', start_idx)
    if end_idx == -1: end_idx = len(text)
    
    recursion_text = text[start_idx:end_idx]

    # New Java codes
    beg_java = """\\
public class BeginnerRecursion {
    // 1. Basic Recursion: Factorial
    public static int factorial(int n) {
        if (n <= 1) return 1; // Base case
        return n * factorial(n - 1); // Recursive step
    }

    // 2. Classic Recursion: Fibonacci Sequence
    public static int fibonacci(int n) {
        if (n <= 1) return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
        System.out.println("Basic Recursion (Factorial 5): " + factorial(5));
        System.out.println("Fibonacci (7th term): " + fibonacci(7));
    }
}"""

    int_java = """\\
public class IntermediateRecursion {
    // 1. Palindrome Check using Recursion
    public static boolean isPalindrome(String str, int left, int right) {
        if (left >= right) return true;
        if (str.charAt(left) != str.charAt(right)) return false;
        return isPalindrome(str, left + 1, right - 1);
    }

    // 2. Reverse a String using Recursion
    public static String reverseString(String str) {
        if (str.isEmpty()) return str;
        return reverseString(str.substring(1)) + str.charAt(0);
    }

    public static void main(String[] args) {
        String testStr = "racecar";
        System.out.println("Is '" + testStr + "' a Palindrome? " + isPalindrome(testStr, 0, testStr.length() - 1));
        
        String word = "hello";
        System.out.println("Reversed '" + word + "': " + reverseString(word));
    }
}"""

    adv_java = """\\
public class AdvancedRecursion {
    // 1. Optimized Fibonacci with Memoization (Real-time efficiency)
    static long[] memo = new long[100];
    public static long fibMemo(int n) {
        if (n <= 1) return n;
        if (memo[n] != 0) return memo[n];
        return memo[n] = fibMemo(n - 1) + fibMemo(n - 2);
    }

    // 2. Palindromic Partitions (Advanced Backtracking + Recursion)
    public static void printPalindromes(String str, String current) {
        if (str.isEmpty()) {
            System.out.println(current.trim());
            return;
        }
        for (int i = 1; i <= str.length(); i++) {
            String prefix = str.substring(0, i);
            if (isPal(prefix)) {
                printPalindromes(str.substring(i), current + "(" + prefix + ") ");
            }
        }
    }
    
    private static boolean isPal(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) if (s.charAt(l++) != s.charAt(r--)) return false;
        return true;
    }

    public static void main(String[] args) {
        System.out.println("Optimized Fib(50) (Real-time): " + fibMemo(50));
        System.out.println("Palindromic Partitions of 'aab':");
        printPalindromes("aab", "");
    }
}"""

    # We need to replace the content of "java": """...""" for Beginner, Intermediate, Advanced
    # Let's do it carefully using regex inside the recursion text
    
    def replacer(match):
        prefix = match.group(1)
        # Determine which level we are in based on looking back
        # But lookbehind is hard. Let's just do sequential replacements.
        return match.group(0) # dummy

    # Split into 3 chunks: Beginner, Intermediate, Advanced
    blocks = re.split(r'("Beginner": {|"Intermediate": {|"Advanced": {)', recursion_text)
    # blocks[0] is `"Recursion": { ... `
    # blocks[1] is `"Beginner": {`
    # blocks[2] is beginner content
    # blocks[3] is `"Intermediate": {`
    # blocks[4] is intermediate content
    # blocks[5] is `"Advanced": {`
    # blocks[6] is advanced content
    
    if len(blocks) == 7:
        blocks[2] = re.sub(r'"java":\s*"""(.*?)"""', f'"java": """{beg_java}"""', blocks[2], flags=re.DOTALL)
        blocks[4] = re.sub(r'"java":\s*"""(.*?)"""', f'"java": """{int_java}"""', blocks[4], flags=re.DOTALL)
        blocks[6] = re.sub(r'"java":\s*"""(.*?)"""', f'"java": """{adv_java}"""', blocks[6], flags=re.DOTALL)
        
    new_recursion_text = "".join(blocks)
    
    new_text = text[:start_idx] + new_recursion_text + text[end_idx:]
    
    with open('main.py', 'w', encoding='utf-8') as f:
        f.write(new_text)

if __name__ == '__main__':
    update_recursion_java()
