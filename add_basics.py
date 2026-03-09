import json
import re

def update_main_py():
    with open('main.py', 'r', encoding='utf-8') as f:
        text = f.read()

    new_module = """\
    # ==================== BASIC PROGRAMMING ====================
    "Basic Programming": {
        "Beginner": {
            "definition": (
                "Basic Programming concepts form the foundation of software development. This level covers variable declarations, "
                "basic arithmetic operations, and introduction to conditional logic (if-else statements). These building blocks "
                "are essential before moving on to complex data structures and algorithms."
            ),
            "working": (
                "1. Arithmetic: Using standard mathematical operators (+, -, *, /, %)\\n"
                "2. Conditionals: Using if, else if, and else blocks to dictate code execution flow based on boolean conditions."
            ),
            "algorithm": (
                "ADDITION:\\n  sum = a + b\\n  return sum\\n\\n"
                "EVEN OR ODD:\\n  if n % 2 == 0 return Even\\n  else return Odd\\n\\n"
                "MAXIMUM OF THREE:\\n  if a > b and a > c return a\\n  else if b > c return b\\n  else return c"
            ),
            "time_complexity": {
                "Addition": "O(1)",
                "Even/Odd": "O(1)",
                "Maximum of Three": "O(1)"
            },
            "space_complexity": "O(1) — only primitive variables are used.",
            "applications": (
                "• Core logic for calculators\\n"
                "• Simple decision-making in scripts\\n"
                "• Foundation for all complex algorithms"
            ),
            "advantages": (
                "• Extremely fast execution (constant time)\\n"
                "• Easy to comprehend and debug"
            ),
            "disadvantages": (
                "• Solves only trivial problems on their own\\n"
                "• Hardcoding conditions can lead to messy spaghetti code"
            ),
            "interview_notes": (
                "★ Always handle edge cases like negative numbers or zero.\\n"
                "★ Understand the exact behavior of the modulo (%) operator."
            ),
            "java": \"\"\"\\
public class BeginnerBasics {
    // 1. Addition of Two Numbers: Demonstrates variable declaration and arithmetic
    public static int add(int a, int b) {
        return a + b;
    }

    // 2. Check Even or Odd Number: Introduces conditional statements
    public static String checkEvenOdd(int n) {
        if (n % 2 == 0) return "Even";
        return "Odd";
    }

    // 3. Find Maximum of Three Numbers: Reinforces conditional logic
    public static int findMax(int a, int b, int c) {
        if (a >= b && a >= c) return a;
        if (b >= a && b >= c) return b;
        return c;
    }

    public static void main(String[] args) {
        System.out.println("Addition: " + add(5, 7));
        System.out.println("Parity of 10: " + checkEvenOdd(10));
        System.out.println("Max of 3, 7, 2: " + findMax(3, 7, 2));
    }
}\"\"\"
        },

        "Intermediate": {
            "definition": (
                "The Intermediate level introduces iteration and string/number manipulation. Loops (for, while) allow code "
                "to execute multiple times, which is necessary for reversing strings, checking for palindromes, and "
                "identifying patterns like prime numbers."
            ),
            "working": (
                "1. Reversing: Using a loop to iterate backwards through a string, or repeatedly using modulo 10 to extract digits.\\n"
                "2. Prime Check: Looping from 2 up to the square root of a number to check for factors.\\n"
                "3. Palindrome Check: Reversing the data and comparing it to the original, or using two pointers."
            ),
            "algorithm": (
                "REVERSE STRING:\\n  for i from length-1 down to 0:\\n    result += str[i]\\n\\n"
                "PRIME CHECK:\\n  if n < 2 return false\\n  for i from 2 to sqrt(n):\\n    if n % i == 0 return false\\n  return true"
            ),
            "time_complexity": {
                "Reverse String/Number": "O(n) where n is length of string/number of digits",
                "Check Palindrome": "O(n)",
                "Prime Number Check": "O(√n)"
            },
            "space_complexity": "O(n) for string reversal (due to immutability in Java), O(1) for number reversal/prime check.",
            "applications": (
                "• Cryptography and security (Primes)\\n"
                "• Data parsing and formatting (String manipulation)\\n"
                "• Validating user input"
            ),
            "advantages": (
                "• Loops dramatically increase the power of scripts\\n"
                "• Math-based loops (like √n prime check) are highly optimized"
            ),
            "disadvantages": (
                "• Prone to infinite loops if exit conditions are wrong\\n"
                "• String concatenation in loops can be slow (use StringBuilder)"
            ),
            "interview_notes": (
                "★ Mention StringBuilder for string reversal in Java to prevent O(n²) string copies.\\n"
                "★ For primes, looping only up to the square root is a classic optimization."
            ),
            "java": \"\"\"\\
public class IntermediateBasics {
    // 1. Reverse a String: Teaches string manipulation and loop usage
    public static String reverseString(String str) {
        StringBuilder sb = new StringBuilder();
        for (int i = str.length() - 1; i >= 0; i--) {
            sb.append(str.charAt(i));
        }
        return sb.toString();
    }

    // 2. Check Palindrome: Involves string reversal and comparison
    public static boolean isPalindrome(String str) {
        int left = 0, right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left++) != str.charAt(right--)) return false;
        }
        return true;
    }

    // 3. Prime Number Check: Introduces mathematical loops
    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println("Reverse 'hello': " + reverseString("hello"));
        System.out.println("Is 'radar' palindrome? " + isPalindrome("radar"));
        System.out.println("Is 29 prime? " + isPrime(29));
    }
}\"\"\"
        },

        "Advanced": {
            "definition": (
                "The Advanced level of basic programming dips into series generation and mathematical recursive concepts. "
                "Here we cover Factorials and Fibonacci Series, which introduce the concept of accumulating series data "
                "and making choices about whether to loop (iteration) or call the function itself (recursion)."
            ),
            "working": (
                "1. Factorial: N! = N * (N-1) * (N-2) ... * 1. Can be built with a simple loop accumulating a product.\\n"
                "2. Fibonacci: A sequence where each number is the sum of the two preceding ones. Can be calculated recursively or iteratively."
            ),
            "algorithm": (
                "FACTORIAL (Iterative):\\n  result = 1\\n  for i from 1 to N:\\n    result *= i\\n\\n"
                "FIBONACCI (Iterative):\\n  a = 0, b = 1\\n  for i from 2 to N:\\n    c = a + b\\n    a = b, b = c"
            ),
            "time_complexity": {
                "Factorial (Iterative)": "O(n)",
                "Fibonacci Series (Iterative)": "O(n)"
            },
            "space_complexity": "O(1) for both iterative approaches.",
            "applications": (
                "• Combinatorics and probability calculations\\n"
                "• Modeling natural phenomena and population growth\\n"
                "• Benchmarking performance of programming languages"
            ),
            "advantages": (
                "• Iterative solutions avoid call stack overflow limits\\n"
                "• Prepares the mind for Dynamic Programming concepts"
            ),
            "disadvantages": (
                "• Factorials grow exponentially fast and will overflow standard integer types very quickly"
            ),
            "interview_notes": (
                "★ Beware of integer overflow! Factorial of 13+ exceeds 32-bit int. Use long or BigInteger.\\n"
                "★ Be able to compare the iterative Fibonacci (O(n) time, O(1) space) against the recursive one (O(2^n) time)."
            ),
            "java": \"\"\"\\
public class AdvancedBasics {
    // 1. Factorial of a Number: Shows the use of loops
    public static long factorial(int n) {
        long result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    // 2. Fibonacci Series: A classic example for loops and series generation
    public static void printFibonacciSeries(int n) {
        if (n < 1) return;
        long a = 0, b = 1;
        System.out.print(a + " ");
        if (n > 1) System.out.print(b + " ");
        
        for (int i = 2; i < n; i++) {
            long c = a + b;
            System.out.print(c + " ");
            a = b;
            b = c;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        System.out.println("Factorial of 10: " + factorial(10));
        System.out.print("First 10 Fibonacci numbers: ");
        printFibonacciSeries(10);
    }
}\"\"\"
        }
    },
"""

    # Insert right after "DSA_CONTENT = {"
    target_str = "DSA_CONTENT = {"
    idx = text.find(target_str)
    if idx == -1: return
    
    insert_pos = idx + len(target_str) + 1
    new_text = text[:insert_pos] + new_module + text[insert_pos:]
    
    with open('main.py', 'w', encoding='utf-8') as f:
        f.write(new_text)

if __name__ == '__main__':
    update_main_py()
