from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
import os
import visualizer_engine as ve

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["?????"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# DSA CONTENT DATABASE
# ==============================

DSA_CONTENT = {
    # ==================== BASIC PROGRAMMING ====================
    "Basic Programming": {
        "Beginner": {
            "definition": (
                "Basic Programming concepts form the foundation of software development. This level covers variable declarations, "
                "basic arithmetic operations, and introduction to conditional logic (if-else statements). These building blocks "
                "are essential before moving on to complex data structures and algorithms."
            ),
            "working": (
                "1. Arithmetic: Using standard mathematical operators (+, -, *, /, %)\n"
                "2. Conditionals: Using if, else if, and else blocks to dictate code execution flow based on boolean conditions."
            ),
            "algorithm": (
                "ADDITION:\n  sum = a + b\n  return sum\n\n"
                "EVEN OR ODD:\n  if n % 2 == 0 return Even\n  else return Odd\n\n"
                "MAXIMUM OF THREE:\n  if a > b and a > c return a\n  else if b > c return b\n  else return c"
            ),
            "time_complexity": {
                "Addition": "O(1)",
                "Even/Odd": "O(1)",
                "Maximum of Three": "O(1)"
            },
            "space_complexity": "O(1) — only primitive variables are used.",
            "applications": (
                "• Core logic for calculators\n"
                "• Simple decision-making in scripts\n"
                "• Foundation for all complex algorithms"
            ),
            "advantages": (
                "• Extremely fast execution (constant time)\n"
                "• Easy to comprehend and debug"
            ),
            "disadvantages": (
                "• Solves only trivial problems on their own\n"
                "• Hardcoding conditions can lead to messy spaghetti code"
            ),
            "interview_notes": (
                "★ Always handle edge cases like negative numbers or zero.\n"
                "★ Understand the exact behavior of the modulo (%) operator."
            ),
            "java": """\
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
}"""
        },

        "Intermediate": {
            "definition": (
                "The Intermediate level introduces iteration and string/number manipulation. Loops (for, while) allow code "
                "to execute multiple times, which is necessary for reversing strings, checking for palindromes, and "
                "identifying patterns like prime numbers."
            ),
            "working": (
                "1. Reversing: Using a loop to iterate backwards through a string, or repeatedly using modulo 10 to extract digits.\n"
                "2. Prime Check: Looping from 2 up to the square root of a number to check for factors.\n"
                "3. Palindrome Check: Reversing the data and comparing it to the original, or using two pointers."
            ),
            "algorithm": (
                "REVERSE STRING:\n  for i from length-1 down to 0:\n    result += str[i]\n\n"
                "PRIME CHECK:\n  if n < 2 return false\n  for i from 2 to sqrt(n):\n    if n % i == 0 return false\n  return true"
            ),
            "time_complexity": {
                "Reverse String/Number": "O(n) where n is length of string/number of digits",
                "Check Palindrome": "O(n)",
                "Prime Number Check": "O(√n)"
            },
            "space_complexity": "O(n) for string reversal (due to immutability in Java), O(1) for number reversal/prime check.",
            "applications": (
                "• Cryptography and security (Primes)\n"
                "• Data parsing and formatting (String manipulation)\n"
                "• Validating user input"
            ),
            "advantages": (
                "• Loops dramatically increase the power of scripts\n"
                "• Math-based loops (like √n prime check) are highly optimized"
            ),
            "disadvantages": (
                "• Prone to infinite loops if exit conditions are wrong\n"
                "• String concatenation in loops can be slow (use StringBuilder)"
            ),
            "interview_notes": (
                "★ Mention StringBuilder for string reversal in Java to prevent O(n²) string copies.\n"
                "★ For primes, looping only up to the square root is a classic optimization."
            ),
            "java": """\
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
}"""
        },

        "Advanced": {
            "definition": (
                "The Advanced level of basic programming dips into series generation and mathematical recursive concepts. "
                "Here we cover Factorials and Fibonacci Series, which introduce the concept of accumulating series data "
                "and making choices about whether to loop (iteration) or call the function itself (recursion)."
            ),
            "working": (
                "1. Factorial: N! = N * (N-1) * (N-2) ... * 1. Can be built with a simple loop accumulating a product.\n"
                "2. Fibonacci: A sequence where each number is the sum of the two preceding ones. Can be calculated recursively or iteratively."
            ),
            "algorithm": (
                "FACTORIAL (Iterative):\n  result = 1\n  for i from 1 to N:\n    result *= i\n\n"
                "FIBONACCI (Iterative):\n  a = 0, b = 1\n  for i from 2 to N:\n    c = a + b\n    a = b, b = c"
            ),
            "time_complexity": {
                "Factorial (Iterative)": "O(n)",
                "Fibonacci Series (Iterative)": "O(n)"
            },
            "space_complexity": "O(1) for both iterative approaches.",
            "applications": (
                "• Combinatorics and probability calculations\n"
                "• Modeling natural phenomena and population growth\n"
                "• Benchmarking performance of programming languages"
            ),
            "advantages": (
                "• Iterative solutions avoid call stack overflow limits\n"
                "• Prepares the mind for Dynamic Programming concepts"
            ),
            "disadvantages": (
                "• Factorials grow exponentially fast and will overflow standard integer types very quickly"
            ),
            "interview_notes": (
                "★ Beware of integer overflow! Factorial of 13+ exceeds 32-bit int. Use long or BigInteger.\n"
                "★ Be able to compare the iterative Fibonacci (O(n) time, O(1) space) against the recursive one (O(2^n) time)."
            ),
            "java": """\
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
}"""
        }
    },

    # ==================== STACK ====================
    "Stack": {
        "Beginner": {
            "definition": (
                "A Stack is a linear data structure that follows the LIFO (Last In, First Out) principle — "
                "the last element inserted is the first one to be removed. Think of it like a stack of dinner "
                "plates: you add to the top and remove from the top. It has one open end (the top) and supports "
                "three primary operations: Push (add), Pop (remove), and Peek (view top without removing)."
            ),
            "working": (
                "1. PUSH: Check if the stack is full (overflow). If not, increment the top pointer and insert the element.\n"
                "2. POP: Check if the stack is empty (underflow). If not, return the top element and decrement the pointer.\n"
                "3. PEEK: Simply return the element at the top without modifying the stack.\n"
                "4. isEmpty: Returns true if top == -1.\n\n"
                "Example walkthrough:\n"
                "  Push(10) → Stack: [10]  top=0\n"
                "  Push(20) → Stack: [10, 20]  top=1\n"
                "  Push(30) → Stack: [10, 20, 30]  top=2\n"
                "  Pop()    → Returns 30, Stack: [10, 20]  top=1\n"
                "  Peek()   → Returns 20 (no change)"
            ),
            "algorithm": (
                "PUSH(stack, x):\n"
                "  if top == MAX-1 → print 'Stack Overflow'\n"
                "  else → top = top + 1; stack[top] = x\n\n"
                "POP(stack):\n"
                "  if top == -1 → print 'Stack Underflow'\n"
                "  else → x = stack[top]; top = top - 1; return x\n\n"
                "PEEK(stack):\n"
                "  if top == -1 → print 'Stack is Empty'\n"
                "  else → return stack[top]"
            ),
            "time_complexity": {
                "Push": "O(1) — direct index access",
                "Pop": "O(1) — direct index access",
                "Peek": "O(1) — direct index access",
                "isEmpty": "O(1) — simple comparison",
                "Search": "O(n) — must scan all elements"
            },
            "space_complexity": "O(n) — where n is the maximum number of elements the stack can hold.",
            "applications": (
                "• Undo / Redo functionality in text editors (Ctrl+Z)\n"
                "• Browser back/forward navigation history\n"
                "• Function call management (call stack)\n"
                "• Balancing parentheses and brackets in compilers\n"
                "• Expression conversion (infix → postfix → prefix)\n"
                "• Backtracking in puzzles (maze solving)"
            ),
            "advantages": (
                "• Extremely simple to implement using arrays or linked lists\n"
                "• All primary operations run in O(1) time\n"
                "• Efficient memory usage — no extra overhead per element (array-based)\n"
                "• Natural fit for problems with reversed-order processing"
            ),
            "disadvantages": (
                "• Only the top element is directly accessible\n"
                "• Array-based stacks have a fixed size limit\n"
                "• Stack overflow if push is called beyond capacity\n"
                "• Not suitable for random access of elements"
            ),
            "interview_notes": (
                "★ Stack Overflow occurs when you push onto a full stack.\n"
                "★ Stack Underflow occurs when you pop from an empty stack.\n"
                "★ Java's built-in Stack class extends Vector — prefer Deque for production.\n"
                "★ Common interview problems: Valid Parentheses, Min Stack, Daily Temperatures.\n"
                "★ Know how to reverse a string/array using a stack."
            ),
            "java": """\
import java.util.Stack;

public class StackDemo {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();

        // Push elements
        stack.push(10);
        stack.push(20);
        stack.push(30);
        System.out.println("Stack after pushes: " + stack);

        // Peek — view top without removing
        System.out.println("Top element (peek): " + stack.peek());

        // Pop — remove top element
        System.out.println("Popped: " + stack.pop());
        System.out.println("Stack after pop: " + stack);

        // Check empty
        System.out.println("Is empty? " + stack.isEmpty());

        // Search — returns 1-based position from top
        System.out.println("Position of 10: " + stack.search(10));
    }
}

/*
Output:
Stack after pushes: [10, 20, 30]
Top element (peek): 30
Popped: 30
Stack after pop: [10, 20]
Is empty? false
Position of 10: 2
*/"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, a Stack is implemented from scratch using either arrays or singly linked lists. "
                "The array-based stack uses a fixed-size array and a top index. The linked-list-based stack dynamically "
                "allocates nodes — each node holds data and a pointer to the next node. The head of the linked list "
                "acts as the top of the stack. Both implementations must handle overflow and underflow gracefully."
            ),
            "working": (
                "ARRAY-BASED STACK:\n"
                "  - Allocate array of size MAX.\n"
                "  - Maintain 'top' variable initialized to -1.\n"
                "  - Push increments top and stores element at arr[top].\n"
                "  - Pop reads arr[top] and decrements top.\n\n"
                "LINKED LIST STACK:\n"
                "  - Each node: { int data; Node next; }\n"
                "  - 'head' pointer represents the top of the stack.\n"
                "  - Push: create new node, point its next to current head, update head.\n"
                "  - Pop: save head.data, move head to head.next, return saved data.\n\n"
                "EXPRESSION EVALUATION (Postfix):\n"
                "  Input: '3 4 + 2 * 7 /'\n"
                "  Push 3, push 4 → see '+' → pop both, push 7\n"
                "  Push 2 → see '*' → pop both, push 14\n"
                "  Push 7 → see '/' → pop both, push 2 → Result: 2"
            ),
            "algorithm": (
                "BALANCED PARENTHESES CHECK:\n"
                "  for each char c in string:\n"
                "    if c is '(' or '{' or '[' → push(c)\n"
                "    if c is ')' → if stack empty or pop() != '(' → return false\n"
                "    (repeat for } and ])\n"
                "  return stack.isEmpty()\n\n"
                "POSTFIX EVALUATION:\n"
                "  for each token in expression:\n"
                "    if token is number → push(token)\n"
                "    if token is operator:\n"
                "      b = pop(); a = pop()\n"
                "      push(a operator b)\n"
                "  return pop() as result"
            ),
            "time_complexity": {
                "Array Push/Pop": "O(1)",
                "Linked List Push/Pop": "O(1)",
                "Parentheses Check": "O(n) — scan entire string",
                "Postfix Evaluation": "O(n) — single pass",
                "Infix to Postfix": "O(n) — single pass"
            },
            "space_complexity": "Array stack: O(n) fixed. Linked list stack: O(n) dynamic with extra pointer overhead per node.",
            "applications": (
                "• Infix to Postfix / Prefix expression conversion\n"
                "• Postfix expression evaluation\n"
                "• Balanced parentheses / bracket matching in compilers\n"
                "• Implementing function call stacks in interpreters\n"
                "• Next Greater Element problem\n"
                "• Stock span problem"
            ),
            "advantages": (
                "• Linked list implementation has no size limit (dynamic)\n"
                "• Constant time push/pop in both implementations\n"
                "• No memory wasted — linked list grows only as needed\n"
                "• Cleanly models LIFO behavior for recursive problems"
            ),
            "disadvantages": (
                "• Linked list nodes carry extra memory for 'next' pointer\n"
                "• Array-based has fixed capacity — must resize manually\n"
                "• No O(1) random access; searching requires O(n)\n"
                "• Cache performance of linked list is worse than array"
            ),
            "interview_notes": (
                "★ How to implement a stack using two queues — common interview question.\n"
                "★ How to implement a queue using two stacks.\n"
                "★ Min Stack: maintain a second stack that tracks the current minimum.\n"
                "★ Next Greater Element uses stack in O(n) vs brute force O(n²).\n"
                "★ Infix → Postfix: use operator precedence map + stack.\n"
                "★ Know recursion's relation to the call stack deeply."
            ),
            "java": """\
// Custom Stack using Array + Parentheses Validator
public class IntermediateStack {

    // ── 1. Array-Based Stack ──────────────────────────
    static class ArrayStack {
        int[] arr;
        int top = -1;
        int capacity;

        ArrayStack(int size) {
            capacity = size;
            arr = new int[size];
        }

        void push(int x) {
            if (top == capacity - 1) {
                System.out.println("Stack Overflow!");
                return;
            }
            arr[++top] = x;
        }

        int pop() {
            if (top == -1) {
                System.out.println("Stack Underflow!");
                return -1;
            }
            return arr[top--];
        }

        int peek() { return (top == -1) ? -1 : arr[top]; }
        boolean isEmpty() { return top == -1; }
    }

    // ── 2. Balanced Parentheses Check ─────────────────
    static boolean isBalanced(String s) {
        ArrayStack stack = new ArrayStack(s.length());
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
                if (stack.isEmpty()) return false;
                char top = (char) stack.pop();
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) return false;
            }
        }
        return stack.isEmpty();
    }

    // ── 3. Min Stack ──────────────────────────────────
    static class MinStack {
        ArrayStack main = new ArrayStack(100);
        ArrayStack minTracker = new ArrayStack(100);

        void push(int x) {
            main.push(x);
            if (minTracker.isEmpty() || x <= minTracker.peek())
                minTracker.push(x);
        }

        int pop() {
            int val = main.pop();
            if (val == minTracker.peek()) minTracker.pop();
            return val;
        }

        int getMin() { return minTracker.peek(); }
    }

    public static void main(String[] args) {
        // Test balanced parentheses
        System.out.println(isBalanced("{[()]}"));  // true
        System.out.println(isBalanced("{[(])}"));  // false

        // Test min stack
        MinStack ms = new MinStack();
        ms.push(5); ms.push(3); ms.push(7); ms.push(2);
        System.out.println("Min: " + ms.getMin()); // 2
        ms.pop();
        System.out.println("Min after pop: " + ms.getMin()); // 3
    }
}"""
        },

        "Advanced": {
            "definition": (
                "At the advanced level, stacks power complex algorithms: Depth-First Search (DFS), backtracking, "
                "monotonic stack problems, and iterative tree traversals. A Monotonic Stack maintains elements in "
                "strictly increasing or decreasing order, enabling O(n) solutions to problems that would otherwise "
                "require O(n²). The call stack in the OS stores stack frames — each frame holds local variables, "
                "return address, and parameters for recursive calls."
            ),
            "working": (
                "MONOTONIC STACK (Next Greater Element):\n"
                "  Maintain a stack of indices of elements awaiting their 'next greater'.\n"
                "  For each element arr[i]:\n"
                "    While stack not empty AND arr[stack.top] < arr[i]:\n"
                "      result[stack.pop()] = arr[i]\n"
                "    push(i)\n"
                "  Remaining elements in stack have no greater element → result = -1\n\n"
                "ITERATIVE DFS using Stack:\n"
                "  Push start node onto stack.\n"
                "  While stack not empty:\n"
                "    node = pop()\n"
                "    if not visited: mark visited, process node\n"
                "    push all unvisited neighbors\n\n"
                "LARGEST RECTANGLE IN HISTOGRAM:\n"
                "  Use stack to track bar indices.\n"
                "  For each bar, pop while current bar is shorter than stack top.\n"
                "  Compute area using popped bar as the shortest — O(n) total."
            ),
            "algorithm": (
                "NEXT GREATER ELEMENT — O(n):\n"
                "  stack = empty\n"
                "  result = [-1] * n\n"
                "  for i in 0..n-1:\n"
                "    while stack not empty and arr[stack.top] < arr[i]:\n"
                "      result[stack.pop()] = arr[i]\n"
                "    stack.push(i)\n\n"
                "LARGEST HISTOGRAM RECTANGLE — O(n):\n"
                "  push sentinel 0 at end of heights\n"
                "  for i in 0..n:\n"
                "    while stack not empty and heights[i] < heights[stack.top]:\n"
                "      h = heights[stack.pop()]\n"
                "      w = i - stack.top - 1\n"
                "      maxArea = max(maxArea, h * w)\n"
                "    stack.push(i)"
            ),
            "time_complexity": {
                "Next Greater Element": "O(n) — each element pushed/popped once",
                "Largest Rectangle": "O(n) — monotonic stack, single pass",
                "Iterative DFS": "O(V + E) — vertices + edges",
                "Iterative Inorder": "O(n) — visits each node once",
                "Stock Span Problem": "O(n) — single pass with stack"
            },
            "space_complexity": "O(n) for the stack in all above algorithms. O(V) for DFS visited set.",
            "applications": (
                "• Depth-First Search (DFS) in graph traversal\n"
                "• Backtracking algorithms (N-Queens, Sudoku Solver)\n"
                "• Largest Rectangle in Histogram (used in maximal rectangle in matrix)\n"
                "• Next Greater / Smaller Element problems\n"
                "• Iterative tree traversals (inorder, preorder, postorder)\n"
                "• Trapping Rainwater problem\n"
                "• Asteroid Collision (LeetCode 735)"
            ),
            "advantages": (
                "• Monotonic stack reduces O(n²) brute-force to O(n)\n"
                "• Iterative DFS avoids system call stack overflow on deep graphs\n"
                "• Enables elegant solutions to span, histogram, and rainwater problems\n"
                "• Fundamental to understanding recursion and OS memory management"
            ),
            "disadvantages": (
                "• Monotonic stack solutions can be non-intuitive — hard to spot in interviews\n"
                "• Iterative DFS logic is more complex than recursive version\n"
                "• Space is still O(n) in the worst case\n"
                "• Requires careful handling of boundary conditions"
            ),
            "interview_notes": (
                "★ Trapping Rainwater (LeetCode 42) — two-pointer OR stack-based O(n).\n"
                "★ Largest Rectangle in Histogram (LeetCode 84) — classic monotonic stack.\n"
                "★ Daily Temperatures (LeetCode 739) — next warmer day = next greater element.\n"
                "★ Asteroid Collision (LeetCode 735) — stack simulation.\n"
                "★ Remove K Digits (LeetCode 402) — monotonic stack for smallest number.\n"
                "★ Implement iterative postorder traversal — two stacks or reverse trick.\n"
                "★ Know how OS call stacks differ from data structure stacks."
            ),
            "java": """\
import java.util.*;

public class AdvancedStack {

    // ── 1. Next Greater Element — O(n) ───────────────
    static int[] nextGreaterElement(int[] arr) {
        int n = arr.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);
        Deque<Integer> stack = new ArrayDeque<>(); // stores indices

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] < arr[i]) {
                result[stack.pop()] = arr[i];
            }
            stack.push(i);
        }
        return result;
    }

    // ── 2. Largest Rectangle in Histogram — O(n) ─────
    static int largestRectangle(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int maxArea = 0;
        int n = heights.length;

        for (int i = 0; i <= n; i++) {
            int currHeight = (i == n) ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > currHeight) {
                int h = heights[stack.pop()];
                int w = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, h * w);
            }
            stack.push(i);
        }
        return maxArea;
    }

    // ── 3. Trapping Rainwater — O(n) ─────────────────
    static int trapRainwater(int[] height) {
        Deque<Integer> stack = new ArrayDeque<>();
        int water = 0;

        for (int i = 0; i < height.length; i++) {
            while (!stack.isEmpty() && height[i] > height[stack.peek()]) {
                int bottom = stack.pop();
                if (stack.isEmpty()) break;
                int left = stack.peek();
                int boundedHeight = Math.min(height[left], height[i]) - height[bottom];
                int width = i - left - 1;
                water += boundedHeight * width;
            }
            stack.push(i);
        }
        return water;
    }

    // ── 4. Iterative DFS ──────────────────────────────
    static void dfs(Map<Integer, List<Integer>> graph, int start) {
        Deque<Integer> stack = new ArrayDeque<>();
        Set<Integer> visited = new HashSet<>();
        stack.push(start);

        while (!stack.isEmpty()) {
            int node = stack.pop();
            if (visited.contains(node)) continue;
            visited.add(node);
            System.out.print(node + " ");
            for (int neighbor : graph.getOrDefault(node, List.of())) {
                if (!visited.contains(neighbor)) stack.push(neighbor);
            }
        }
    }

    public static void main(String[] args) {
        // Next Greater Element
        int[] arr = {4, 5, 2, 10, 8};
        System.out.println("Next Greater: " + Arrays.toString(nextGreaterElement(arr)));
        // → [5, 10, 10, -1, -1]

        // Largest Rectangle
        int[] hist = {2, 1, 5, 6, 2, 3};
        System.out.println("Max Rectangle Area: " + largestRectangle(hist));
        // → 10

        // Trapping Rainwater
        int[] terrain = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
        System.out.println("Water Trapped: " + trapRainwater(terrain));
        // → 6
    }
}"""
        }
    },

    # ==================== QUEUE ====================
    "Queue": {
        "Beginner": {
            "definition": (
                "A Queue is a linear data structure that follows the FIFO (First In, First Out) principle — "
                "the first element inserted is the first one to be removed, just like a real-world queue at a "
                "ticket counter. It has two ends: the REAR (where elements are added via Enqueue) and the "
                "FRONT (where elements are removed via Dequeue). Unlike a stack, a queue is open at both ends."
            ),
            "working": (
                "1. ENQUEUE: Add element at the rear. If rear == MAX-1, the queue is full.\n"
                "2. DEQUEUE: Remove element from the front. If front > rear, the queue is empty.\n"
                "3. PEEK/FRONT: View the front element without removing it.\n"
                "4. isEmpty: Return true if front > rear (or queue has no elements).\n\n"
                "Example walkthrough:\n"
                "  Enqueue(10) → Queue: [10]  front=0, rear=0\n"
                "  Enqueue(20) → Queue: [10, 20]  front=0, rear=1\n"
                "  Enqueue(30) → Queue: [10, 20, 30]  front=0, rear=2\n"
                "  Dequeue()   → Returns 10, Queue: [20, 30]  front=1, rear=2\n"
                "  Peek()      → Returns 20"
            ),
            "algorithm": (
                "ENQUEUE(queue, x):\n"
                "  if rear == MAX-1 → print 'Queue Full'\n"
                "  else → rear = rear + 1; queue[rear] = x\n\n"
                "DEQUEUE(queue):\n"
                "  if front > rear → print 'Queue Empty'\n"
                "  else → x = queue[front]; front = front + 1; return x\n\n"
                "PEEK(queue):\n"
                "  if isEmpty → print 'Empty'\n"
                "  else → return queue[front]"
            ),
            "time_complexity": {
                "Enqueue": "O(1) — direct rear index insertion",
                "Dequeue": "O(1) — direct front index removal",
                "Peek": "O(1) — access front element",
                "isEmpty": "O(1) — simple condition check",
                "Search": "O(n) — must traverse all elements"
            },
            "space_complexity": "O(n) — where n is the maximum capacity of the queue.",
            "applications": (
                "• CPU and disk scheduling (Round Robin scheduling)\n"
                "• Ticket booking and customer service systems\n"
                "• Breadth-First Search (BFS) in graphs and trees\n"
                "• Print spooler queues (printer job management)\n"
                "• Asynchronous data transfer between processes\n"
                "• Keyboard input buffering"
            ),
            "advantages": (
                "• Maintains insertion order — guarantees fairness (FIFO)\n"
                "• O(1) enqueue and dequeue operations\n"
                "• Simple to implement with arrays or linked lists\n"
                "• Ideal for producer-consumer and scheduling scenarios"
            ),
            "disadvantages": (
                "• Simple array queue wastes space after dequeues (front index shifts)\n"
                "• No random access to middle elements\n"
                "• Fixed capacity in array-based implementation\n"
                "• Circular queue needed to solve space wastage issue"
            ),
            "interview_notes": (
                "★ A simple array queue wastes space — Circular Queue fixes this.\n"
                "★ Java: prefer LinkedList or ArrayDeque over Queue interface for stacks/queues.\n"
                "★ BFS always uses a queue — memorize this relationship.\n"
                "★ Know the difference: Queue (FIFO) vs Stack (LIFO) vs Deque (both).\n"
                "★ Common interview: implement Queue using two Stacks."
            ),
            "java": """\
import java.util.LinkedList;
import java.util.Queue;

public class QueueDemo {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();

        // Enqueue elements
        queue.add(10);
        queue.add(20);
        queue.add(30);
        System.out.println("Queue: " + queue);

        // Peek — view front element
        System.out.println("Front (peek): " + queue.peek());

        // Dequeue — remove front element
        System.out.println("Dequeued: " + queue.poll());
        System.out.println("Queue after dequeue: " + queue);

        // Size and empty check
        System.out.println("Size: " + queue.size());
        System.out.println("Is empty? " + queue.isEmpty());
    }
}

/*
Output:
Queue: [10, 20, 30]
Front (peek): 10
Dequeued: 10
Queue after dequeue: [20, 30]
Size: 2
Is empty? false
*/"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we explore specialized queue types: Circular Queue (fixes space waste "
                "in linear queues), Deque / Double-Ended Queue (insert and delete from both ends), and Priority Queue "
                "(elements processed by priority, not order). We also implement Queue using two Stacks, a classic "
                "interview problem. The Circular Queue uses modular arithmetic ((rear+1) % capacity) to wrap around "
                "and reuse freed slots."
            ),
            "working": (
                "CIRCULAR QUEUE:\n"
                "  front and rear pointers wrap around using % capacity.\n"
                "  Enqueue: rear = (rear + 1) % capacity; arr[rear] = x\n"
                "  Dequeue: front = (front + 1) % capacity\n"
                "  Full condition: (rear + 1) % capacity == front\n"
                "  Empty condition: front == -1\n\n"
                "PRIORITY QUEUE (Min-Heap based):\n"
                "  Elements with highest priority (smallest value in min-heap) are dequeued first.\n"
                "  Java's PriorityQueue uses a binary min-heap internally.\n"
                "  Poll() always returns the smallest element in O(log n).\n\n"
                "QUEUE USING TWO STACKS:\n"
                "  Stack1 (inbox) and Stack2 (outbox).\n"
                "  Enqueue: always push to Stack1.\n"
                "  Dequeue: if Stack2 empty, transfer all Stack1 → Stack2, then pop Stack2."
            ),
            "algorithm": (
                "CIRCULAR QUEUE ENQUEUE:\n"
                "  if (rear+1) % cap == front → 'Queue Full'\n"
                "  if front == -1 → front = 0\n"
                "  rear = (rear+1) % cap\n"
                "  arr[rear] = x\n\n"
                "CIRCULAR QUEUE DEQUEUE:\n"
                "  if front == -1 → 'Queue Empty'\n"
                "  x = arr[front]\n"
                "  if front == rear → front = rear = -1  (last element)\n"
                "  else → front = (front+1) % cap\n"
                "  return x\n\n"
                "QUEUE USING 2 STACKS — DEQUEUE:\n"
                "  if stack2 is empty:\n"
                "    while stack1 not empty: stack2.push(stack1.pop())\n"
                "  return stack2.pop()"
            ),
            "time_complexity": {
                "Circular Enqueue/Dequeue": "O(1)",
                "Priority Queue Insert": "O(log n) — heap sift-up",
                "Priority Queue Poll": "O(log n) — heap sift-down",
                "Queue via 2 Stacks Enqueue": "O(1) amortized",
                "Queue via 2 Stacks Dequeue": "O(n) worst case, O(1) amortized",
                "Deque Insert/Delete (both ends)": "O(1)"
            },
            "space_complexity": "Circular Queue: O(n). Priority Queue (heap): O(n). Queue via 2 Stacks: O(n) combined.",
            "applications": (
                "• Circular Queue: CPU scheduling (Round Robin), streaming buffers\n"
                "• Priority Queue: Dijkstra's shortest path, Prim's MST, task schedulers\n"
                "• Deque: Sliding window maximum, palindrome checking\n"
                "• Queue via 2 Stacks: interview pattern, undo-redo with ordering\n"
                "• BFS level-order tree traversal uses a queue"
            ),
            "advantages": (
                "• Circular queue eliminates memory waste of linear queue\n"
                "• Priority queue enables smart scheduling by priority\n"
                "• Deque is the most flexible — works as both stack and queue\n"
                "• Amortized O(1) dequeue via two-stack implementation"
            ),
            "disadvantages": (
                "• Circular queue has fixed capacity; harder to resize\n"
                "• Priority queue: O(log n) instead of O(1) for insert/delete\n"
                "• Queue via two stacks: O(n) worst case on single dequeue\n"
                "• More complex to implement than basic queue"
            ),
            "interview_notes": (
                "★ Implement Queue using two Stacks — must know amortized analysis.\n"
                "★ Sliding Window Maximum (LeetCode 239) — uses Deque in O(n).\n"
                "★ Top K Frequent Elements — Priority Queue (max-heap) solution.\n"
                "★ Merge K Sorted Lists — Priority Queue.\n"
                "★ BFS with level tracking — use queue + size-based level loop.\n"
                "★ Know: Java PriorityQueue is a min-heap; for max-heap use Collections.reverseOrder()."
            ),
            "java": """\
import java.util.*;

public class IntermediateQueue {

    // ── 1. Circular Queue ─────────────────────────────
    static class CircularQueue {
        int[] arr;
        int front = -1, rear = -1, cap;

        CircularQueue(int size) { arr = new int[size]; cap = size; }

        void enqueue(int x) {
            if ((rear + 1) % cap == front) { System.out.println("Queue Full"); return; }
            if (front == -1) front = 0;
            rear = (rear + 1) % cap;
            arr[rear] = x;
        }

        int dequeue() {
            if (front == -1) { System.out.println("Queue Empty"); return -1; }
            int val = arr[front];
            if (front == rear) { front = rear = -1; }
            else front = (front + 1) % cap;
            return val;
        }
    }

    // ── 2. Queue Using Two Stacks ─────────────────────
    static class QueueViaStacks {
        Deque<Integer> inbox = new ArrayDeque<>();
        Deque<Integer> outbox = new ArrayDeque<>();

        void enqueue(int x) { inbox.push(x); }

        int dequeue() {
            if (outbox.isEmpty()) {
                while (!inbox.isEmpty()) outbox.push(inbox.pop());
            }
            return outbox.isEmpty() ? -1 : outbox.pop();
        }

        int peek() {
            if (outbox.isEmpty()) {
                while (!inbox.isEmpty()) outbox.push(inbox.pop());
            }
            return outbox.isEmpty() ? -1 : outbox.peek();
        }
    }

    // ── 3. Priority Queue (Task Scheduler) ───────────
    static void taskScheduler(int[][] tasks) {
        // tasks[i] = {priority, taskId}
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[0] - a[0]); // max-heap
        for (int[] t : tasks) pq.offer(t);
        System.out.print("Execution order: ");
        while (!pq.isEmpty()) System.out.print("Task#" + pq.poll()[1] + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        // Circular Queue
        CircularQueue cq = new CircularQueue(4);
        cq.enqueue(1); cq.enqueue(2); cq.enqueue(3);
        System.out.println("Dequeued: " + cq.dequeue()); // 1
        cq.enqueue(4); // wraps around

        // Queue via Stacks
        QueueViaStacks q = new QueueViaStacks();
        q.enqueue(10); q.enqueue(20); q.enqueue(30);
        System.out.println("Front: " + q.peek());    // 10
        System.out.println("Dequeue: " + q.dequeue()); // 10

        // Priority Queue
        taskScheduler(new int[][]{{3,1},{1,2},{5,3},{2,4}});
        // → Task#3 Task#1 Task#4 Task#2
    }
}"""
        },

        "Advanced": {
            "definition": (
                "At the advanced level, queues are the backbone of graph algorithms (BFS, multi-source BFS, "
                "0-1 BFS), level-order tree traversal, and the Sliding Window Maximum problem. The Monotonic Deque "
                "maintains a decreasing order of elements in the window, solving sliding window max in O(n). "
                "0-1 BFS uses a Deque instead of a standard queue to handle 0-weight and 1-weight edges efficiently "
                "without the overhead of Dijkstra's priority queue."
            ),
            "working": (
                "SLIDING WINDOW MAXIMUM (Monotonic Deque):\n"
                "  Maintain deque of indices in decreasing order of arr values.\n"
                "  For each element arr[i]:\n"
                "    Remove from back while arr[deque.back] < arr[i] (they can never be max)\n"
                "    Add i to back.\n"
                "    Remove from front if front index is outside window [i-k+1, i]\n"
                "    Record arr[deque.front] as the window maximum.\n\n"
                "MULTI-SOURCE BFS:\n"
                "  Initialize queue with ALL source nodes simultaneously.\n"
                "  BFS expands outward from all sources at once.\n"
                "  Useful for: nearest 0 in matrix, rotten oranges, walls and gates.\n\n"
                "0-1 BFS:\n"
                "  Use a Deque. For 0-weight edge: push to FRONT.\n"
                "  For 1-weight edge: push to BACK.\n"
                "  Gives shortest path in O(V+E) vs Dijkstra's O((V+E) log V)."
            ),
            "algorithm": (
                "SLIDING WINDOW MAX — O(n):\n"
                "  deque = empty (stores indices)\n"
                "  for i in 0..n-1:\n"
                "    while deque not empty and arr[deque.back] < arr[i]:\n"
                "      deque.removeBack()\n"
                "    deque.addBack(i)\n"
                "    if deque.front < i - k + 1: deque.removeFront()\n"
                "    if i >= k-1: result.add(arr[deque.front])\n\n"
                "BFS LEVEL-ORDER TREE:\n"
                "  queue.add(root)\n"
                "  while queue not empty:\n"
                "    size = queue.size()  // nodes in current level\n"
                "    for i in 0..size-1:\n"
                "      node = queue.poll()\n"
                "      process(node)\n"
                "      if node.left: queue.add(node.left)\n"
                "      if node.right: queue.add(node.right)"
            ),
            "time_complexity": {
                "BFS (graph)": "O(V + E)",
                "Level-Order Traversal": "O(n)",
                "Sliding Window Max": "O(n) — each element added/removed from deque once",
                "Multi-Source BFS": "O(V + E)",
                "0-1 BFS": "O(V + E) — faster than Dijkstra for 0/1 weights"
            },
            "space_complexity": "O(V) for BFS queue. O(k) for sliding window deque (k = window size).",
            "applications": (
                "• BFS for shortest path in unweighted graphs\n"
                "• Level-order traversal of binary trees\n"
                "• Rotting Oranges (multi-source BFS)\n"
                "• Sliding Window Maximum (Monotonic Deque)\n"
                "• 01 Matrix problem (nearest 0 via BFS)\n"
                "• Word Ladder problem (BFS on string graph)"
            ),
            "advantages": (
                "• BFS guarantees shortest path in unweighted graphs\n"
                "• Monotonic deque gives O(n) sliding window solutions\n"
                "• Multi-source BFS processes all sources simultaneously — elegant and efficient\n"
                "• 0-1 BFS outperforms Dijkstra for binary-weight graphs"
            ),
            "disadvantages": (
                "• BFS uses O(V) memory — can be large for dense graphs\n"
                "• Monotonic deque logic is non-trivial to derive under pressure\n"
                "• BFS doesn't work for weighted graphs (use Dijkstra instead)\n"
                "• Level-by-level BFS requires size-tracking per level"
            ),
            "interview_notes": (
                "★ Sliding Window Maximum (LeetCode 239) — must-know monotonic deque pattern.\n"
                "★ Rotting Oranges (LeetCode 994) — multi-source BFS from all rotten cells.\n"
                "★ Word Ladder (LeetCode 127) — BFS on implicit graph of strings.\n"
                "★ Binary Tree Right Side View — level-order BFS, pick last in each level.\n"
                "★ 01 Matrix (LeetCode 542) — multi-source BFS from all 0-cells.\n"
                "★ Course Schedule II (LeetCode 210) — topological sort using BFS (Kahn's algorithm)."
            ),
            "java": """\
import java.util.*;

public class AdvancedQueue {

    // ── 1. Sliding Window Maximum — O(n) ─────────────
    static int[] slidingWindowMax(int[] arr, int k) {
        int n = arr.length;
        int[] result = new int[n - k + 1];
        Deque<Integer> deque = new ArrayDeque<>(); // stores indices

        for (int i = 0; i < n; i++) {
            // Remove indices outside window
            while (!deque.isEmpty() && deque.peekFirst() < i - k + 1)
                deque.pollFirst();
            // Remove smaller elements from back
            while (!deque.isEmpty() && arr[deque.peekLast()] < arr[i])
                deque.pollLast();
            deque.offerLast(i);
            if (i >= k - 1) result[i - k + 1] = arr[deque.peekFirst()];
        }
        return result;
    }

    // ── 2. Rotting Oranges (Multi-Source BFS) ────────
    static int rottingOranges(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        Queue<int[]> q = new LinkedList<>();
        int fresh = 0;

        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) q.offer(new int[]{r, c});
                if (grid[r][c] == 1) fresh++;
            }

        if (fresh == 0) return 0;
        int minutes = 0;
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] curr = q.poll();
                for (int[] d : dirs) {
                    int nr = curr[0] + d[0], nc = curr[1] + d[1];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        fresh--;
                        q.offer(new int[]{nr, nc});
                    }
                }
            }
            minutes++;
        }
        return fresh == 0 ? minutes - 1 : -1;
    }

    // ── 3. Level-Order Tree Traversal ─────────────────
    static class TreeNode {
        int val; TreeNode left, right;
        TreeNode(int v) { val = v; }
    }

    static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        while (!q.isEmpty()) {
            int size = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                level.add(node.val);
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
            result.add(level);
        }
        return result;
    }

    public static void main(String[] args) {
        // Sliding Window Max
        int[] arr = {1, 3, -1, -3, 5, 3, 6, 7};
        System.out.println("Window Max (k=3): " + Arrays.toString(slidingWindowMax(arr, 3)));
        // → [3, 3, 5, 5, 6, 7]

        // Rotting Oranges
        int[][] grid = {{2,1,1},{1,1,0},{0,1,1}};
        System.out.println("Minutes to rot all: " + rottingOranges(grid));
        // → 4
    }
}"""
        }
    },

    # ==================== LINEAR SEARCH ====================
    "Linear Search": {
        "Beginner": {
            "definition": (
                "Linear Search (also called Sequential Search) is the simplest searching algorithm. It checks "
                "each element in the array one by one from left to right until the target element is found or "
                "the entire array has been scanned. It works on both sorted and unsorted arrays and requires "
                "no preprocessing. It is best suited for small datasets or unsorted collections."
            ),
            "working": (
                "1. Start at index 0 (the first element).\n"
                "2. Compare the current element with the target value.\n"
                "3. If they match, return the current index (element found).\n"
                "4. If they do not match, move to the next index.\n"
                "5. Repeat until the element is found or the array ends.\n"
                "6. If the end is reached without a match, return -1 (not found).\n\n"
                "Example:\n"
                "  Array: [4, 8, 2, 9, 5]  Target: 9\n"
                "  Compare 4 → No\n"
                "  Compare 8 → No\n"
                "  Compare 2 → No\n"
                "  Compare 9 → YES! Return index 3."
            ),
            "algorithm": (
                "LINEAR_SEARCH(arr, n, target):\n"
                "  for i from 0 to n-1:\n"
                "    if arr[i] == target:\n"
                "      return i  // found at index i\n"
                "  return -1     // not found"
            ),
            "time_complexity": {
                "Best Case": "O(1) — target is the first element",
                "Average Case": "O(n/2) ≈ O(n) — target is in the middle",
                "Worst Case": "O(n) — target is last or not present",
                "Space": "O(1) — no extra space needed"
            },
            "space_complexity": "O(1) — in-place algorithm, no auxiliary space required.",
            "applications": (
                "• Searching in small, unsorted datasets\n"
                "• Finding an element in a linked list (no random access)\n"
                "• Searching in streams where data arrives one at a time\n"
                "• When the array is very small and binary search overhead isn't worth it\n"
                "• Searching objects by a non-comparable key"
            ),
            "advantages": (
                "• Works on unsorted arrays — no preprocessing needed\n"
                "• Simple to understand and implement\n"
                "• No extra memory required — O(1) space\n"
                "• Works on any data type that supports equality comparison"
            ),
            "disadvantages": (
                "• Very slow for large datasets — O(n) every time\n"
                "• Much less efficient than binary search on sorted arrays\n"
                "• Not scalable — performance degrades linearly with size\n"
                "• Cannot take advantage of sorted order"
            ),
            "interview_notes": (
                "★ Best case O(1) — element is at index 0.\n"
                "★ Worst case O(n) — element is at end or absent.\n"
                "★ Linear search is used as a subroutine in some advanced algorithms.\n"
                "★ Sentinel Linear Search: place target at end to eliminate boundary check.\n"
                "★ Know when to prefer linear over binary: unsorted data, very small n."
            ),
            "java": """\
public class LinearSearchDemo {

    // Basic Linear Search
    static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) return i;
        }
        return -1;
    }

    // Search for ALL occurrences
    static void findAll(int[] arr, int target) {
        boolean found = false;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                System.out.println("Found at index: " + i);
                found = true;
            }
        }
        if (!found) System.out.println("Not found");
    }

    // Sentinel Linear Search (optimized — removes boundary check)
    static int sentinelSearch(int[] arr, int target) {
        int n = arr.length;
        int last = arr[n - 1];
        arr[n - 1] = target; // place sentinel at end
        int i = 0;
        while (arr[i] != target) i++;
        arr[n - 1] = last; // restore
        if (i < n - 1 || arr[n - 1] == target) return i;
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {4, 8, 2, 9, 5, 9, 1};

        System.out.println("Search 9: index " + linearSearch(arr, 9)); // 3
        System.out.println("Search 7: index " + linearSearch(arr, 7)); // -1

        System.out.print("All occurrences of 9: ");
        findAll(arr, 9); // index 3 and 5

        System.out.println("Sentinel search 5: index " + sentinelSearch(arr, 5)); // 4
    }
}

/*
Output:
Search 9: index 3
Search 7: index -1
All occurrences of 9:
  Found at index: 3
  Found at index: 5
Sentinel search 5: index 4
*/"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we extend linear search to more complex data: 2D arrays (matrices), "
                "strings, linked lists, and use it with custom comparators for objects. We also look at the "
                "Transposition and Move-to-Front heuristics that optimize repeated searches by bringing frequently "
                "searched elements closer to the front over time, reducing average search time."
            ),
            "working": (
                "2D MATRIX LINEAR SEARCH:\n"
                "  Treat the matrix as a flattened array using index math:\n"
                "  row = i / cols;  col = i % cols\n"
                "  Or simply: nested loop over rows and columns.\n\n"
                "MOVE-TO-FRONT HEURISTIC:\n"
                "  When element at index i is found, swap arr[i] with arr[0].\n"
                "  Frequently searched elements naturally move to the front.\n"
                "  Amortized faster over many repeated searches.\n\n"
                "TRANSPOSITION HEURISTIC:\n"
                "  When element found at index i, swap arr[i] with arr[i-1].\n"
                "  Slower migration but more stable than move-to-front.\n\n"
                "LINKED LIST LINEAR SEARCH:\n"
                "  Start at head. Traverse node-by-node comparing data.\n"
                "  No index access — must follow next pointers."
            ),
            "algorithm": (
                "2D MATRIX SEARCH:\n"
                "  for row in 0..rows-1:\n"
                "    for col in 0..cols-1:\n"
                "      if matrix[row][col] == target:\n"
                "        return (row, col)\n"
                "  return (-1, -1)\n\n"
                "MOVE-TO-FRONT:\n"
                "  for i in 0..n-1:\n"
                "    if arr[i] == target:\n"
                "      swap(arr[i], arr[0])\n"
                "      return 0\n"
                "  return -1"
            ),
            "time_complexity": {
                "1D Linear Search": "O(n)",
                "2D Matrix Search": "O(rows × cols)",
                "Linked List Search": "O(n) — no index access",
                "Move-to-Front (amortized)": "O(n) first search, faster subsequently",
                "String Search (character)": "O(length)"
            },
            "space_complexity": "O(1) for all variants. Linked list traversal only uses a pointer variable.",
            "applications": (
                "• Searching in 2D grids and matrices\n"
                "• Finding elements in singly/doubly linked lists\n"
                "• Text editor find (character or word search)\n"
                "• Self-organizing lists using Move-to-Front\n"
                "• Cache eviction policy simulation"
            ),
            "advantages": (
                "• No extra space needed\n"
                "• Works on any data structure with sequential access\n"
                "• Heuristics (MTF, transposition) improve amortized performance\n"
                "• Easy to extend for 2D or multi-dimensional data"
            ),
            "disadvantages": (
                "• Still O(n) per search without heuristics\n"
                "• Heuristics disturb element ordering (bad if order matters)\n"
                "• Move-to-Front can degrade to O(n) if all elements searched once\n"
                "• Poor cache performance on linked lists vs arrays"
            ),
            "interview_notes": (
                "★ 2D matrix search: if matrix is row-sorted and column-sorted, use O(n+m) search (top-right corner).\n"
                "★ Move-to-Front is used in LRU Cache concepts.\n"
                "★ Linked list search is always O(n) regardless of position.\n"
                "★ Know how to find the first, last, and all occurrences of a target.\n"
                "★ String character search is linear scan — indexOf() in Java is O(n)."
            ),
            "java": """\
public class IntermediateLinearSearch {

    // ── 1. 2D Matrix Linear Search ────────────────────
    static int[] searchMatrix(int[][] matrix, int target) {
        for (int r = 0; r < matrix.length; r++)
            for (int c = 0; c < matrix[0].length; c++)
                if (matrix[r][c] == target) return new int[]{r, c};
        return new int[]{-1, -1};
    }

    // ── 2. Sorted Matrix — O(n+m) Corner Search ───────
    static int[] sortedMatrixSearch(int[][] m, int target) {
        int r = 0, c = m[0].length - 1;
        while (r < m.length && c >= 0) {
            if (m[r][c] == target) return new int[]{r, c};
            else if (m[r][c] > target) c--;
            else r++;
        }
        return new int[]{-1, -1};
    }

    // ── 3. Linked List Search ─────────────────────────
    static class Node {
        int data; Node next;
        Node(int d) { data = d; }
    }

    static int searchLinkedList(Node head, int target) {
        int index = 0;
        Node curr = head;
        while (curr != null) {
            if (curr.data == target) return index;
            curr = curr.next; index++;
        }
        return -1;
    }

    // ── 4. Move-to-Front Self-Organizing Search ───────
    static int moveToFront(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                if (i != 0) { int tmp = arr[i]; arr[i] = arr[0]; arr[0] = tmp; }
                return 0;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        // 2D Matrix
        int[][] matrix = {{1,3,5},{7,9,11},{13,15,17}};
        System.out.println("Matrix search 9: " +
            java.util.Arrays.toString(searchMatrix(matrix, 9))); // [1, 1]

        // Sorted Matrix (O(n+m))
        System.out.println("Sorted matrix search 15: " +
            java.util.Arrays.toString(sortedMatrixSearch(matrix, 15))); // [2, 1]

        // Linked List
        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);
        System.out.println("Linked list search 20: index " + searchLinkedList(head, 20)); // 1

        // Move-to-Front
        int[] arr = {5, 3, 8, 1, 9};
        System.out.println("MTF search 8: index " + moveToFront(arr, 8)); // 0 (8 moved to front)
    }
}"""
        },

        "Advanced": {
            "definition": (
                "At the advanced level, linear search underpins more sophisticated algorithms. It appears in "
                "randomized search, parallel search, and as the base case in divide-and-conquer hybrids like "
                "TimSort and Introsort. Linear scan is used for finding the maximum subarray (Kadane's Algorithm), "
                "searching in rotated sorted arrays, and as the backbone of streaming algorithms where data cannot "
                "be stored and must be processed in a single pass."
            ),
            "working": (
                "KADANE'S ALGORITHM (Maximum Subarray) — Linear Scan:\n"
                "  Track currentSum and maxSum.\n"
                "  For each element:\n"
                "    currentSum = max(element, currentSum + element)\n"
                "    maxSum = max(maxSum, currentSum)\n"
                "  Single pass O(n) — uses linear search logic.\n\n"
                "SEARCH IN ROTATED SORTED ARRAY:\n"
                "  First, find the pivot (rotation point) using linear scan or binary search.\n"
                "  Then search in the correct half.\n"
                "  Linear scan finds pivot in O(n).\n\n"
                "STREAMING SEARCH (Boyer-Moore Majority Vote):\n"
                "  Find the majority element (appears > n/2 times) in one pass.\n"
                "  Maintain a candidate and count.\n"
                "  Increment count if same as candidate, else decrement.\n"
                "  When count hits 0, update candidate."
            ),
            "algorithm": (
                "KADANE'S — O(n):\n"
                "  maxSum = arr[0]; currSum = arr[0]\n"
                "  for i in 1..n-1:\n"
                "    currSum = max(arr[i], currSum + arr[i])\n"
                "    maxSum = max(maxSum, currSum)\n"
                "  return maxSum\n\n"
                "MAJORITY VOTE — O(n):\n"
                "  candidate = arr[0]; count = 1\n"
                "  for i in 1..n-1:\n"
                "    if arr[i] == candidate: count++\n"
                "    else if count == 0: candidate = arr[i]; count = 1\n"
                "    else: count--\n"
                "  return candidate"
            ),
            "time_complexity": {
                "Kadane's Algorithm": "O(n) — single pass",
                "Boyer-Moore Majority Vote": "O(n) — single pass, O(1) space",
                "Find Pivot (rotated array)": "O(n) linear scan",
                "Streaming Search": "O(n) — one pass, cannot revisit elements",
                "Parallel Linear Search": "O(n/p) — p processors"
            },
            "space_complexity": "O(1) for Kadane's and Boyer-Moore. O(n) for parallel variants.",
            "applications": (
                "• Kadane's Algorithm (Maximum Subarray Sum — LeetCode 53)\n"
                "• Boyer-Moore Majority Vote (Majority Element — LeetCode 169)\n"
                "• Finding pivot in rotated array\n"
                "• Streaming data processing (single pass analytics)\n"
                "• Finding first bad version (linear fallback)\n"
                "• Subroutine in TimSort (galloping mode)"
            ),
            "advantages": (
                "• Kadane's solves a seemingly hard problem in O(n) with one pass\n"
                "• Boyer-Moore uses only O(1) space — ideal for streaming\n"
                "• Linear scan is cache-friendly — predictable memory access pattern\n"
                "• No preprocessing required — works on raw unsorted streams"
            ),
            "disadvantages": (
                "• Cannot beat O(n) for unsorted data — fundamental lower bound\n"
                "• Streaming algorithms may require a second pass to verify\n"
                "• Parallel linear search requires coordination overhead\n"
                "• Cannot exploit sorted structure — use binary search instead"
            ),
            "interview_notes": (
                "★ Kadane's Algorithm (LeetCode 53) — must know; explain max(nums[i], currSum+nums[i]).\n"
                "★ Maximum Product Subarray (LeetCode 152) — Kadane's variant with min/max tracking.\n"
                "★ Majority Element (LeetCode 169) — Boyer-Moore, O(n) time O(1) space.\n"
                "★ Find Minimum in Rotated Sorted Array — linear O(n) or binary O(log n).\n"
                "★ Single Number (LeetCode 136) — XOR trick is a linear scan pattern.\n"
                "★ Best Time to Buy and Sell Stock — O(n) single pass tracking min price."
            ),
            "java": """\
public class AdvancedLinearSearch {

    // ── 1. Kadane's Algorithm — Max Subarray ─────────
    static int maxSubarray(int[] arr) {
        int maxSum = arr[0], currSum = arr[0];
        for (int i = 1; i < arr.length; i++) {
            currSum = Math.max(arr[i], currSum + arr[i]);
            maxSum = Math.max(maxSum, currSum);
        }
        return maxSum;
    }

    // ── 2. Boyer-Moore Majority Vote ─────────────────
    static int majorityElement(int[] nums) {
        int candidate = nums[0], count = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == candidate) count++;
            else if (count == 0) { candidate = nums[i]; count = 1; }
            else count--;
        }
        return candidate;
    }

    // ── 3. Best Time to Buy and Sell Stock ────────────
    static int maxProfit(int[] prices) {
        int minPrice = prices[0], maxProfit = 0;
        for (int price : prices) {
            minPrice = Math.min(minPrice, price);
            maxProfit = Math.max(maxProfit, price - minPrice);
        }
        return maxProfit;
    }

    // ── 4. Find Pivot in Rotated Sorted Array ────────
    static int findPivot(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++)
            if (arr[i] > arr[i + 1]) return i;
        return -1;
    }

    // ── 5. Maximum Product Subarray ───────────────────
    static int maxProduct(int[] nums) {
        int maxProd = nums[0], minProd = nums[0], result = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int temp = maxProd;
            maxProd = Math.max(nums[i], Math.max(maxProd * nums[i], minProd * nums[i]));
            minProd = Math.min(nums[i], Math.min(temp * nums[i], minProd * nums[i]));
            result = Math.max(result, maxProd);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println("Max Subarray: " + maxSubarray(new int[]{-2,1,-3,4,-1,2,1,-5,4})); // 6
        System.out.println("Majority Element: " + majorityElement(new int[]{2,2,1,1,1,2,2})); // 2
        System.out.println("Max Profit: " + maxProfit(new int[]{7,1,5,3,6,4})); // 5
        System.out.println("Pivot Index: " + findPivot(new int[]{4,5,6,7,0,1,2})); // 3
        System.out.println("Max Product: " + maxProduct(new int[]{2,3,-2,4})); // 6
    }
}"""
        }
    },

    # ==================== ARRAYS ====================
    "Arrays": {
        "Beginner": {
            "definition": (
                "An Array is a collection of items stored at contiguous memory locations. It is the most "
                "fundamental and widely used data structure in computer science. The main idea is to store "
                "multiple items of the same type together, making it easy to calculate the position of each "
                "element by simply adding an offset to a base value. Think of it like a row of lockers where "
                "each locker has a unique number (index) and stores one item."
            ),
            "working": (
                "1. CONTIGUOUS MEMORY: Elements are placed one after another in memory.\n"
                "2. INDEXING: Elements are accessed via an index (usually 0 to n-1).\n"
                "3. RANDOM ACCESS: Any element can be reached in O(1) time if the index is known.\n"
                "4. FIXED SIZE: Traditional arrays have a static size determined at creation time.\n\n"
                "Example walkthrough:\n"
                "  Array: [10, 20, 30, 40]\n"
                "  Index:  0   1   2   3\n"
                "  Accessing index 2 returns 30."
            ),
            "algorithm": (
                "ACCESS(arr, i):\n"
                "  return arr[i] // O(1) time\n\n"
                "SEARCH(arr, x):\n"
                "  for i from 0 to n-1:\n"
                "    if arr[i] == x return i\n"
                "  return -1 // O(n) time\n\n"
                "TRAVERSE(arr):\n"
                "  for i from 0 to n-1:\n"
                "    print arr[i]"
            ),
            "time_complexity": {
                "Access": "O(1) — constant time",
                "Search": "O(n) — linear scan",
                "Insertion": "O(n) — must shift elements",
                "Deletion": "O(n) — must shift elements",
                "Update": "O(1) — if index known"
            },
            "space_complexity": "O(n) — where n is the number of elements in the array.",
            "applications": (
                "• Storing lists of similar items\n"
                "• Building block for Stacks, Queues, and Heaps\n"
                "• Mathematical matrices and tables\n"
                "• Lookup tables and cache storage\n"
                "• Digital image processing (2D pixel arrays)"
            ),
            "advantages": (
                "• Extremely fast access of elements via index\n"
                "• Memory efficient — no overhead for pointers or metadata\n"
                "• High cache locality — contiguous memory is CPU-friendly\n"
                "• Simple and easy to implement"
            ),
            "disadvantages": (
                "• Fixed size limits flexibility (static arrays)\n"
                "• Costly insertions and deletions (shifting elements)\n"
                "• Can waste memory if declared larger than needed\n"
                "• Requires a large contiguous block of memory"
            ),
            "interview_notes": (
                "★ Always check for 'ArrayIndexOutOfBounds' exceptions.\n"
                "★ Know the difference between static arrays and dynamic arrays (ArrayList).\n"
                "★ Practice basic operations: reverse an array, find second largest.\n"
                "★ Arrays are the starting point for most coding interviews."
            ),
            "java": """\
import java.util.Arrays;

public class ArrayDemo {
    public static void main(String[] args) {
        // Declaration and Initialization
        int[] arr = {10, 20, 30, 40, 50};

        // Access via index
        System.out.println("Element at index 2: " + arr[2]);

        // Traverse using loop
        System.out.println("Array elements:");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        // Arrays utility class
        Arrays.sort(arr);
        System.out.println("Sorted: " + Arrays.toString(arr));
    }
}"""
        },
        "Intermediate": {
            "definition": (
                "At the intermediate level, we move beyond 1D arrays to 2D matrices and advanced patterns "
                "like Prefix Sums and Two-Pointer techniques. A matrix is essentially an 'array of arrays' "
                "used to represent grids, images, and graph adjacency lists. Prefix Sums involve pre-calculating "
                "cumulative totals to answer range queries in constant time."
            ),
            "working": (
                "2D ARRAYS (MATRICES):\n"
                "  Stored in Row-Major or Column-Major order in memory.\n"
                "  Accessed as arr[row][col].\n\n"
                "PREFIX SUMS:\n"
                "  P[i] = arr[0] + arr[1] + ... + arr[i].\n"
                "  Sum of range [L, R] = P[R] - P[L-1].\n\n"
                "TWO POINTERS:\n"
                "  Useful for sorted arrays (e.g., finding a pair that sums to a target).\n"
                "  One pointer at 'left', one at 'right', moving towards each other."
            ),
            "algorithm": (
                "PREFIX SUM PRECOMPUTATION:\n"
                "  P[0] = arr[0]\n"
                "  for i from 1 to n-1:\n"
                "    P[i] = P[i-1] + arr[i]\n\n"
                "TWO POINTER SUM CHECK:\n"
                "  while left < right:\n"
                "    current_sum = arr[left] + arr[right]\n"
                "    if current_sum == target return true\n"
                "    if current_sum < target left++\n"
                "    else right--"
            ),
            "time_complexity": {
                "Prefix Sum Precompute": "O(n)",
                "Range Sum Query": "O(1)",
                "Two Pointer Search": "O(n)",
                "2D Transpose": "O(rows * cols)",
                "Matrix Search (sorted)": "O(log(rows*cols))"
            },
            "space_complexity": "O(n) for prefix array; O(1) extra space for two-pointer approach.",
            "applications": (
                "• Financial data analysis (moving averages)\n"
                "• Image filtering and convolution matrices\n"
                "• Dynamic Programming (using 1D or 2D arrays)\n"
                "• Solving linear equations\n"
                "• Competitive programming range queries"
            ),
            "advantages": (
                "• Prefix sums reduce O(n) queries to O(1)\n"
                "• Two-pointer avoids O(n²) nested loops\n"
                "• Matrices naturally model spatial data (grids, maps)"
            ),
            "disadvantages": (
                "• Extra space needed for prefix arrays\n"
                "• Two-pointer only works effectively on sorted data\n"
                "• Large matrices consume significant memory"
            ),
            "interview_notes": (
                "★ Range Sum Query (LeetCode 303) is a classic prefix sum problem.\n"
                "★ Container with Most Water (LeetCode 11) is solved using two-pointers.\n"
                "★ Rotate Matrix (90 degrees) is a common high-frequencey interview task.\n"
                "★ Practice row-wise vs column-wise traversal of a matrix."
            ),
            "java": """\
public class IntermediateArray {
    // 1. Prefix Sum Example
    public static int[] buildPrefixSum(int[] arr) {
        int[] p = new int[arr.length];
        p[0] = arr[0];
        for (int i = 1; i < arr.length; i++) p[i] = p[i-1] + arr[i];
        return p;
    }

    // 2. TwoSum (Sorted) using Two Pointers
    public static boolean hasPairs(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int sum = arr[left] + arr[right];
            if (sum == target) return true;
            if (sum < target) left++;
            else right--;
        }
        return false;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 4, 7, 11};
        System.out.println("Pair exists? " + hasPairs(arr, 9)); // true (2+7)
    }
}"""
        },
        "Advanced": {
            "definition": (
                "Advanced array topics cover complex algorithms like Kadane's for maximum subarray sum, "
                "Sliding Window patterns for subarray constraints, and Dutch National Flag for partitioning. "
                "These techniques often transform O(n²) or O(n³) brute-force solutions into elegant O(n) "
                "linear scans by leveraging clever indexing and state management."
            ),
            "working": (
                "KADANE'S ALGORITHM:\n"
                "  Tracks the maximum subarray sum ending at each index.\n"
                "  At each step, decide: start fresh at current item or extend previous sum.\n\n"
                "SLIDING WINDOW (Dynamic Size):\n"
                "  Expand 'right' pointer until condition is met.\n"
                "  Shrink 'left' pointer to find the minimal/maximal valid window.\n\n"
                "DUTCH NATIONAL FLAG:\n"
                "  Uses three pointers (low, mid, high) to partition an array into three groups "
                "  (e.g., 0s, 1s, and 2s) in a single pass."
            ),
            "algorithm": (
                "KADANE'S MAX SUBARRAY:\n"
                "  max_so_far = -inf; current_max = 0\n"
                "  for x in arr:\n"
                "    current_max = max(x, current_max + x)\n"
                "    max_so_far = max(max_so_far, current_max)\n"
                "  return max_so_far\n\n"
                "DUTCH NATIONAL FLAG:\n"
                "  while mid <= high:\n"
                "    if arr[mid] == 0: swap(low, mid); low++; mid++\n"
                "    if arr[mid] == 1: mid++\n"
                "    if arr[mid] == 2: swap(mid, high); high--"
            ),
            "time_complexity": {
                "Kadane's Sum": "O(n)",
                "Sliding Window (avg)": "O(n)",
                "Dutch National Flag": "O(n)",
                "3Sum (Sorted)": "O(n²)",
                "Trapping Rainwater": "O(n)"
            },
            "space_complexity": "O(1) extra space for these algorithms, making them highly optimized.",
            "applications": (
                "• Stock market profit analysis (Kadane's variant)\n"
                "• Network packet windowing and congestion control\n"
                "• Large-scale log analysis and data cleaning\n"
                "• Resource allocation and scheduling\n"
                "• Terrain modeling (water trapping)"
            ),
            "advantages": (
                "• Linear O(n) performance is the best possible for array processing\n"
                "• Minimal memory footprint (O(1) space)\n"
                "• Robustness across various dataset sizes"
            ),
            "disadvantages": (
                "• Logic can be counter-intuitive compared to nested loops\n"
                "• Harder to debug due to transient state\n"
                "• Specific to certain problem patterns"
            ),
            "interview_notes": (
                "★ Kadane's (LeetCode 53) is one of the most famous array interview questions.\n"
                "★ Trapping Rain Water (LeetCode 42) — master the O(n) two-pointer approach.\n"
                "★ Sort Colors (LeetCode 75) uses the Dutch National Flag algorithm.\n"
                "★ Sliding Window: always be clear on what variable or sum you are tracking."
            ),
            "java": """\
import java.util.*;

public class AdvancedArray {
    // Kadane's: Maximum Subarray Sum
    public static int maxSubArray(int[] nums) {
        int maxSoFar = nums[0], currentMax = nums[0];
        for (int i = 1; i < nums.length; i++) {
            currentMax = Math.max(nums[i], currentMax + nums[i]);
            maxSoFar = Math.max(maxSoFar, currentMax);
        }
        return maxSoFar;
    }

    // Dutch National Flag (Sort 0, 1, 2)
    public static void sortColors(int[] nums) {
        int lo = 0, mid = 0, hi = nums.length - 1;
        while (mid <= hi) {
            if (nums[mid] == 0) {
                int t = nums[lo]; nums[lo] = nums[mid]; nums[mid] = t;
                lo++; mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                int t = nums[mid]; nums[mid] = nums[hi]; nums[hi] = t;
                hi--;
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println("Max Subarray: " + maxSubArray(nums)); // 6
    }
}"""
        }
    },

    # ==================== STRINGS ====================
    "Strings": {
        "Beginner": {
            "definition": (
                "A String is a sequence of characters, typically used to represent text. In many programming "
                "languages like Java and Python, Strings are 'immutable' — once created, they cannot be "
                "modified. Instead, any modification creates a completely new string. Think of a string as "
                "an array of characters with special behaviors for text processing and manipulation."
            ),
            "working": (
                "1. CHARACTER ARRAY: Strings are stored internally as an array of chars (or bytes).\n"
                "2. IMMUTABILITY: Modifying a string creates a new instance (Java/Python).\n"
                "3. STRING POOL: Languages often use a special pool to save memory by sharing identical strings.\n"
                "4. CONCATENATION: Combining strings using '+' or builder classes.\n\n"
                "Example walkthrough:\n"
                "  String: 'DSA'\n"
                "  Memory: ['D', 'S', 'A']\n"
                "  s[1] = 'S'"
            ),
            "algorithm": (
                "LENGTH(s):\n"
                "  return the count of characters\n\n"
                "REVERSE(s):\n"
                "  swap s[i] and s[n-1-i] for i = 0 to n/2\n\n"
                "CONCAT(s1, s2):\n"
                "  create new string with enough space for both, then copy chars"
            ),
            "time_complexity": {
                "Access char": "O(1)",
                "Concatenation": "O(n + m) — reallocation + copy",
                "Reverse": "O(n)",
                "Comparison": "O(n) — must check each char",
                "Substring": "O(n) — in many modern languages"
            },
            "space_complexity": "O(n) — where n is the length of the string.",
            "applications": (
                "• User input handling (usernames, passwords)\n"
                "• Data transport (JSON, XML, CSV formats)\n"
                "• Web development (URLs, HTML content)\n"
                "• Text search and indexing\n"
                "• Natural Language Processing (NLP)"
            ),
            "advantages": (
                "• Easy to use and human-readable\n"
                "• Thread-safe due to immutability in many languages\n"
                "• Built-in rich library functions for trimming, splitting, etc."
            ),
            "disadvantages": (
                "• Memory intensive concat in loops (use StringBuilder!)\n"
                "• Immutability can lead to many temporary objects\n"
                "• Pattern matching can be slow without advanced algorithms"
            ),
            "interview_notes": (
                "★ Always mention immutability and the String Pool in Java interviews.\n"
                "★ Use StringBuilder or StringBuffer for frequent string modifications.\n"
                "★ Common task: reverse a string without using built-in library functions.\n"
                "★ Practice: Palindrome check (ignore case and non-alphanumeric)."
            ),
            "java": """\
public class StringDemo {
    public static void main(String[] args) {
        String s = "Hello DSA";

        // Access char
        System.out.println("Char at 6: " + s.charAt(6));

        // Substring
        System.out.println("Sub: " + s.substring(0, 5));

        // StringBuilder for modifications
        StringBuilder sb = new StringBuilder("Apple");
        sb.append(" Pie");
        System.out.println(sb.toString()); // Apple Pie

        // Palindrome check
        String p = "madam";
        String rev = new StringBuilder(p).reverse().toString();
        System.out.println("Is Polindrome? " + p.equals(rev));
    }
}"""
        },
        "Intermediate": {
            "definition": (
                "Intermediate string topics focus on pattern matching and sliding window techniques. "
                "Naive pattern matching (scanning for a substring inside a larger string) takes O(N * M) time. "
                "Sliding windows allow us to find the longest or shortest substring that meets specific "
                "criteria (like having unique characters) in O(N) linear time."
            ),
            "working": (
                "SLIDING WINDOW (Fixed vs Variable):\n"
                "  Maintains a range [left, right] over the string.\n"
                "  Uses a Frequency Map or Hash Set to track characters in the current window.\n\n"
                "PATTERN SEARCHING (Naive):\n"
                "  Align pattern to each index of text and check all chars.\n\n"
                "ANAGRAMS:\n"
                "  Two strings are anagrams if they have the same character counts."
            ),
            "algorithm": (
                "LONGEST SUBSTRING WITHOUT REPEATED CHARS:\n"
                "  while right < n:\n"
                "    if s[right] exists in window: shrink left\n"
                "    add s[right] to window; update max_len; right++\n\n"
                "ANAGRAM CHECK (O(N)):\n"
                "  count[26] = {0}\n"
                "  for char c in s1: count[c-'a']++\n"
                "  for char c in s2: count[c-'a']--\n"
                "  check if all counts are zero"
            ),
            "time_complexity": {
                "Anagram Check": "O(N)",
                "Sliding Window Substring": "O(N)",
                "Naive Search": "O(N * M)",
                "Regex (simple)": "O(N)",
                "String to Integer": "O(N)"
            },
            "space_complexity": "O(1) for fixed alphabet sets; O(N) for string-based maps.",
            "applications": (
                "• Password strength checking and validation\n"
                "• Finding similarities between documents\n"
                "• Spell checking and autocomplete foundations\n"
                "• Data parsing from logs or unstructured text\n"
                "• Network packet header inspection"
            ),
            "advantages": (
                "• Sliding window provides massive speedup over brute-force O(N²)\n"
                "• Hash-based methods give reliable constant-time character tracking"
            ),
            "disadvantages": (
                "• Handling multi-byte characters (Unicode) adds complexity\n"
                "• Large windows in sliding window can consume memory"
            ),
            "interview_notes": (
                "★ Longest Substring Without Repeating Characters (LeetCode 3) is a top-tier question.\n"
                "★ Valid Anagram (LeetCode 242) — explain why sorting is O(N log N) vs counting O(N).\n"
                "★ Group Anagrams (LeetCode 49) — use a sorted string or frequency map as key.\n"
                "★ Be comfortable converting between char and ASCII/Unicode values."
            ),
            "java": """\
import java.util.*;

public class IntermediateString {
    // Slinding Window: Longest Unique Substring
    public static int lengthOfLongestSubstring(String s) {
        int n = s.length(), res = 0;
        Map<Character, Integer> map = new HashMap<>(); 
        for (int j = 0, i = 0; j < n; j++) {
            if (map.containsKey(s.charAt(j))) i = Math.max(map.get(s.charAt(j)), i);
            res = Math.max(res, j - i + 1);
            map.put(s.charAt(j), j + 1);
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("abcabcbb")); // 3
    }
}"""
        },
        "Advanced": {
            "definition": (
                "Advanced string processing involves powerful algorithms like KMP (Knuth-Morris-Pratt), "
                "Z-Algorithm, and data structures like Tries and Suffix Trees. These enable O(N) searching "
                "and complex prefix/suffix operations. KMP uses a 'Longest Prefix Suffix' (LPS) array to "
                "avoid redundant comparisons, while Tries allow for extremely fast dictionary lookups and "
                "autocomplete features."
            ),
            "working": (
                "KMP ALGORITHM:\n"
                "  Precomputes LPS array. When mismatch occurs, it knows where to skip characters to avoid "
                "  re-checking chars already matched.\n\n"
                "TRIE (Prefix Tree):\n"
                "  Each node represents a character. Shared prefixes occupy the same path.\n"
                "  Search/Insert takes O(Length of word).\n\n"
                "EDIT DISTANCE (Dynamic Programming):\n"
                "  Computes the minimum operations (insert, delete, replace) to transform word1 to word2."
            ),
            "algorithm": (
                "KMP PATTERN SEARCH:\n"
                "  i = 0 (text), j = 0 (pattern)\n"
                "  while i < n:\n"
                "    if text[i] == pattern[j]: i++; j++\n"
                "    if j == m: return i - m; j = lps[j-1]\n"
                "    else if text[i] != pattern[j]:\n"
                "      if j != 0: j = lps[j-1]\n"
                "      else: i++"
            ),
            "time_complexity": {
                "KMP Search": "O(N + M)",
                "Z-Algorithm": "O(N + M)",
                "Trie Search": "O(L) where L = word length",
                "Edit Distance": "O(N * M)",
                "Manacher's (Longest Palindrome)": "O(N)"
            },
            "space_complexity": "O(M) for KMP LPS; O(Alphabet * WordCount * AvgLength) for Tries.",
            "applications": (
                "• Genome sequencing and DNA pattern matching\n"
                "• Google autocomplete and search suggestions\n"
                "• Document differencing (git diff, Unix diff)\n"
                "• Plagiarism detectors\n"
                "• Intelligent spell checkers"
            ),
            "advantages": (
                "• KMP handles the worst-case text patterns efficiently\n"
                "• Tries provide near-ideal performance for dictionary operations\n"
                "• Advanced DP solves fuzzy matching and similarity problems"
            ),
            "disadvantages": (
                "• KMP/Z algorithms are complex to implement bug-free\n"
                "• Tries can be memory-hungry if many unique prefixes exist"
            ),
            "interview_notes": (
                "★ Implement 'strStr()' (LeetCode 28) — mention KMP for extra credit.\n"
                "★ Word Break (LeetCode 139) — solved with DP or Trie.\n"
                "★ Edit Distance (LeetCode 72) is a classic 'Hard' DP problem.\n"
                "★ Manacher's Algorithm is the O(N) holy grail for palindromic substrings."
            ),
            "java": """\
import java.util.*;

public class AdvancedString {
    // 1. KMP LSP Precomputation
    static int[] computeLPS(String pat) {
        int m = pat.length(), len = 0, i = 1;
        int[] lps = new int[m];
        while (i < m) {
            if (pat.charAt(i) == pat.charAt(len)) lps[i++] = ++len;
            else if (len != 0) len = lps[len-1];
            else lps[i++] = 0;
        }
        return lps;
    }

    // 2. Trie Implementation Skeleton
    static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd = false;
        void insert(String word) {
            TrieNode curr = this;
            for (char c : word.toCharArray()) {
                if (curr.children[c-'a'] == null) curr.children[c-'a'] = new TrieNode();
                curr = curr.children[c-'a'];
            }
            curr.isEnd = true;
        }
    }

    public static void main(String[] args) {
        String p = "ABABC";
        System.out.println("LPS: " + Arrays.toString(computeLPS(p))); // [0, 0, 1, 2, 0]
    }
}"""
        }
    },

    # ==================== LINKED LISTS ====================
    "Linked Lists": {
        "Beginner": {
            "definition": (
                "A Linked List is a linear data structure where elements (nodes) are not stored at contiguous "
                "memory locations. Instead, each node contains two parts: Data and a Pointer (next) to the "
                "next node in the sequence. Unlike arrays, linked lists can easily grow and shrink in size "
                "dynamically. Think of it like a scavenger hunt where each clue leads you to the location "
                "of the next clue."
            ),
            "working": (
                "1. NODES: The building blocks of the list.\n"
                "2. HEAD: A pointer to the first node. If Head is null, list is empty.\n"
                "3. NEXT: A pointer to the next node. The last node's next is null.\n"
                "4. DYNAMIC SIZE: No need to specify capacity beforehand.\n\n"
                "Example walkthrough:\n"
                "  Head -> [10 | *] -> [20 | *] -> [30 | null]\n"
                "  To add 40: create node, point 30's next to 40."
            ),
            "algorithm": (
                "TRAVERSAL:\n"
                "  curr = head\n"
                "  while curr is not null:\n"
                "    print curr.data; curr = curr.next\n\n"
                "INSERT AT FRONT:\n"
                "  newNode.next = head; head = newNode\n\n"
                "DELETE NODE (given node):\n"
                "  node.data = node.next.data; node.next = node.next.next"
            ),
            "time_complexity": {
                "Access char": "O(n) — must traverse from head",
                "Search": "O(n) — must check each node",
                "Insert at head": "O(1)",
                "Insert at tail": "O(n) — O(1) if tail pointer exists",
                "Delete at head": "O(1)"
            },
            "space_complexity": "O(n) — where n is the number of nodes.",
            "applications": (
                "• Implementation of Stacks and Queues\n"
                "• Undo/Redo functionality in applications\n"
                "• Dynamic memory allocation systems\n"
                "• Music playlists (Next/Previous tracks)\n"
                "• Chaining in Hash Tables"
            ),
            "advantages": (
                "• Dynamic size — grows and shrinks at runtime\n"
                "• Efficient insertion and deletion (no shifting needed)\n"
                "• No memory waste (no need to pre-allocate large blocks)"
            ),
            "disadvantages": (
                "• No random access — searching index 'i' takes O(i)\n"
                "• Extra memory for pointers (the 'next' reference)\n"
                "• Not cache-friendly (nodes scattered in memory)\n"
                "• Reversing a linked list is more complex than an array"
            ),
            "interview_notes": (
                "★ Always handle the 'Head == null' (empty list) corner case.\n"
                "★ Practice 'Reverse a Linked List' until you can do it in your sleep.\n"
                "★ Know the difference: Singly vs Doubly vs Circular lists.\n"
                "★ A 'Dummy Head' node can often simplify insertion/deletion logic."
            ),
            "java": """\
class Node {
    int data;
    Node next;
    Node(int d) { data = d; next = null; }
}

public class LinkedListDemo {
    public static void main(String[] args) {
        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);

        // Traverse
        Node curr = head;
        while (curr != null) {
            System.out.print(curr.data + " -> ");
            curr = curr.next;
        }
        System.out.println("null");
    }
}"""
        },
        "Intermediate": {
            "definition": (
                "Intermediate linked list patterns include the 'Two-Pointer' or 'Fast & Slow Pointer' "
                "technique (Tortoise and Hare), used for cycle detection and finding the middle of a list. "
                "We also explore Doubly Linked Lists (pointers to both next and prev nodes) and Circular "
                "Linked Lists (last node points back to the head), which allow bidirectional and circular "
                "traversal respectively."
            ),
            "working": (
                "FAST & SLOW POINTERS:\n"
                "  Two pointers starting at head. Slow moves 1 step, Fast moves 2 steps.\n"
                "  If they meet, a cycle exists. If Fast reaches null, no cycle.\n\n"
                "DOUBLY LINKED LIST (DLL):\n"
                "  Each node has 'next' AND 'prev'. Allows O(1) delete if node is known.\n\n"
                "CIRCULAR LIST:\n"
                "  Tail node's next points to Head node. Used for round-robin tasks."
            ),
            "algorithm": (
                "FIND MIDDLE OF LIST:\n"
                "  slow = fast = head\n"
                "  while fast and fast.next:\n"
                "    slow = slow.next; fast = fast.next.next\n"
                "  return slow\n\n"
                "REVERSE LIST (Iterative):\n"
                "  prev = null; curr = head\n"
                "  while curr:\n"
                "    nextTemp = curr.next; curr.next = prev\n"
                "    prev = curr; curr = nextTemp\n"
                "  return prev"
            ),
            "time_complexity": {
                "Cycle Detection": "O(n)",
                "Middle of List": "O(n)",
                "Reverse List": "O(n)",
                "DLL Insert/Delete": "O(1) if node known",
                "Merge Sorted Lists": "O(n+m)"
            },
            "space_complexity": "O(1) extra space for most pointer-based algorithms.",
            "applications": (
                "• LRU Cache (uses DLL + HashMap)\n"
                "• Browser history (Doubly Linked for Back/Forward)\n"
                "• CPU scheduling (Round-robin via Circular List)\n"
                "• Large number arithmetic (storing digits in nodes)\n"
                "• Blockchain (each block is a node in a chain)"
            ),
            "advantages": (
                "• DLL allows moving backwards comfortably\n"
                "• Fast/Slow pointer avoids needing extra memory (sets) for search\n"
                "• Circular lists model repetitive processes perfectly"
            ),
            "disadvantages": (
                "• DLL uses even more memory than SLD (two pointers per node)\n"
                "• Circular lists can lead to infinite loops if not handled carefully"
            ),
            "interview_notes": (
                "★ Linked List Cycle (LeetCode 141) — Floyd's Cycle-Finding Algorithm.\n"
                "★ Merge Two Sorted Lists (LeetCode 21) — use a dummy head node.\n"
                "★ Remove Nth Node From End (LeetCode 19) — use two pointers with a gap of N.\n"
                "★ Practice both Iterative and Recursive versions of list reversal."
            ),
            "java": """\
public class IntermediateList {
    static class Node { int val; Node next; Node(int v) {val=v;} }

    // Floyd's Cycle Finding
    public static boolean hasCycle(Node head) {
        Node slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }

    // Find Middle (Tortoise and Hare)
    public static Node getMiddle(Node head) {
        Node slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}"""
        },
        "Advanced": {
            "definition": (
                "Advanced linked list problems involve flattening multi-level lists, cloning lists with "
                "random pointers, and merging K sorted lists using Heaps. These problems often require a "
                "combination of linked lists with other data structures like HashMaps or Priority Queues "
                "to achieve optimal time complexities."
            ),
            "working": (
                "CLONE WITH RANDOM POINTERS:\n"
                "  Iterative: copy nodes and insert them between original nodes, adjust random pointers, "
                "  then separate the lists. Avoids extra O(N) space for map.\n\n"
                "MERGE K SORTED LISTS:\n"
                "  Use a Min-Heap (Priority Queue) to store the head of each list. Progressively "
                "  poll the min and add the next node from that specific list.\n\n"
                "FLATTEN A MULTI-LEVEL LIST:\n"
                "  Use recursion or a stack to process child pointers while maintaining the next sequence."
            ),
            "algorithm": (
                "MERGE K SORTED LISTS (Heap approach):\n"
                "  pq = MinHeap()\n"
                "  for head in K_lists: pq.add(head)\n"
                "  while pq not empty:\n"
                "    node = pq.poll()\n"
                "    tail.next = node; tail = node\n"
                "    if node.next: pq.add(node.next)"
            ),
            "time_complexity": {
                "Merge K Lists": "O(N log K)",
                "Clone with Random": "O(N)",
                "Flatten List": "O(N)",
                "Intersection of Lists": "O(N)",
                "Palindrome List": "O(N)"
            },
            "space_complexity": "O(K) for heap in Merge K; O(1) extra for optimized Clone/Intersection.",
            "applications": (
                "• Advanced memory management and garbage collection\n"
                "• Complex routing and multilevel data representations\n"
                "• Distributed key-value stores (consistent hashing chains)\n"
                "• High-performance task scheduling systems"
            ),
            "advantages": (
                "• Heap-based merge is significantly faster than pairwise merging\n"
                "• In-place cloning avoids the space overhead of hash tables"
            ),
            "disadvantages": (
                "• Logic for multi-pointer manipulation is highly error-prone\n"
                "• Complex pointer updates can be hard to visualize and debug"
            ),
            "interview_notes": (
                "★ Merge K Sorted Lists (LeetCode 23) is a classic Hard problem.\n"
                "★ Copy List with Random Pointer (LeetCode 138) — learn the interweaving trick.\n"
                "★ Palindrome Linked List (LeetCode 234) — find middle, reverse second half, compare.\n"
                "★ Intersection of Two Linked Lists (LeetCode 160) — use two pointers that swap heads."
            ),
            "java": """\
import java.util.*;

public class AdvancedList {
    static class Node { int val; Node next; Node(int v){val=v;} }

    // Merge K Sorted Lists - O(N log K)
    public Node mergeKLists(Node[] lists) {
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
        for (Node l : lists) if (l != null) pq.add(l);
        
        Node dummy = new Node(0), tail = dummy;
        while (!pq.isEmpty()) {
            tail.next = pq.poll();
            tail = tail.next;
            if (tail.next != null) pq.add(tail.next);
        }
        return dummy.next;
    }
}"""
        }
    },
    "Bubble Sort": {
        "Beginner": {
            "definition": (
                "Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the array, "
                "compares adjacent elements, and swaps them if they are in the wrong order. After each complete pass "
                "through the array, the largest unsorted element 'bubbles up' to its correct position at the end. "
                "The algorithm is named because smaller elements gradually 'bubble' toward the front like air "
                "bubbles rising in water."
            ),
            "working": (
                "1. Start with the first element (index 0).\n"
                "2. Compare arr[0] with arr[1]. If arr[0] > arr[1], swap them.\n"
                "3. Move to the next pair: compare arr[1] with arr[2]. Swap if needed.\n"
                "4. Continue until the end of the array — the largest element is now at the last position.\n"
                "5. Repeat the process for the remaining n-1 elements (the last is already sorted).\n"
                "6. After n-1 passes, the array is fully sorted.\n\n"
                "Example:\n"
                "  Initial:  [5, 3, 8, 4, 2]\n"
                "  Pass 1:   [3, 5, 4, 2, 8]  (8 bubbles to end)\n"
                "  Pass 2:   [3, 4, 2, 5, 8]  (5 bubbles to position)\n"
                "  Pass 3:   [3, 2, 4, 5, 8]\n"
                "  Pass 4:   [2, 3, 4, 5, 8]  ✓ Sorted"
            ),
            "algorithm": (
                "BUBBLE_SORT(arr, n):\n"
                "  for i from 0 to n-2:\n"
                "    for j from 0 to n-2-i:\n"
                "      if arr[j] > arr[j+1]:\n"
                "        swap(arr[j], arr[j+1])\n\n"
                "OPTIMIZED BUBBLE SORT:\n"
                "  for i from 0 to n-2:\n"
                "    swapped = false\n"
                "    for j from 0 to n-2-i:\n"
                "      if arr[j] > arr[j+1]:\n"
                "        swap(arr[j], arr[j+1])\n"
                "        swapped = true\n"
                "    if not swapped: break  // array is sorted early"
            ),
            "time_complexity": {
                "Best Case": "O(n) — with optimization flag; already sorted array",
                "Average Case": "O(n²) — random order",
                "Worst Case": "O(n²) — reverse sorted array",
                "Number of Comparisons": "n*(n-1)/2 in worst case",
                "Number of Swaps": "O(n²) worst case"
            },
            "space_complexity": "O(1) — in-place sorting, only a temporary variable for swapping.",
            "applications": (
                "• Educational tool for learning sorting concepts\n"
                "• Nearly sorted arrays (with optimization, approaches O(n))\n"
                "• Situations where simplicity is more important than performance\n"
                "• Detecting if an array is already sorted (optimized version exits in O(n))\n"
                "• Small datasets where O(n²) is acceptable"
            ),
            "advantages": (
                "• Extremely simple to understand and implement\n"
                "• In-place sort — no additional memory required\n"
                "• Stable sort — equal elements maintain their original order\n"
                "• Optimized version detects already-sorted arrays in O(n)\n"
                "• Easy to verify correctness manually"
            ),
            "disadvantages": (
                "• Very slow: O(n²) time complexity for average and worst cases\n"
                "• Not suitable for large datasets\n"
                "• Performs many unnecessary swaps even for nearly sorted data\n"
                "• Far outclassed by Merge Sort O(n log n) and Quick Sort O(n log n) avg"
            ),
            "interview_notes": (
                "★ Bubble Sort is stable — it preserves the relative order of equal elements.\n"
                "★ Optimization: add a 'swapped' flag — if no swap in a pass, array is sorted.\n"
                "★ After k passes, the last k elements are guaranteed to be sorted.\n"
                "★ Total comparisons in worst case: n*(n-1)/2.\n"
                "★ Know why Bubble Sort is rarely used in practice vs Merge/Quick Sort.\n"
                "★ Cocktail Shaker Sort is a bidirectional variant of Bubble Sort."
            ),
            "java": """\
import java.util.Arrays;

public class BubbleSortDemo {

    // Basic Bubble Sort
    static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    // Optimized Bubble Sort (early exit)
    static void optimizedBubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) {
                System.out.println("Sorted early at pass " + (i + 1));
                break;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr1 = {5, 3, 8, 4, 2};
        bubbleSort(arr1);
        System.out.println("Sorted: " + Arrays.toString(arr1));
        // → [2, 3, 4, 5, 8]

        int[] arr2 = {1, 2, 3, 5, 4}; // nearly sorted
        optimizedBubbleSort(arr2);
        System.out.println("Sorted: " + Arrays.toString(arr2));
        // → Sorted early at pass 1
        // → [1, 2, 3, 4, 5]
    }
}

/*
Trace for [5, 3, 8, 4, 2]:
Pass 1: [3, 5, 4, 2, 8] — 8 sorted
Pass 2: [3, 4, 2, 5, 8] — 5, 8 sorted
Pass 3: [3, 2, 4, 5, 8] — 4, 5, 8 sorted
Pass 4: [2, 3, 4, 5, 8] ✓ Done
*/"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we explore Bubble Sort's variants and comparisons with other O(n²) algorithms. "
                "Cocktail Shaker Sort (Bidirectional Bubble Sort) runs passes in both directions, reducing the number of "
                "passes needed. We also implement Bubble Sort for strings, custom objects, and linked lists. Understanding "
                "the stability property is key: Bubble Sort's stability makes it useful when the relative order of equal "
                "elements must be preserved."
            ),
            "working": (
                "COCKTAIL SHAKER SORT:\n"
                "  Forward pass: move largest to right end.\n"
                "  Backward pass: move smallest to left end.\n"
                "  Repeat, shrinking range from both sides.\n"
                "  Faster than bubble sort for certain distributions (turtles).\n\n"
                "STABILITY DEMONSTRATION:\n"
                "  Array of pairs: [(1,'B'), (1,'A'), (2,'C')]\n"
                "  Bubble Sort on key 1: keeps (1,'B') before (1,'A') if no swap needed.\n"
                "  This preserves original relative order — that's stability.\n\n"
                "SORTING STRINGS:\n"
                "  Compare strings using compareTo() in Java.\n"
                "  Alphabetical order: 'apple'.compareTo('banana') < 0 (apple comes first)."
            ),
            "algorithm": (
                "COCKTAIL SHAKER SORT:\n"
                "  left = 0; right = n-1\n"
                "  while left < right:\n"
                "    // Forward pass\n"
                "    for i from left to right-1:\n"
                "      if arr[i] > arr[i+1]: swap; last = i\n"
                "    right = last\n"
                "    // Backward pass\n"
                "    for i from right-1 down to left:\n"
                "      if arr[i] > arr[i+1]: swap; first = i\n"
                "    left = first + 1"
            ),
            "time_complexity": {
                "Cocktail Shaker Best": "O(n) — with early exit",
                "Cocktail Shaker Average": "O(n²)",
                "Cocktail Shaker Worst": "O(n²)",
                "String Bubble Sort": "O(n² × L) — L = average string length",
                "Stable Sort Verification": "O(n²) — same as base bubble sort"
            },
            "space_complexity": "O(1) for all variants — all are in-place.",
            "applications": (
                "• Sorting small arrays of objects where stability matters\n"
                "• Cocktail Shaker: datasets where small elements are at the end ('turtles')\n"
                "• Sorting strings alphabetically in simple scripts\n"
                "• Teaching the concept of stable sorting\n"
                "• Used in Tim Sort as a subroutine for small runs"
            ),
            "advantages": (
                "• Cocktail Shaker reduces passes for certain distributions\n"
                "• Stable sort preserves order of equal elements\n"
                "• Can sort any comparable data — strings, objects, custom types\n"
                "• Adaptive (optimized) version is fast on nearly sorted data"
            ),
            "disadvantages": (
                "• Still O(n²) — not practical for n > 10,000\n"
                "• Cocktail Shaker only a constant factor improvement\n"
                "• Many better stable alternatives: Merge Sort is O(n log n) and stable\n"
                "• String sorting with compareTo adds multiplicative L factor"
            ),
            "interview_notes": (
                "★ Why is Bubble Sort stable? — it only swaps when arr[j] > arr[j+1], never on equal.\n"
                "★ Cocktail Shaker fixes the 'turtle' problem — small elements at end move slowly in normal bubble sort.\n"
                "★ Compare Bubble, Selection, and Insertion sort: all O(n²), but Insertion Sort is fastest in practice.\n"
                "★ Merge Sort is O(n log n) and stable — preferred over Bubble Sort in practice.\n"
                "★ Java's Arrays.sort() uses TimSort (Merge + Insertion) for objects."
            ),
            "java": """\
import java.util.Arrays;

public class IntermediateBubbleSort {

    // ── 1. Cocktail Shaker Sort ───────────────────────
    static void cocktailSort(int[] arr) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int last = left;
            for (int i = left; i < right; i++) {
                if (arr[i] > arr[i + 1]) {
                    int tmp = arr[i]; arr[i] = arr[i+1]; arr[i+1] = tmp;
                    last = i;
                }
            }
            right = last;
            int first = right;
            for (int i = right - 1; i >= left; i--) {
                if (arr[i] > arr[i + 1]) {
                    int tmp = arr[i]; arr[i] = arr[i+1]; arr[i+1] = tmp;
                    first = i;
                }
            }
            left = first + 1;
        }
    }

    // ── 2. String Bubble Sort ─────────────────────────
    static void bubbleSortStrings(String[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j].compareTo(arr[j + 1]) > 0) {
                    String tmp = arr[j]; arr[j] = arr[j+1]; arr[j+1] = tmp;
                }
            }
        }
    }

    // ── 3. Stable Sort Demo with Objects ─────────────
    static class Student {
        String name; int grade;
        Student(String n, int g) { name = n; grade = g; }
        public String toString() { return name + "(" + grade + ")"; }
    }

    static void bubbleSortStudents(Student[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - 1 - i; j++) {
                if (arr[j].grade > arr[j+1].grade) {
                    Student tmp = arr[j]; arr[j] = arr[j+1]; arr[j+1] = tmp;
                }
            }
        }
    }

    public static void main(String[] args) {
        // Cocktail Sort
        int[] arr = {5, 1, 4, 2, 8, 0, 2};
        cocktailSort(arr);
        System.out.println("Cocktail Sorted: " + Arrays.toString(arr));

        // String Sort
        String[] words = {"banana", "apple", "cherry", "date"};
        bubbleSortStrings(words);
        System.out.println("String Sorted: " + Arrays.toString(words));

        // Stable sort demo
        Student[] students = {
            new Student("Alice", 85), new Student("Bob", 92),
            new Student("Charlie", 85), new Student("Diana", 78)
        };
        bubbleSortStudents(students);
        System.out.println("Students by grade: " + Arrays.toString(students));
        // Alice and Charlie both have 85 — original order preserved (stable)
    }
}"""
        },

        "Advanced": {
            "definition": (
                "At the advanced level, Bubble Sort serves as a baseline to understand sorting complexity theory. "
                "We explore how Bubble Sort relates to inversion counting: each swap reduces inversions by exactly 1, "
                "and the total number of swaps equals the number of inversions in the array. This connects sorting to "
                "lower bound theory — any comparison-based sort needs Ω(n log n) comparisons in the worst case. "
                "We also explore how modern hybrid sorts (TimSort, IntroSort) use insertion sort for small chunks "
                "instead of bubble sort, and why."
            ),
            "working": (
                "INVERSION COUNT CONNECTION:\n"
                "  An inversion is a pair (i,j) where i < j but arr[i] > arr[j].\n"
                "  Each bubble sort swap removes exactly 1 inversion.\n"
                "  Sorted array → 0 inversions.\n"
                "  Reverse sorted array → n*(n-1)/2 inversions (maximum).\n"
                "  Total swaps in bubble sort = number of inversions.\n\n"
                "WHY O(n²) IS A LOWER BOUND FOR BUBBLE SORT:\n"
                "  Bubble sort compares only adjacent elements.\n"
                "  To move an element from position n-1 to position 0: n-1 swaps minimum.\n"
                "  Merge Sort compares non-adjacent elements — solves multiple inversions per comparison.\n\n"
                "MERGE SORT vs BUBBLE SORT:\n"
                "  Merge Sort: O(n log n) — divides problem, each merge eliminates many inversions at once.\n"
                "  Bubble Sort: O(n²) — eliminates exactly 1 inversion per comparison (if swap occurs)."
            ),
            "algorithm": (
                "COUNT INVERSIONS USING MERGE SORT — O(n log n):\n"
                "  inversions = 0\n"
                "  MERGE_COUNT(arr, left, right):\n"
                "    if left >= right: return 0\n"
                "    mid = (left + right) / 2\n"
                "    inv = MERGE_COUNT(arr, left, mid)\n"
                "         + MERGE_COUNT(arr, mid+1, right)\n"
                "         + MERGE(arr, left, mid, right)\n"
                "  MERGE: whenever right-half element is taken before left-half, add remaining left elements count"
            ),
            "time_complexity": {
                "Bubble Sort": "O(n²) — eliminates 1 inversion per swap",
                "Count Inversions (brute)": "O(n²)",
                "Count Inversions (merge sort)": "O(n log n)",
                "Merge Sort": "O(n log n) — eliminates multiple inversions per merge",
                "Lower bound (comparison sort)": "Ω(n log n) — information theory proof"
            },
            "space_complexity": "Bubble Sort: O(1). Merge Sort: O(n) auxiliary for merging.",
            "applications": (
                "• Understanding inversion count — input for more complex algorithms\n"
                "• Measuring how 'unsorted' an array is (by counting inversions)\n"
                "• Theoretically grounding the case for O(n log n) sorting algorithms\n"
                "• Analyzing stability in sorting algorithms\n"
                "• Understanding TimSort's decision: insertion sort for n < 32 runs"
            ),
            "advantages": (
                "• Inversion count insight helps design adaptive algorithms\n"
                "• Perfect pedagogical tool to understand why O(n log n) is optimal\n"
                "• Leads to understanding TimSort and IntroSort design decisions\n"
                "• O(n) on already-sorted arrays with optimization (best adaptive behavior)"
            ),
            "disadvantages": (
                "• O(n²) makes it impractical for real-world large data\n"
                "• Merge Sort is always better for general sorting\n"
                "• Insertion Sort is faster than Bubble Sort in practice for small n\n"
                "• No situation in production where Bubble Sort is the right choice"
            ),
            "interview_notes": (
                "★ Count Inversions (GFG, LeetCode) — use merge sort to count in O(n log n).\n"
                "★ Why is Ω(n log n) the lower bound for comparison-based sorting? — decision tree argument.\n"
                "★ TimSort uses Insertion Sort for small runs (n < 32) — why not Bubble Sort? Insertion is faster.\n"
                "★ How many swaps does Bubble Sort make? — exactly the number of inversions.\n"
                "★ Patience Sorting connects to the Longest Increasing Subsequence.\n"
                "★ Know Merge Sort, Quick Sort, and Heap Sort at advanced level — these replace Bubble Sort."
            ),
            "java": """\
import java.util.Arrays;

public class AdvancedBubbleSort {

    // ── 1. Count Inversions via Merge Sort — O(n log n)
    static long countInversions(int[] arr) {
        return mergeCount(arr, 0, arr.length - 1);
    }

    static long mergeCount(int[] arr, int left, int right) {
        if (left >= right) return 0;
        int mid = (left + right) / 2;
        long inv = mergeCount(arr, left, mid) + mergeCount(arr, mid + 1, right);
        return inv + merge(arr, left, mid, right);
    }

    static long merge(int[] arr, int left, int mid, int right) {
        int[] tmp = new int[right - left + 1];
        int i = left, j = mid + 1, k = 0;
        long inv = 0;
        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) tmp[k++] = arr[i++];
            else {
                inv += (mid - i + 1); // all remaining left elements form inversions
                tmp[k++] = arr[j++];
            }
        }
        while (i <= mid) tmp[k++] = arr[i++];
        while (j <= right) tmp[k++] = arr[j++];
        System.arraycopy(tmp, 0, arr, left, tmp.length);
        return inv;
    }

    // ── 2. Compare: Bubble vs Insertion on same data ─
    static int[] bubbleSort(int[] arr) {
        int[] a = arr.clone(); int swaps = 0;
        for (int i = 0; i < a.length - 1; i++)
            for (int j = 0; j < a.length - 1 - i; j++)
                if (a[j] > a[j+1]) { int t=a[j]; a[j]=a[j+1]; a[j+1]=t; swaps++; }
        System.out.println("Bubble swaps: " + swaps);
        return a;
    }

    static int[] insertionSort(int[] arr) {
        int[] a = arr.clone(); int shifts = 0;
        for (int i = 1; i < a.length; i++) {
            int key = a[i], j = i - 1;
            while (j >= 0 && a[j] > key) { a[j+1] = a[j--]; shifts++; }
            a[j+1] = key;
        }
        System.out.println("Insertion shifts: " + shifts);
        return a;
    }

    // ── 3. Sort K-Sorted Array using Min-Heap ────────
    static int[] sortKSorted(int[] arr, int k) {
        // For nearly sorted arrays, Insertion Sort is also O(nk) — better than O(n²)
        // Here we use min-heap for O(n log k)
        java.util.PriorityQueue<Integer> pq = new java.util.PriorityQueue<>();
        int[] result = new int[arr.length];
        int ri = 0;
        for (int i = 0; i < arr.length; i++) {
            pq.offer(arr[i]);
            if (pq.size() > k) result[ri++] = pq.poll();
        }
        while (!pq.isEmpty()) result[ri++] = pq.poll();
        return result;
    }

    public static void main(String[] args) {
        int[] arr = {6, 3, 5, 2, 4, 1};

        System.out.println("Inversions: " + countInversions(arr.clone())); // 11

        System.out.println("--- Bubble Sort ---");
        bubbleSort(arr);
        System.out.println("--- Insertion Sort ---");
        insertionSort(arr);
        // Both have same number of swaps/shifts = number of inversions

        // K-Sorted Array
        int[] kArr = {3, 2, 1, 5, 4, 7, 6, 5};
        System.out.println("K-Sorted Result: " + Arrays.toString(sortKSorted(kArr, 3)));
    }
}"""
        }
    },

    # ==================== RECURSION ====================
    "Recursion": {
        "Beginner": {
            "definition": (
                "Recursion is a programming technique where a function calls itself, directly or indirectly, "
                "to solve a problem by breaking it down into smaller, similar sub-problems. Every recursive "
                "function must have a 'Base Case' to stop the execution and 'Recursive Steps' that lead "
                "towards that base case. It is fundamentally linked to the Stack data structure, as each call "
                "creates a new frame on the system's call stack."
            ),
            "working": (
                "1. BASE CASE: The condition that ends the recursion (stops the loop).\n"
                "2. RECURSIVE CALL: The function calling itself with a modified (usually smaller) input.\n"
                "3. CALL STACK: Each call is pushed onto the stack. When the base case hits, calls begin 'unwinding' and returning values.\n"
                "4. STACK OVERFLOW: Occurs if the recursion is too deep or missing a base case."
            ),
            "algorithm": (
                "FACTORIAL(n):\n"
                "  if n == 0 return 1\n"
                "  return n * FACTORIAL(n-1)\n\n"
                "FIBONACCI(n):\n"
                "  if n <= 1 return n\n"
                "  return FIBONACCI(n-1) + FIBONACCI(n-2)"
            ),
            "time_complexity": {
                "Factorial": "O(n)",
                "Fibonacci (naive)": "O(2^n) — exponential",
                "Binary Search (rec)": "O(log n)",
                "Tree Traversal": "O(n)",
                "DFS": "O(V + E)"
            },
            "space_complexity": "O(d) — where d is the maximum depth of the recursion (stack space).",
            "applications": (
                "• Mathematical computations (Factorials, Powers, Fibonacci)\n"
                "• Tree and Graph traversals (DFS, Preorder, Inorder)\n"
                "• Divide and Conquer algorithms (MergeSort, QuickSort)\n"
                "• Solving puzzles (Tower of Hanoi)\n"
                "• Dynamic Programming (Top-down approach with memoization)"
            ),
            "advantages": (
                "• Leads to clean, elegant, and readable code for complex problems\n"
                "• Naturally models hierarchical data (trees) and patterns\n"
                "• Easier to implement than iterative versions for some algorithms (like DFS)"
            ),
            "disadvantages": (
                "• Risk of StackOverflow if recursion depth is too high\n"
                "• Often carries more overhead (memory/time) than iterative loops\n"
                "• Can be hard to debug and visualize for beginners"
            ),
            "interview_notes": (
                "★ Always identify the Base Case first.\n"
                "★ Understand the difference between recursion and iteration.\n"
                "★ Mention Memoization to optimize exponential recursive problems like Fibonacci.\n"
                "★ Tail Recursion: explain how some compilers optimize calls to reuse stack frames."
            ),
            "java": """\
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
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, recursion is applied to divide-and-conquer problems and to "
                "understand the mechanics of Merge Sort, Quick Sort, and Binary Search through recursive "
                "decomposition. Recursion trees help visualize the call depth and total work done. We also "
                "study Tail Recursion — a special form where the recursive call is the last action in the "
                "function, enabling compiler optimization that reuses the current stack frame instead of "
                "creating a new one, reducing space complexity from O(n) to O(1)."
            ),
            "working": (
                "RECURSION TREE ANALYSIS:\n"
                "  Each call spawns sub-calls; the tree's height = recursion depth.\n"
                "  Total work = sum of work at each level.\n"
                "  For Merge Sort: T(n) = 2T(n/2) + O(n) → O(n log n) by Master Theorem.\n\n"
                "TAIL CALL OPTIMIZATION:\n"
                "  Regular: factorial(5) → 5 * factorial(4) → keeps frame alive waiting for return.\n"
                "  Tail: accumulaor-based factorial(5, 1) → factorial(4, 5) → frame reused.\n\n"
                "MUTUAL RECURSION:\n"
                "  isEven(n) calls isOdd(n-1) and vice versa — two functions calling each other."
            ),
            "algorithm": (
                "TAIL RECURSIVE FACTORIAL:\n"
                "  factorial(n, acc=1):\n"
                "    if n == 0: return acc\n"
                "    return factorial(n-1, n * acc)  // no operations after call\n\n"
                "MASTER THEOREM (simplified):\n"
                "  T(n) = aT(n/b) + f(n)\n"
                "  Case 1: f(n) = O(n^log_b(a) - ε) → T(n) = O(n^log_b(a))\n"
                "  Case 2: f(n) = O(n^log_b(a)) → T(n) = O(n^log_b(a) * log n)\n"
                "  Case 3: f(n) = Ω(n^log_b(a) + ε) → T(n) = O(f(n))"
            ),
            "time_complexity": {
                "Tail Recursive Factorial": "O(n) time, O(1) stack space",
                "Merge Sort Recurrence": "T(n) = 2T(n/2) + n → O(n log n)",
                "Binary Search Recurrence": "T(n) = T(n/2) + 1 → O(log n)",
                "Fibonacci (naive)": "T(n) = T(n-1) + T(n-2) → O(2^n)",
                "Fibonacci (memoized)": "O(n) — each subproblem solved once"
            },
            "space_complexity": "O(1) for tail-recursive with TCO; O(n) for standard recursion stack.",
            "applications": (
                "• Sorting algorithms (Merge Sort, Quick Sort)\n"
                "• Binary Search trees (insert, delete, search)\n"
                "• Power computation x^n using fast exponentiation\n"
                "• GCD using Euclidean algorithm\n"
                "• Tower of Hanoi"
            ),
            "advantages": (
                "• Tail call optimization eliminates stack overflow risk\n"
                "• Master theorem provides instant complexity analysis\n"
                "• Clean expression of divide-and-conquer"
            ),
            "disadvantages": (
                "• Java does not automatically apply TCO (unlike Scala/Haskell)\n"
                "• Mutual recursion can be confusing to trace\n"
                "• Function call overhead remains even with TCO in some runtimes"
            ),
            "interview_notes": (
                "★ Power Function (LeetCode 50) — fast exponentiation using recursion in O(log n).\n"
                "★ Be ready to apply Master Theorem to analyze T(n) = 2T(n/2) + n.\n"
                "★ Tail recursion is a talking point for functional language interviews.\n"
                "★ Flatten Nested List Iterator — elegant recursive solution."
            ),
            "java": """\
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
        },

        "Advanced": {
            "definition": (
                "At the advanced level, recursion is the backbone of complex combinatorial enumeration, "
                "tree DP, and graph DFS. We explore how the call stack maps directly to DFS traversal, how "
                "memoized recursion bridges to bottom-up DP, and how the 'return type trick' accumulates "
                "state during tree traversals. We also study stack-overflow-safe recursion using trampolining "
                "or explicit stack simulation — converting recursive algorithms to iterative ones to handle "
                "extremely deep inputs."
            ),
            "working": (
                "TRAMPOLINING:\n"
                "  Replace recursive call with a thunk (lazy function).\n"
                "  Driver loop calls thunks until a non-thunk value is returned.\n"
                "  Avoids growing the call stack — used for very deep recursions.\n\n"
                "TREE DP WITH RETURN TRICKS:\n"
                "  Each recursive call returns a pair (height, isDiameterUpdated).\n"
                "  Diameter of tree = max(leftHeight + rightHeight) seen across all nodes.\n\n"
                "CONVERTING RECURSION TO ITERATIVE DFS:\n"
                "  Push (node, state) pairs onto an explicit stack.\n"
                "  Pop and process until stack is empty."
            ),
            "algorithm": (
                "DIAMETER OF BINARY TREE — O(n):\n"
                "  height(node):\n"
                "    if null: return 0\n"
                "    left = height(node.left)\n"
                "    right = height(node.right)\n"
                "    diameter = max(diameter, left + right)  // update global\n"
                "    return 1 + max(left, right)\n\n"
                "FLATTEN BST TO LINKED LIST — in-place:\n"
                "  Use Morris Inorder Traversal (no extra space)\n"
                "  Temporarily modify tree to follow threads"
            ),
            "time_complexity": {
                "Tree Diameter (recursion)": "O(n)",
                "LCA of Binary Tree": "O(n)",
                "Serialize / Deserialize Tree": "O(n)",
                "Flatten Binary Tree": "O(n)",
                "All Paths Root to Leaf": "O(n * h)"
            },
            "space_complexity": "O(h) for recursive tree algorithms where h = height. O(1) for Morris traversal.",
            "applications": (
                "• Tree DP (diameter, views, path sums)\n"
                "• Parsing nested expressions (compilers)\n"
                "• Divide-and-conquer algorithms (Karatsuba multiplication)\n"
                "• Recursive descent parsers\n"
                "• DFS-based graph cycle detection"
            ),
            "advantages": (
                "• Most tree problems become elegant with recursion\n"
                "• Recursion maps naturally to inductive proofs\n"
                "• Memoized recursion gives correct DP without manual table construction"
            ),
            "disadvantages": (
                "• Stack depth limits recursion to ~10,000 levels in Java by default\n"
                "• Converting to iterative requires manual state management\n"
                "• Hard to debug recursive bugs in very deep call stacks"
            ),
            "interview_notes": (
                "★ Diameter of Binary Tree (LeetCode 543) — return height, track diameter globally.\n"
                "★ Binary Tree Maximum Path Sum (LeetCode 124) — Hard, uses the same return trick.\n"
                "★ Flatten Binary Tree to Linked List (LeetCode 114) — in-place with O(1) space.\n"
                "★ Be ready to convert any recursive DFS to iterative using an explicit stack."
            ),
            "java": """\
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
        }
    },

    # ==================== BACKTRACKING ====================
    "Backtracking": {
        "Beginner": {
            "definition": (
                "Backtracking is an algorithmic technique for solving problems recursively by trying to build "
                "a solution incrementally, one piece at a time, and removing those solutions that fail to "
                "satisfy the constraints of the problem at any point in time. It is effectively a brute-force "
                "approach that is optimized by 'pruning' search paths that clearly cannot lead to a valid "
                "solution. Think of it like exploring a maze: if you hit a dead end, you go back to the last "
                "junction and try a different path."
            ),
            "working": (
                "1. CHOICE: What part of the solution to build next (e.g., place a Queen or a number).\n"
                "2. CONSTRAINTS: Check if the current choice is valid according to problem rules.\n"
                "3. GOAL: Check if the complete solution is found (e.g., all Queens placed).\n"
                "4. BACKTRACK: If a choice leads to failure, undo the choice (reset state) and try the next possibility."
            ),
            "algorithm": (
                "BACKTRACK(state):\n"
                "  if state is GOAL: return success\n"
                "  for choice in possible_choices:\n"
                "    if choice is VALID:\n"
                "      MAKE_CHOICE(choice)\n"
                "      if BACKTRACK(state) is success: return success\n"
                "      UNDO_CHOICE(choice) // The 'Backtrack' step\n"
                "  return failure"
            ),
            "time_complexity": {
                "Permutations": "O(n!)",
                "Subsets": "O(2^n)",
                "N-Queens": "O(n!)",
                "Sudoku Solver": "O(9^(n*n))",
                "Maze Path": "O(4^(n*m))"
            },
            "space_complexity": "O(depth) — usually O(n) for the recursion stack.",
            "applications": (
                "• Solving puzzles like Sudoku, Crosswords, and N-Queens\n"
                "• Combinatorial problems (Generating Permutations and Subsets)\n"
                "• Graph problems (Finding Hamiltonian paths, M-Coloring)\n"
                "• Maze solving and Pathfinding in games\n"
                "• Resource allocation constraints"
            ),
            "advantages": (
                "• Guarantees finding all possible solutions (if exploring the whole space)\n"
                "• Simple recursive structure that is easy to extend with new constraints\n"
                "• More efficient than simple brute-force via intelligent pruning"
            ),
            "disadvantages": (
                "• Can be extremely slow for large inputs due to exponential complexity\n"
                "• High memory usage for deep recursion trees\n"
                "• Pruning logic can be complex to identify"
            ),
            "interview_notes": (
                "★ The most critical part of backtracking is the 'Undo Choice' step.\n"
                "★ Use a 'Visited' set or boolean array to track choices in graphs or permutations.\n"
                "★ Practice Permutations (LeetCode 46) and Subsets (LeetCode 78).\n"
                "★ Pruning optimization: if you can prove a branch fails early, skip it immediately."
            ),
            "java": """\
import java.util.*;

public class BacktrackingDemo {
    // Generate all Permutations
    public static void permute(int[] nums, List<Integer> curr, boolean[] used) {
        if (curr.size() == nums.length) {
            System.out.println(curr);
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            curr.add(nums[i]);
            permute(nums, curr, used);
            curr.remove(curr.size() - 1); // Backtrack
            used[i] = false;              // Backtrack
        }
    }

    public static void main(String[] args) {
        permute(new int[]{1, 2, 3}, new ArrayList<>(), new boolean[3]);
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we apply backtracking to generate all permutations, combinations, "
                "and subsets of a given set. These are the building blocks of most combinatorial search "
                "problems. We categorize backtracking problems into three types: Subset problems (pick or skip), "
                "Permutation problems (use each element once in different orders), and Combination Sum problems "
                "(find all combinations that sum to a target). Understanding when to use a 'startIndex' to "
                "avoid duplicates vs. a 'used[]' array is crucial."
            ),
            "working": (
                "SUBSETS (Power Set):\n"
                "  At each index, choose to include or exclude the element.\n"
                "  Result: 2^n subsets.\n\n"
                "COMBINATION SUM:\n"
                "  Same element can be repeated — don't increment start index on recursion.\n"
                "  Prune: if remaining < 0, backtrack immediately.\n\n"
                "PERMUTATIONS (with 'used' array):\n"
                "  Mark element as used before recursing; unmark after returning.\n"
                "  Result: n! permutations."
            ),
            "algorithm": (
                "SUBSETS:\n"
                "  backtrack(start, current):\n"
                "    result.add(current.copy())\n"
                "    for i from start to n-1:\n"
                "      current.add(nums[i]); backtrack(i+1, current); current.removeLast()\n\n"
                "COMBINATION SUM:\n"
                "  backtrack(start, remaining, path):\n"
                "    if remaining == 0: result.add(path.copy()); return\n"
                "    for i from start to n-1:\n"
                "      if candidates[i] > remaining: break  // pruning\n"
                "      path.add(candidates[i]); backtrack(i, remaining - candidates[i], path); path.removeLast()"
            ),
            "time_complexity": {
                "Subsets": "O(2^n) — two choices per element",
                "Permutations": "O(n!) — all orderings",
                "Combinations": "O(C(n,k)) — n choose k",
                "Combination Sum": "O(2^target) — bounded by pruning",
                "Letter Combos (Phone)": "O(4^n) — 4 letters per digit"
            },
            "space_complexity": "O(n) for the recursion stack and current path; O(2^n * n) for storing all results.",
            "applications": (
                "• Generating all possible passwords or PIN combinations\n"
                "• Scheduling and assignment problems (assign jobs to workers)\n"
                "• Combinatorics in statistics and probability\n"
                "• Feature selection in machine learning\n"
                "• Generating test cases for software testing"
            ),
            "advantages": (
                "• Elegant: one framework handles subsets, permutations, and combinations\n"
                "• Pruning avoids exploring invalid branches early\n"
                "• Easy to add new constraints without restructuring"
            ),
            "disadvantages": (
                "• Still exponential — only feasible for n <= 20-25\n"
                "• Difficult to handle duplicate elements correctly (requires careful sorting + skipping)\n"
                "• Hard to estimate running time without analyzing the search tree"
            ),
            "interview_notes": (
                "★ Subsets (LeetCode 78) and Subsets II (contains duplicates — sort + skip).\n"
                "★ Combination Sum (LeetCode 39) — allow reuse; Combination Sum II — no reuse.\n"
                "★ Letter Combinations of a Phone Number (LeetCode 17) — classic backtracking.\n"
                "★ Always sort the array first when duplicates can appear in input."
            ),
            "java": """\
import java.util.*;

public class IntermediateBacktracking {

    // 1. Generate all Subsets
    static List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrackSubsets(nums, 0, new ArrayList<>(), res);
        return res;
    }
    static void backtrackSubsets(int[] nums, int start, List<Integer> path, List<List<Integer>> res) {
        res.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrackSubsets(nums, i + 1, path, res);
            path.remove(path.size() - 1);
        }
    }

    // 2. Combination Sum (unlimited reuse)
    static List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> res = new ArrayList<>();
        backtrackCombSum(candidates, 0, target, new ArrayList<>(), res);
        return res;
    }
    static void backtrackCombSum(int[] cands, int start, int rem, List<Integer> path, List<List<Integer>> res) {
        if (rem == 0) { res.add(new ArrayList<>(path)); return; }
        for (int i = start; i < cands.length; i++) {
            if (cands[i] > rem) break; // pruning
            path.add(cands[i]);
            backtrackCombSum(cands, i, rem - cands[i], path, res); // i, not i+1 (reuse allowed)
            path.remove(path.size() - 1);
        }
    }

    public static void main(String[] args) {
        System.out.println("Subsets of [1,2,3]: " + subsets(new int[]{1, 2, 3}));
        System.out.println("Comb Sum target=7: " + combinationSum(new int[]{2, 3, 6, 7}, 7));
    }
}"""
        },

        "Advanced": {
            "definition": (
                "At the advanced level, backtracking solves some of the hardest constraint satisfaction "
                "problems: N-Queens, Sudoku Solver, and Word Search. These problems require sophisticated "
                "pruning strategies — using bitmasks to track column/diagonal conflicts for N-Queens in O(1) "
                "vs. O(n) sets, or using a visited matrix for Word Search DFS. We also explore how "
                "Dancing Links (Algorithm X by Knuth) extends backtracking with highly efficient "
                "constraint propagation for exact cover problems."
            ),
            "working": (
                "N-QUEENS BITMASK:\n"
                "  Use three integers: cols, diag1, diag2 tracking conflicts.\n"
                "  For each row, available positions = ~(cols | diag1 | diag2) & fullMask.\n"
                "  Extract rightmost set bit: pos = available & (-available).\n"
                "  Recurse with shifted diagonals.\n\n"
                "SUDOKU SOLVER:\n"
                "  Find the first empty cell.\n"
                "  Try digits 1-9; check validity against row, col, 3x3 box.\n"
                "  Recurse. If no valid digit, backtrack and reset cell.\n\n"
                "WORD SEARCH IN GRID:\n"
                "  Start DFS from every cell matching word[0].\n"
                "  Mark cell as visited (or XOR with '#').\n"
                "  Explore 4 directions; unmark on backtrack."
            ),
            "algorithm": (
                "N-QUEENS BITMASK — O(n!):\n"
                "  solve(row, cols, diag1, diag2):\n"
                "    if row == n: count++; return\n"
                "    avail = ~(cols | diag1 | diag2) & ((1<<n)-1)\n"
                "    while avail:\n"
                "      pos = avail & (-avail)\n"
                "      solve(row+1, cols|pos, (diag1|pos)>>1, (diag2|pos)<<1)\n"
                "      avail &= ~pos\n\n"
                "SUDOKU SOLVER:\n"
                "  isValid(board, row, col, digit) → check row, col, box\n"
                "  for empty cells: try 1-9; if valid → place → recurse → remove"
            ),
            "time_complexity": {
                "N-Queens (bitmask)": "O(N!) — each row has fewer valid placements",
                "Sudoku Solver": "O(9^M) — M = number of empty cells",
                "Word Search": "O(M * N * 4^L) — L = word length",
                "Palindrome Partitioning": "O(2^n * n)",
                "Restore IP Addresses": "O(3^4) — at most 4 segments, each 1-3 digits"
            },
            "space_complexity": "O(n) for recursion stack; O(n²) for the board state.",
            "applications": (
                "• Constraint satisfaction problems (scheduling, resource allocation)\n"
                "• Game AI (Sudoku, Crossword, N-Queens solvers)\n"
                "• Constraint programming (SAT solvers)\n"
                "• Bioinformatics (sequence alignment with constraints)\n"
                "• Automated theorem proving"
            ),
            "advantages": (
                "• Bitmask pruning makes N-Queens exponentially faster\n"
                "• Can solve problems that seem impossible with brute force\n"
                "• Well-defined pattern: choose, recurse, unchoose"
            ),
            "disadvantages": (
                "• Still worst-case exponential for most problems\n"
                "• Multi-constraint pruning logic is extremely complex\n"
                "• Hard to parallelize due to shared mutable state"
            ),
            "interview_notes": (
                "★ N-Queens (LeetCode 51/52) — classic bitmask optimization.\n"
                "★ Sudoku Solver (LeetCode 37) — must handle backtracking perfectly.\n"
                "★ Word Search II (LeetCode 212) — combine Backtracking + Trie for pruning.\n"
                "★ Palindrome Partitioning (LeetCode 131) — backtrack + DP precomputation."
            ),
            "java": """\
public class AdvancedBacktracking {

    // N-Queens — Count Solutions via Bitmask
    static int totalNQueens(int n) {
        return nQueens(n, 0, 0, 0, 0, (1 << n) - 1);
    }
    static int nQueens(int n, int row, int cols, int diag1, int diag2, int full) {
        if (row == n) return 1;
        int avail = full & ~(cols | diag1 | diag2);
        int count = 0;
        while (avail != 0) {
            int pos = avail & (-avail);
            avail &= ~pos;
            count += nQueens(n, row + 1, cols | pos, (diag1 | pos) >> 1, (diag2 | pos) << 1, full);
        }
        return count;
    }

    // Sudoku Solver
    static boolean solveSudoku(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (char c = '1'; c <= '9'; c++) {
                        if (isValidSudoku(board, i, j, c)) {
                            board[i][j] = c;
                            if (solveSudoku(board)) return true;
                            board[i][j] = '.';
                        }
                    }
                    return false; // No valid digit found — backtrack
                }
            }
        }
        return true; // All cells filled
    }
    static boolean isValidSudoku(char[][] board, int row, int col, char c) {
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == c) return false;     // row check
            if (board[i][col] == c) return false;     // col check
            int boxR = 3 * (row / 3) + i / 3;
            int boxC = 3 * (col / 3) + i % 3;
            if (board[boxR][boxC] == c) return false; // box check
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println("N-Queens solutions for n=4: " + totalNQueens(4)); // 2
    }
}"""
        }
    },

    # ==================== TREES ====================
    "Trees": {
        "Beginner": {
            "definition": (
                "A Tree is a hierarchical, non-linear data structure consisting of nodes connected by edges. It "
                "starts with a single 'Root' node, and every node (except the root) has exactly one parent. "
                "Nodes with the same parent are called siblings. A 'Leaf' node is one that has no children. "
                "Trees are used to represent naturally hierarchical data like file systems, corporate "
                "structures, and XML/HTML documents."
            ),
            "working": (
                "1. ROOT: The topmost node of the tree.\n"
                "2. CHILD/PARENT: Nodes directly linked below and above a node.\n"
                "3. SUBTREE: Any node and all its descendants form a tree themselves.\n"
                "4. HEIGHT: The max distance from a node to a leaf.\n"
                "5. DEPTH: The distance from the root to a specific node.\n"
                "6. LEAF: A node with zero children."
            ),
            "algorithm": (
                "PREORDER(node):   // Root, Left, Right\n"
                "  print node.data; PREORDER(node.left); PREORDER(node.right)\n\n"
                "INORDER(node):    // Left, Root, Right\n"
                "  INORDER(node.left); print node.data; INORDER(node.right)\n\n"
                "POSTORDER(node):  // Left, Right, Root\n"
                "  POSTORDER(node.left); POSTORDER(node.right); print node.data"
            ),
            "time_complexity": {
                "Traversal (DFS)": "O(n) — visits each node once",
                "Height Check": "O(n)",
                "Search (Binary Tree)": "O(n)",
                "Insert (Binary Tree)": "O(n)",
                "LCA Search": "O(n)"
            },
            "space_complexity": "O(h) — where h is the height of the tree (stack space for recursion).",
            "applications": (
                "• Storing hierarchical file systems (folders and files)\n"
                "• Organization charts in HR systems\n"
                "• Document Object Model (DOM) in web browsers\n"
                "• Expression trees for compilers and calculators\n"
                "• Routing algorithms in networks"
            ),
            "advantages": (
                "• Represents hierarchical relationships naturally\n"
                "• Efficient traversal and search (when structured as BST)\n"
                "• Faster access and insertion than linked lists in many cases"
            ),
            "disadvantages": (
                "• More complex to implement and manage than linear structures\n"
                "• Unbalanced trees can lead to poor (linear) performance\n"
                "• Higher memory usage due to multiple pointers per node"
            ),
            "interview_notes": (
                "★ Remember: Height is from bottom up, Depth is from top down.\n"
                "★ Master the 3 DFS traversals: Preorder, Inorder, Postorder.\n"
                "★ Know how to calculate the height and diameter of a tree.\n"
                "★ Trees are usually the first exposure to non-linear data structures in interviews."
            ),
            "java": """\
class Node {
    int data;
    Node left, right;
    Node(int d) { data = d; }
}

public class TreeDemo {
    public static void inorder(Node root) {
        if (root == null) return;
        inorder(root.left);
        System.out.print(root.data + " ");
        inorder(root.right);
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        
        System.out.print("Inorder: ");
        inorder(root); // 4 2 1 3
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we extend tree concepts to Binary Trees and their key properties. "
                "We study level-order traversal (BFS), ancestor relationships (Lowest Common Ancestor), "
                "and important tree metrics like diameter and depth. We also explore balanced trees conceptually: "
                "a balanced binary tree has height O(log n), guaranteeing fast operations, while a completely "
                "unbalanced tree degrades to O(n). Constructing a binary tree from its preorder and inorder "
                "traversals is a classic intermediate problem that tests deep understanding of tree structure."
            ),
            "working": (
                "LEVEL-ORDER BFS:\n"
                "  Use a queue. Process level by level using the queue's size as a marker.\n"
                "  Result: a 2D list where each sub-list represents one level.\n\n"
                "LCA (Lowest Common Ancestor):\n"
                "  Recurse into left and right subtrees.\n"
                "  If current node is p or q, return it.\n"
                "  If both sides return non-null, current node IS the LCA.\n\n"
                "DIAMETER OF TREE:\n"
                "  The longest path between any two nodes.\n"
                "  At each node: diameter candidate = leftHeight + rightHeight."
            ),
            "algorithm": (
                "LCA(root, p, q):\n"
                "  if root is null OR root == p OR root == q: return root\n"
                "  leftLCA = LCA(root.left, p, q)\n"
                "  rightLCA = LCA(root.right, p, q)\n"
                "  if both non-null: return root\n"
                "  return leftLCA if leftLCA != null else rightLCA\n\n"
                "CONSTRUCT FROM INORDER + PREORDER:\n"
                "  root = preorder[0]\n"
                "  mid = index of root in inorder\n"
                "  root.left = CONSTRUCT(inorder[0..mid-1], preorder[1..mid])\n"
                "  root.right = CONSTRUCT(inorder[mid+1..], preorder[mid+1..])"
            ),
            "time_complexity": {
                "Level-Order BFS": "O(n) — visits every node once",
                "LCA (Binary Tree)": "O(n)",
                "Diameter of Tree": "O(n)",
                "Construct from Traversals": "O(n) — with HashMap for inorder indices",
                "Check Balanced": "O(n)"
            },
            "space_complexity": "O(n) for BFS queue; O(h) for recursive DFS.",
            "applications": (
                "• JSON/XML parsing and AST construction\n"
                "• Network topology mapping\n"
                "• Genealogy trees and LCA queries\n"
                "• Expression evaluation trees\n"
                "• Dependency resolution graphs"
            ),
            "advantages": (
                "• BFS naturally reveals tree structure level by level\n"
                "• LCA is foundational for many advanced graph algorithms\n"
                "• Diameter helps profile tree shape"
            ),
            "disadvantages": (
                "• BFS requires O(n) queue space in worst case (last level of complete tree)\n"
                "• Recursive LCA may overflow on deeply unbalanced trees\n"
                "• Construction from traversals requires careful index management"
            ),
            "interview_notes": (
                "★ Binary Tree Level Order Traversal (LeetCode 102) — always use BFS with level-size tracking.\n"
                "★ Lowest Common Ancestor (LeetCode 236) — must-know recursive pattern.\n"
                "★ Construct Binary Tree from Pre/Inorder (LeetCode 105) — test of index management.\n"
                "★ Check if tree is Balanced (LeetCode 110) — use height-returning recursion."
            ),
            "java": """\
import java.util.*;

public class IntermediateTree {
    static class Node { int data; Node left, right; Node(int d){data=d;} }

    // Level-order BFS
    static List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Queue<Node> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int size = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                Node n = q.poll();
                level.add(n.data);
                if (n.left != null) q.offer(n.left);
                if (n.right != null) q.offer(n.right);
            }
            res.add(level);
        }
        return res;
    }

    // Lowest Common Ancestor
    static Node lca(Node root, int p, int q) {
        if (root == null || root.data == p || root.data == q) return root;
        Node left = lca(root.left, p, q);
        Node right = lca(root.right, p, q);
        if (left != null && right != null) return root;
        return left != null ? left : right;
    }

    // Diameter
    static int maxDia = 0;
    static int height(Node root) {
        if (root == null) return 0;
        int l = height(root.left), r = height(root.right);
        maxDia = Math.max(maxDia, l + r);
        return 1 + Math.max(l, r);
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2); root.right = new Node(3);
        root.left.left = new Node(4); root.left.right = new Node(5);
        System.out.println("Level Order: " + levelOrder(root));
        System.out.println("LCA(4,5): " + lca(root, 4, 5).data); // 2
        height(root);
        System.out.println("Diameter: " + maxDia); // 3
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced tree topics include AVL Trees (self-balancing BSTs), Red-Black Trees, Serialize "
                "and Deserialize Binary Trees, and complex path-sum problems. AVL trees maintain a "
                "balance factor (height difference between subtrees ≤ 1) via rotations (LL, RR, LR, RL) "
                "after every insert or delete. Morris Traversal achieves O(n) inorder traversal with O(1) "
                "space by temporarily modifying tree links. The Binary Tree Maximum Path Sum problem "
                "(LeetCode 124) is a landmark hard problem using the post-order accumulation trick."
            ),
            "working": (
                "AVL ROTATIONS:\n"
                "  Right Rotation (LL Case): Pivot left child up, root becomes right child.\n"
                "  Left Rotation (RR Case): Pivot right child up, root becomes left child.\n"
                "  LR Case: Left-rotate left child first, then right-rotate root.\n"
                "  RL Case: Right-rotate right child first, then left-rotate root.\n\n"
                "SERIALIZE / DESERIALIZE:\n"
                "  Preorder serialize: write node value then recurse; use 'null' for empty.\n"
                "  Deserialize: read value from stream, recurse for left then right.\n\n"
                "MAX PATH SUM:\n"
                "  At each node: gain = max(leftGain, 0) + max(rightGain, 0) + node.val.\n"
                "  Update global max with gain; return only single-path gain to parent."
            ),
            "algorithm": (
                "SERIALIZE (Preorder):\n"
                "  if null: append '#,'; return\n"
                "  append node.val + ','\n"
                "  SERIALIZE(left); SERIALIZE(right)\n\n"
                "MAX PATH SUM:\n"
                "  dfs(node):\n"
                "    leftGain = max(dfs(left), 0)\n"
                "    rightGain = max(dfs(right), 0)\n"
                "    maxPath = max(maxPath, node.val + leftGain + rightGain)  // update global\n"
                "    return node.val + max(leftGain, rightGain)  // propagate one direction only"
            ),
            "time_complexity": {
                "AVL Insert/Delete": "O(log n) — guaranteed by balancing",
                "Serialize/Deserialize": "O(n)",
                "Max Path Sum": "O(n)",
                "Morris Inorder": "O(n) time, O(1) space",
                "Vertical Order Traversal": "O(n log n)"
            },
            "space_complexity": "O(n) for serialization string; O(1) for Morris; O(h) for most recursions.",
            "applications": (
                "• Database indexing (Red-Black Trees in Java TreeMap)\n"
                "• File system implementation\n"
                "• Compiler symbol tables\n"
                "• Network routing tables\n"
                "• Decision trees in machine learning"
            ),
            "advantages": (
                "• AVL guarantees O(log n) for all operations\n"
                "• Morris traversal is the most space-efficient traversal\n"
                "• Serialization enables persistence and network transmission of trees"
            ),
            "disadvantages": (
                "• AVL rotations add implementation complexity\n"
                "• Morris traversal temporarily corrupts tree structure\n"
                "• Red-Black trees are harder to implement than AVL"
            ),
            "interview_notes": (
                "★ Serialize and Deserialize Binary Tree (LeetCode 297) — premium Hard problem.\n"
                "★ Binary Tree Maximum Path Sum (LeetCode 124) — classic Hard with global accumulator.\n"
                "★ Binary Tree Right Side View (LeetCode 199) — BFS picking last element per level.\n"
                "★ Know why Red-Black Trees are preferred over AVL in practice (fewer rotations)."
            ),
            "java": """\
import java.util.*;

public class AdvancedTree {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    static int maxPath = Integer.MIN_VALUE;

    // Binary Tree Maximum Path Sum
    static int dfs(TreeNode root) {
        if (root == null) return 0;
        int left = Math.max(dfs(root.left), 0);
        int right = Math.max(dfs(root.right), 0);
        maxPath = Math.max(maxPath, root.val + left + right);
        return root.val + Math.max(left, right); // propagate ONE side only
    }

    // Serialize (Preorder)
    static String serialize(TreeNode root) {
        if (root == null) return "# ";
        return root.val + " " + serialize(root.left) + serialize(root.right);
    }

    // Deserialize
    static TreeNode deserialize(String data) {
        Queue<String> q = new LinkedList<>(Arrays.asList(data.split(" ")));
        return buildTree(q);
    }
    static TreeNode buildTree(Queue<String> q) {
        String val = q.poll();
        if (val.equals("#")) return null;
        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = buildTree(q);
        node.right = buildTree(q);
        return node;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(-10);
        root.left = new TreeNode(9); root.right = new TreeNode(20);
        root.right.left = new TreeNode(15); root.right.right = new TreeNode(7);
        dfs(root);
        System.out.println("Max Path Sum: " + maxPath); // 42
        String serial = serialize(root);
        System.out.println("Serialized: " + serial);
    }
}"""
        }
    },

    # ==================== BINARY SEARCH TREES ====================
    "Binary Search Trees": {
        "Beginner": {
            "definition": (
                "A Binary Search Tree (BST) is a specialized binary tree where each node follows a specific "
                "ordering property: all nodes in the left subtree have values less than the node's value, "
                "and all nodes in the right subtree have values greater than the node's value. This property "
                "must hold for every node in the tree, enabling efficient searching, insertion, and deletion "
                "similar to binary search in an array."
            ),
            "working": (
                "1. ORDERING: For any node X: all left(X) < X and all right(X) > X.\n"
                "2. SEARCHING: Compare target with current node; if smaller move left, if larger move right.\n"
                "3. INSERTION: Always happens at a leaf position that maintains the BST property.\n"
                "4. INORDER PROPERTY: An Inorder traversal of a BST always yields values in sorted order."
            ),
            "algorithm": (
                "SEARCH(root, val):\n"
                "  if root is null or root.val == val: return root\n"
                "  if val < root.val: return SEARCH(root.left, val)\n"
                "  return SEARCH(root.right, val)\n\n"
                "INSERT(root, val):\n"
                "  if root is null: return new Node(val)\n"
                "  if val < root.val: root.left = INSERT(root.left, val)\n"
                "  else: root.right = INSERT(root.right, val)\n"
                "  return root"
            ),
            "time_complexity": {
                "Search (Avg)": "O(log n)",
                "Insert (Avg)": "O(log n)",
                "Delete (Avg)": "O(log n)",
                "Search (Worst)": "O(n) — if the tree is skewed",
                "Traversal": "O(n)"
            },
            "space_complexity": "O(h) — stack space for recursion; O(1) for iterative search.",
            "applications": (
                "• Implementing searching and sorting algorithms\n"
                "• Building Maps and Sets in some libraries (Red-Black Trees)\n"
                "• Databases for indexing data records\n"
                "• Systems requiring dynamic data sorting\n"
                "• Auto-complete suggestions in some contexts"
            ),
            "advantages": (
                "• Efficient searching and insertion (logarithmic on average)\n"
                "• Naturally maintains data in sorted order (Inorder traversal)\n"
                "• Flexible sizing like a linked list but better search speed"
            ),
            "disadvantages": (
                "• Can become 'skewed' (like a linked list), losing log speed\n"
                "• Requires balancing (AVL, Red-Black) for guaranteed performance\n"
                "• Deletion of nodes with two children can be tricky"
            ),
            "interview_notes": (
                "★ The #1 BST trick: Inorder traversal = Sorted Array.\n"
                "★ Valid BST check: verify values stay within [min, max] range for each node.\n"
                "★ Successor/Predecessor: know how to find these without a parent pointer.\n"
                "★ Mention 'Self-Balancing Trees' (AVL/Red-Black) if performance hits O(n)."
            ),
            "java": """\
public class BSTDemo {
    static class Node {
        int val; Node left, right;
        Node(int v) { val = v; }
    }

    public static Node insert(Node root, int val) {
        if (root == null) return new Node(val);
        if (val < root.val) root.left = insert(root.left, val);
        else if (val > root.val) root.right = insert(root.right, val);
        return root;
    }

    public static boolean search(Node root, int val) {
        if (root == null) return false;
        if (root.val == val) return true;
        return val < root.val ? search(root.left, val) : search(root.right, val);
    }

    public static void main(String[] args) {
        Node root = null;
        root = insert(root, 50); insert(root, 30); insert(root, 70);
        System.out.println("Has 30? " + search(root, 30)); // true
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "Intermediate BST topics cover deletion (the trickiest BST operation), BST validation, "
                "finding the k-th smallest element, and converting BSTs to other structures. BST deletion "
                "has three cases: deleting a leaf, a node with one child, and a node with two children "
                "(replace with inorder successor or predecessor). We also study self-balancing BSTs "
                "conceptually: AVL trees and Red-Black Trees prevent O(n) worst-case by maintaining "
                "height balance invariants through rotations."
            ),
            "working": (
                "BST DELETION (3 cases):\n"
                "  Case 1 (Leaf): Simply remove the node.\n"
                "  Case 2 (One child): Replace node with its single child.\n"
                "  Case 3 (Two children):\n"
                "    Find the inorder successor (smallest in right subtree).\n"
                "    Copy successor's value to current node.\n"
                "    Delete the successor from the right subtree.\n\n"
                "BST VALIDATION:\n"
                "  Use min/max bounds: each node must be in range (min, max).\n"
                "  Left subtree: upper bound = current node value.\n"
                "  Right subtree: lower bound = current node value."
            ),
            "algorithm": (
                "BST DELETE(root, val):\n"
                "  if root.val < val: root.right = DELETE(root.right, val)\n"
                "  elif root.val > val: root.left = DELETE(root.left, val)\n"
                "  else:\n"
                "    if !root.left: return root.right\n"
                "    if !root.right: return root.left\n"
                "    successor = findMin(root.right)\n"
                "    root.val = successor.val\n"
                "    root.right = DELETE(root.right, successor.val)\n"
                "  return root\n\n"
                "VALIDATE BST (bounds check):\n"
                "  validate(root, min=-inf, max=+inf):\n"
                "    if root.val <= min or root.val >= max: return false\n"
                "    return validate(left, min, root.val) and validate(right, root.val, max)"
            ),
            "time_complexity": {
                "BST Delete": "O(h) — O(log n) avg, O(n) worst",
                "BST Validate": "O(n)",
                "K-th Smallest": "O(h + k)",
                "BST to Sorted List": "O(n)",
                "BST Iterator (next)": "O(h) amortized O(1)"
            },
            "space_complexity": "O(h) for recursion depth. O(1) extra for iterative inorder.",
            "applications": (
                "• Dictionary implementations in some languages\n"
                "• Range queries on sorted data\n"
                "• Ordered statistics (k-th smallest, rank of element)\n"
                "• Event simulation systems (ordered events)\n"
                "• Floor/Ceiling computations for real-number indexing"
            ),
            "advantages": (
                "• Naturally ordered — inorder traversal gives sorted sequence\n"
                "• Range queries easier than hash maps\n"
                "• Supports floor, ceiling, predecessor, successor in O(log n)"
            ),
            "disadvantages": (
                "• Deletion complexity (three cases) is error-prone\n"
                "• No guarantee of balance without self-balancing variants\n"
                "• Java's TreeMap (Red-Black based) should be preferred for production"
            ),
            "interview_notes": (
                "★ Delete Node in BST (LeetCode 450) — implement all three deletion cases.\n"
                "★ Validate BST (LeetCode 98) — must use min/max bounds, NOT just left < root < right.\n"
                "★ Kth Smallest in BST (LeetCode 230) — inorder traversal + counter.\n"
                "★ Convert Sorted Array to BST (LeetCode 108) — divide and conquer."
            ),
            "java": """\
public class IntermediateBST {
    static class Node { int val; Node left, right; Node(int v){val=v;} }

    // BST Delete
    static Node delete(Node root, int val) {
        if (root == null) return null;
        if (val < root.val) root.left = delete(root.left, val);
        else if (val > root.val) root.right = delete(root.right, val);
        else {
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            Node succ = root.right;
            while (succ.left != null) succ = succ.left;
            root.val = succ.val;
            root.right = delete(root.right, succ.val);
        }
        return root;
    }

    // Validate BST
    static boolean isValid(Node root, long min, long max) {
        if (root == null) return true;
        if (root.val <= min || root.val >= max) return false;
        return isValid(root.left, min, root.val) && isValid(root.right, root.val, max);
    }

    public static void main(String[] args) {
        Node root = new Node(5);
        root.left = new Node(3); root.right = new Node(7);
        root.left.left = new Node(2); root.left.right = new Node(4);
        System.out.println("Valid BST? " + isValid(root, Long.MIN_VALUE, Long.MAX_VALUE)); // true
        root = delete(root, 3);
        System.out.println("After delete 3, root.left.val: " + root.left.val); // 4
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced BST topics encompass AVL and Red-Black Trees, where self-balancing is maintained "
                "through rotations. AVL trees perform single and double rotations to maintain a balance "
                "factor of at most 1 at every node. Red-Black Trees use color properties (every node is "
                "red or black, no two consecutive red nodes, equal black-height on all paths) to guarantee "
                "O(log n) operations. Java's TreeMap and TreeSet internally use Red-Black Trees. "
                "We also study augmented BSTs that store additional metadata (subtree size, max value) "
                "to answer order-statistics queries in O(log n)."
            ),
            "working": (
                "AVL RIGHT ROTATION (Node y has left-heavy subtree):\n"
                "  x = y.left\n"
                "  y.left = x.right\n"
                "  x.right = y\n"
                "  update heights of y and x\n"
                "  return x (new root)\n\n"
                "RED-BLACK TREE PROPERTIES:\n"
                "  1. Every node is red or black.\n"
                "  2. Root is black.\n"
                "  3. Every leaf (null) is black.\n"
                "  4. No two consecutive red nodes.\n"
                "  5. All root-to-leaf paths have the same black-height.\n\n"
                "AUGMENTED BST (Order Statistic Tree):\n"
                "  Each node stores subtree size.\n"
                "  K-th smallest: navigate using sizes in O(log n)."
            ),
            "algorithm": (
                "AVL INSERT (simplified):\n"
                "  Standard BST insert\n"
                "  computeHeight: height = 1 + max(leftH, rightH)\n"
                "  balance = leftH - rightH\n"
                "  if balance > 1: check child; rightRotate or leftRightRotate\n"
                "  if balance < -1: check child; leftRotate or rightLeftRotate\n\n"
                "K-TH SMALLEST (Augmented BST):\n"
                "  leftSize = size(root.left)\n"
                "  if k == leftSize + 1: return root.val\n"
                "  elif k <= leftSize: recurse into left\n"
                "  else: recurse into right with k = k - leftSize - 1"
            ),
            "time_complexity": {
                "AVL Insert/Delete": "O(log n) guaranteed",
                "Red-Black Insert/Delete": "O(log n) guaranteed",
                "Augmented BST K-th Min": "O(log n)",
                "Count nodes in range": "O(log n + result)",
                "BST to DLL (in-place)": "O(n)"
            },
            "space_complexity": "O(log n) for recursion in balanced BSTs. O(n) total tree storage.",
            "applications": (
                "• Java TreeMap, TreeSet (Red-Black Trees)\n"
                "• Linux OS kernel CFS scheduler (Red-Black Tree)\n"
                "• Database B-Tree indexes\n"
                "• Interval scheduling and range monitoring\n"
                "• Order statistics in competitive programming"
            ),
            "advantages": (
                "• Guaranteed O(log n) unlike unbalanced BST\n"
                "• Red-Black Trees have fewer rotations than AVL on insert-heavy workloads\n"
                "• Augmented BSTs enable powerful order-statistic queries"
            ),
            "disadvantages": (
                "• Complex implementation — especially Red-Black recoloring cases\n"
                "• Augmentation increases code complexity\n"
                "• Skip Lists and B-Trees preferred in production for some use cases"
            ),
            "interview_notes": (
                "★ Understand why Java TreeMap uses Red-Black over AVL.\n"
                "★ Be able to draw and explain at least one AVL rotation.\n"
                "★ Count of Smaller Numbers After Self (LeetCode 315) — augmented BST / BIT.\n"
                "★ BST to Greater Sum Tree (LeetCode 1038) — reverse inorder + accumulation."
            ),
            "java": """\
import java.util.TreeMap;

public class AdvancedBST {
    // Java TreeMap is a Red-Black BST internally
    public static void main(String[] args) {
        TreeMap<Integer, String> map = new TreeMap<>();
        map.put(5, "five"); map.put(3, "three"); map.put(7, "seven");
        map.put(1, "one"); map.put(4, "four");

        System.out.println("Floor of 6: " + map.floorKey(6));   // 5 (largest key <= 6)
        System.out.println("Ceiling of 6: " + map.ceilingKey(6)); // 7 (smallest key >= 6)
        System.out.println("Submap [3,6]: " + map.subMap(3, true, 6, true));

        // Count elements in a range [lo, hi]
        int lo = 3, hi = 6;
        int count = map.subMap(lo, true, hi, true).size();
        System.out.println("Elements in [3,6]: " + count); // 3 (keys 3, 4, 5)
    }
}"""
        }
    },

    # ==================== HEAP / PRIORITY QUEUE ====================
    "Heap / Priority Queue": {
        "Beginner": {
            "definition": (
                "A Heap is a specialized tree-based data structure that satisfies the heap property: in a "
                "Max-Heap, for any given node I, the value of I is greater than or equal to the values of its "
                "children. In a Min-Heap, the value of I is less than or equal to the values of its children. "
                "This makes heaps ideal for implementing priority queues, where the highest (or lowest) "
                "priority element is always at the root. Unlike a BST, a heap does not have a strict "
                "left-to-right order."
            ),
            "working": (
                "1. COMPLETE BINARY TREE: Heaps are always balanced and represented efficiently as arrays.\n"
                "2. ARRAY REPRESENTATION: For index i, children are at 2i+1 and 2i+2. Parent is at (i-1)/2.\n"
                "3. HEAPIFY UP: On insertion, move the new element up until the heap property is restored.\n"
                "4. HEAPIFY DOWN: On deletion (at root), move the last element to the root and sift it down."
            ),
            "algorithm": (
                "INSERT(val):\n"
                "  add to end of array; siftUp(last_index)\n\n"
                "EXTRACT_MIN():\n"
                "  min = root; root = last_element; siftDown(0); return min"
            ),
            "time_complexity": {
                "Insert": "O(log n)",
                "Delete (Root)": "O(log n)",
                "Peek (Min/Max)": "O(1)",
                "Build Heap": "O(n) — using bottom-up approach",
                "Heapsort": "O(n log n)"
            },
            "space_complexity": "O(n) — stored in a single contiguous array.",
            "applications": (
                "• Implementing Priority Queues (Task scheduling, Event simulation)\n"
                "• Dijkstra's Shortest Path algorithm\n"
                "• Prim's Minimum Spanning Tree algorithm\n"
                "• Heapsort — an in-place sorting algorithm\n"
                "• Finding the K-th smallest/largest element in a stream"
            ),
            "advantages": (
                "• Guarantees O(1) access to the highest/lowest priority element\n"
                "• Efficient insertion and deletion (logarithmic time)\n"
                "• Very space-efficient compared to pointer-based trees"
            ),
            "disadvantages": (
                "• Not suitable for searching specific elements (takes O(n))\n"
                "• Only the root is directly accessible; no sorted traversal like BST\n"
                "• More complex to implement heapify logic manually"
            ),
            "interview_notes": (
                "★ Java's PriorityQueue is a Min-Heap by default.\n"
                "★ Know how to convert an array to a heap in O(n) time.\n"
                "★ Top K Elements (LeetCode 347) is a classic heap problem.\n"
                "★ Mention 'Binary Heap' vs 'Fibonacci Heap' for advanced graph algorithms."
            ),
            "java": """\
import java.util.PriorityQueue;

public class HeapDemo {
    public static void main(String[] args) {
        // Default: Min-Heap
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        minHeap.add(10); minHeap.add(5); minHeap.add(20);

        System.out.println("Min element: " + minHeap.peek()); // 5
        System.out.println("Popped: " + minHeap.poll());    // 5

        // Max-Heap using Comparator
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        maxHeap.add(10); maxHeap.add(30); maxHeap.add(20);
        System.out.println("Max element: " + maxHeap.peek()); // 30
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we implement heaps from scratch and use them to solve classic "
                "problems: Kth Largest Element, Merge K Sorted Lists, and Median of Data Stream. The "
                "'Two-Heap' pattern — maintaining a Max-Heap for the lower half and a Min-Heap for the upper "
                "half of a stream — allows the running median to be retrieved in O(1) at any time. Heap Sort "
                "is an in-place O(n log n) sorting algorithm built using the heap data structure: build a "
                "Max-Heap, then repeatedly extract-max to get sorted order."
            ),
            "working": (
                "TWO-HEAP PATTERN (Running Median):\n"
                "  maxHeap holds the lower half (size >= minHeap).\n"
                "  minHeap holds the upper half.\n"
                "  On insert: offer to maxHeap; rebalance by moving maxHeap.peek to minHeap if needed.\n"
                "  Median = maxHeap.peek() or average of both tops.\n\n"
                "HEAP SORT:\n"
                "  Build Max-Heap from array (O(n)).\n"
                "  Repeatedly: swap root with last element, reduce heap size, heapify-down (O(log n) each).\n"
                "  Result: array sorted in ascending order."
            ),
            "algorithm": (
                "BUILD MAX-HEAP (Bottom-Up):\n"
                "  for i from n/2-1 down to 0: heapifyDown(arr, i, n)\n\n"
                "HEAP SORT Step:\n"
                "  for i from n-1 down to 1:\n"
                "    swap(arr[0], arr[i])\n"
                "    heapifyDown(arr, 0, i)\n\n"
                "HEAPIFY DOWN(arr, i, n):\n"
                "  largest = i; l = 2i+1; r = 2i+2\n"
                "  if l < n and arr[l] > arr[largest]: largest = l\n"
                "  if r < n and arr[r] > arr[largest]: largest = r\n"
                "  if largest != i: swap; heapifyDown(largest)"
            ),
            "time_complexity": {
                "Heap Sort": "O(n log n)",
                "Build Heap": "O(n) — bottom-up method",
                "Kth Largest": "O(n log k) — min-heap of size k",
                "Merge K Lists": "O(N log K) — N total nodes, K lists",
                "Median Insert": "O(log n)"
            },
            "space_complexity": "O(1) for Heap Sort; O(k) for kth-largest; O(2) median heaps.",
            "applications": (
                "• Heap Sort (in-place, no extra memory)\n"
                "• Streaming median calculation\n"
                "• K-way merge (DBMS external sort)\n"
                "• Real-time event simulation\n"
                "• Hospital emergency room priority queueing"
            ),
            "advantages": (
                "• Heap Sort uses O(1) space unlike Merge Sort\n"
                "• Two-heap pattern is O(1) median retrieval at all times\n"
                "• Priority-based processing is extremely natural with heaps"
            ),
            "disadvantages": (
                "• Heap Sort is not stable and has poor cache performance vs Quick Sort\n"
                "• Two-heap pattern requires constant rebalancing logic\n"
                "• Java PriorityQueue does not support O(log n) decrease-key (need indexed heap)"
            ),
            "interview_notes": (
                "★ Find Median from Data Stream (LeetCode 295) — the classic two-heap problem.\n"
                "★ Kth Largest Element in Array (LeetCode 215) — min-heap of size k.\n"
                "★ Merge K Sorted Lists (LeetCode 23) — add head of each list to min-heap.\n"
                "★ Know Build-Heap O(n) amortized proof — often asked in system design."
            ),
            "java": """\
import java.util.*;

public class IntermediateHeap {

    // Heap Sort
    static void heapSort(int[] arr) {
        int n = arr.length;
        for (int i = n / 2 - 1; i >= 0; i--) heapify(arr, n, i);
        for (int i = n - 1; i > 0; i--) {
            int tmp = arr[0]; arr[0] = arr[i]; arr[i] = tmp;
            heapify(arr, i, 0);
        }
    }
    static void heapify(int[] arr, int n, int i) {
        int largest = i, l = 2*i+1, r = 2*i+2;
        if (l < n && arr[l] > arr[largest]) largest = l;
        if (r < n && arr[r] > arr[largest]) largest = r;
        if (largest != i) {
            int tmp = arr[i]; arr[i] = arr[largest]; arr[largest] = tmp;
            heapify(arr, n, largest);
        }
    }

    // Find Median from Stream (Two Heaps)
    static PriorityQueue<Integer> lo = new PriorityQueue<>(Collections.reverseOrder()); // max-heap
    static PriorityQueue<Integer> hi = new PriorityQueue<>(); // min-heap
    static void addNum(int num) {
        lo.offer(num);
        hi.offer(lo.poll());
        if (lo.size() < hi.size()) lo.offer(hi.poll());
    }
    static double findMedian() {
        return lo.size() > hi.size() ? lo.peek() : (lo.peek() + hi.peek()) / 2.0;
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6, 7};
        heapSort(arr);
        System.out.println("Heap Sorted: " + Arrays.toString(arr)); // [5, 6, 7, 11, 12, 13]

        addNum(1); addNum(2);
        System.out.println("Median after 1,2: " + findMedian()); // 1.5
        addNum(3);
        System.out.println("Median after 1,2,3: " + findMedian()); // 2.0
    }
}"""
        },

        "Advanced": {
            "definition": (
                "At the advanced level, heaps are used in complex graph algorithms and scheduling systems. "
                "Dijkstra's shortest path algorithm runs in O((V+E) log V) using a Min-Heap as the priority "
                "queue. Prim's MST algorithm is similarly powered by a heap. We also explore the D-ary Heap "
                "(generalization of binary heap with D children per node), which offers better cache "
                "performance for large heaps, and the Fibonacci Heap which supports decrease-key in O(1) "
                "amortized, making Dijkstra's run in O(E + V log V)."
            ),
            "working": (
                "DIJKSTRA WITH MIN-HEAP:\n"
                "  Initialize dist[source] = 0; all others = infinity.\n"
                "  Push (0, source) into min-heap.\n"
                "  While heap not empty: pop (d, u). Skip if d > dist[u].\n"
                "  For each neighbor v: if dist[u] + w < dist[v]: update, push (dist[v], v).\n\n"
                "LAZY DELETION HEAP:\n"
                "  When an element's priority changes, don't remove it directly.\n"
                "  Mark old entry as invalid; add new entry.\n"
                "  Skip invalid entries when popping."
            ),
            "algorithm": (
                "DIJKSTRA'S O((V+E) log V):\n"
                "  dist[] = {inf}; dist[src] = 0; pq.add({0, src})\n"
                "  while pq not empty:\n"
                "    (d, u) = pq.poll()\n"
                "    if d > dist[u]: continue  // lazy deletion\n"
                "    for (v, w) in adj[u]:\n"
                "      if dist[u] + w < dist[v]:\n"
                "        dist[v] = dist[u] + w; pq.add({dist[v], v})"
            ),
            "time_complexity": {
                "Dijkstra (Binary Heap)": "O((V + E) log V)",
                "Dijkstra (Fibonacci Heap)": "O(E + V log V)",
                "Prim's MST (Binary Heap)": "O(E log V)",
                "D-ary Heap Insert": "O(log_D n)",
                "Decrease-Key (Fibonacci)": "O(1) amortized"
            },
            "space_complexity": "O(V + E) for graph; O(V) for the heap.",
            "applications": (
                "• Dijkstra's shortest path (GPS, network routing)\n"
                "• Prim's MST (network design, cluster analysis)\n"
                "• A* pathfinding algorithm (game AI, robotics)\n"
                "• Task scheduling with priorities and dependencies\n"
                "• Approximate nearest neighbor in machine learning"
            ),
            "advantages": (
                "• Heap-based Dijkstra is optimal for sparse graphs\n"
                "• D-ary heaps reduce cache misses for large priority queues\n"
                "• Fibonacci Heap gives theoretical improvement for dense graphs"
            ),
            "disadvantages": (
                "• Fibonacci Heap is extremely complex to implement correctly\n"
                "• Decrease-key operation is hard to use with Java's PriorityQueue\n"
                "• For most practical graph sizes, Binary Heap + Lazy Deletion is preferred"
            ),
            "interview_notes": (
                "★ Network Delay Time (LeetCode 743) — Dijkstra with adjacency list.\n"
                "★ Swim in Rising Water (LeetCode 778) — binary search on time or Dijkstra.\n"
                "★ Cheapest Flights Within K Stops (LeetCode 787) — modified Dijkstra with stop constraint.\n"
                "★ Know why Fibonacci Heap is theoretically better but rarely used in practice."
            ),
            "java": """\
import java.util.*;

public class AdvancedHeap {
    // Dijkstra's Algorithm using Min-Heap
    static int[] dijkstra(int n, List<int[]>[] adj, int src) {
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, src});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int d = curr[0], u = curr[1];
            if (d > dist[u]) continue; // lazy deletion of stale entries
            for (int[] edge : adj[u]) {
                int v = edge[0], w = edge[1];
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.offer(new int[]{dist[v], v});
                }
            }
        }
        return dist;
    }

    @SuppressWarnings("unchecked")
    public static void main(String[] args) {
        int n = 4;
        List<int[]>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        adj[0].add(new int[]{1, 1}); adj[0].add(new int[]{2, 4});
        adj[1].add(new int[]{2, 2}); adj[1].add(new int[]{3, 6});
        adj[2].add(new int[]{3, 3});
        int[] dist = dijkstra(n, adj, 0);
        System.out.println("Distances from 0: " + Arrays.toString(dist)); // [0, 1, 3, 6]
    }
}"""
        }
    },

    # ==================== HASHING ====================
    "Hashing": {
        "Beginner": {
            "definition": (
                "Hashing is a technique that uses a mathematical 'Hash Function' to map data (keys) of "
                "arbitrary size to fixed-size values (hash codes), which serve as indices in an array called "
                "a Hash Table. This allows for near-instant (constant time) data retrieval regardless of the "
                "size of the dataset. It is the core technology behind HashMaps, Sets, and database indexing."
            ),
            "working": (
                "1. HASH FUNCTION: A function that takes a key and returns an integer index.\n"
                "2. COLLISION: When two different keys produce the same hash index.\n"
                "3. CHAINING: Storing all colliding elements in a linked list at that index.\n"
                "4. OPEN ADDRESSING: Finding the next available slot in the array if a collision occurs.\n"
                "5. LOAD FACTOR: The ratio of filled slots to total capacity (triggering a resize)."
            ),
            "algorithm": (
                "GET(key):\n"
                "  index = hash(key) % capacity\n"
                "  search for key in bucket at index\n\n"
                "PUT(key, val):\n"
                "  index = hash(key) % capacity\n"
                "  if key exists: update value; else: add to bucket"
            ),
            "time_complexity": {
                "Search (Avg)": "O(1)",
                "Insert (Avg)": "O(1)",
                "Delete (Avg)": "O(1)",
                "Search (Worst)": "O(n) — if all keys collide",
                "Space": "O(n)"
            },
            "space_complexity": "O(n) — plus overhead for buckets/linked list nodes.",
            "applications": (
                "• Database indexing for fast record lookup\n"
                "• Implementing Sets and Maps (Dictionaries)\n"
                "• Caching (storing results of expensive operations)\n"
                "• Cryptographic signatures and data integrity\n"
                "• Spell checkers and word frequencies"
            ),
            "advantages": (
                "• Extremely fast data retrieval on average\n"
                "• Decouples data from its physical location in memory\n"
                "• Works with any data type that can be hashed (strings, objects, etc.)"
            ),
            "disadvantages": (
                "• Complexity of designing a good hash function to minimize collisions\n"
                "• Performance degrades to O(n) under heavy collisions\n"
                "• Does not maintain any order (unsorted data)"
            ),
            "interview_notes": (
                "★ Java HashMap uses Chaining (with nodes converting to trees in Java 8+).\n"
                "★ A good hash function should be fast and distribute keys uniformly.\n"
                "★ Practice 'Two Sum' using a HashMap — it's the #1 LeetCode problem.\n"
                "★ Mention 'Consistent Hashing' for distributed systems (System Design)."
            ),
            "java": """\
import java.util.HashMap;

public class HashingDemo {
    public static void main(String[] args) {
        HashMap<String, Integer> map = new HashMap<>();
        map.put("Apple", 100);
        map.put("Banana", 150);

        System.out.println("Price of Apple: " + map.get("Apple"));
        System.out.println("Contains Grape? " + map.containsKey("Grape"));

        // Iterate
        for (String key : map.keySet()) {
            System.out.println(key + " -> " + map.get(key));
        }
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, hashing is applied to solve classic interview problems efficiently. "
                "We explore custom hash map implementations, rolling hash for string matching, and how to handle "
                "collisions through open addressing (linear probing, quadratic probing, double hashing). The "
                "frequency-counting pattern — using a HashMap to count element occurrences — is the backbone "
                "of problems like Top K Frequent Elements, Valid Anagram, and Group Anagrams."
            ),
            "working": (
                "FREQUENCY MAP PATTERN:\n"
                "  HashMap<element, count> built in O(n).\n"
                "  Used to detect duplicates, find majority, check anagrams.\n\n"
                "ROLLING HASH (Rabin-Karp):\n"
                "  Pre-compute hash for window; slide by subtracting oldest and adding newest char.\n"
                "  Enables substring search in O(n + m) average time.\n\n"
                "OPEN ADDRESSING:\n"
                "  Linear Probing: check slot+1, slot+2, ... until empty.\n"
                "  Quadratic Probing: check slot+1^2, slot+2^2, ...\n"
                "  Double Hashing: use a second hash function to compute stride."
            ),
            "algorithm": (
                "GROUP ANAGRAMS (Sort as Key):\n"
                "  for each word: key = sorted(word)\n"
                "  map.getOrDefault(key, []).add(word)\n"
                "  return map.values()\n\n"
                "TOP K FREQUENT (Heap-based):\n"
                "  build frequency map\n"
                "  maintain min-heap of size K\n"
                "  return keys in heap"
            ),
            "time_complexity": {
                "Frequency Map Build": "O(n)",
                "Group Anagrams": "O(n * L * log L) — L = avg word length",
                "Top K Frequent": "O(n log k)",
                "Rabin-Karp Search": "O(n + m) avg",
                "Custom HashMap Lookup": "O(1) avg, O(n) worst"
            },
            "space_complexity": "O(n) for the hash map; O(k) for top-k heap results.",
            "applications": (
                "• Caching systems (LRU Cache = HashMap + DLL)\n"
                "• Duplicate detection in logs and data streams\n"
                "• String pattern matching (Rabin-Karp)\n"
                "• Counting word frequencies in documents\n"
                "• Session management in web applications"
            ),
            "advantages": (
                "• Frequency map pattern solves many O(n) problems in a single pass\n"
                "• Rolling hash enables O(n) string search without preprocessing\n"
                "• Flexible key types — any object with hashCode() can be a key"
            ),
            "disadvantages": (
                "• Hash collisions degrade performance to O(n) in worst case\n"
                "• No stable ordering — iteration order not guaranteed in HashMap\n"
                "• Memory overhead from bucket arrays and node objects"
            ),
            "interview_notes": (
                "★ Two Sum (LeetCode 1) — use map to find complement in O(n).\n"
                "★ Group Anagrams (LeetCode 49) — sort each word as map key.\n"
                "★ Longest Consecutive Sequence (LeetCode 128) — HashSet for O(n).\n"
                "★ LRU Cache (LeetCode 146) — combines HashMap and Doubly Linked List."
            ),
            "java": """\
import java.util.*;

public class IntermediateHashing {

    // Group Anagrams
    static Map<String, List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            char[] arr = s.toCharArray();
            Arrays.sort(arr);
            String key = new String(arr);
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        return map;
    }

    // Top K Frequent Elements
    static int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int n : nums) count.merge(n, 1, Integer::sum);
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        for (var e : count.entrySet()) {
            pq.offer(new int[]{e.getKey(), e.getValue()});
            if (pq.size() > k) pq.poll();
        }
        return pq.stream().mapToInt(a -> a[0]).toArray();
    }

    public static void main(String[] args) {
        System.out.println(groupAnagrams(new String[]{"eat","tea","tan","ate","nat","bat"}));
        System.out.println(Arrays.toString(topKFrequent(new int[]{1,1,1,2,2,3}, 2))); // [2,1]
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced hashing topics include Consistent Hashing (used in distributed systems to minimize "
                "rebalancing when nodes are added/removed), Bloom Filters (space-efficient probabilistic data "
                "structures that test set membership with no false negatives but possible false positives), "
                "and Cuckoo Hashing (guarantees O(1) worst-case lookup by using two hash functions "
                "and displacing existing keys). These are critical for large-scale system design interviews "
                "and distributed database architectures."
            ),
            "working": (
                "CONSISTENT HASHING:\n"
                "  Place server nodes on a virtual ring of 2^32 positions.\n"
                "  Each key maps to the 'next' server clockwise.\n"
                "  Adding/removing a server only redistributes keys from adjacent range.\n\n"
                "BLOOM FILTER:\n"
                "  K hash functions; each hash sets a bit in a bitarray.\n"
                "  Lookup: check all K bits. If ANY is 0, definitely not in set.\n"
                "  If ALL are 1, probably in set (false positives possible).\n\n"
                "LRU CACHE (HashMap + DLL):\n"
                "  HashMap maps key -> DLL node for O(1) access.\n"
                "  DLL moves recently accessed node to front in O(1)."
            ),
            "algorithm": (
                "LRU CACHE GET(key):\n"
                "  if key in map: move its DLL node to front; return value\n"
                "  else: return -1\n\n"
                "LRU CACHE PUT(key, val):\n"
                "  if key in map: update node and move to front\n"
                "  else: create new node at front; if over capacity: remove LRU from tail"
            ),
            "time_complexity": {
                "LRU Get/Put": "O(1) — HashMap + DLL",
                "Bloom Filter Insert": "O(k) — k hash function calls",
                "Bloom Filter Lookup": "O(k) — k hash function calls",
                "Consistent Hashing Lookup": "O(log n) — binary search on ring",
                "Cuckoo Hashing Lookup": "O(1) worst case"
            },
            "space_complexity": "O(n) for LRU cache; O(m) for Bloom Filter bitarray (independent of data count).",
            "applications": (
                "• CDN and distributed caches (Consistent Hashing)\n"
                "• Spell checkers and malware URL filters (Bloom Filters)\n"
                "• Browser cache and OS page cache (LRU)\n"
                "• Database query result caching\n"
                "• Duplicate URL detection in web crawlers"
            ),
            "advantages": (
                "• Consistent hashing minimizes reshuffling in distributed systems\n"
                "• Bloom filters use negligible memory for large-scale membership tests\n"
                "• LRU cache provides the best real-world hit rate for temporal locality"
            ),
            "disadvantages": (
                "• Bloom filters have false positives — cannot use for exact membership\n"
                "• LRU cache with linked list has memory overhead per node\n"
                "• Consistent hashing adds lattency due to ring traversal"
            ),
            "interview_notes": (
                "★ LRU Cache (LeetCode 146) — most asked hard system design coding problem.\n"
                "★ Design Consistent Hashing — critical for distributed system design interviews.\n"
                "★ Bloom filter vs HashSet: which to choose when memory is constrained?\n"
                "★ LFU Cache (LeetCode 460) — extension of LRU using frequency map."
            ),
            "java": """\
import java.util.*;

public class AdvancedHashing {

    // LRU Cache Implementation
    static class LRUCache {
        int capacity;
        Map<Integer, Integer> map = new LinkedHashMap<>() {
            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                return size() > capacity; // Auto-evict LRU
            }
        };

        LRUCache(int cap) { capacity = cap; }

        int get(int key) {
            if (!map.containsKey(key)) return -1;
            int val = map.remove(key);
            map.put(key, val); // move to end (most recently used)
            return val;
        }

        void put(int key, int val) {
            map.remove(key); // remove if exists to reset order
            map.put(key, val);
        }
    }

    public static void main(String[] args) {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 1); cache.put(2, 2);
        System.out.println(cache.get(1));    // 1
        cache.put(3, 3);                      // evicts key 2
        System.out.println(cache.get(2));    // -1 (evicted)
        System.out.println(cache.get(3));    // 3
    }
}"""
        }
    },

    # ==================== GRAPHS ====================
    "Graphs": {
        "Beginner": {
            "definition": (
                "A Graph is a non-linear data structure consisting of a finite set of vertices (or nodes) "
                "and a set of edges that connect pairs of vertices. Graphs can be Directed (edges have arrows) "
                "or Undirected, and Weighted (edges have values) or Unweighted. They are the most versatile "
                "data structure, capable of modeling anything from social networks to city maps and "
                "network routing."
            ),
            "working": (
                "1. VERTEX (Node): An entity in the graph (e.g., a person or city).\n"
                "2. EDGE: A connection between two vertices (e.g., a friendship or road).\n"
                "3. ADJACENCY LIST: Each node has a list of its neighbors (efficient for most graphs).\n"
                "4. ADJACENCY MATRIX: A 2D array where matrix[i][j] is 1 if an edge exists.\n"
                "5. CONNECTEDNESS: Whether there is a path between all pairs of nodes."
            ),
            "algorithm": (
                "BFS (Breadth-First Search):\n"
                "  Visit neighbors layer by layer using a Queue.\n\n"
                "DFS (Depth-First Search):\n"
                "  Visit deep into a path recursively before moving to siblings."
            ),
            "time_complexity": {
                "BFS / DFS": "O(V + E) — vertices + edges",
                "Matrix Search": "O(V²)",
                "Dijkstra": "O(E log V)",
                "Kruskal's MST": "O(E log E)",
                "Topological Sort": "O(V + E)"
            },
            "space_complexity": "O(V + E) for adjacency list; O(V²) for adjacency matrix.",
            "applications": (
                "• Social Networks (Facebook friend graphs)\n"
                "• Google Maps (road networks and traffic routing)\n"
                "• Recommendation Engines (collaborative filtering)\n"
                "• Web Crawling and indexing pages\n"
                "• Dependency management (Package managers like NPM)"
            ),
            "advantages": (
                "• Can model complex relationships that trees cannot (cycles, multiple paths)\n"
                "• Highly flexible and adaptable to many real-world problems\n"
                "• Mature algorithms exist for shortest path and connectivity"
            ),
            "disadvantages": (
                "• Much harder to implement and traverse than linear structures\n"
                "• Large graphs can take significant memory and compute time\n"
                "• Cycle detection and pathfinding can be computationally expensive"
            ),
            "interview_notes": (
                "★ Use BFS for finding the shortest path in an unweighted graph.\n"
                "★ Use DFS for finding paths, cycles, or components.\n"
                "★ Topological Sort: remember this only works on Directed Acyclic Graphs (DAGs).\n"
                "★ Practice representing a graph from an edge list given in LeetCode."
            ),
            "java": """\
import java.util.*;

public class GraphDemo {
    // Adjacency List Representation
    static class Graph {
        int V;
        List<Integer>[] adj;
        Graph(int v) {
            V = v; adj = new ArrayList[v];
            for (int i = 0; i < v; i++) adj[i] = new ArrayList<>();
        }
        void addEdge(int u, int v) { adj[u].add(v); adj[v].add(u); }
    }

    public static void main(String[] args) {
        Graph g = new Graph(4);
        g.addEdge(0, 1); g.addEdge(1, 2); g.addEdge(2, 3);
        System.out.println("Neighbors of node 1: " + g.adj[1]);
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we implement BFS and DFS from scratch and use them to solve "
                "real problems: detecting cycles, finding connected components, and performing topological sort. "
                "Topological Sort (Kahn's Algorithm using BFS, or DFS-based) orders nodes of a DAG so that "
                "for every directed edge (u, v), u appears before v. It is used for task scheduling with "
                "dependencies. Cycle detection in undirected graphs uses DSU or DFS with a parent pointer, "
                "while directed graph cycle detection uses a 'recursion stack' visited set."
            ),
            "working": (
                "TOPOLOGICAL SORT (Kahn's BFS):\n"
                "  Compute in-degrees of all nodes.\n"
                "  Start BFS from nodes with in-degree = 0.\n"
                "  For each processed node, reduce neighbors' in-degrees; add to queue if 0.\n"
                "  If all nodes processed: DAG order found. Else: cycle exists.\n\n"
                "CYCLE DETECTION (Directed - DFS):\n"
                "  visited[] tracks discovered nodes.\n"
                "  recStack[] tracks nodes in current DFS path.\n"
                "  If a neighbor is in recStack: cycle found.\n\n"
                "CONNECTED COMPONENTS (Undirected):\n"
                "  Run DFS/BFS from each unvisited node; each DFS tree = one component."
            ),
            "algorithm": (
                "KAHN'S TOPOLOGICAL SORT:\n"
                "  in-degree[] for all nodes\n"
                "  queue = all nodes with in-degree 0\n"
                "  while queue not empty:\n"
                "    node = dequeue; order.add(node)\n"
                "    for neighbor: in-degree[neighbor]--, if 0: enqueue\n"
                "  if order.size != V: cycle detected (cannot complete sort)\n\n"
                "BFS SHORTEST PATH (Unweighted):\n"
                "  dist[src] = 0; queue = [src]\n"
                "  while queue: pop u; for v in adj[u]: if dist[v]==inf: dist[v]=dist[u]+1; enqueue"
            ),
            "time_complexity": {
                "BFS / DFS Full": "O(V + E)",
                "Topological Sort": "O(V + E)",
                "Cycle Detection Directed": "O(V + E)",
                "Connected Components": "O(V + E)",
                "Bipartite Check": "O(V + E)"
            },
            "space_complexity": "O(V) for visited[], queue, and in-degree arrays.",
            "applications": (
                "• Build system dependency resolution (Make, Gradle)\n"
                "• Course schedule with prerequisites\n"
                "• Network packet routing\n"
                "• Social network friend circle detection\n"
                "• Compiler dependency analysis"
            ),
            "advantages": (
                "• Topological sort is the foundation for DP on DAGs\n"
                "• BFS finds shortest path without weightings\n"
                "• Kahn's algorithm detects cycles as a byproduct"
            ),
            "disadvantages": (
                "• Topological sort only works on DAGs — cycles make it impossible\n"
                "• Connected component analysis requires separate pass for each component\n"
                "• DFS cycle detection state management is error-prone for directed graphs"
            ),
            "interview_notes": (
                "★ Course Schedule (LeetCode 207 & 210) — topological sort classic.\n"
                "★ Number of Islands (LeetCode 200) — count connected components via DFS/BFS.\n"
                "★ Clone Graph (LeetCode 133) — BFS/DFS with HashMap for node mapping.\n"
                "★ Is Graph Bipartite? (LeetCode 785) — BFS 2-coloring check."
            ),
            "java": """\
import java.util.*;

public class IntermediateGraph {

    // Topological Sort (Kahn's BFS)
    static List<Integer> topoSort(int V, List<Integer>[] adj) {
        int[] inDeg = new int[V];
        for (int u = 0; u < V; u++)
            for (int v : adj[u]) inDeg[v]++;

        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < V; i++) if (inDeg[i] == 0) q.offer(i);

        List<Integer> order = new ArrayList<>();
        while (!q.isEmpty()) {
            int u = q.poll();
            order.add(u);
            for (int v : adj[u]) if (--inDeg[v] == 0) q.offer(v);
        }
        return order.size() == V ? order : List.of(); // empty = cycle
    }

    // BFS Shortest Path (unweighted)
    static int[] bfsShortestPath(int V, List<Integer>[] adj, int src) {
        int[] dist = new int[V];
        Arrays.fill(dist, -1);
        dist[src] = 0;
        Queue<Integer> q = new LinkedList<>();
        q.offer(src);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj[u]) if (dist[v] == -1) { dist[v] = dist[u] + 1; q.offer(v); }
        }
        return dist;
    }

    @SuppressWarnings("unchecked")
    public static void main(String[] args) {
        int V = 6;
        List<Integer>[] adj = new ArrayList[V];
        for (int i = 0; i < V; i++) adj[i] = new ArrayList<>();
        adj[5].add(2); adj[5].add(0); adj[4].add(0); adj[4].add(1); adj[2].add(3); adj[3].add(1);
        System.out.println("Topo order: " + topoSort(V, adj)); // [4, 5, 0, 2, 3, 1]
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced graph algorithms include Dijkstra's SSSP with negative weight detection (Bellman-Ford), "
                "Floyd-Warshall for All-Pairs Shortest Path (APSP), Kruskal's and Prim's MST algorithms, "
                "and Tarjan's/Kosaraju's algorithm for Strongly Connected Components (SCCs). "
                "Strongly Connected Components partition a directed graph into subgraphs where every node "
                "can reach every other node. SCC algorithms run in O(V + E) and are used in social network "
                "analysis, compiler optimizations, and Bayesian network inference."
            ),
            "working": (
                "KRUSKAL'S MST:\n"
                "  Sort all edges by weight.\n"
                "  For each edge (u, v): if find(u) != find(v), include edge and union(u, v).\n"
                "  Stop after V-1 edges are included.\n\n"
                "FLOYD-WARSHALL (O(V³)):\n"
                "  dist[i][j] = weight of direct edge (or inf if no edge).\n"
                "  for k: for i: for j: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])\n\n"
                "TARJAN'S SCC (O(V + E)):\n"
                "  DFS with discovery time and low-link values.\n"
                "  Nodes on stack whose low-link = disc time form an SCC."
            ),
            "algorithm": (
                "KRUSKAL'S ALGORITHM:\n"
                "  sort edges by weight\n"
                "  for edge (u, v, w) in sorted order:\n"
                "    if find(u) != find(v): mst.add(edge); union(u, v); totalWeight += w\n"
                "  return mst\n\n"
                "BELLMAN-FORD (detects negative cycles):\n"
                "  relax all edges V-1 times\n"
                "  if any edge still relaxes on V-th pass: negative cycle exists"
            ),
            "time_complexity": {
                "Bellman-Ford": "O(V * E)",
                "Floyd-Warshall": "O(V³)",
                "Kruskal's MST": "O(E log E + E * alpha(V))",
                "Prim's MST": "O(E log V)",
                "Tarjan's SCC": "O(V + E)"
            },
            "space_complexity": "O(V²) for Floyd-Warshall; O(V + E) for others.",
            "applications": (
                "• Network design (MST for minimum cable layout)\n"
                "• Currency arbitrage detection (negative cycle in Bellman-Ford)\n"
                "• Compiler optimization (SCC for detecting mutually recursive functions)\n"
                "• Road network all-pairs distance (Floyd-Warshall)\n"
                "• Social influence analysis (SCC in Twitter follow graphs)"
            ),
            "advantages": (
                "• Kruskal's + DSU is elegant and highly efficient\n"
                "• Bellman-Ford handles negative edges (Dijkstra cannot)\n"
                "• Tarjan's SCC is O(V + E) with a single DFS pass"
            ),
            "disadvantages": (
                "• Floyd-Warshall is O(V³) — impractical for large graphs\n"
                "• Bellman-Ford is O(VE) — much slower than Dijkstra for non-negative graphs\n"
                "• Tarjan's algorithm has complex bookkeeping"
            ),
            "interview_notes": (
                "★ Minimum Spanning Tree (Kruskal's) — know both MST algorithms.\n"
                "★ Critical Connections (LeetCode 1192) — bridges in graph using Tarjan's.\n"
                "★ Alien Dictionary (LeetCode 269) — topological sort + graph construction.\n"
                "★ Floyd-Warshall vs Dijkstra: use Floyd for small dense graphs with APSP needs."
            ),
            "java": """\
import java.util.*;

public class AdvancedGraph {
    static int[] parent, rank;
    static int find(int x) { return parent[x] == x ? x : (parent[x] = find(parent[x])); }
    static boolean union(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        if (rank[px] < rank[py]) { int t = px; px = py; py = t; }
        parent[py] = px;
        if (rank[px] == rank[py]) rank[px]++;
        return true;
    }

    // Kruskal's MST
    static int kruskal(int V, int[][] edges) {
        parent = new int[V]; rank = new int[V];
        for (int i = 0; i < V; i++) parent[i] = i;
        Arrays.sort(edges, Comparator.comparingInt(e -> e[2]));
        int cost = 0;
        for (int[] e : edges) if (union(e[0], e[1])) cost += e[2];
        return cost;
    }

    // Floyd-Warshall APSP
    static int[][] floydWarshall(int V, int[][] dist) {
        for (int k = 0; k < V; k++)
            for (int i = 0; i < V; i++)
                for (int j = 0; j < V; j++)
                    if (dist[i][k] != Integer.MAX_VALUE && dist[k][j] != Integer.MAX_VALUE)
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
        return dist;
    }

    public static void main(String[] args) {
        int[][] edges = {{0,1,4},{0,2,3},{1,3,2},{2,3,1}};
        System.out.println("MST Cost: " + kruskal(4, edges)); // 6
    }
}"""
        }
    },

    # ==================== GREEDY ALGORITHMS ====================
    "Greedy Algorithms": {
        "Beginner": {
            "definition": (
                "A Greedy Algorithm is an algorithmic paradigm that follows the problem-solving heuristic of "
                "making the locally optimal choice at each stage with the hope of finding a global optimum. "
                "It follows the philosophy of 'take what you can get right now.' While greed does not always "
                "lead to the best overall solution, it is highly efficient (often O(n log n)) and works "
                "perfectly for problems with specific mathematical properties."
            ),
            "working": (
                "1. SELECTION: Choose the locally best option (e.g., shortest available edge or highest value per weight).\n"
                "2. FEASIBILITY: Ensure the choice doesn't violate problem constraints.\n"
                "3. IRREVOCABILITY: Once a choice is made, it is never changed or reconsidered.\n"
                "4. OPTIMAL SUBSTRUCTURE: The global solution can be reached by combining local greedy choices."
            ),
            "algorithm": (
                "GREEDY_TEMPLATE:\n"
                "  sort elements based on a greedy criteria\n"
                "  for each element:\n"
                "    if element is feasible: add to solution\n"
                "  return solution"
            ),
            "time_complexity": {
                "Typical Greedy": "O(n log n) — usually dominated by sorting",
                "Fractional Knapsack": "O(n log n)",
                "Huffman Coding": "O(n log n)",
                "Activity Selection": "O(n log n)",
                "Dijkstra": "O(E log V)"
            },
            "space_complexity": "O(n) — to store the input and the solution results.",
            "applications": (
                "• Network designs (Minimum Spanning Trees - Kruskal's/Prim's)\n"
                "• Data compression (Huffman Coding)\n"
                "• Task scheduling and interval management\n"
                "• Currency exchange and change-making (for standard coin systems)\n"
                "• Shortest path algorithms (Dijkstra)"
            ),
            "advantages": (
                "• Extremely fast compared to Dynamic Programming (DP)\n"
                "• Easy to implement and understand\n"
                "• Provides exact or very good approximate solutions for many problems"
            ),
            "disadvantages": (
                "• Can fail to find the optimal solution if choices have long-term consequences\n"
                "• Proving a greedy strategy is correct is often harder than the algorithm itself\n"
                "• Highly sensitive to the initial sorting criteria"
            ),
            "interview_notes": (
                "★ The #1 interview task: explain why a greedy approach works vs. why it fails.\n"
                "★ Practice: Fractional Knapsack (Greedy) vs. 0/1 Knapsack (DP).\n"
                "★ Activity Selection: always sort by Finish Time, not Start Time!\n"
                "★ Greedy is often the first thing you should try before jumping to DP."
            ),
            "java": """\
import java.util.*;

public class GreedyDemo {
    // Activity Selection Problem
    public static int selectActivities(int[][] activities) {
        // Sort by finish time
        Arrays.sort(activities, (a, b) -> Integer.compare(a[1], b[1]));
        
        int count = 1, lastFinish = activities[0][1];
        for (int i = 1; i < activities.length; i++) {
            if (activities[i][0] >= lastFinish) { // If starts after last finished
                count++;
                lastFinish = activities[i][1];
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int[][] acts = {{1, 3}, {2, 5}, {4, 6}, {6, 8}, {5, 9}};
        System.out.println("Max Activities: " + selectActivities(acts)); // 3
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we apply greedy strategies to classic optimization problems: "
                "Huffman Coding, Fractional Knapsack, and Interval Scheduling. Huffman Coding builds an "
                "optimal prefix-free binary encoding for characters by greedily combining the two least "
                "frequent characters into a single node using a Min-Heap. Fractional Knapsack maximizes "
                "value by sorting items by value-to-weight ratio and taking fractions of items. These "
                "contrast with the 0/1 Knapsack problem, which requires Dynamic Programming."
            ),
            "working": (
                "HUFFMAN CODING:\n"
                "  Build a frequency table for all characters.\n"
                "  Add all (freq, char) pairs to a min-heap.\n"
                "  While heap size > 1: merge two smallest nodes into a parent.\n"
                "  The final tree defines variable-length prefix codes.\n"
                "  Most frequent char gets shortest code (e.g., 0), rare chars get longer codes.\n\n"
                "FRACTIONAL KNAPSACK:\n"
                "  Compute value/weight ratio for each item.\n"
                "  Sort descending by ratio.\n"
                "  Greedily fill knapsack, taking fractions if needed."
            ),
            "algorithm": (
                "HUFFMAN CODING:\n"
                "  pq = MinHeap of (freq, node)\n"
                "  while pq.size > 1:\n"
                "    left = pq.poll(); right = pq.poll()\n"
                "    merged = new Node(left.freq + right.freq)\n"
                "    merged.left = left; merged.right = right\n"
                "    pq.add(merged)\n"
                "  root = pq.poll(); encode(root, \"\")"
            ),
            "time_complexity": {
                "Huffman Coding": "O(n log n) — n = number of distinct chars",
                "Fractional Knapsack": "O(n log n) — sorting step dominates",
                "Job Scheduling": "O(n log n)",
                "Interval Merging": "O(n log n)",
                "Minimum Coins": "O(n) — for canonical coin systems"
            },
            "space_complexity": "O(n) for Huffman tree; O(1) extra for Fractional Knapsack.",
            "applications": (
                "• Data compression (ZIP uses Huffman variant DEFLATE)\n"
                "• Task scheduling with deadlines and profits\n"
                "• Interval management in calendar systems\n"
                "• Network bandwidth allocation\n"
                "• JPEG image compression (Huffman coding)"
            ),
            "advantages": (
                "• Huffman is provably optimal for symbol-by-symbol coding\n"
                "• Greedy solutions are simple and fast to implement\n"
                "• No extra memory table needed unlike DP"
            ),
            "disadvantages": (
                "• Greedy doesn't work for 0/1 Knapsack — DP required\n"
                "• Huffman requires two passes (frequency count, then build)\n"
                "• Changing input invalidates the Huffman tree entirely"
            ),
            "interview_notes": (
                "★ Meeting Rooms II (LeetCode 253) — interval scheduling with min-heap.\n"
                "★ Gas Station (LeetCode 134) — greedy from highest surplus point.\n"
                "★ Jump Game (LeetCode 55) — greedy reach tracking.\n"
                "★ Fractional vs 0/1 Knapsack: always clarify which one the interviewer means."
            ),
            "java": """\
import java.util.*;

public class IntermediateGreedy {

    // Huffman Coding (simplified)
    static class HuffNode implements Comparable<HuffNode> {
        char ch; int freq; HuffNode left, right;
        HuffNode(char c, int f) { ch = c; freq = f; }
        HuffNode(int f, HuffNode l, HuffNode r) { freq = f; left = l; right = r; }
        public int compareTo(HuffNode o) { return this.freq - o.freq; }
    }
    static void encode(HuffNode node, String code) {
        if (node.left == null && node.right == null) {
            System.out.println(node.ch + ": " + code); return;
        }
        encode(node.left, code + "0"); encode(node.right, code + "1");
    }
    static void huffman(char[] chars, int[] freqs) {
        PriorityQueue<HuffNode> pq = new PriorityQueue<>();
        for (int i = 0; i < chars.length; i++) pq.offer(new HuffNode(chars[i], freqs[i]));
        while (pq.size() > 1) {
            HuffNode l = pq.poll(), r = pq.poll();
            pq.offer(new HuffNode(l.freq + r.freq, l, r));
        }
        encode(pq.poll(), "");
    }

    // Jump Game - Greedy
    static boolean canJump(int[] nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) return false;
            maxReach = Math.max(maxReach, i + nums[i]);
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println("Huffman codes:");
        huffman(new char[]{'a','b','c','d'}, new int[]{5,20,10,30});
        System.out.println("Can jump [2,3,1,1,4]? " + canJump(new int[]{2,3,1,1,4})); // true
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced greedy concepts include proving greedy correctness using the Exchange Argument, "
                "understanding when greedy fails (0/1 Knapsack, Shortest Superstring), and applying greedy "
                "to graph algorithms like Kruskal's MST and Dijkstra's SSSP. The Exchange Argument proof "
                "technique shows that any optimal solution can be transformed step-by-step into the greedy "
                "solution without worsening quality, proving greedy's optimality. Regret-based greedy "
                "(scheduling to minimize total lateness) and the concept of matroid theory provide a "
                "formal framework for identifying when greedy gives optimal results."
            ),
            "working": (
                "EXCHANGE ARGUMENT PROOF (Activity Selection):\n"
                "  Suppose OPT doesn't start with activity with earliest finish.\n"
                "  Swap OPT's first activity with the greedy choice.\n"
                "  The new solution is at least as good (finishes no later).\n"
                "  By induction, greedy = optimal.\n\n"
                "SCHEDULING TO MINIMIZE LATENESS:\n"
                "  Sort jobs by deadline (earliest deadline first).\n"
                "  Assign each job consecutive time starting from 0.\n"
                "  Maximum lateness is minimized.\n\n"
                "GREEDY FAILS EXAMPLE (0/1 Knapsack):\n"
                "  Items: (v=10, w=5), (v=6, w=4), (v=6, w=4). Capacity=8.\n"
                "  Greedy ratio: picks (10,5) then can't fit others. Value=10.\n"
                "  Optimal: picks both (6,4) items. Value=12. Greedy fails!"
            ),
            "algorithm": (
                "MINIMIZE MAX LATENESS:\n"
                "  sort jobs by deadline: j[0].deadline <= j[1].deadline <= ...\n"
                "  t = 0\n"
                "  for each job: start = t; finish = t + duration; lateness = max(0, finish - deadline)\n"
                "  t += duration\n"
                "  return max lateness across all jobs\n\n"
                "WHEN GREEDY IS OPTIMAL:\n"
                "  Problem has matroid structure: hereditary property and exchange property."
            ),
            "time_complexity": {
                "Minimize Lateness": "O(n log n)",
                "Kruskal's MST": "O(E log E)",
                "Dijkstra (greedy)": "O(E log V)",
                "Huffman Coding": "O(n log n)",
                "Regret-Based Greedy": "O(n log n)"
            },
            "space_complexity": "O(1) to O(n) depending on problem; most greedy solutions are O(1) extra.",
            "applications": (
                "• Optimal file compression (Huffman, Arithmetic coding)\n"
                "• Network design and MST construction\n"
                "• OS process scheduling algorithms\n"
                "• Financial market making (bid/ask greedy strategies)\n"
                "• DNA sequence local alignment"
            ),
            "advantages": (
                "• When applicable, greedy is always faster than DP or backtracking\n"
                "• Exchange argument proofs are elegant and rigorous\n"
                "• Matroid theory provides a formal framework for greedy applicability"
            ),
            "disadvantages": (
                "• Proving greedy correctness requires non-trivial mathematical argument\n"
                "• Easy to misidentify a greedy solution for a problem that requires DP\n"
                "• No general algorithm to determine if greedy works — must prove each case"
            ),
            "interview_notes": (
                "★ Minimum number of platforms (sorting-based greedy) — O(n log n).\n"
                "★ Candy distribution (LeetCode 135) — two-pass greedy.\n"
                "★ Task Scheduler (LeetCode 621) — greedy with max-heap.\n"
                "★ Explain why greedy fails for 0/1 Knapsack with a concrete counterexample."
            ),
            "java": """\
import java.util.*;

public class AdvancedGreedy {

    // Minimize Maximum Lateness (EDF Scheduling)
    static int minMaxLateness(int[] durations, int[] deadlines) {
        int n = durations.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, Comparator.comparingInt(i -> deadlines[i])); // EDF

        int t = 0, maxLate = 0;
        for (int i : idx) {
            t += durations[i];
            maxLate = Math.max(maxLate, t - deadlines[i]);
        }
        return maxLate;
    }

    // Task Scheduler (LeetCode 621)
    static int leastInterval(char[] tasks, int n) {
        int[] count = new int[26];
        for (char c : tasks) count[c - 'A']++;
        int maxFreq = Arrays.stream(count).max().getAsInt();
        int maxCount = 0;
        for (int c : count) if (c == maxFreq) maxCount++;
        return Math.max(tasks.length, (maxFreq - 1) * (n + 1) + maxCount);
    }

    public static void main(String[] args) {
        System.out.println("Max Lateness: " + minMaxLateness(new int[]{3,2,1}, new int[]{6,8,9})); // 0
        System.out.println("Min Intervals: " + leastInterval(new char[]{'A','A','A','B','B','B'}, 2)); // 8
    }
}"""
        }
    },

    # ==================== DYNAMIC PROGRAMMING ====================
    "Dynamic Programming": {
        "Beginner": {
            "definition": (
                "Dynamic Programming (DP) is a method for solving complex problems by breaking them down into "
                "simpler subproblems and storing the results of these subproblems to avoid redundant "
                "computations. It is applicable to problems that exhibit 'Optimal Substructure' and "
                "'Overlapping Subproblems.' Think of it as recursion with memory: instead of re-calculating "
                "the same value repeatedly, you calculate it once and look it up in a table (cache) later."
            ),
            "working": (
                "1. DEFINE STATE: Identify the variables that uniquely describe a subproblem.\n"
                "2. RECURSION RELATION: Express the solution of a large problem in terms of smaller ones.\n"
                "3. MEMOIZATION (Top-Down): Start from the goal and recurse, saving results in a map/array.\n"
                "4. TABULATION (Bottom-Up): Start from base cases and fill a table iteratively until the goal is reached.\n"
                "5. BASE CASE: The simplest versions of the problem with known solutions."
            ),
            "algorithm": (
                "FIBONACCI_TABULATION(n):\n"
                "  dp = [0, 1] + [0]*(n-1)\n"
                "  for i from 2 to n:\n"
                "    dp[i] = dp[i-1] + dp[i-2]\n"
                "  return dp[n]\n\n"
                "0/1_KNAPSACK_RECURRENCE:\n"
                "  dp[i][w] = max(dp[i-1][w], val[i] + dp[i-1][w-weight[i]])"
            ),
            "time_complexity": {
                "Fibonacci": "O(n)",
                "Knapsack": "O(n * W)",
                "LCS": "O(n * m)",
                "Edit Distance": "O(n * m)",
                "Coin Change": "O(n * amount)"
            },
            "space_complexity": "O(n) or O(n * m) — for storing the DP table. Can often be optimized to O(n).",
            "applications": (
                "• Optimization problems (finding the best, shortest, or cheapest path)\n"
                "• Bioinformatics (DNA sequence alignment)\n"
                "• Financial modeling (Investment strategies)\n"
                "• Text processing (Diff and merge tools)\n"
                "• Determining change for a sum with specific coins"
            ),
            "advantages": (
                "• Dramatic speedup over naive recursion (Exponential to Linear/Polynomial)\n"
                "• Guarantees an optimal solution if correctly formulated\n"
                "• Systematic approach to solving complex problems"
            ),
            "disadvantages": (
                "• High memory consumption for multi-dimensional DP tables\n"
                "• Can be difficult to identify the correct 'state' and transitions\n"
                "• Purely mathematical thinking required for recurrence relations"
            ),
            "interview_notes": (
                "★ Start with the recursive solution first, then optimize with DP.\n"
                "★ Practice the '5 Steps Table': State, Base Case, Transition, Goal, Order.\n"
                "★ Longest Common Subsequence (LeetCode 1143) is the fundamental DP model.\n"
                "★ Space optimization: mention that we usually only need the previous row/state."
            ),
            "java": """\
public class DPDemo {
    // Bottom-Up Tabulation for Fibonacci
    public static long fib(int n) {
        if (n <= 1) return n;
        long[] dp = new long[n + 1];
        dp[0] = 0; dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }

    // 0/1 Knapsack recursive with memoization
    static Integer[][] memo = new Integer[101][1001];
    public static int knapsack(int[] wt, int[] val, int w, int n) {
        if (n == 0 || w == 0) return 0;
        if (memo[n][w] != null) return memo[n][w];
        
        if (wt[n-1] > w) return memo[n][w] = knapsack(wt, val, w, n-1);
        else return memo[n][w] = Math.max(
            val[n-1] + knapsack(wt, val, w - wt[n-1], n-1),
            knapsack(wt, val, w, n-1)
        );
    }

    public static void main(String[] args) {
        System.out.println("Fib(50): " + fib(50));
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we tackle the core DP patterns: Longest Common Subsequence (LCS), "
                "Longest Increasing Subsequence (LIS), Coin Change, Unbounded Knapsack, and Matrix Chain "
                "Multiplication. The LCS pattern (comparing two sequences character by character) is the "
                "template for many string DP problems like Edit Distance and Minimum ASCII Delete Sum. "
                "Space optimization is a key skill: for many 2D DP tables, only the previous row needs to "
                "be stored, reducing space from O(n*m) to O(m)."
            ),
            "working": (
                "LCS (Longest Common Subsequence):\n"
                "  if s1[i] == s2[j]: dp[i][j] = 1 + dp[i-1][j-1]\n"
                "  else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n\n"
                "EDIT DISTANCE (Levenshtein):\n"
                "  if s1[i]==s2[j]: dp[i][j] = dp[i-1][j-1]\n"
                "  else: dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) (replace, delete, insert)\n\n"
                "LIS (Patience Sorting / DP):\n"
                "  dp[i] = max length of IS ending at index i\n"
                "  dp[i] = 1 + max(dp[j]) for j < i and arr[j] < arr[i]"
            ),
            "algorithm": (
                "COIN CHANGE (Minimum Coins):\n"
                "  dp[0] = 0; dp[1..amount] = infinity\n"
                "  for each coin:\n"
                "    for amount from coin to target:\n"
                "      dp[amount] = min(dp[amount], 1 + dp[amount - coin])\n"
                "  return dp[target] (or -1 if infinity)\n\n"
                "LCS SPACE OPTIMIZED:\n"
                "  Use rolling 1D array: process col by col, keeping only current + previous value"
            ),
            "time_complexity": {
                "LCS": "O(n * m)",
                "Edit Distance": "O(n * m)",
                "Coin Change": "O(n * amount)",
                "LIS (DP)": "O(n²)",
                "LIS (Patience Sorting)": "O(n log n)"
            },
            "space_complexity": "O(n * m) for 2D DP; O(m) with space optimization.",
            "applications": (
                "• Spell checking (Edit Distance)\n"
                "• DNA sequence alignment (LCS)\n"
                "• Diff tools for version control (LCS of file lines)\n"
                "• Optimal change-making in vending machines\n"
                "• Stock market trading strategies (LIS variant)"
            ),
            "advantages": (
                "• DP with space optimization reduces memory dramatically\n"
                "• One recurrence handles many problems (LCS template)\n"
                "• Bottom-up DP avoids recursion overhead"
            ),
            "disadvantages": (
                "• High memory for multi-dimensional DP tables\n"
                "• Identifying state and transition is problem-specific and non-obvious\n"
                "• DP solutions can be hard to extend or modify"
            ),
            "interview_notes": (
                "★ Longest Common Subsequence (LeetCode 1143) — foundational 2D DP.\n"
                "★ Edit Distance (LeetCode 72) — the three transitions (replace, insert, delete).\n"
                "★ Coin Change (LeetCode 322) — unbounded knapsack pattern.\n"
                "★ Russian Doll Envelopes (LeetCode 354) — LIS in O(n log n)."
            ),
            "java": """\
public class IntermediateDP {

    // LCS
    static int lcs(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        int[][] dp = new int[n+1][m+1];
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                dp[i][j] = s1.charAt(i-1) == s2.charAt(j-1)
                    ? 1 + dp[i-1][j-1]
                    : Math.max(dp[i-1][j], dp[i][j-1]);
        return dp[n][m];
    }

    // Coin Change
    static int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        java.util.Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int coin : coins)
            for (int i = coin; i <= amount; i++)
                dp[i] = Math.min(dp[i], 1 + dp[i - coin]);
        return dp[amount] > amount ? -1 : dp[amount];
    }

    // Edit Distance
    static int editDistance(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        int[][] dp = new int[n+1][m+1];
        for (int i = 0; i <= n; i++) dp[i][0] = i;
        for (int j = 0; j <= m; j++) dp[0][j] = j;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                dp[i][j] = s1.charAt(i-1) == s2.charAt(j-1) ? dp[i-1][j-1]
                    : 1 + Math.min(dp[i-1][j-1], Math.min(dp[i-1][j], dp[i][j-1]));
        return dp[n][m];
    }

    public static void main(String[] args) {
        System.out.println("LCS:  " + lcs("ABCBDAB", "BDCAB")); // 4
        System.out.println("Coins: " + coinChange(new int[]{1,5,11}, 15)); // 3
        System.out.println("Edit:  " + editDistance("horse", "ros")); // 3
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced DP encompasses Bitmask DP (for TSP-style problems on small sets), Interval DP "
                "(for problems on subarrays like Matrix Chain Multiplication and Burst Balloons), and "
                "DP on Trees. Bitmask DP represents the visited/selected subset as a bitmask, enabling "
                "O(2^n * n) solutions for NP-Hard problems on small inputs. Tree DP computes results "
                "bottom-up on trees and is used for House Robber on Trees and Minimum Vertex Cover. "
                "The Broken Profile DP enables optimization over a grid cell by cell."
            ),
            "working": (
                "BITMASK DP (TSP variant):\n"
                "  dp[mask][node] = min cost to visit subset 'mask' ending at 'node'.\n"
                "  Transition: for each unvisited node j not in mask:\n"
                "    dp[mask | (1<<j)][j] = min(dp[mask | (1<<j)][j], dp[mask][i] + cost[i][j])\n\n"
                "INTERVAL DP (Burst Balloons):\n"
                "  dp[i][j] = max coins from bursting all balloons between i and j.\n"
                "  Try each balloon k as the LAST to burst in range [i,j].\n"
                "  dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1])\n\n"
                "TREE DP:\n"
                "  dp[node][0] = max value NOT selecting current node.\n"
                "  dp[node][1] = max value SELECTING current node.\n"
                "  Recurse and combine child states."
            ),
            "algorithm": (
                "BITMASK DP (Assignment Problem):\n"
                "  dp = {0: [0, ...inf...][n]}\n"
                "  for mask from 1 to (1<<n)-1:\n"
                "    person = popcount(mask) - 1  // which person is this mask for?\n"
                "    for task from 0 to n-1:\n"
                "      if bit task is set in mask:\n"
                "        dp[mask][task] = min over dp[mask ^ (1<<task)][prev] + cost[person][task]"
            ),
            "time_complexity": {
                "Bitmask DP (TSP)": "O(2^n * n²)",
                "Interval DP (Burst Balloons)": "O(n³)",
                "Tree DP (Max Independent Set)": "O(n)",
                "Broken Profile DP": "O(2^cols * rows * cols)",
                "DP on Digits": "O(n * 10 * 2) per digit constraint"
            },
            "space_complexity": "O(2^n * n) for bitmask DP; O(n²) for interval DP; O(n) for tree DP.",
            "applications": (
                "• Traveling Salesman Problem approximations\n"
                "• Job assignment optimization\n"
                "• Balloon burst game theory problems\n"
                "• Minimum Vertex Cover on trees\n"
                "• Scheduling problems with state encoding"
            ),
            "advantages": (
                "• Bitmask DP gives exact solutions for NP-Hard problems on small inputs (n <= 20)\n"
                "• Interval DP is the correct approach for all contiguous subarray problems\n"
                "• Tree DP elegantly handles tree-structured constraint problems"
            ),
            "disadvantages": (
                "• Bitmask DP memory is O(2^n * n) — infeasible for n > 25\n"
                "• Interval DP is O(n³) — may TLE for n > 500\n"
                "• Hard to recognize which DP variant applies to a given problem"
            ),
            "interview_notes": (
                "★ Burst Balloons (LeetCode 312) — interval DP with 'last to burst' insight.\n"
                "★ Minimum cost to merge stones (LeetCode 1000) — interval DP variant.\n"
                "★ House Robber III (LeetCode 337) — tree DP returning (rob, skip) pairs.\n"
                "★ Bitmask DP is often hinted by 'n <= 20 & visiting all nodes' constraints."
            ),
            "java": """\
public class AdvancedDP {

    // House Robber III (Tree DP)
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    static int[] robTree(TreeNode root) {
        if (root == null) return new int[]{0, 0};
        int[] left = robTree(root.left);
        int[] right = robTree(root.right);
        // [0] = max profit NOT robbing this node
        // [1] = max profit robbing this node
        int skip = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        int rob = root.val + left[0] + right[0];
        return new int[]{skip, rob};
    }

    // Longest Increasing Subsequence O(n log n)
    static int lisLength(int[] nums) {
        java.util.ArrayList<Integer> tails = new java.util.ArrayList<>();
        for (int num : nums) {
            int lo = 0, hi = tails.size();
            while (lo < hi) { int mid = (lo+hi)/2; if (tails.get(mid) < num) lo=mid+1; else hi=mid; }
            if (lo == tails.size()) tails.add(num);
            else tails.set(lo, num);
        }
        return tails.size();
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(2); root.right = new TreeNode(3);
        root.left.right = new TreeNode(3); root.right.right = new TreeNode(1);
        int[] res = robTree(root);
        System.out.println("Max rob: " + Math.max(res[0], res[1])); // 7

        int[] nums = {10, 9, 2, 5, 3, 7, 101, 18};
        System.out.println("LIS length: " + lisLength(nums)); // 4
    }
}"""
        }
    },

    # ==================== BIT MANIPULATION ====================
    "Bit Manipulation": {
        "Beginner": {
            "definition": (
                "Bit Manipulation involves performing operations directly on the individual bits (0s and 1s) "
                "that make up a data type. It uses bitwise operators like AND (&), OR (|), XOR (^), NOT (~), "
                "and bit shifts (<<, >>). This is extremely efficient and used in low-level systems "
                "programming, cryptography, and competitive programming to optimize performance and memory."
            ),
            "working": (
                "1. AND (&): 1 if both bits are 1. Clears bits.\n"
                "2. OR (|): 1 if either bit is 1. Sets bits.\n"
                "3. XOR (^): 1 if bits are different. x ^ x = 0; x ^ 0 = x.\n"
                "4. NOT (~): Flips all bits (0 becomes 1, 1 becomes 0).\n"
                "5. SHIFT: `x << k` multiplies x by 2^k; `x >> k` divides by 2^k."
            ),
            "algorithm": (
                "CHECK_IF_ODD(n):\n"
                "  return (n & 1) == 1\n\n"
                "SET_BIT(n, i):\n"
                "  return n | (1 << i)\n\n"
                "CLEAR_BIT(n, i):\n"
                "  return n & ~(1 << i)\n\n"
                "IS_POWER_OF_2(n):\n"
                "  return n > 0 && (n & (n-1)) == 0"
            ),
            "time_complexity": {
                "Bitwise Ops": "O(1) — single CPU instruction",
                "Count Set Bits": "O(number of bits) or O(1) via __builtin_popcount",
                "Bit Revision": "O(1)"
            },
            "space_complexity": "O(1) — operations happen in-place within registers.",
            "applications": (
                "• Graphics and image processing (pixel manipulation)\n"
                "• Device drivers and hardware level programming\n"
                "• Compression algorithms and encryption\n"
                "• Efficient Flag management (one byte for 8 booleans)\n"
                "• Optimization in high-performance engines"
            ),
            "advantages": (
                "• The fastest possible operations in computing\n"
                "• Consumes zero heap memory\n"
                "• Powerful tricks for solving problems (e.g., finding the single non-duplicate number)"
            ),
            "disadvantages": (
                "• Code is hard to read and maintain for non-experts\n"
                "• Platform dependent (Endianness, bit-width differences)\n"
                "• Prone to difficult-to-catch overflow bugs"
            ),
            "interview_notes": (
                "★ Master the XOR trick: finding the 'One Unique Element' (LeetCode 136).\n"
                "★ Count set bits (Hamming Weight): practice Brian Kernighan’s algorithm.\n"
                "★ Bit Shifting: understand the difference between logical (>>>) and arithmetic (>>) shifts.\n"
                "★ Power of two check (n & (n-1)) is a very common warm-up question."
            ),
            "java": """\
public class BitDemo {
    public static void main(String[] args) {
        int n = 5; // binary 101

        // 1. Check if i-th bit is set
        boolean isSet = (n & (1 << 2)) != 0; // check bit at pos 2
        System.out.println("Bit at pos 2 set? " + isSet);

        // 2. Count set bits
        System.out.println("Set bits: " + Integer.bitCount(n));

        // 3. XOR Trick: Find unique element
        int[] arr = {2, 3, 5, 3, 2};
        int res = 0;
        for(int x : arr) res ^= x;
        System.out.println("Unique element: " + res); // 5
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, bit manipulation is used to solve classic problems: find the "
                "single non-duplicate number (XOR approach), count set bits (Brian Kernighan's Algorithm), "
                "generate all subsets of a set using bitmask enumeration, and implement addition without "
                "using the '+' operator. Bitmask enumeration — iterating through all 2^n subsets of an "
                "n-element set by iterating from 0 to (1<<n)-1 and checking each bit — is a powerful "
                "technique for exponential search in a compact and cache-friendly way."
            ),
            "working": (
                "GENERATE ALL SUBSETS (Bitmask):\n"
                "  for mask from 0 to (1<<n)-1:\n"
                "    for bit from 0 to n-1:\n"
                "      if mask & (1 << bit): include element[bit] in subset\n\n"
                "BRIAN KERNIGHAN'S (Count Set Bits):\n"
                "  count = 0\n"
                "  while n != 0: n = n & (n-1); count++ // removes lowest set bit each time\n\n"
                "ADD WITHOUT PLUS:\n"
                "  while b != 0: carry = a & b; a = a ^ b; b = carry << 1\n"
                "  sum = a"
            ),
            "algorithm": (
                "FIND TWO NON-DUPLICATE NUMBERS (XOR trick):\n"
                "  xor = XOR of all elements (gives xor of two unique numbers)\n"
                "  bit = xor & (-xor)  // rightmost set bit distinguishes the two numbers\n"
                "  a, b = 0, 0\n"
                "  for each element: if element & bit: a ^= element; else b ^= element\n"
                "  return a, b\n\n"
                "SUBSET SUM USING BITMASK:\n"
                "  for mask: sum = sum of elements where bit is set; check if sum == target"
            ),
            "time_complexity": {
                "Bitmask Subset Enumeration": "O(2^n * n) — n elements",
                "Brian Kernighan's Bit Count": "O(number of set bits)",
                "Add Without +": "O(number of bit carries)",
                "Find Two Non-Duplicates": "O(n)",
                "Reverse Bits": "O(32) = O(1)"
            },
            "space_complexity": "O(1) for all intermediate bit manipulation tricks.",
            "applications": (
                "• Compact state representation in game AI and combinatorial search\n"
                "• Feature flags using integer bitmasks\n"
                "• Fast set operations (union, intersection, difference) using OR, AND, XOR\n"
                "• Error detection/correction codes\n"
                "• Hardware register manipulation in embedded systems"
            ),
            "advantages": (
                "• Bitmask subsets use 2x less memory than explicit list tracking\n"
                "• Bitwise operations are single CPU cycles — fastest possible\n"
                "• XOR tricks solve duplicate-finding in O(n) time and O(1) space"
            ),
            "disadvantages": (
                "• Code readability suffers dramatically\n"
                "• Works only for small n (typically n <= 20-25 for bitmask DP)\n"
                "• Signed vs unsigned integer behavior is platform-dependent"
            ),
            "interview_notes": (
                "★ Single Number II (LeetCode 137) — XOR + bitmask for number appearing 2/3 times.\n"
                "★ Missing Number (LeetCode 268) — XOR all indices and values.\n"
                "★ Counting Bits (LeetCode 338) — dp[i] = dp[i >> 1] + (i & 1).\n"
                "★ Add without Plus (LeetCode 371) — XOR as sum, AND-shift as carry."
            ),
            "java": """\
public class IntermediateBit {

    // Brian Kernighan's: Count Set Bits O(number of 1s)
    static int countBits(int n) {
        int count = 0;
        while (n != 0) { n &= (n - 1); count++; }
        return count;
    }

    // Generate all subsets using bitmask
    static void allSubsets(int[] arr) {
        int n = arr.length;
        for (int mask = 0; mask < (1 << n); mask++) {
            System.out.print("{ ");
            for (int i = 0; i < n; i++)
                if ((mask & (1 << i)) != 0) System.out.print(arr[i] + " ");
            System.out.println("}");
        }
    }

    // Find two non-duplicate numbers
    static int[] findTwoUnique(int[] nums) {
        int xor = 0;
        for (int n : nums) xor ^= n;
        int bit = xor & (-xor); // lowest set bit
        int a = 0, b = 0;
        for (int n : nums) { if ((n & bit) != 0) a ^= n; else b ^= n; }
        return new int[]{a, b};
    }

    public static void main(String[] args) {
        System.out.println("Set bits in 13 (1101): " + countBits(13)); // 3
        System.out.println("Subsets of [1,2,3]:"); allSubsets(new int[]{1, 2, 3}); // 8 subsets
        int[] res = findTwoUnique(new int[]{1,2,1,3,2,5});
        System.out.println("Two unique: " + res[0] + " and " + res[1]); // 3 and 5
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced bit manipulation combines bitmasks with DP (Bitmask DP), applies bitwise tricks "
                "to optimize graph algorithms, and uses intrinsic processor functions. Key techniques "
                "include: Gosper's Hack for enumerating all subsets of size k in O(1) per step, "
                "Lowest Set Bit isolation (n & -n), subset enumeration via 'submask = (submask - 1) & mask', "
                "and SIMD vectorization using bitwise ops for bulk data processing. In competitive programming, "
                "bitset-accelerated DP reduces O(n^2 / w) operations by using 64-bit words as bit vectors."
            ),
            "working": (
                "GOSPER'S HACK (next k-bit permutation):\n"
                "  c = n & -n\n"
                "  r = n + c\n"
                "  next = (((r ^ n) >> 2) / c) | r\n"
                "  Used to iterate all C(n,k) subsets of size k.\n\n"
                "SUBSET ENUMERATION OF MASK:\n"
                "  for sub = mask; sub > 0; sub = (sub - 1) & mask:\n"
                "    process subset 'sub'\n"
                "  (also processes sub = 0)\n\n"
                "BITSET DP (Shortest Superstring):\n"
                "  Represent visited set as bitmask; accelerate transition using 64-bit words."
            ),
            "algorithm": (
                "MAXIMUM SUBSET XOR:\n"
                "  Sort descending; use Gaussian elimination on bits\n"
                "  basis[]: for each number, reduce via XOR with basis elements\n\n"
                "NEXT PERMUTATION OF BITMASK (Gosper):\n"
                "  c = x & (-x); r = x + c\n"
                "  x = (((r^x) >> 2) / c) | r  // O(1)"
            ),
            "time_complexity": {
                "Subset Enumeration of Mask": "O(2^population(mask)) total",
                "Gosper's Hack (k subsets)": "O(C(n,k)) total",
                "Bitset-Accelerated DP": "O(n² / 64)",
                "Maximum XOR (Gaussian Elim)": "O(32 * n)",
                "Segment OR / prefix XOR": "O(n)"
            },
            "space_complexity": "O(2^n) for bitmask DP state; O(n) for XOR basis.",
            "applications": (
                "• Genetic algorithms with binary genome encoding\n"
                "• SIMD vectorized array operations in systems programming\n"
                "• Compact graph encoding in competitive programming\n"
                "• FEC (Forward Error Correction) in communications\n"
                "• Chess engine bitboard representation"
            ),
            "advantages": (
                "• Bitset DP gives 64x speedup over naive implementations\n"
                "• Gosper's Hack generates k-subsets in optimal order\n"
                "• XOR basis enables O(32n) maximum XOR queries"
            ),
            "disadvantages": (
                "• Extremely low code readability and maintainability\n"
                "• Architecture-dependent: assumes 64-bit words\n"
                "• Challenging to debug and verify correctness"
            ),
            "interview_notes": (
                "★ Maximum XOR of Two Numbers (LeetCode 421) — greedy bit by bit using XOR prefix.\n"
                "★ AND of Numbers in Range (LeetCode 201) — bit-level pattern recognition.\n"
                "★ Subsets with Bitmask DP (LeetCode 78/90) — O(2^n) enumeration.\n"
                "★ Know Gosper's Hack for iterating exactly C(n,k) subsets in interviews."
            ),
            "java": """\
public class AdvancedBit {

    // XOR Basis (Maximum XOR)
    static int[] basis = new int[30];
    static void insert(int num) {
        for (int b : basis) {
            if (b == 0 || num == 0) break;
            num = Math.min(num, num ^ b);
        }
        if (num > 0) basis[Integer.numberOfLeadingZeros(num)] = num;
    }
    static int queryMax(int num) {
        for (int b : basis) num = Math.max(num, num ^ b);
        return num;
    }

    // Subset Enumeration of a Mask
    static void subsetEnum(int mask) {
        for (int sub = mask; sub > 0; sub = (sub - 1) & mask) {
            System.out.print(Integer.toBinaryString(sub) + " ");
        }
    }

    public static void main(String[] args) {
        // Maximum XOR from array [3, 10, 5, 25, 2, 8]
        int[] nums = {3, 10, 5, 25, 2, 8};
        for (int n : nums) insert(n);
        System.out.println("Max XOR: " + queryMax(0)); // 28 (5 XOR 25)

        System.out.print("Subsets of 0b1011: ");
        subsetEnum(0b1011); // 1011 1010 1001 1000 0011 0010 0001
    }
}"""
        }
    },

    # ==================== TRIES ====================
    "Tries": {
        "Beginner": {
            "definition": (
                "A Trie (pronounced 'try'), or Prefix Tree, is a tree-like data structure used for storing "
                "a dynamic set of strings where keys are usually strings. Unlike a binary search tree, no "
                "node in the tree stores the key associated with that node; instead, its position in the tree "
                "defines the key. All descendants of a node share a common prefix, making it extremely efficient "
                "for dictionary lookups and autocomplete search."
            ),
            "working": (
                "1. ROOT: Represents an empty string, serves as the starting point.\n"
                "2. PATHS: Each edge is labeled with a character (a-z, etc.).\n"
                "3. NODES: Usually contain an array/map of child pointers and a boolean 'isEndOfWord'.\n"
                "4. PREFIX MATCHING: Searching for 'App' finds the node where all words starting with 'App' reside."
            ),
            "algorithm": (
                "INSERT(word):\n"
                "  curr = root\n"
                "  for char c in word:\n"
                "    if c not in curr.children: add child node\n"
                "    curr = curr.children[c]\n"
                "  curr.isEndOfWord = true\n\n"
                "SEARCH(word):\n"
                "  traverse path of chars; return true if path exists and final node.isEndOfWord is true"
            ),
            "time_complexity": {
                "Insert": "O(L) — where L is word length",
                "Search": "O(L)",
                "Prefix Search": "O(L)",
                "Delete": "O(L)"
            },
            "space_complexity": "O(AlphabetSize * WordCount * AverageLength) — can be memory-heavy.",
            "applications": (
                "• Autocomplete and predictive text suggestions\n"
                "• Spell checkers and dictionary lookups\n"
                "• IP routing (longest prefix matching)\n"
                "• Bioinformatics (matching DNA patterns)\n"
                "• T9 predictive text for old mobile phones"
            ),
            "advantages": (
                "• Faster than HashMaps for some string searches (no hash conflicts)\n"
                "• Naturally supports alphabetical ordering\n"
                "• Efficiently handles shared prefixes (saves space for overlapping words)"
            ),
            "disadvantages": (
                "• Large memory overhead for sparse data sets (lots of null pointers)\n"
                "• More complex to implement delete logic than BST\n"
                "• Slower than a hash map for exact full-string match because of pointer hopping"
            ),
            "interview_notes": (
                "★ Implement 'Prefix Search' alongside 'Word Search'.\n"
                "★ Discuss memory optimization using a HashMap in each node instead of a fixed array.\n"
                "★ Be ready to implement a Trie from scratch (LeetCode 208).\n"
                "★ Application: Longest Common Prefix (LCP) and Word Search puzzles."
            ),
            "java": """\
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false;
}

public class TrieDemo {
    TrieNode root = new TrieNode();

    public void insert(String word) {
        TrieNode curr = root;
        for(char c : word.toCharArray()) {
            int idx = c - 'a';
            if(curr.children[idx] == null) curr.children[idx] = new TrieNode();
            curr = curr.children[idx];
        }
        curr.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode curr = root;
        for(char c : word.toCharArray()) {
            int idx = c - 'a';
            if(curr.children[idx] == null) return false;
            curr = curr.children[idx];
        }
        return curr.isEnd;
    }

    public static void main(String[] args) {
        TrieDemo t = new TrieDemo();
        t.insert("apple");
        System.out.println("Has apple? " + t.search("apple")); // true
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we extend Trie functionality to support prefix search and "
                "deletion, and solve more advanced problems like Word Search II (combining Trie with DFS "
                "grid search). We also study compressed variants: the Patricia Trie (Radix Tree) stores "
                "edges as strings instead of individual characters, reducing the number of nodes dramatically "
                "for sparse sets. The 'count' field in each Trie node tracks how many words pass through it, "
                "enabling efficient word frequency counting and prefix frequency queries."
            ),
            "working": (
                "TRIE WITH COUNT:\n"
                "  Each node stores: children[26], isEnd, count.\n"
                "  On insert: increment count for each traversed node.\n"
                "  countWordsWithPrefix(prefix): traverse to prefix end; return count at that node.\n\n"
                "TRIE DELETION:\n"
                "  Traverse to end of word; set isEnd = false.\n"
                "  Recursively delete nodes that are now unreferenced (all children null and !isEnd).\n\n"
                "WORD SEARCH II (Trie + DFS):\n"
                "  Build Trie from word list.\n"
                "  DFS from each grid cell; at each step check if Trie path continues.\n"
                "  Mark found words in Trie; backtrack by restoring grid character."
            ),
            "algorithm": (
                "STARTS WITH (Prefix Search):\n"
                "  curr = root; for each char: if child null: return false; else: move to child\n"
                "  return true  // prefix found\n\n"
                "AUTOCOMPLETE (Suggest):\n"
                "  Navigate to prefix node.\n"
                "  DFS from that node: collect all words ending with isEnd=true."
            ),
            "time_complexity": {
                "Insert with Count": "O(L)",
                "Prefix Count": "O(L)",
                "Delete (recursive)": "O(L)",
                "Autocomplete (collect)": "O(L + output)",
                "Word Search II (all words)": "O(M * N * 4^L * W) with pruning"
            },
            "space_complexity": "O(n * L * 26) for standard Trie; O(n * L) for compressed Patricia Trie.",
            "applications": (
                "• Search engine autocomplete and query suggestion\n"
                "• Contact list search in smartphones\n"
                "• IDE code completion and IntelliSense\n"
                "• Network IP address prefix routing tables\n"
                "• DNA motif pattern searching"
            ),
            "advantages": (
                "• Prefix queries are O(L) regardless of how many words exist\n"
                "• Shared prefixes save memory vs storing words as individual strings\n"
                "• Count field enables frequency analytics without extra data structures"
            ),
            "disadvantages": (
                "• Deletion is complex and requires careful null-checking\n"
                "• High memory for alphabets larger than 26 (e.g., Unicode)\n"
                "• HashMap at each node is more flexible but slower than array[26]"
            ),
            "interview_notes": (
                "★ Word Search II (LeetCode 212) — combine Trie with backtracking DFS.\n"
                "★ Replace Words (LeetCode 648) — find shortest root prefix using Trie.\n"
                "★ Implement Magic Dictionary (LeetCode 676) — Trie with one-miss search.\n"
                "★ Design Search Autocomplete System (LeetCode 642) — Trie + sort."
            ),
            "java": """\
import java.util.*;

public class IntermediateTrie {
    static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd;
        int count; // words passing through this node
    }
    TrieNode root = new TrieNode();

    void insert(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            int i = c - 'a';
            if (cur.children[i] == null) cur.children[i] = new TrieNode();
            cur = cur.children[i];
            cur.count++;
        }
        cur.isEnd = true;
    }

    int countWithPrefix(String prefix) {
        TrieNode cur = root;
        for (char c : prefix.toCharArray()) {
            int i = c - 'a';
            if (cur.children[i] == null) return 0;
            cur = cur.children[i];
        }
        return cur.count;
    }

    List<String> autocomplete(String prefix) {
        TrieNode cur = root;
        for (char c : prefix.toCharArray()) {
            int i = c - 'a';
            if (cur.children[i] == null) return List.of();
            cur = cur.children[i];
        }
        List<String> result = new ArrayList<>();
        dfs(cur, new StringBuilder(prefix), result);
        return result;
    }
    void dfs(TrieNode node, StringBuilder sb, List<String> result) {
        if (node.isEnd) result.add(sb.toString());
        for (int i = 0; i < 26; i++) {
            if (node.children[i] != null) {
                dfs(node.children[i], sb.append((char)('a'+i)), result);
                sb.deleteCharAt(sb.length() - 1);
            }
        }
    }

    public static void main(String[] args) {
        IntermediateTrie t = new IntermediateTrie();
        t.insert("apple"); t.insert("app"); t.insert("applet"); t.insert("ball");
        System.out.println("Count with prefix 'app': " + t.countWithPrefix("app")); // 3
        System.out.println("Autocomplete 'app': " + t.autocomplete("app")); // [app, apple, applet]
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced Trie topics include the XOR Trie (for maximum XOR of pairs in an array), the "
                "Aho-Corasick Automaton (multi-pattern string matching in O(n + m) time), and Compressed "
                "Radix Trees used in Linux kernel network routing. The XOR Trie inserts binary representations "
                "of numbers and enables finding the maximum XOR pair in O(32 * n) time, far superior to the "
                "O(n²) brute force. Aho-Corasick extends the Trie with failure links, allowing simultaneous "
                "matching of all patterns in a single O(text_length) pass."
            ),
            "working": (
                "XOR TRIE:\n"
                "  Insert each number bit by bit (MSB first, 30 bits).\n"
                "  For maximum XOR with x: at each bit, try to go opposite direction (greedy maximization).\n"
                "  If opposite direction child exists: go there; add that bit to XOR result.\n"
                "  Else: go same direction; that bit of XOR result is 0.\n\n"
                "AHO-CORASICK FAILURE LINKS:\n"
                "  Build: compute BFS failure link = longest proper suffix that is a valid prefix.\n"
                "  Search: follow failure links on mismatch (similar to KMP but for multiple patterns).\n"
                "  Result: all occurrences of all patterns in one O(n) pass."
            ),
            "algorithm": (
                "XOR TRIE MAX PAIR:\n"
                "  for each num in array: insert(num)\n"
                "  maxXOR = 0\n"
                "  for each num: maxXOR = max(maxXOR, query(num))\n"
                "  query(num): at each bit greedily choose opposite direction\n\n"
                "AHO-CORASICK BUILD:\n"
                "  BFS from root; for each node compute fail = fail link to longest matching suffix"
            ),
            "time_complexity": {
                "XOR Trie (max pair)": "O(32 * n)",
                "Aho-Corasick Build": "O(sum of pattern lengths)",
                "Aho-Corasick Search": "O(text_length + total_matches)",
                "Compressed Radix Trie": "O(L) per op, fewer nodes",
                "Suffix Trie Build": "O(n²) — use Suffix Array for O(n log n)"
            },
            "space_complexity": "O(32 * n) for XOR Trie; O(sum of pattern lengths) for Aho-Corasick.",
            "applications": (
                "• Network intrusion detection (Aho-Corasick for virus signatures)\n"
                "• Maximum XOR problems in competitive programming\n"
                "• IP routing table lookups (Radix Trie in Linux kernel)\n"
                "• Genome sequencing and motif finding\n"
                "• Plagiarism detection and substring matching"
            ),
            "advantages": (
                "• XOR Trie enables O(n log MAXVAL) max XOR vs O(n²) brute force\n"
                "• Aho-Corasick searches all patterns simultaneously in one pass\n"
                "• Compressed tries use far less memory for sparse datasets"
            ),
            "disadvantages": (
                "• XOR Trie requires fixed bit-width (32 or 64) — not dynamic\n"
                "• Aho-Corasick failure link computation is complex\n"
                "• These structures are rarely needed outside competitive programming"
            ),
            "interview_notes": (
                "★ Maximum XOR of Two Numbers in Array (LeetCode 421) — XOR Trie.\n"
                "★ Word Search II (LeetCode 212) — Trie-guided backtracking.\n"
                "★ Aho-Corasick is mentioned in system design for log scanning.\n"
                "★ Understand why compressed Tries are preferred in production."
            ),
            "java": """\
public class AdvancedTrie {

    // XOR Trie for Maximum XOR
    static int[][] xorTrie = new int[2000010][2];
    static int xorIdx = 1;

    static void insertXOR(int num) {
        int cur = 0;
        for (int i = 30; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (xorTrie[cur][bit] == 0) xorTrie[cur][bit] = xorIdx++;
            cur = xorTrie[cur][bit];
        }
    }

    static int queryXOR(int num) {
        int cur = 0, res = 0;
        for (int i = 30; i >= 0; i--) {
            int bit = (num >> i) & 1;
            int want = 1 - bit; // try opposite for max XOR
            if (xorTrie[cur][want] != 0) { res |= (1 << i); cur = xorTrie[cur][want]; }
            else cur = xorTrie[cur][bit];
        }
        return res;
    }

    public static void main(String[] args) {
        int[] nums = {3, 10, 5, 25, 2, 8};
        int max = 0;
        for (int n : nums) insertXOR(n);
        for (int n : nums) max = Math.max(max, queryXOR(n));
        System.out.println("Max XOR pair: " + max); // 28 (5 ^ 25)
    }
}"""
        }
    },

    # ==================== SEGMENT TREES ====================
    "Segment Trees": {
        "Beginner": {
            "definition": (
                "A Segment Tree is a powerful, tree-based data structure used for storing information "
                "about intervals or segments of an array. It allows answering range queries (like finding "
                "Sum, Min, or Max in a specific range [L, R]) and performing point/range updates in "
                "O(log N) time. This makes it significantly faster than naive loops (O(N)) for datasets "
                "that change frequently."
            ),
            "working": (
                "1. STRUCTURE: A binary tree where each node represents a range [L, R].\n"
                "2. LEAVES: Individual array elements [i, i].\n"
                "3. INTERNAL NODES: Store the result of their children (e.g., sum of left and right segments).\n"
                "4. UPDATE: Modify a leaf and update only its ancestors (path length log N).\n"
                "5. QUERY: Combine results of segments that completely cover the requested range."
            ),
            "algorithm": (
                "BUILD(node, L, R):\n"
                "  if L == R: tree[node] = arr[L]; return\n"
                "  BUILD(left_child, L, mid); BUILD(right_child, mid+1, R)\n"
                "  tree[node] = tree[left] + tree[right]\n\n"
                "QUERY(node, L, R, queryL, queryR):\n"
                "  if range outside: return 0\n"
                "  if range inside: return tree[node]\n"
                "  return QUERY(left) + QUERY(right)"
            ),
            "time_complexity": {
                "Build": "O(N)",
                "Query Range": "O(log N)",
                "Point Update": "O(log N)",
                "Range Update": "O(log N) — with Lazy Propagation"
            },
            "space_complexity": "O(4 * N) — for the array representation of the segment tree.",
            "applications": (
                "• Competitive programming (Dynamic range queries)\n"
                "• Finding Lowest Common Ancestor (LCA)\n"
                "• Frequency counting in geographic regions\n"
                "• Real-time stock price analysis (Min/Max in periods)\n"
                "• Collaborative document editing (tracking changes in ranges)"
            ),
            "advantages": (
                "• Fast logarithmic updates AND queries\n"
                "• Extremely flexible: can handle Sum, Min, Max, GCD, product, etc.\n"
                "• Stable and predictable performance"
            ),
            "disadvantages": (
                "• High memory consumption (4x the original array)\n"
                "• Complex implementation (requires careful recursive split/merge)\n"
                "• Static structure (hard to insert/delete new elements at arbitrary positions)"
            ),
            "interview_notes": (
                "★ Master Range Sum Query (Mutable) (LeetCode 307).\n"
                "★ Mention 'Lazy Propagation' when asked about O(log N) range updates.\n"
                "★ Be able to explain why the tree size is up to 4N.\n"
                "★ Alternatively, learn Fenwick Tree (BIT) for simpler range sum problems."
            ),
            "java": """\
public class SegmentTreeDemo {
    int[] tree; int n;
    public SegmentTreeDemo(int[] arr) {
        n = arr.length;
        tree = new int[4 * n];
        build(arr, 1, 0, n - 1);
    }
    void build(int[] arr, int node, int start, int end) {
        if(start == end) { tree[node] = arr[start]; return; }
        int mid = (start + end) / 2;
        build(arr, 2*node, start, mid);
        build(arr, 2*node+1, mid+1, end);
        tree[node] = tree[2*node] + tree[2*node+1];
    }
    int query(int node, int start, int end, int L, int R) {
        if(R < start || end < L) return 0;
        if(L <= start && end <= R) return tree[node];
        int mid = (start + end)/2;
        return query(2*node, start, mid, L, R) + query(2*node+1, mid+1, end, L, R);
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7};
        SegmentTreeDemo st = new SegmentTreeDemo(arr);
        System.out.println("Sum range [1, 2]: " + st.query(1, 0, 3, 1, 2)); // 8
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we add update operations to the Segment Tree and introduce "
                "the Fenwick Tree (Binary Indexed Tree / BIT) as a simpler alternative for prefix sum "
                "queries. The Segment Tree supports point updates in O(log N) by updating only the path "
                "from the modified leaf to the root. The Fenwick Tree achieves the same O(n log n) build "
                "and O(log n) update/query using very compact code based on the 'lowbit' operation (n & -n), "
                "making it a go-to choice in competitive programming for prefix sum problems."
            ),
            "working": (
                "POINT UPDATE IN SEGMENT TREE:\n"
                "  update(node, start, end, idx, delta):\n"
                "    if start == end: tree[node] += delta; return\n"
                "    mid = (start+end)/2\n"
                "    if idx <= mid: update(leftChild, start, mid, idx, delta)\n"
                "    else: update(rightChild, mid+1, end, idx, delta)\n"
                "    tree[node] = tree[leftChild] + tree[rightChild]\n\n"
                "FENWICK TREE (BIT):\n"
                "  update(i, delta): while i <= n: bit[i] += delta; i += (i & -i)\n"
                "  query(i): sum = 0; while i > 0: sum += bit[i]; i -= (i & -i)\n"
                "  Range query [l,r] = query(r) - query(l-1)"
            ),
            "algorithm": (
                "FENWICK TREE BUILD (O(n log n)):\n"
                "  for i from 1 to n: update(i, arr[i])\n\n"
                "FENWICK TREE BUILD (O(n) linear):\n"
                "  for i from 1 to n: bit[i] = arr[i]\n"
                "  for i from 1 to n: parent = i + (i & -i); if parent <= n: bit[parent] += bit[i]"
            ),
            "time_complexity": {
                "Segment Tree Point Update": "O(log N)",
                "Segment Tree Range Query": "O(log N)",
                "Fenwick Tree Update": "O(log N)",
                "Fenwick Tree Prefix Query": "O(log N)",
                "Fenwick Tree Build": "O(n) or O(n log n)"
            },
            "space_complexity": "O(4N) for Segment Tree; O(N) for Fenwick Tree (more compact).",
            "applications": (
                "• Online stock price running sum and range queries\n"
                "• Inversion count in arrays (Fenwick Tree)\n"
                "• Rank queries in competitive programming\n"
                "• Flight seat reservation range availability\n"
                "• Game scoreboard dynamic rankings"
            ),
            "advantages": (
                "• Fenwick Tree is 4x more memory-efficient than Segment Tree\n"
                "• Fenwick Tree update/query code is ~10 lines vs 60+ for Segment Tree\n"
                "• Segment Tree is more flexible (supports min/max/GCD, not just sums)"
            ),
            "disadvantages": (
                "• Fenwick Tree only supports commutative operations like sum/max\n"
                "• Range updates require 2 Fenwick Trees (technique)\n"
                "• Segment Tree code is much longer and error-prone"
            ),
            "interview_notes": (
                "★ Range Sum Query (Mutable) (LeetCode 307) — solve with both BIT and Seg Tree.\n"
                "★ Count of Smaller Numbers After Self (LeetCode 315) — BIT with coordinate compression.\n"
                "★ Count of Range Sum (LeetCode 327) — Segment Tree or merge sort.\n"
                "★ BIT is preferred in interviews for its conciseness."
            ),
            "java": """\
public class IntermediateSegTree {

    // Fenwick Tree (BIT)
    static int[] bit;
    static int n;

    static void update(int i, int delta) {
        for (; i <= n; i += (i & -i)) bit[i] += delta;
    }

    static int query(int i) {
        int sum = 0;
        for (; i > 0; i -= (i & -i)) sum += bit[i];
        return sum;
    }

    static int rangeQuery(int l, int r) { return query(r) - query(l - 1); }

    // Segment Tree Point Update
    static int[] tree2;
    static void update2(int node, int start, int end, int idx, int delta) {
        if (start == end) { tree2[node] += delta; return; }
        int mid = (start + end) / 2;
        if (idx <= mid) update2(2*node, start, mid, idx, delta);
        else update2(2*node+1, mid+1, end, idx, delta);
        tree2[node] = tree2[2*node] + tree2[2*node+1];
    }

    public static void main(String[] args) {
        int[] arr = {0, 1, 3, 5, 7, 9, 11}; // 1-indexed
        n = arr.length - 1;
        bit = new int[n + 1];
        for (int i = 1; i <= n; i++) update(i, arr[i]);
        System.out.println("Range [2,5]: " + rangeQuery(2, 5)); // 24
        update(3, 6); // arr[3] becomes 5+6=11
        System.out.println("After update, range [2,5]: " + rangeQuery(2, 5)); // 30
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced Segment Tree topics include Lazy Propagation (for O(log N) range updates), "
                "Persistent Segment Trees (maintaining multiple historical versions of the tree for "
                "offline range queries), and Merge Sort Trees (storing sorted arrays in each segment tree "
                "node for order-statistic queries). Lazy Propagation works by marking internal nodes with "
                "pending updates that are 'pushed down' only when the node is visited, deferring actual "
                "updates to minimize redundant work from O(N log N) to O(log N) per range update."
            ),
            "working": (
                "LAZY PROPAGATION:\n"
                "  lazy[node] = pending delta for all elements in this node's range.\n"
                "  On visit: push lazy down to children before querying or further updates.\n"
                "  pushDown(node): tree[child] += lazy[node] * rangeSize; lazy[child] += lazy[node]; lazy[node] = 0\n\n"
                "PERSISTENT SEGMENT TREE:\n"
                "  On update: don't modify existing node; create new node with updated value.\n"
                "  Previous version's root still valid (points to old, unchanged nodes).\n"
                "  Enable queries like: 'what was the sum at time t?' in O(log N).\n\n"
                "MERGE SORT TREE:\n"
                "  Each node stores sorted array of its range elements.\n"
                "  Range K-th smallest: binary search across nodes."
            ),
            "algorithm": (
                "LAZY PROPAGATION RANGE UPDATE:\n"
                "  update(node, start, end, l, r, val):\n"
                "    if no overlap: return\n"
                "    if complete overlap: tree[node] += val*(end-start+1); lazy[node] += val; return\n"
                "    pushDown(node); update children; tree[node] = tree[left] + tree[right]"
            ),
            "time_complexity": {
                "Lazy Propagation Range Update": "O(log N) amortized",
                "Lazy Propagation Range Query": "O(log N)",
                "Persistent Segment Tree (version q)": "O(log N) per update",
                "Merge Sort Tree K-th": "O(log² N)",
                "2D Segment Tree": "O(log² N)"
            },
            "space_complexity": "O(N log N) for merge sort tree; O(N log Q) for persistent versions.",
            "applications": (
                "• Version control systems (persistent trees trace each state)\n"
                "• Database MVCC (Multi-Version Concurrency Control)\n"
                "• Offline range K-th smallest queries\n"
                "• Competitive programming interval assignment\n"
                "• Terrain elevation range min/max with updates"
            ),
            "advantages": (
                "• Lazy propagation makes range updates as fast as point updates\n"
                "• Persistent trees enable time-travel queries without duplication\n"
                "• Extreme flexibility: any monoid operation can be stored"
            ),
            "disadvantages": (
                "• Lazy propagation adds significant code complexity\n"
                "• Persistent trees use O(N log Q) space — can be large\n"
                "• Worst-case constant factors are high compared to BIT"
            ),
            "interview_notes": (
                "★ Falling Squares (LeetCode 699) — range max segment tree with lazy.\n"
                "★ The Skyline Problem (LeetCode 218) — segment tree or sorted events.\n"
                "★ K-th Smallest in Sorted Matrix — merge sort tree variant.\n"
                "★ Persistent Seg Tree is often hinted by 'queries on previous array states'."
            ),
            "java": """\
public class AdvancedSegTree {
    int[] tree, lazy;
    int n;

    AdvancedSegTree(int n) {
        this.n = n;
        tree = new int[4 * n];
        lazy = new int[4 * n];
    }

    void pushDown(int node, int size) {
        if (lazy[node] != 0) {
            int half = size / 2;
            tree[2*node] += lazy[node] * half;
            tree[2*node+1] += lazy[node] * (size - half);
            lazy[2*node] += lazy[node];
            lazy[2*node+1] += lazy[node];
            lazy[node] = 0;
        }
    }

    void rangeUpdate(int node, int start, int end, int l, int r, int val) {
        if (r < start || end < l) return;
        if (l <= start && end <= r) {
            tree[node] += val * (end - start + 1);
            lazy[node] += val;
            return;
        }
        pushDown(node, end - start + 1);
        int mid = (start + end) / 2;
        rangeUpdate(2*node, start, mid, l, r, val);
        rangeUpdate(2*node+1, mid+1, end, l, r, val);
        tree[node] = tree[2*node] + tree[2*node+1];
    }

    int rangeQuery(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return 0;
        if (l <= start && end <= r) return tree[node];
        pushDown(node, end - start + 1);
        int mid = (start + end) / 2;
        return rangeQuery(2*node, start, mid, l, r) + rangeQuery(2*node+1, mid+1, end, l, r);
    }

    public static void main(String[] args) {
        AdvancedSegTree st = new AdvancedSegTree(6);
        st.rangeUpdate(1, 1, 6, 1, 3, 2); // add 2 to range [1,3]
        st.rangeUpdate(1, 1, 6, 2, 5, 4); // add 4 to range [2,5]
        System.out.println("Range [1,6] sum: " + st.rangeQuery(1, 1, 6, 1, 6)); // 6+8+8+4+4=26
    }
}"""
        }
    },

    # ==================== DISJOINT SET UNION (DSU) ====================
    "Disjoint Set (Union Find)": {
        "Beginner": {
            "definition": (
                "A Disjoint-Set Union (DSU) or Union-Find is a data structure that keeps track of a "
                "partition of a set into several disjoint (non-overlapping) subsets. It provides "
                "near-constant time operations to 'Union' two sets and 'Find' which set an element "
                "belongs to. It is the backbone of Kruskal's MST algorithm and most cycle detection "
                "algorithms in undirected graphs."
            ),
            "working": (
                "1. PARENT ARRAY: Each element points to its parent node. The representative points to itself.\n"
                "2. FIND: Follow parent pointers up until you reach the root (REPRESENTATIVE).\n"
                "3. UNION: Make the root of one set point to the root of the other set.\n"
                "4. PATH COMPRESSION: During 'Find', make every node along the path point directly to the root.\n"
                "5. UNION BY RANK/SIZE: Always attach the shorter tree to the taller one to keep the tree flat."
            ),
            "algorithm": (
                "FIND(x):\n"
                "  if parent[x] == x: return x\n"
                "  return parent[x] = FIND(parent[x]) // Path Compression\n\n"
                "UNION(x, y):\n"
                "  rootX = FIND(x); rootY = FIND(y)\n"
                "  if rootX != rootY: parent[rootX] = rootY"
            ),
            "time_complexity": {
                "Find / Union": "O(α(N)) — where α is the Inverse Ackermann Function (nearly O(1))",
                "Initialization": "O(N)",
                "Worst Case (naive)": "O(N)"
            },
            "space_complexity": "O(n) — for path and rank arrays.",
            "applications": (
                "• Minimum Spanning Trees (Kruskal's Algorithm)\n"
                "• Finding connected components in a graph\n"
                "• Detecting cycles in undirected graphs\n"
                "• Image segmentation (grouping pixels)\n"
                "• Social networks (finding clusters of friends)"
            ),
            "advantages": (
                "• Extremely fast performance (as fast as any computer operation)\n"
                "• Minimal memory footprint (just arrays)\n"
                "• Easy to implement for dynamic connectivity problems"
            ),
            "disadvantages": (
                "• Only works on undirected graphs (for simple connectivity)\n"
                "• Path compression and union-by-rank are mandatory for high speed\n"
                "• Deleting an element from a set is difficult to implement"
            ),
            "interview_notes": (
                "★ Path Compression + Union by Rank = Inverse Ackermann time. Explain this!\n"
                "★ Redundant Connection (LeetCode 684) — classic cycle detection problem.\n"
                "★ Number of Islands (LeetCode 200) — can be solved with DSU (though BFS is more common).\n"
                "★ Always mention that roots are unified, not individual nodes."
            ),
            "java": """\
public class DSUDemo {
    int[] parent;
    public DSUDemo(int n) {
        parent = new int[n];
        for(int i=0; i<n; i++) parent[i] = i;
    }
    public int find(int x) {
        if(parent[x] == x) return x;
        return parent[x] = find(parent[x]); // Path compression
    }
    public void union(int x, int y) {
        int rX = find(x), rY = find(y);
        if(rX != rY) parent[rX] = rY;
    }

    public static void main(String[] args) {
        DSUDemo dsu = new DSUDemo(5);
        dsu.union(0, 1); dsu.union(1, 2);
        System.out.println("2 and 0 connected? " + (dsu.find(2) == dsu.find(0))); // true
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we implement DSU with the two key optimizations: "
                "Path Compression and Union by Rank/Size. Path Compression flattens the tree structure "
                "by making every node on the find path point directly to the root. Union by Rank ensures "
                "the shallower tree is attached under the taller one. Together, these optimizations give "
                "the nearly constant O(α(n)) amortized time per operation, where α is the inverse Ackermann "
                "function, which is practically 4 for all real inputs. This enables Kruskal's MST to run "
                "in near-linear time."
            ),
            "working": (
                "PATH COMPRESSION:\n"
                "  find(x):\n"
                "    if parent[x] != x: parent[x] = find(parent[x])  // flatten path\n"
                "    return parent[x]\n\n"
                "UNION BY RANK:\n"
                "  union(x, y):\n"
                "    px, py = find(x), find(y)\n"
                "    if px == py: return false  // already same set\n"
                "    if rank[px] < rank[py]: swap(px, py)\n"
                "    parent[py] = px\n"
                "    if rank[px] == rank[py]: rank[px]++\n\n"
                "KRUSKAL'S MST USING DSU:\n"
                "  Sort edges by weight; for each edge: if find(u) != find(v): include and union."
            ),
            "algorithm": (
                "CYCLE DETECTION IN UNDIRECTED GRAPH:\n"
                "  for each edge (u, v):\n"
                "    if find(u) == find(v): cycle found!\n"
                "    else: union(u, v)\n\n"
                "COUNT CONNECTED COMPONENTS:\n"
                "  n = nodes; components = n\n"
                "  for each edge: if union(u, v) succeeded: components--\n"
                "  return components"
            ),
            "time_complexity": {
                "Find (with path compression)": "O(α(n)) ≈ O(1)",
                "Union (with rank)": "O(α(n)) ≈ O(1)",
                "Kruskal's MST": "O(E log E + E * α(V))",
                "Cycle Detection": "O(E * α(V))",
                "m operations total": "O(m * α(n))"
            },
            "space_complexity": "O(n) for parent[] and rank[] arrays.",
            "applications": (
                "• Kruskal's MST algorithm (backbone)\n"
                "• Network connectivity testing (online, dynamic)\n"
                "• Cycle detection in undirected graphs\n"
                "• Percolation theory in statistical physics\n"
                "• Dynamic connectivity problems in competitive programming"
            ),
            "advantages": (
                "• Nearly O(1) per operation with both optimizations\n"
                "• Extremely simple to implement despite its power\n"
                "• Handles millions of union/find operations efficiently"
            ),
            "disadvantages": (
                "• Supports union and find, but not split or deletion\n"
                "• Not suitable for directed graph connectivity (use SCC algorithms)\n"
                "• Path compression mutates the structure (harder to persist)"
            ),
            "interview_notes": (
                "★ Number of Provinces (LeetCode 547) — DSU connected components.\n"
                "★ Redundant Connection (LeetCode 684) — union-find cycle detection.\n"
                "★ Number of Operations to Make Network Connected (LeetCode 1319).\n"
                "★ Accounts Merge (LeetCode 721) — DSU with string keys via HashMap."
            ),
            "java": """\
public class IntermediateDSU {
    int[] parent, rank;

    IntermediateDSU(int n) {
        parent = new int[n]; rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]); // path compression
        return parent[x];
    }

    boolean union(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        if (rank[px] < rank[py]) { int t = px; px = py; py = t; }
        parent[py] = px;
        if (rank[px] == rank[py]) rank[px]++;
        return true;
    }

    // Count connected components
    static int countComponents(int n, int[][] edges) {
        IntermediateDSU dsu = new IntermediateDSU(n);
        int comp = n;
        for (int[] e : edges) if (dsu.union(e[0], e[1])) comp--;
        return comp;
    }

    public static void main(String[] args) {
        int[][] edges = {{0,1},{0,2},{3,4}};
        System.out.println("Components: " + countComponents(5, edges)); // 2
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced DSU topics include the Weighted DSU (stores edge weights for path queries), "
                "Rollback DSU (supports undo of union operations using a log for offline algorithms), "
                "and DSU on Trees (small-to-large merging). Rollback DSU is critical for offline divide "
                "and conquer graph algorithms where you need to test connectivity with and without "
                "certain edges. The Offline LCA (Lowest Common Ancestor) algorithm by Tarjan uses DSU "
                "to solve all LCA queries in O((V + Q) * α(V)) in a single DFS pass."
            ),
            "working": (
                "WEIGHTED DSU (Potential-based):\n"
                "  Each node stores weight relative to its parent.\n"
                "  find(x): if x is root, return (x, 0); else return (root, w[x] + find(parent[x]).w)\n"
                "  Enables queries: 'what is the 'distance' between u and v in their component?'\n\n"
                "ROLLBACK DSU (No Path Compression):\n"
                "  Store undo log as stack of (node, old_parent, old_rank) tuples.\n"
                "  union: do union and push to log.\n"
                "  rollback: pop from log, restore parent and rank."
            ),
            "algorithm": (
                "ONLINE CONNECTIVITY (Rollback DSU for D&C):\n"
                "  divide queries into two halves\n"
                "  edges active in left half: permanently union them\n"
                "  edges active in right half: permanently union then rollback\n"
                "  answer queries recursively using log"
            ),
            "time_complexity": {
                "DSU with Path Compression + Rank": "O(m * α(n))",
                "Rollback DSU (no compress)": "O(m * log n)",
                "Tarjan's Offline LCA": "O((V + Q) * α(V))",
                "Small-to-Large DSU": "O(n log n)",
                "Weighted DSU Find": "O(α(n)) amortized"
            },
            "space_complexity": "O(n + Q) for offline LCA; O(log n) for rollback stack depth per level.",
            "applications": (
                "• Online dynamic connectivity in system monitoring\n"
                "• Offline LCA for tree queries in competitive programming\n"
                "• Variable unification in type inference systems (compilers)\n"
                "• Network clique detection\n"
                "• D&C on graph structures with rollback"
            ),
            "advantages": (
                "• Rollback DSU enables undo of structural changes\n"
                "• Weighted DSU extends standard DSU without additional data structures\n"
                "• Offline LCA is optimal for batch LCA queries"
            ),
            "disadvantages": (
                "• Rollback DSU cannot use path compression (loses rollback ability)\n"
                "• Weighted DSU adds constant factor overhead\n"
                "• Only applicable to offline queries"
            ),
            "interview_notes": (
                "★ Swim in Rising Water (LeetCode 778) — DSU + binary search on time.\n"
                "★ Remove Max Number of Edges to Keep Graph Fully Traversable (LeetCode 1579).\n"
                "★ Accounts Merge (LeetCode 721) — DSU with string-keyed components.\n"
                "★ Know the difference between DSU for undirected vs directed connectivity."
            ),
            "java": """\
public class AdvancedDSU {
    int[] parent, rank;
    java.util.Deque<int[]> log = new java.util.ArrayDeque<>();

    AdvancedDSU(int n) {
        parent = new int[n]; rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int x) {
        while (parent[x] != x) x = parent[x]; // NO path compression for rollback
        return x;
    }

    boolean union(int x, int y) {
        x = find(x); y = find(y);
        if (x == y) { log.push(new int[]{-1, -1, -1, -1}); return false; }
        if (rank[x] < rank[y]) { int t = x; x = y; y = t; }
        log.push(new int[]{y, parent[y], x, rank[x]});
        parent[y] = x;
        if (rank[x] == rank[y]) rank[x]++;
        return true;
    }

    void rollback() {
        int[] op = log.pop();
        if (op[0] == -1) return;
        parent[op[0]] = op[1]; // restore child's parent
        rank[op[2]] = op[3];   // restore root's rank
    }

    public static void main(String[] args) {
        AdvancedDSU dsu = new AdvancedDSU(4);
        dsu.union(0, 1); dsu.union(1, 2);
        System.out.println("0-2 connected? " + (dsu.find(0) == dsu.find(2))); // true
        dsu.rollback(); // undo union(1,2)
        System.out.println("0-2 after rollback? " + (dsu.find(0) == dsu.find(2))); // false
    }
}"""
        }
    },

    # ==================== ADVANCED GRAPH ALGORITHMS ====================
    "Advanced Graph Algorithms": {
        "Beginner": {
            "definition": (
                "Advanced Graph Algorithms cover complex pathfinding, connectivity, and flow problems "
                "beyond basic search. This includes Dijkstra's for shortest paths in weighted graphs, "
                "Bellman-Ford for negative weights, Floyd-Warshall for all-pairs calculations, and "
                "Tarjan's/Kosaraju's for finding Strongly Connected Components (SCCs). These are essential "
                "for solving real-world routing and network topology problems."
            ),
            "working": (
                "1. DIJKSTRA: Uses a Priority Queue to pick the 'closest' unvisited node. (No negative weights).\n"
                "2. BELLMAN-FORD: Relaxes all edges (V-1) times. Detects negative cycles.\n"
                "3. FLOYD-WARSHALL: Uses DP to find all shortest paths between all pairs (O(V³)).\n"
                "4. TARJAN: Uses DFS and discovery times to identify components where every node can reach every other node."
            ),
            "algorithm": (
                "DIJKSTRA(source):\n"
                "  dist[source] = 0; pq.push({0, source})\n"
                "  while pq:\n"
                "    u = pq.pop()\n"
                "    for v in neighbors(u):\n"
                "       if dist[v] > dist[u] + weight(u,v):\n"
                "          dist[v] = dist[u] + weight(u,v); pq.push({dist[v], v})\n\n"
                "FLOYD-WARSHALL:\n"
                "  for k: for i: for j: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])"
            ),
            "time_complexity": {
                "Dijkstra": "O(E log V)",
                "Bellman-Ford": "O(V * E)",
                "Floyd-Warshall": "O(V³)",
                "Tarjan’s / Kosaraju’s": "O(V + E)",
                "Bridges / Artifacts": "O(V + E)"
            },
            "space_complexity": "O(V + E) for graphs; O(V²) for Floyd-Warshall table.",
            "applications": (
                "• GPS Navigation and road route optimization\n"
                "• Network routing protocols (OSPF uses Dijkstra)\n"
                "• Arbitrage detection in currency trading (negative cycles)\n"
                "• Social network analysis (communities and clusters)\n"
                "• Circuit design and dependency resolution"
            ),
            "advantages": (
                "• Solves specific, hard constraints (negative weights, all-pairs)\n"
                "• Highly robust and widely used in industry\n"
                "• Foundational for specialized fields like GIS and Logistics"
            ),
            "disadvantages": (
                "• High time complexity (V*E or V³) for large networks\n"
                "• Dijkstra fails on negative weights; Bellman-Ford is slow\n"
                "• Implementations are complex and require deep knowledge of graph theory"
            ),
            "interview_notes": (
                "★ Dijkstra’s is the most important advanced algorithm to know.\n"
                "★ Explain 'Negative Cycle' and why Dijkstra fails while Bellman-Ford succeeds.\n"
                "★ Practice: Network Delay Time (LeetCode 743) and Cheapest Flights (LeetCode 787).\n"
                "★ Mention 'Pruning' or 'A* Search' for real-world optimizations."
            ),
            "java": """\
import java.util.*;

public class AdvancedGraph {
    // Dijkstra's Shortest Path
    public void dijkstra(int n, List<int[]>[] adj, int src) {
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.add(new int[]{src, 0});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int u = curr[0];
            if (curr[1] > dist[u]) continue;

            for (int[] edge : adj[u]) {
                int v = edge[0], weight = edge[1];
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    pq.add(new int[]{v, dist[v]});
                }
            }
        }
        System.out.println("Dist: " + Arrays.toString(dist));
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we dive deeper into Dijkstra's implementation nuances and study "
                "Topological Sort-based shortest paths on DAGs. We also explore Prim's MST as an alternative "
                "to Kruskal's, and the bidirectional BFS optimization for unweighted graphs. For DAGs "
                "specifically, the Longest/Shortest Path can be computed in O(V+E) using topological order "
                "DP, avoiding the need for more expensive Dijkstra/Bellman-Ford on these acyclic structures."
            ),
            "working": (
                "PRIM'S MST (O(E log V)):\n"
                "  Start with any node; maintain a Min-Heap of (weight, node) pairs.\n"
                "  While heap not empty: pick cheapest unvisited edge; add to MST.\n"
                "  Offer neighbors of newly added node to heap.\n\n"
                "DAG SHORTEST PATH:\n"
                "  Topological sort the graph.\n"
                "  Initialize dist[src] = 0; all others = infinity.\n"
                "  Relax edges in topological order.\n\n"
                "BIDIRECTIONAL BFS:\n"
                "  Run BFS simultaneously from source and target.\n"
                "  When frontiers meet: path found (cuts search space by ~half)."
            ),
            "algorithm": (
                "PRIM'S MST:\n"
                "  visited[src] = true; pq.add((0, src))\n"
                "  while pq not empty:\n"
                "    (w, u) = pq.poll()\n"
                "    if visited[u]: continue\n"
                "    visited[u] = true; mst_cost += w\n"
                "    for (v, weight) in adj[u]: if !visited[v]: pq.add((weight, v))"
            ),
            "time_complexity": {
                "Prim's MST": "O(E log V)",
                "DAG Shortest Path": "O(V + E)",
                "Bidirectional BFS": "O(b^(d/2)) vs O(b^d) for standard BFS",
                "Johnson's Algorithm": "O(V² log V + VE)",
                "0-1 BFS": "O(V + E) — for edges with weight 0 or 1"
            },
            "space_complexity": "O(V + E) for graphs and auxiliary buffers.",
            "applications": (
                "• Network cable layout optimization (Prim's MST)\n"
                "• Pipeline routing with cost minimization\n"
                "• Facebook 6-degrees of separation (bidirectional BFS)\n"
                "• Compiler data-flow analysis on CFGs\n"
                "• Package dependency resolution with version ordering"
            ),
            "advantages": (
                "• Prim's is better for dense graphs than Kruskal's\n"
                "• DAG shortest path is O(V+E) — faster than Dijkstra for DAGs\n"
                "• Bidirectional BFS dramatically reduces search space"
            ),
            "disadvantages": (
                "• Bidirectional BFS is tricky to implement correctly\n"
                "• Prim's with adjacency matrix is O(V²) — use heap for sparse graphs\n"
                "• DAG methods don't work for graphs with cycles"
            ),
            "interview_notes": (
                "★ Min Cost to Connect All Points (LeetCode 1584) — Prim's or Kruskal's.\n"
                "★ Word Ladder (LeetCode 127) — BFS / Bidirectional BFS.\n"
                "★ Longest Path in DAG — topological sort + DP.\n"
                "★ Path With Minimum Effort (LeetCode 1631) — modified Dijkstra on grid."
            ),
            "java": """\
import java.util.*;

public class IntermediateGraphAlgo {
    // Prim's MST
    @SuppressWarnings("unchecked")
    static int primsMST(int V, List<int[]>[] adj) {
        boolean[] visited = new boolean[V];
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, 0}); // (weight, node)
        int mstCost = 0;
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int w = curr[0], u = curr[1];
            if (visited[u]) continue;
            visited[u] = true;
            mstCost += w;
            for (int[] edge : adj[u]) if (!visited[edge[0]]) pq.offer(new int[]{edge[1], edge[0]});
        }
        return mstCost;
    }

    public static void main(String[] args) {
        int V = 4;
        List<int[]>[] adj = new ArrayList[V];
        for (int i = 0; i < V; i++) adj[i] = new ArrayList<>();
        adj[0].add(new int[]{1, 1}); adj[1].add(new int[]{0, 1});
        adj[0].add(new int[]{2, 4}); adj[2].add(new int[]{0, 4});
        adj[1].add(new int[]{2, 2}); adj[2].add(new int[]{1, 2});
        adj[1].add(new int[]{3, 5}); adj[3].add(new int[]{1, 5});
        adj[2].add(new int[]{3, 1}); adj[3].add(new int[]{2, 1});
        System.out.println("Prim's MST Cost: " + primsMST(V, adj)); // 4
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced graph algorithm topics include Max-Flow algorithms (Ford-Fulkerson, Edmonds-Karp, "
                "Dinic's), network flow applications (bipartite matching, min-cut), and 2-SAT. "
                "Dinic's Algorithm runs in O(V² * E) and is faster than Ford-Fulkerson for unit capacity "
                "networks. The Max-Flow Min-Cut Theorem states that the maximum flow from source to sink equals "
                "the minimum capacity cut separating them, connecting flow and connectivity in a fundamental way. "
                "A* search extends Dijkstra with a heuristic function for faster pathfinding in practice."
            ),
            "working": (
                "FORD-FULKERSON IDEA:\n"
                "  Find any augmenting path from source to sink (DFS/BFS).\n"
                "  Push minimum bottleneck flow along this path.\n"
                "  Update residual graph (subtract flow on forward edges, add on backward).\n"
                "  Repeat until no augmenting path exists.\n\n"
                "A* SEARCH:\n"
                "  Like Dijkstra but priority = dist[u] + heuristic(u, target).\n"
                "  Heuristic h(u): admissible estimate of cost from u to target.\n"
                "  Expands fewer nodes than Dijkstra by focusing search toward target."
            ),
            "algorithm": (
                "EDMONDS-KARP (BFS-based Ford-Fulkerson):\n"
                "  Complexity: O(V * E²)\n"
                "  while BFS finds augmenting path:\n"
                "    bottleneck = min capacity on path\n"
                "    for each edge on path: capacity[u][v] -= bottleneck; capacity[v][u] += bottleneck\n"
                "    totalFlow += bottleneck\n"
                "  return totalFlow"
            ),
            "time_complexity": {
                "Ford-Fulkerson": "O(E * maxFlow)",
                "Edmonds-Karp": "O(V * E²)",
                "Dinic's Algorithm": "O(V² * E)",
                "A* Search": "O(E log V) with admissible heuristic",
                "Bipartite Matching": "O(V * E) via max-flow"
            },
            "space_complexity": "O(V²) for capacity matrix in flow algorithms.",
            "applications": (
                "• Image segmentation (graph cut / min-cut)\n"
                "• Project selection problems (max-flow min-cut)\n"
                "• Job assignment and bipartite matching\n"
                "• Game AI pathfinding (A*)\n"
                "• Network reliability analysis"
            ),
            "advantages": (
                "• Max-flow solves a huge class of optimization problems\n"
                "• A* is dramatically faster than Dijkstra in practice for specific targets\n"
                "• Dinic's unit-capacity network runs in O(E * sqrt(V))"
            ),
            "disadvantages": (
                "• Flow algorithms are complex with many edge cases\n"
                "• A* quality depends entirely on heuristic accuracy\n"
                "• Max-flow only handles single source/sink; multi-commodity is NP-hard"
            ),
            "interview_notes": (
                "★ Maximum Flow problems appear in advanced technical interviews.\n"
                "★ A* is essential knowledge for robotics and game development interviews.\n"
                "★ Bipartite Matching (LeetCode 1349) — students to exam rooms.\n"
                "★ Know Max-Flow Min-Cut theorem statement and intuition clearly."
            ),
            "java": """\
import java.util.*;

public class AdvancedGraphAlgo {
    // Edmonds-Karp Max Flow
    static int maxFlow(int[][] cap, int s, int t, int n) {
        int flow = 0;
        int[] parent = new int[n];
        while (true) {
            Arrays.fill(parent, -1);
            parent[s] = s;
            Queue<Integer> q = new LinkedList<>();
            q.offer(s);
            while (!q.isEmpty() && parent[t] == -1) {
                int u = q.poll();
                for (int v = 0; v < n; v++)
                    if (parent[v] == -1 && cap[u][v] > 0) { parent[v] = u; q.offer(v); }
            }
            if (parent[t] == -1) break;
            int bottleneck = Integer.MAX_VALUE;
            for (int v = t; v != s; v = parent[v])
                bottleneck = Math.min(bottleneck, cap[parent[v]][v]);
            for (int v = t; v != s; v = parent[v]) {
                cap[parent[v]][v] -= bottleneck;
                cap[v][parent[v]] += bottleneck;
            }
            flow += bottleneck;
        }
        return flow;
    }

    public static void main(String[] args) {
        int[][] cap = {
            {0, 16, 13, 0, 0, 0},
            {0, 0, 10, 12, 0, 0},
            {0, 4, 0, 0, 14, 0},
            {0, 0, 9, 0, 0, 20},
            {0, 0, 0, 7, 0, 4},
            {0, 0, 0, 0, 0, 0}
        };
        System.out.println("Max Flow: " + maxFlow(cap, 0, 5, 6)); // 23
    }
}"""
        }
    },

    # ==================== BINARY SEARCH ====================
    "Binary Search": {
        "Beginner": {
            "definition": (
                "Binary Search is a highly efficient algorithm for finding an item from a sorted list of items. "
                "It works by repeatedly dividing in half the portion of the list that could contain the item, "
                "until you've narrowed down the possible locations to just one. It follows the 'Divide and "
                "Conquer' strategy and is significantly faster than linear search for large datasets. "
                "Imagine looking for a word in a physical dictionary: you open the middle, see if your word "
                "is before or after, and discard the half you don't need."
            ),
            "working": (
                "1. PRE-CONDITION: The array must be sorted.\n"
                "2. INITIALIZE: Set `low = 0` and `high = n - 1`.\n"
                "3. FIND MIDDLE: `mid = low + (high - low) / 2`.\n"
                "4. COMPARE: If `arr[mid] == target`, item found. If `target < arr[mid]`, search the left half (`high = mid - 1`). "
                "If `target > arr[mid]`, search the right half (`low = mid + 1`).\n"
                "5. REPEAT: Continue until `low > high` (not found)."
            ),
            "algorithm": (
                "BINARY_SEARCH(arr, target):\n"
                "  low = 0, high = arr.length - 1\n"
                "  while low <= high:\n"
                "    mid = low + (high - low) / 2\n"
                "    if arr[mid] == target: return mid\n"
                "    if arr[mid] < target: low = mid + 1\n"
                "    else: high = mid - 1\n"
                "  return -1"
            ),
            "time_complexity": {
                "Best Case": "O(1) — target is exactly at the middle",
                "Average Case": "O(log n)",
                "Worst Case": "O(log n) — target is at the ends or not present"
            },
            "space_complexity": "O(1) for iterative; O(log n) for recursive due to stack space.",
            "applications": (
                "• Searching in massive sorted databases\n"
                "• Version control (git bisect to find broken commits)\n"
                "• Debugging (binary search through log files)\n"
                "• Libraries for `Arrays.binarySearch` in Java and `bisect` in Python\n"
                "• Solving 'Search in Rotated Sorted Array' puzzles"
            ),
            "advantages": (
                "• Blazingly fast for searching in large arrays\n"
                "• much better than linear search (e.g., searches 1 million items in just 20 steps)\n"
                "• Simple to implement and extremely reliable"
            ),
            "disadvantages": (
                "• Requires the data to be sorted beforehand (sorting takes O(n log n))\n"
                "• Only efficient for contiguous memory structures (arrays) with random access\n"
                "• Not suitable for datasets that change frequently (insertions/deletions)"
            ),
            "interview_notes": (
                "★ Always mention that the input must be sorted.\n"
                "★ Explain why we use `mid = low + (high - low) / 2` instead of `(low + high) / 2` (to avoid overflow).\n"
                "★ Practice: Search in Rotated Sorted Array (LeetCode 33).\n"
                "★ Mention 'Binary Search on Answer' for complex optimization problems."
            ),
            "java": """\
public class BinarySearchDemo {
    public static int binarySearch(int[] arr, int target) {
        int low = 0, high = arr.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == target) return mid;
            if (arr[mid] < target) low = mid + 1;
            else high = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] data = {1, 3, 5, 7, 9, 11};
        System.out.println("Index of 7: " + binarySearch(data, 7)); // 3
        System.out.println("Index of 4: " + binarySearch(data, 4)); // -1
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, Binary Search is applied beyond just finding a target value. "
                "We use it to find the leftmost or rightmost occurrence of a value, find insertion positions, "
                "and most powerfully: 'Binary Search on the Answer.' This technique applies binary search "
                "not on an array but on the ANSWER SPACE of a problem. If we can define a monotonic predicate "
                "(e.g., 'can we achieve X days?'), we binary search on the answer to find the minimum or "
                "maximum feasible value. This transforms many O(n²) or O(n³) problems to O(n log n)."
            ),
            "working": (
                "LEFTMOST OCCURRENCE:\n"
                "  When arr[mid] == target: don't stop; continue with high = mid - 1.\n"
                "  Answer is 'low' after the loop.\n\n"
                "BINARY SEARCH ON ANSWER:\n"
                "  Define: canAchieve(mid) → true/false (monotonic predicate).\n"
                "  low = min_possible_answer, high = max_possible_answer.\n"
                "  Binary search: if canAchieve(mid): result = mid; narrow range.\n\n"
                "PEAK FINDING:\n"
                "  If arr[mid] < arr[mid+1]: peak is on the right.\n"
                "  Else: peak is on the left or at mid."
            ),
            "algorithm": (
                "BINARY SEARCH ON ANSWER template:\n"
                "  lo = 1, hi = max_value\n"
                "  while lo < hi:\n"
                "    mid = (lo + hi) / 2\n"
                "    if canAchieve(mid): hi = mid  // minimize\n"
                "    else: lo = mid + 1\n"
                "  return lo\n\n"
                "LEFTMOST occurrence:\n"
                "  lo=0, hi=n-1, result=-1\n"
                "  if arr[mid] == target: result=mid; hi=mid-1  // keep searching left"
            ),
            "time_complexity": {
                "Leftmost / Rightmost": "O(log n)",
                "Binary Search on Answer": "O(log(range) * cost_of_check)",
                "Peak Finding": "O(log n)",
                "Search in Rotated Array": "O(log n)",
                "Find Min in Rotated Array": "O(log n)"
            },
            "space_complexity": "O(1) for all iterative binary search variants.",
            "applications": (
                "• Database index lookup (B-Tree binary search)\n"
                "• Optimal resource allocation (binary search on answer)\n"
                "• Finding thresholds in A/B testing\n"
                "• Minimum time/speed problems (Koko eating bananas, ship packages)\n"
                "• Square root and power calculations"
            ),
            "advantages": (
                "• Binary search on answer reduces exponential search to O(log n) steps\n"
                "• Very general and applicable to any monotonic predicate\n"
                "• O(1) space — no extra memory needed"
            ),
            "disadvantages": (
                "• Predicate function must be truly monotonic — hard to verify sometimes\n"
                "• Off-by-one errors are extremely common in boundary conditions\n"
                "• Not applicable to non-sorted or non-monotonic problems"
            ),
            "interview_notes": (
                "★ Koko Eating Bananas (LeetCode 875) — binary search on eating speed.\n"
                "★ Capacity to Ship Packages (LeetCode 1011) — binary search on capacity.\n"
                "★ Find Peak Element (LeetCode 162) — log(n) using binary decisions.\n"
                "★ Search in Rotated Sorted Array (LeetCode 33) — identify sorted half first."
            ),
            "java": """\
public class IntermediateBinarySearch {

    // Leftmost Occurrence
    static int leftmost(int[] arr, int target) {
        int lo = 0, hi = arr.length - 1, result = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == target) { result = mid; hi = mid - 1; }
            else if (arr[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return result;
    }

    // Koko Eating Bananas (Binary Search on Answer)
    static int minEatingSpeed(int[] piles, int h) {
        int lo = 1, hi = 0;
        for (int p : piles) hi = Math.max(hi, p);
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            int hours = 0;
            for (int p : piles) hours += (int) Math.ceil((double) p / mid);
            if (hours <= h) hi = mid; else lo = mid + 1;
        }
        return lo;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 3, 3, 5, 6};
        System.out.println("Leftmost 3: " + leftmost(arr, 3)); // 2
        System.out.println("Min speed: " + minEatingSpeed(new int[]{3,6,7,11}, 8)); // 4
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced binary search topics include fractional binary search (binary search on real-valued "
                "answers with floating-point precision like finding the minimum radius of circles), "
                "parallel binary search (solving K independent binary searches in O(n log n) instead of "
                "O(Kn log n)), and binary search on arrays with specific structures like the "
                "'Median of Two Sorted Arrays' problem. The OOXX pattern (finding the boundary between "
                "false and true in a boolean predicate array) generalizes all binary search problems "
                "into a single formulation."
            ),
            "working": (
                "FRACTIONAL BINARY SEARCH:\n"
                "  lo, hi = real-valued bounds; iterate ~100 times (enough for double precision).\n"
                "  mid = (lo + hi) / 2.0\n"
                "  if condition(mid): hi = mid; else lo = mid\n\n"
                "MEDIAN OF TWO SORTED ARRAYS (O(log min(m,n))):\n"
                "  Binary search on partition of smaller array.\n"
                "  Ensure: A[partA-1] <= B[partB] and B[partB-1] <= A[partA].\n"
                "  Median is found at the partition boundary."
            ),
            "algorithm": (
                "MEDIAN OF TWO SORTED ARRAYS:\n"
                "  Ensure A is smaller; lo=0, hi=m\n"
                "  partA = (lo+hi)/2; partB = (m+n+1)/2 - partA\n"
                "  if A[partA-1] <= B[partB] and B[partB-1] <= A[partA]: found!\n"
                "  elif A[partA-1] > B[partB]: hi = partA - 1\n"
                "  else: lo = partA + 1"
            ),
            "time_complexity": {
                "Fractional Binary Search": "O(log(1/ε)) ≈ O(100) iterations",
                "Median of Two Arrays": "O(log min(m,n))",
                "Parallel Binary Search": "O((n + Q) log n)",
                "Exponential Search": "O(log n) — useful for unbounded arrays",
                "Ternary Search": "O(log n) — for unimodal functions"
            },
            "space_complexity": "O(1) for all binary search variants.",
            "applications": (
                "• Optimal circle placement and coverage radius\n"
                "• Finding optimal cut points in dividing arrays\n"
                "• Split array largest sum with binary search on answer\n"
                "• Database join optimization with unknown row counts\n"
                "• Game theory Nash equilibrium approximate solutions"
            ),
            "advantages": (
                "• Fractional binary search avoids error-prone loop-counting\n"
                "• Median of two arrays is the optimal O(log n) approach\n"
                "• Parallel binary search eliminates redundant work across queries"
            ),
            "disadvantages": (
                "• Floating-point binary search requires careful epsilon handling\n"
                "• Median of two arrays is one of the most error-prone implementations\n"
                "• Parallel binary search is rarely needed outside competitive programming"
            ),
            "interview_notes": (
                "★ Median of Two Sorted Arrays (LeetCode 4) — Hard, O(log min(m,n)).\n"
                "★ Split Array Largest Sum (LeetCode 410) — binary search on answer.\n"
                "★ Find K-th Smallest in Matrix (LeetCode 378) — binary search on value.\n"
                "★ Use 100-iteration loop for floating-point binary search to avoid epsilon bugs."
            ),
            "java": """\
public class BinarySearch {

    // Median of Two Sorted Arrays O(log min(m,n))
    static double findMedianSortedArrays(int[] A, int[] B) {
        if (A.length > B.length) return findMedianSortedArrays(B, A);
        int m = A.length, n = B.length;
        int lo = 0, hi = m;
        while (lo <= hi) {
            int partA = (lo + hi) / 2;
            int partB = (m + n + 1) / 2 - partA;
            int maxLeftA = (partA == 0) ? Integer.MIN_VALUE : A[partA - 1];
            int minRightA = (partA == m) ? Integer.MAX_VALUE : A[partA];
            int maxLeftB = (partB == 0) ? Integer.MIN_VALUE : B[partB - 1];
            int minRightB = (partB == n) ? Integer.MAX_VALUE : B[partB];
            if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
                if ((m + n) % 2 == 0)
                    return (Math.max(maxLeftA, maxLeftB) + Math.min(minRightA, minRightB)) / 2.0;
                else
                    return Math.max(maxLeftA, maxLeftB);
            } else if (maxLeftA > minRightB) hi = partA - 1;
            else lo = partA + 1;
        }
        throw new IllegalArgumentException();
    }

    public static void main(String[] args) {
        System.out.println(findMedianSortedArrays(new int[]{1,3}, new int[]{2})); // 2.0
        System.out.println(findMedianSortedArrays(new int[]{1,2}, new int[]{3,4})); // 2.5
    }
}"""
        }
    },

    # ==================== SELECTION SORT ====================
    "Selection Sort": {
        "Beginner": {
            "definition": (
                "Selection Sort is a simple comparison-based sorting algorithm. It works by dividing the "
                "input list into two parts: the sublist of items already sorted, which is built up from "
                "left to right, and the sublist of items remaining to be sorted. In each iteration, it "
                "finds the minimum element from the unsorted part and 'selects' it to be placed at the "
                "beginning of the unsorted section."
            ),
            "working": (
                "1. START: Assume the first element is the minimum.\n"
                "2. FIND MIN: Scan the rest of the array to find the actual minimum value.\n"
                "3. SWAP: Swap this minimum with the first element of the unsorted part.\n"
                "4. MOVE BOUNDARY: Move the boundary between sorted and unsorted one position to the right.\n"
                "5. REPEAT: Continue until the entire array is sorted."
            ),
            "algorithm": (
                "SELECTION_SORT(arr):\n"
                "  for i from 0 to n-1:\n"
                "    min_idx = i\n"
                "    for j from i+1 to n:\n"
                "      if arr[j] < arr[min_idx]: min_idx = j\n"
                "    swap(arr[i], arr[min_idx])"
            ),
            "time_complexity": {
                "Best Case": "O(n²) — even if sorted, it keeps looking for min",
                "Average Case": "O(n²)",
                "Worst Case": "O(n²)"
            },
            "space_complexity": "O(1) — sorts the array in-place without extra memory.",
            "applications": (
                "• Education (simplest sort to teach for small data)\n"
                "• Sorting small arrays where memory write cost is more important than comparison\n"
                "• When data can't be held in memory (external sorting basics)\n"
                "• When a stable sort isn't required"
            ),
            "advantages": (
                "• Easy to implement and understand\n"
                "• In-place sorting (zero extra memory)\n"
                "• Performs well on small datasets"
            ),
            "disadvantages": (
                "• Very slow for large datasets compared to O(n log n) sorts\n"
                "• Not stable: does not preserve the relative order of equal elements\n"
                "• Independent of input: it always takes n² time regardless of initial order"
            ),
            "interview_notes": (
                "★ Note that it makes at most O(n) swaps, which is better than Bubble Sort.\n"
                "★ Explain that it is NOT a stable sort.\n"
                "★ Be ready to code it iteratively on a whiteboard.\n"
                "★ Discussion: Comparison with Insertion Sort (Insertion is usually better)."
            ),
            "java": """\
public class SelectionSortDemo {
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIdx]) minIdx = j;
            }
            // Swap
            int temp = arr[minIdx];
            arr[minIdx] = arr[i];
            arr[i] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {64, 25, 12, 22, 11};
        selectionSort(arr);
        for (int x : arr) System.out.print(x + " "); // 11 12 22 25 64 
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we understand Selection Sort's fundamental weakness: it always "
                "performs O(n²) comparisons regardless of input, making it adaptive to nothing. However, "
                "its key strength is that it makes at most O(n) swaps — one per pass — which is optimal. "
                "A stable variant of Selection Sort can be implemented by using insertion instead of swap, "
                "preserving relative order. We also study the Cycle Sort algorithm, an in-place, non-stable "
                "sort that minimizes the number of writes to memory, making it useful in scenarios where "
                "writes to disk or flash memory are expensive."
            ),
            "working": (
                "STABLE SELECTION SORT:\n"
                "  Instead of swapping the minimum with arr[i]: shift elements right and insert minimum at i.\n"
                "  This preserves relative order of equal elements.\n\n"
                "CYCLE SORT (minimum writes):\n"
                "  For each element, count how many elements are smaller (its correct position).\n"
                "  Cycle the element to its correct position; continue until all placed.\n"
                "  Result: exactly (n - number of cycles) writes to memory."
            ),
            "algorithm": (
                "STABLE SELECTION SORT:\n"
                "  for i from 0 to n-1:\n"
                "    min_idx = find minimum from arr[i..n-1]\n"
                "    key = arr[min_idx]\n"
                "    while min_idx > i: arr[min_idx] = arr[min_idx-1]; min_idx--  // shift right\n"
                "    arr[i] = key\n\n"
                "CYCLE SORT:\n"
                "  for pos from 0 to n-2:\n"
                "    count = number of elements smaller than arr[pos]\n"
                "    while count != pos: swap arr[pos] with correct position"
            ),
            "time_complexity": {
                "Selection Sort (all cases)": "O(n²)",
                "Cycle Sort Comparisons": "O(n²)",
                "Cycle Sort Writes": "O(n) — optimal minimum writes",
                "Stable Selection Sort": "O(n²)",
                "Heap Sort (upgrade)": "O(n log n) — same idea, faster"
            },
            "space_complexity": "O(1) for both Selection Sort and Cycle Sort — fully in-place.",
            "applications": (
                "• EEPROM/Flash memory sorting (Cycle Sort minimizes writes)\n"
                "• Systems where write operations are costly or limited\n"
                "• Small dataset in-place sorting in embedded systems\n"
                "• Teaching stable sort concepts using insertion approach\n"
                "• Baseline for understanding Heap Sort (Selection with a Heap)"
            ),
            "advantages": (
                "• Minimal swaps (O(n)) — useful when write cost >> compare cost\n"
                "• Cycle Sort gives provably minimum writes\n"
                "• Can be made stable with insertion strategy"
            ),
            "disadvantages": (
                "• Still O(n²) comparisons — no advantage for large data\n"
                "• Stable variant adds more shifts, slower in practice\n"
                "• Not adaptive — cannot benefit from partially sorted input"
            ),
            "interview_notes": (
                "★ 'How to make Selection Sort stable?' — use insertion, not swap.\n"
                "★ 'What sort minimizes writes?' — Cycle Sort.\n"
                "★ Heap Sort is essentially Selection Sort with a Heap data structure.\n"
                "★ Selection Sort is preferred over Bubble Sort for fewer writes."
            ),
            "java": """\
public class SelectionSort {

    // Standard Selection Sort
    static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < arr.length; j++)
                if (arr[j] < arr[minIdx]) minIdx = j;
            int temp = arr[minIdx]; arr[minIdx] = arr[i]; arr[i] = temp;
        }
    }

    // Stable Selection Sort (using insertion instead of swap)
    static void stableSelectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++)
                if (arr[j] < arr[minIdx]) minIdx = j;
            int key = arr[minIdx];
            while (minIdx > i) { arr[minIdx] = arr[minIdx - 1]; minIdx--; }
            arr[i] = key;
        }
    }

    public static void main(String[] args) {
        int[] a = {64, 25, 12, 22, 11};
        selectionSort(a);
        System.out.print("Sorted: ");
        for (int x : a) System.out.print(x + " "); // 11 12 22 25 64
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced analysis of Selection Sort reveals that it can be substantially improved by using "
                "a Heap data structure to find the minimum in O(log n) instead of O(n), yielding the "
                "Heap Sort algorithm with O(n log n) time. This connection illustrates how data structures "
                "directly improve algorithmic complexity. Tournament Sort (used in external sorting) extends "
                "this idea further: it uses a tournament tree (winner tree) to repeatedly extract the "
                "global minimum in O(log n), supporting external memory sorting where data doesn't fit in RAM."
            ),
            "working": (
                "HEAP SORT (Selection with Heap):\n"
                "  Phase 1 (Heapify): Build a Max-Heap from the array in O(n).\n"
                "  Phase 2 (Extraction): Repeatedly extract maximum and place at end in O(n log n).\n\n"
                "TOURNAMENT SORT (External Sorting):\n"
                "  Load k runs into a tournament tree (winner tree of size k).\n"
                "  Extract minimum; refill from the winning stream.\n"
                "  Each extraction costs O(log k).\n"
                "  Used when data is on disk and cannot fit into RAM."
            ),
            "algorithm": (
                "HEAP SORT:\n"
                "  build_max_heap(arr)  // O(n)\n"
                "  for i from n-1 down to 1:\n"
                "    swap(arr[0], arr[i])  // place max at end\n"
                "    heapify(arr, i, 0)    // restore heap property\n\n"
                "HEAPIFY(arr, n, root):\n"
                "  largest = root; l = 2*root+1; r = 2*root+2\n"
                "  if l < n and arr[l] > arr[largest]: largest = l\n"
                "  if r < n and arr[r] > arr[largest]: largest = r\n"
                "  if largest != root: swap; heapify(arr, n, largest)"
            ),
            "time_complexity": {
                "Heap Sort Build": "O(n)",
                "Heap Sort Extraction": "O(n log n)",
                "Tournament Sort": "O(n log k) where k = merge runs",
                "Overall Heap Sort": "O(n log n) all cases",
                "Space": "O(1) in-place"
            },
            "space_complexity": "O(1) for Heap Sort; O(k) for Tournament Sort with k-way merge.",
            "applications": (
                "• External sorting of terabytes of logs\n"
                "• Priority queue implementation via selection extraction\n"
                "• Systems with guaranteed O(n log n) requirements\n"
                "• K-way merge sort for distributed data processing\n"
                "• Operating system scheduling algorithms"
            ),
            "advantages": (
                "• Heap Sort is O(n log n) worst case with O(1) space — best of both worlds\n"
                "• Tournament Sort is optimal for external k-way merge\n"
                "• Heap Sort doesn't need recursion — fully iterative"
            ),
            "disadvantages": (
                "• Heap Sort is cache-unfriendly (non-sequential access) — slower than Quick Sort in practice\n"
                "• Not stable — cannot preserve order of equal elements\n"
                "• Tournament Sort setup cost is high for small datasets"
            ),
            "interview_notes": (
                "★ Heap Sort = Selection Sort + Max-Heap. Know both phases.\n"
                "★ Why is Heap Sort not used in practice? Cache misses.\n"
                "★ Kth Largest Element (LeetCode 215) — partial heap sort (QuickSelect is faster avg).\n"
                "★ Know that std::sort_heap in C++ implements this approach."
            ),
            "java": """\
public class AdvancedSelectionSort {

    // Heap Sort
    static void heapSort(int[] arr) {
        int n = arr.length;
        // Build max heap
        for (int i = n / 2 - 1; i >= 0; i--) heapify(arr, n, i);
        // Extract elements
        for (int i = n - 1; i > 0; i--) {
            int temp = arr[0]; arr[0] = arr[i]; arr[i] = temp;
            heapify(arr, i, 0);
        }
    }

    static void heapify(int[] arr, int n, int root) {
        int largest = root, l = 2*root+1, r = 2*root+2;
        if (l < n && arr[l] > arr[largest]) largest = l;
        if (r < n && arr[r] > arr[largest]) largest = r;
        if (largest != root) {
            int temp = arr[root]; arr[root] = arr[largest]; arr[largest] = temp;
            heapify(arr, n, largest);
        }
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6, 7};
        heapSort(arr);
        System.out.print("Heap Sorted: ");
        for (int x : arr) System.out.print(x + " "); // 5 6 7 11 12 13
    }
}"""
        }
    },

    # ==================== INSERTION SORT ====================
    "Insertion Sort": {
        "Beginner": {
            "definition": (
                "Insertion Sort is a simple sorting algorithm that builds the final sorted array one item "
                "at a time. It is much like the way you sort playing cards in your hands: you take one "
                "card and insert it into its correct position relative to the cards you already hold. It "
                "is very efficient for small datasets and 'mostly sorted' data."
            ),
            "working": (
                "1. START: Consider the first element to be sorted.\n"
                "2. TAKE NEXT: Pick the next element and store it in a temporary variable (key).\n"
                "3. SHIFT: Compare the key with elements in the sorted part (from right to left). Shift "
                "elements to the right that are larger than the key.\n"
                "4. INSERT: Insert the key into the empty slot.\n"
                "5. REPEAT: Continue for all elements."
            ),
            "algorithm": (
                "INSERTION_SORT(arr):\n"
                "  for i from 1 to n:\n"
                "    key = arr[i]\n"
                "    j = i - 1\n"
                "    while j >= 0 and arr[j] > key:\n"
                "      arr[j+1] = arr[j]; j--\n"
                "    arr[j+1] = key"
            ),
            "time_complexity": {
                "Best Case": "O(n) — array is already sorted",
                "Average Case": "O(n²)",
                "Worst Case": "O(n²) — array is reverse sorted"
            },
            "space_complexity": "O(1) — in-place sorting.",
            "applications": (
                "• Sorting small lists (used by hybrid algorithms like Timsort)\n"
                "• Sorting arrays that are nearly sorted (very common application)\n"
                "• Real-time data streams (inserting one item at a time)\n"
                "• Simple embedded systems with extreme memory constraints"
            ),
            "advantages": (
                "• Adaptive: much faster if the list is nearly sorted\n"
                "• Stable: preserves order of equal elements\n"
                "• Online: can sort a list as it receives it"
            ),
            "disadvantages": (
                "• Poor performance on large random datasets compared to Merge/Quick Sort\n"
                "• High number of shifts compared to Selection Sort's swaps"
            ),
            "interview_notes": (
                "★ Highlight its O(n) best-case performance.\n"
                "★ Contrast with Selection Sort (Stability and Performance on mostly sorted data).\n"
                "★ Mention that Java's `Arrays.sort` uses a variant of this for small arrays.\n"
                "★ Be ready to dry-run it on a small array like {4, 3, 2, 10, 12, 1, 5, 6}."
            ),
            "java": """\
public class InsertionSortDemo {
    public static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6};
        insertionSort(arr);
        for (int x : arr) System.out.print(x + " "); // 5 11 12 13 
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, Insertion Sort is studied for its adaptiveness and its role as a "
                "component in hybrid sorts. It runs in O(n + d) time, where d is the number of inversions in "
                "the input, making it the best algorithm for near-sorted data. Binary Insertion Sort "
                "improves the comparison count to O(n log n) by using binary search to find the insertion "
                "position, though the number of shifts remains O(n²). Shell Sort is a generalization of "
                "Insertion Sort that first sorts far-apart elements, progressively reducing the gap until "
                "a final Insertion Sort pass on a nearly-sorted array achieves O(n log n) or better."
            ),
            "working": (
                "BINARY INSERTION SORT:\n"
                "  for i from 1 to n-1:\n"
                "    key = arr[i]\n"
                "    pos = binary_search(arr[0..i-1], key)  // O(log i) comparisons\n"
                "    shift arr[pos..i-1] right by one\n"
                "    arr[pos] = key\n\n"
                "SHELL SORT (gap sequence: n/2, n/4, ..., 1):\n"
                "  for each gap from n/2 down to 1:\n"
                "    for i from gap to n-1:\n"
                "      key = arr[i]; j = i\n"
                "      while j >= gap and arr[j-gap] > key: arr[j] = arr[j-gap]; j -= gap\n"
                "      arr[j] = key"
            ),
            "algorithm": (
                "SHELL SORT (Ciura gap sequence: 701, 301, 132, 57, 23, 10, 4, 1):\n"
                "  for each gap in [701, 301, 132, 57, 23, 10, 4, 1]:\n"
                "    for i from gap to n-1: insertion sort step with stride = gap"
            ),
            "time_complexity": {
                "Binary Insertion Sort Comparisons": "O(n log n)",
                "Binary Insertion Sort Shifts": "O(n²) — shifting still O(n) per element",
                "Shell Sort (Shell's original)": "O(n²)",
                "Shell Sort (Hibbard's gaps)": "O(n^(3/2))",
                "Shell Sort (Ciura gaps, practical best)": "O(n log n) approx"
            },
            "space_complexity": "O(1) for all variants — fully in-place.",
            "applications": (
                "• Timsort uses Insertion Sort for small subarrays (<64 elements)\n"
                "• Online sorting: sort data as it arrives in a stream\n"
                "• Shell Sort used in embedded systems as a fast, tiny-code alternative\n"
                "• Nearly sorted data from incremental database updates\n"
                "• PDQ Sort (used in Rust/C++) uses Insertion Sort fallback"
            ),
            "advantages": (
                "• O(n) on nearly sorted data — unbeatable for this case\n"
                "• Binary Insertion Sort reduces comparisons to O(n log n)\n"
                "• Shell Sort breaks the O(n²) barrier with a simple modification"
            ),
            "disadvantages": (
                "• Binary Insertion Sort still has O(n²) shifts despite fewer comparisons\n"
                "• Shell Sort's optimal gap sequence is still an open research problem\n"
                "• Not as fast as Merge Sort or Quick Sort for random data"
            ),
            "interview_notes": (
                "★ 'When is Insertion Sort optimal?' — O(n) for nearly sorted data; O(n + d) where d = inversions.\n"
                "★ Timsort uses Insertion Sort for runs of length < 64 inside Merge Sort.\n"
                "★ Shell Sort is a 'good enough' O(n log n) sort that is trivial to implement.\n"
                "★ Binary Insertion helps comparisons but not shifts — total is still O(n²) time."
            ),
            "java": """\
public class IntermediateInsertionSort {

    // Binary Insertion Sort
    static void binaryInsertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int pos = binarySearch(arr, 0, i - 1, key);
            // Shift elements right
            System.arraycopy(arr, pos, arr, pos + 1, i - pos);
            arr[pos] = key;
        }
    }
    static int binarySearch(int[] arr, int lo, int hi, int key) {
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid] <= key) lo = mid + 1; else hi = mid - 1;
        }
        return lo;
    }

    // Shell Sort
    static void shellSort(int[] arr) {
        int n = arr.length;
        int[] gaps = {701, 301, 132, 57, 23, 10, 4, 1}; // Ciura gaps
        for (int gap : gaps) {
            for (int i = gap; i < n; i++) {
                int key = arr[i], j = i;
                while (j >= gap && arr[j - gap] > key) { arr[j] = arr[j - gap]; j -= gap; }
                arr[j] = key;
            }
        }
    }

    public static void main(String[] args) {
        int[] a1 = {12, 11, 13, 5, 6};
        binaryInsertionSort(a1);
        System.out.print("Binary Insertion: ");
        for (int x : a1) System.out.print(x + " "); // 5 6 11 12 13

        int[] a2 = {64, 34, 25, 12, 22, 11, 90};
        shellSort(a2);
        System.out.print("\nShell Sort: ");
        for (int x : a2) System.out.print(x + " "); // 11 12 22 25 34 64 90
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced Insertion Sort analysis focuses on understanding the Timsort algorithm (Python's "
                "and Java's stable sort for objects), which is a hybrid of Merge Sort and Insertion Sort. "
                "Timsort detects natural runs (already sorted subsequences) in the input and merges them "
                "using a galloping merge strategy. It achieves O(n) for 'well-structured' real-world data "
                "while maintaining O(n log n) worst case. The key insight is that real-world data is rarely "
                "random — it often has natural ordered sequences that Timsort exploits."
            ),
            "working": (
                "TIMSORT ALGORITHM:\n"
                "  1. Find natural runs (sorted sequences, extending short ones with Insertion Sort to minRun size).\n"
                "  2. minRun = 32-64 (chosen to optimize number of merge passes).\n"
                "  3. Push runs onto a stack.\n"
                "  4. Merge adjacent runs when stack invariant is violated (|Z| <= |Y| + |X|).\n\n"
                "GALLOPING MODE:\n"
                "  When one run dominates many consecutive merge steps, switch to galloping merge.\n"
                "  In galloping: search for merge cross-over point exponentially, then binary.\n"
                "  This gives O(log n) merge cost for already-separated runs."
            ),
            "algorithm": (
                "TIMSORT:\n"
                "  minRun = computeMinRun(n) // 32-64 based on n\n"
                "  for i from 0 to n step minRun:\n"
                "    insertionSort(arr, i, min(i+minRun, n))\n"
                "  size = minRun\n"
                "  while size < n:\n"
                "    for left from 0 to n step 2*size:\n"
                "      merge(arr, left, left+size, min(left+2*size, n))\n"
                "    size *= 2"
            ),
            "time_complexity": {
                "Timsort Best": "O(n) — fully sorted or reverse sorted input",
                "Timsort Average/Worst": "O(n log n)",
                "Galloping Merge": "O(log n) per element when one stream dominates",
                "Patience Sorting": "O(n log n) — optimal for LIS computation too",
                "Shell Sort (practical)": "O(n log n) with good gap sequence"
            },
            "space_complexity": "O(n) for Timsort (temporary merge buffer); O(1) for Shell Sort.",
            "applications": (
                "• Timsort is the default sort in Python (sorted()) and Java (Arrays.sort for objects)\n"
                "• Database ascending scan with pre-sorted runs\n"
                "• File system directory listing (already partially sorted by name)\n"
                "• Merge-phase in external sorting pipelines\n"
                "• Competitive programming for guaranteed stable O(n log n)"
            ),
            "advantages": (
                "• Timsort is optimal for real-world data with natural order\n"
                "• Stable — critical for multi-key sorting (first by name, then by age)\n"
                "• Adaptive — O(n) for nearly-sorted, O(n log n) worst case"
            ),
            "disadvantages": (
                "• Complex implementation (800+ lines in CPython)\n"
                "• O(n) extra space — unlike Quick Sort's O(log n)\n"
                "• Overhead for random data vs specialized sorts"
            ),
            "interview_notes": (
                "★ 'What does Java's Arrays.sort use for objects?' — Timsort (stable).\n"
                "★ 'What does Python's sorted() use?' — Timsort.\n"
                "★ Timsort = Merge Sort + Insertion Sort on natural runs.\n"
                "★ Key insight: real-world data has pre-existing order — exploit it!"
            ),
            "java": """\
import java.util.Arrays;

public class AdvancedInsertionSort {

    // Simplified Timsort-like (bottom-up merge with insertion sort runs)
    static final int MIN_RUN = 32;

    static void insertionSort(int[] arr, int lo, int hi) {
        for (int i = lo + 1; i <= hi; i++) {
            int key = arr[i], j = i - 1;
            while (j >= lo && arr[j] > key) { arr[j+1] = arr[j]; j--; }
            arr[j+1] = key;
        }
    }

    static void merge(int[] arr, int lo, int mid, int hi) {
        int[] tmp = Arrays.copyOfRange(arr, lo, mid + 1);
        int i = 0, j = mid + 1, k = lo;
        while (i < tmp.length && j <= hi)
            arr[k++] = (tmp[i] <= arr[j]) ? tmp[i++] : arr[j++];
        while (i < tmp.length) arr[k++] = tmp[i++];
    }

    static void timSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i += MIN_RUN)
            insertionSort(arr, i, Math.min(i + MIN_RUN - 1, n - 1));
        for (int size = MIN_RUN; size < n; size *= 2) {
            for (int lo = 0; lo < n; lo += 2 * size) {
                int mid = Math.min(lo + size - 1, n - 1);
                int hi = Math.min(lo + 2 * size - 1, n - 1);
                if (mid < hi) merge(arr, lo, mid, hi);
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {5, 21, 7, 23, 19, 3, 14, 1, 8, 11, 4, 18, 2};
        timSort(arr);
        System.out.println("TimSort: " + Arrays.toString(arr));
    }
}"""
        }
    },

    # ==================== MERGE SORT ====================
    "Merge Sort": {
        "Beginner": {
            "definition": (
                "Merge Sort is an extremely efficient, stable, divide-and-conquer sorting algorithm. It "
                "works by recursively splitting the array into two halves until each subarray contains "
                "only one element, and then merging those sorted halves back together in a specific "
                "order to produce a fully sorted result. It is the gold standard for predictable "
                "O(n log n) performance."
            ),
            "working": (
                "1. DIVIDE: If the array has more than one element, split it in the middle.\n"
                "2. CONQUER: Recursively call Merge Sort on the left half and right half.\n"
                "3. COMBINE (MERGE): Merge the two sorted halves into a single sorted array. This "
                "step involves using pointers to compare the smallest elements of each half and "
                "picking the smaller one for the result."
            ),
            "algorithm": (
                "MERGE_SORT(arr, L, R):\n"
                "  if L < R:\n"
                "    mid = (L + R) / 2\n"
                "    MERGE_SORT(arr, L, mid)\n"
                "    MERGE_SORT(arr, mid + 1, R)\n"
                "    MERGE(arr, L, mid, R)"
            ),
            "time_complexity": {
                "Best Case": "O(n log n)",
                "Average Case": "O(n log n)",
                "Worst Case": "O(n log n)"
            },
            "space_complexity": "O(n) — requires extra memory for temporary subarrays during merging.",
            "applications": (
                "• Sorting large linked lists (O(1) extra space versions exist for lists)\n"
                "• External Sorting (when data is too large for RAM)\n"
                "• E-commerce platforms sorting product lists by price/rating stably\n"
                "• Implementation of `Arrays.sort` for objects in Java (Timsort variant)"
            ),
            "advantages": (
                "• Guaranteed O(n log n) even in the worst case\n"
                "• Stable: relative order of duplicate elements is preserved\n"
                "• Divide-and-conquer logic makes it easily parallelizable"
            ),
            "disadvantages": (
                "• High memory requirement (O(n) for temporary space)\n"
                "• Slower than Quick Sort for small and medium arrays in practice\n"
                "• Recursive overhead can be high if not optimized"
            ),
            "interview_notes": (
                "★ Emphasize that it is Stable and always O(n log n).\n"
                "★ Be able to explain the Merge step in detail (using two pointers).\n"
                "★ Explain the tradeoff: it uses more memory but is stable compared to Quick Sort.\n"
                "★ Discuss when to use Merge Sort over Quick Sort (stability, external sorting)."
            ),
            "java": """\
public class MergeSortDemo {
    public static void mergeSort(int[] arr, int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    private static void merge(int[] arr, int l, int m, int r) {
        int n1 = m - l + 1, n2 = r - m;
        int[] L = new int[n1], R = new int[n2];
        for (int i = 0; i < n1; ++i) L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j) R[j] = arr[m + 1 + j];

        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) arr[k++] = L[i++];
            else arr[k++] = R[j++];
        }
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }

    public static void main(String[] args) {
        int[] arr = {38, 27, 43, 3, 9, 82, 10};
        mergeSort(arr, 0, arr.length - 1);
        for(int x : arr) System.out.print(x + " "); // 3 9 10 27 38 43 82
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, we study Merge Sort's important applications beyond simple sorting: "
                "counting inversions in an array and External Merge Sort for large files. Counting inversions "
                "(pairs where i < j but arr[i] > arr[j]) can be done in O(n log n) by modifying the merge "
                "step — whenever a right-half element is placed before a left-half element, it forms "
                "inversions with all remaining left-half elements. Bottom-up Merge Sort replaces recursion "
                "with an iterative approach, sorting increasingly large subarrays (1, 2, 4, 8...) without "
                "a call stack, reducing stack overflow risk and overhead."
            ),
            "working": (
                "INVERSION COUNT VIA MERGE SORT:\n"
                "  During merge: when arr[right] < arr[left]:\n"
                "    inversions += (mid - left_ptr + 1)  // all remaining left elements form inversions\n\n"
                "BOTTOM-UP MERGE SORT:\n"
                "  for width from 1 to n (doubling):\n"
                "    for i from 0 to n-1 step 2*width:\n"
                "      merge(arr, i, i+width-1, min(i+2*width-1, n-1))\n"
                "  No recursion; builds sorted runs iteratively."
            ),
            "algorithm": (
                "MERGE SORT INVERSION COUNT:\n"
                "  mergeCount(arr, l, r):\n"
                "    if l >= r: return 0\n"
                "    mid = (l+r)/2\n"
                "    count = mergeCount(arr, l, mid) + mergeCount(arr, mid+1, r)\n"
                "    count += mergeAndCount(arr, l, mid, r)\n"
                "    return count\n\n"
                "  mergeAndCount: standard merge, but: whenever right[j] < left[i]:\n"
                "    count += leftSize - i  // inversions"
            ),
            "time_complexity": {
                "Inversion Count": "O(n log n)",
                "Bottom-Up Merge Sort": "O(n log n) — same, no recursion overhead",
                "External Merge Sort": "O(n log n) but with I/O optimized passes",
                "Natural Merge Sort": "O(n log k) where k = number of runs",
                "Merge Sort on Linked List": "O(n log n) with O(1) extra space"
            },
            "space_complexity": "O(n) for temp storage; O(log n) recursion for top-down; O(1) stack for bottom-up.",
            "applications": (
                "• Counting inversions for array similarity metrics\n"
                "• External sorting of multi-GB log files\n"
                "• Distributed sort-merge in MapReduce pipelines\n"
                "• Stable online multi-key ranking systems\n"
                "• Implementing OLAP cube aggregation efficiently"
            ),
            "advantages": (
                "• Inversion count at no extra asymptotic cost — neat reuse of merge step\n"
                "• Bottom-up avoids recursion depth issues for huge inputs\n"
                "• Naturally parallelizable across multiple CPUs/machines"
            ),
            "disadvantages": (
                "• O(n) auxiliary space is still required\n"
                "• Inversion count modification adds code complexity\n"
                "• Not cache-friendly for very large arrays (non-sequential access)"
            ),
            "interview_notes": (
                "★ Count of Inversions — classic interview problem. Solve via modified Merge Sort in O(n log n).\n"
                "★ 'Why sorted() is stable?' — Merge Sort (Timsort) guarantees stability.\n"
                "★ Bottom-up Merge Sort in linked lists is O(n log n) with O(1) space.\n"
                "★ External Sort: sort chunks individually, then k-way merge with a Min-Heap."
            ),
            "java": """\
public class IntermediateMergeSort {

    static long inversionCount;

    static void mergeSortCount(int[] arr, int l, int r) {
        if (l >= r) return;
        int mid = (l + r) / 2;
        mergeSortCount(arr, l, mid);
        mergeSortCount(arr, mid + 1, r);
        mergeAndCount(arr, l, mid, r);
    }

    static void mergeAndCount(int[] arr, int l, int mid, int r) {
        int[] left = java.util.Arrays.copyOfRange(arr, l, mid + 1);
        int[] right = java.util.Arrays.copyOfRange(arr, mid + 1, r + 1);
        int i = 0, j = 0, k = l;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) arr[k++] = left[i++];
            else {
                arr[k++] = right[j++];
                inversionCount += left.length - i; // key insight
            }
        }
        while (i < left.length) arr[k++] = left[i++];
        while (j < right.length) arr[k++] = right[j++];
    }

    public static void main(String[] args) {
        int[] arr = {8, 4, 2, 1};
        inversionCount = 0;
        mergeSortCount(arr, 0, arr.length - 1);
        System.out.println("Inversions in [8,4,2,1]: " + inversionCount); // 6
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced Merge Sort applications include Polyphase Merge Sort for tape-based external sorting "
                "(minimizing the number of tape passes), Parallel Merge Sort using fork-join parallelism, and "
                "the mathematical analysis of Merge Sort's recurrence T(n) = 2T(n/2) + O(n) via the Master "
                "Theorem. Parallel Merge Sort achieves O(n) time with O(n) parallel processors, or more "
                "practically O(n/p * log n) with p processors. The merge step itself can be parallelized "
                "using a parallel binary search-based merge in O(log² n) with O(n) processors."
            ),
            "working": (
                "PARALLEL MERGE SORT (Fork-Join):\n"
                "  if size <= threshold: sequential merge sort\n"
                "  else: fork two halves; join; merge\n"
                "  With p processors: O((n log n) / p + n log p) time.\n\n"
                "POLYPHASE MERGE SORT (External):\n"
                "  Distribute sorted runs across tapes in Fibonacci ratios.\n"
                "  Merge from multiple tapes at once.\n"
                "  Fewer tape passes than standard 2-way merge."
            ),
            "algorithm": (
                "MASTER THEOREM for Merge Sort:\n"
                "  T(n) = 2T(n/2) + O(n)\n"
                "  a=2, b=2, f(n)=n. log_b(a) = log_2(2) = 1.\n"
                "  f(n) = O(n^1) = O(n^log_b(a)).\n"
                "  Case 2 applies: T(n) = O(n log n).  // CONFIRMED!"
            ),
            "time_complexity": {
                "Sequential Merge Sort": "O(n log n)",
                "Parallel Merge Sort": "O(n/p * log n + log² n) with p processors",
                "Parallel Merge Step": "O(log² n) with O(n) processors",
                "Polyphase External Merge": "O(n log_k n) passes with k tapes",
                "Merge Sort Lower Bound": "Ω(n log n) — provably optimal"
            },
            "space_complexity": "O(n) sequential; O(n log n) if each thread allocates independently.",
            "applications": (
                "• MapReduce shuffle phase (distributed external merge)\n"
                "• Parallel sort for big data in GPU/FPGA systems\n"
                "• Database query sort operations in multi-core systems\n"
                "• Genome sequencing sort pipelines\n"
                "• Multi-tape archival sorting systems"
            ),
            "advantages": (
                "• Linear speedup with parallelism for large datasets\n"
                "• Provably optimal O(n log n) lower bound for comparison sorts\n"
                "• External sorting enables sorting beyond RAM capacity"
            ),
            "disadvantages": (
                "• Parallel implementation requires synchronization overhead\n"
                "• Memory allocation in parallel increases GC pressure\n"
                "• Polyphase sort is extremely complex to implement correctly"
            ),
            "interview_notes": (
                "★ 'What is the lower bound for comparison-based sorting?' — Ω(n log n).\n"
                "★ 'Prove Merge Sort is O(n log n)' — use the Master Theorem recurrence.\n"
                "★ Parallel Merge Sort is O(n log n / p + n) with p processors.\n"
                "★ Count Inversions (Modified Merge Sort) is a top Microsoft/Google interview problem."
            ),
            "java": """\
import java.util.concurrent.*;
import java.util.Arrays;

public class AdvancedMergeSort {

    // Parallel Merge Sort using ForkJoin
    static class ParallelMergeSort extends RecursiveAction {
        int[] arr;
        int lo, hi;
        static final int THRESHOLD = 1000;

        ParallelMergeSort(int[] arr, int lo, int hi) {
            this.arr = arr; this.lo = lo; this.hi = hi;
        }

        @Override
        protected void compute() {
            if (hi - lo <= THRESHOLD) {
                Arrays.sort(arr, lo, hi + 1); // use sequential for small
                return;
            }
            int mid = (lo + hi) / 2;
            ParallelMergeSort left = new ParallelMergeSort(arr, lo, mid);
            ParallelMergeSort right = new ParallelMergeSort(arr, mid + 1, hi);
            invokeAll(left, right); // Fork both
            merge(arr, lo, mid, hi);
        }

        static void merge(int[] arr, int lo, int mid, int hi) {
            int[] tmp = Arrays.copyOfRange(arr, lo, mid + 1);
            int i = 0, j = mid + 1, k = lo;
            while (i < tmp.length && j <= hi)
                arr[k++] = (tmp[i] <= arr[j]) ? tmp[i++] : arr[j++];
            while (i < tmp.length) arr[k++] = tmp[i++];
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[10000];
        for (int i = 0; i < arr.length; i++) arr[i] = arr.length - i;
        ForkJoinPool pool = new ForkJoinPool();
        pool.invoke(new ParallelMergeSort(arr, 0, arr.length - 1));
        System.out.println("First 5: " + Arrays.toString(Arrays.copyOf(arr, 5))); // [1, 2, 3, 4, 5]
        pool.shutdown();
    }
}"""
        }
    },

    # ==================== QUICK SORT ====================
    "Quick Sort": {
        "Beginner": {
            "definition": (
                "Quick Sort is a highly popular, extremely fast divide-and-conquer sorting algorithm. It "
                "works by picking a 'pivot' element from the array and partitioning the other elements "
                "into binary groups: those smaller than the pivot and those larger. It then recursively "
                "sorts the partitions. In practice, it is often the fastest sorting algorithm for general data."
            ),
            "working": (
                "1. PICK PIVOT: Choose an element (e.g., first, last, middle, or random).\n"
                "2. PARTITIONING: Re-arrange the array such that all items < pivot are on the left, "
                "and all items > pivot are on the right.\n"
                "3. RECURSE: Recursively apply the same logic to the left and right subarrays.\n"
                "4. BASE CASE: Stops when a subarray has 0 or 1 element."
            ),
            "algorithm": (
                "QUICK_SORT(arr, low, high):\n"
                "  if low < high:\n"
                "    p = PARTITION(arr, low, high)\n"
                "    QUICK_SORT(arr, low, p - 1)\n"
                "    QUICK_SORT(arr, p + 1, high)"
            ),
            "time_complexity": {
                "Best Case": "O(n log n)",
                "Average Case": "O(n log n)",
                "Worst Case": "O(n²) — occurs if pivot is always the min or max (e.g., already sorted array)"
            },
            "space_complexity": "O(log n) — due to the recursive call stack.",
            "applications": (
                "• General-purpose library sorting functions (standard C `qsort`, Java dual-pivot)\n"
                "• Competitive programming (due to speed and O(1) extra auxiliary space)\n"
                "• Numerical Analysis and scientific computing libraries\n"
                "• Processing large log files in systems"
            ),
            "advantages": (
                "• Extremely fast in practice (low constant factors for operations)\n"
                "• In-place sorting: uses very little extra memory (just stack space)\n"
                "• Cache-friendly: scans the array linearly during partitioning"
            ),
            "disadvantages": (
                "• Unstable: does not naturally preserve order of equal elements\n"
                "• Worst-case performance is poor (O(n²)) if pivot selection is bad\n"
                "• Sensitive to duplicate elements (needs specific variants like 3-way partition)"
            ),
            "interview_notes": (
                "★ Explain how partitioning works (using two pointers: `i` and `j`).\n"
                "★ Discuss 'Pivot Selection' (why Random or Median-of-3 is better than First/Last).\n"
                "★ Compare with Merge Sort (Space vs. Speed vs. Stability).\n"
                "★ Be ready to discuss tailored versions for arrays with many duplicates."
            ),
            "java": """\
public class QuickSortDemo {
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high], i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
            }
        }
        int temp = arr[i + 1]; arr[i + 1] = arr[high]; arr[high] = temp;
        return i + 1;
    }

    public static void main(String[] args) {
        int[] arr = {10, 7, 8, 9, 1, 5};
        quickSort(arr, 0, arr.length - 1);
        for(int x : arr) System.out.print(x + " "); // 1 5 7 8 9 10 
    }
}"""
        },

        "Intermediate": {
            "definition": (
                "At the intermediate level, Quick Sort refinements include the three-way partition (Dutch "
                "National Flag variant) for arrays with many duplicates, and the randomized pivot selection "
                "to guarantee O(n log n) expected time regardless of input order. The three-way partition "
                "maintains three zones: elements less than pivot, equal to pivot, and greater than pivot, "
                "reducing repeated comparisons of equal elements from O(n²) to O(n) for arrays with few "
                "distinct values. QuickSelect — a variant of Quick Sort — finds the k-th smallest "
                "element in O(n) average time without fully sorting the array."
            ),
            "working": (
                "THREE-WAY PARTITION (Dutch National Flag):\n"
                "  lt, i, gt = lo, lo, hi (three-pointer approach)\n"
                "  while i <= gt:\n"
                "    if arr[i] < pivot: swap(arr[lt], arr[i]); lt++; i++\n"
                "    elif arr[i] > pivot: swap(arr[i], arr[gt]); gt--\n"
                "    else: i++\n"
                "  Result: arr[lo..lt-1] < pivot, arr[lt..gt] == pivot, arr[gt+1..hi] > pivot\n\n"
                "QUICKSELECT (K-th Smallest):\n"
                "  Partition around pivot.\n"
                "  If pivot position == k: return arr[k].\n"
                "  If k < pivot: recurse left only.\n"
                "  If k > pivot: recurse right only."
            ),
            "algorithm": (
                "QUICKSELECT(arr, lo, hi, k):\n"
                "  pivot = arr[hi]; partition; pivot_pos = result of partition\n"
                "  if pivot_pos == k: return arr[k]\n"
                "  elif k < pivot_pos: QUICKSELECT(arr, lo, pivot_pos-1, k)\n"
                "  else: QUICKSELECT(arr, pivot_pos+1, hi, k)\n\n"
                "RANDOMIZED QUICK SORT:\n"
                "  swap arr[random(lo, hi)] with arr[hi] before partitioning"
            ),
            "time_complexity": {
                "Three-Way QuickSort (many dupes)": "O(n log n) or O(n) in best case",
                "QuickSelect (Avg)": "O(n)",
                "QuickSelect (Worst)": "O(n²) — without randomization",
                "Randomized QuickSort": "O(n log n) expected",
                "Median of Medians": "O(n) guaranteed — complex constant factor"
            },
            "space_complexity": "O(log n) expected recursive depth for randomized version.",
            "applications": (
                "• Arrays with many repeated elements (3-way partition)\n"
                "• Finding K-th largest/smallest (QuickSelect)\n"
                "• Statistics computation (median, percentiles)\n"
                "• Competitive programming for fast custom sorting\n"
                "• Database null-safe sorting implementations"
            ),
            "advantages": (
                "• Three-way partition handles duplicates far better than standard Quick Sort\n"
                "• QuickSelect beats sorting for single k-th element problems\n"
                "• Randomized pivot eliminates adversarial worst-case inputs"
            ),
            "disadvantages": (
                "• QuickSelect is still O(n²) worst case without median-of-medians\n"
                "• Three-way partition adds pointer management complexity\n"
                "• Unstable — still cannot maintain equal element order"
            ),
            "interview_notes": (
                "★ Kth Largest Element (LeetCode 215) — QuickSelect O(n) avg.\n"
                "★ Sort Colors (LeetCode 75) — Dutch National Flag 3-way partition.\n"
                "★ Wiggle Sort II (LeetCode 324) — QuickSelect + 3-way partition.\n"
                "★ Why randomize? Adversarial inputs (sorted arrays) make any fixed pivot O(n²)."
            ),
            "java": """\
import java.util.*;

public class IntermediateQuickSort {

    // Dutch National Flag 3-Way Partition
    static void threeWayQuickSort(int[] arr, int lo, int hi) {
        if (lo >= hi) return;
        int lt = lo, i = lo, gt = hi;
        int pivot = arr[lo + new Random().nextInt(hi - lo + 1)];
        while (i <= gt) {
            if (arr[i] < pivot) { int t = arr[lt]; arr[lt] = arr[i]; arr[i] = t; lt++; i++; }
            else if (arr[i] > pivot) { int t = arr[i]; arr[i] = arr[gt]; arr[gt] = t; gt--; }
            else i++;
        }
        threeWayQuickSort(arr, lo, lt - 1);
        threeWayQuickSort(arr, gt + 1, hi);
    }

    // QuickSelect - K-th Smallest
    static int quickSelect(int[] arr, int lo, int hi, int k) {
        if (lo == hi) return arr[lo];
        int pivot = arr[lo + new Random().nextInt(hi - lo + 1)];
        int i = lo, j = hi;
        while (i <= j) {
            while (arr[i] < pivot) i++;
            while (arr[j] > pivot) j--;
            if (i <= j) { int t = arr[i]; arr[i] = arr[j]; arr[j] = t; i++; j--; }
        }
        if (k <= j) return quickSelect(arr, lo, j, k);
        if (k >= i) return quickSelect(arr, i, hi, k);
        return arr[k];
    }

    public static void main(String[] args) {
        int[] arr = {3, 3, 3, 1, 2, 4, 4};
        threeWayQuickSort(arr, 0, arr.length - 1);
        System.out.println("3-Way sorted: " + Arrays.toString(arr));
        int[] arr2 = {3, 2, 1, 5, 6, 4};
        System.out.println("2nd smallest: " + quickSelect(arr2, 0, arr2.length-1, 1)); // 2
    }
}"""
        },

        "Advanced": {
            "definition": (
                "Advanced Quick Sort topics include the Introsort hybrid (used by most standard libraries: "
                "Quick Sort for small arrays, Heap Sort when depth exceeds 2*log(n) to avoid O(n²) worst "
                "case, and Insertion Sort for tiny subarrays), and the BFPRT/Median-of-Medians algorithm for "
                "guaranteed O(n) selection. Java's dual-pivot Quick Sort (introduced in Java 7) uses two "
                "pivots to partition into three parts, achieving better cache performance than single-pivot "
                "and running 10-15% faster on real-world data according to benchmarks."
            ),
            "working": (
                "INTROSORT HYBRID:\n"
                "  Start with Quick Sort.\n"
                "  If recursion depth > 2 * floor(log2(n)): switch to Heap Sort.\n"
                "  If subarray size <= 16: switch to Insertion Sort.\n\n"
                "DUAL-PIVOT QUICK SORT (Java 7+):\n"
                "  Choose two pivots p1 <= p2.\n"
                "  Partition into: arr < p1, p1 <= arr <= p2, arr > p2.\n"
                "  Recursively sort 3 parts.\n"
                "  Fewer comparisons for equal elements; better branch prediction.\n\n"
                "BFPRT (Median of Medians):\n"
                "  Divide into groups of 5; sort each group; find median of medians.\n"
                "  Use median as pivot; guarantees 30/70 split, leading to O(n) worst case."
            ),
            "algorithm": (
                "INTROSORT:\n"
                "  introsort(arr, lo, hi, depthLimit):\n"
                "    if size <= 16: insertionSort(arr, lo, hi); return\n"
                "    if depthLimit == 0: heapSort(arr, lo, hi); return\n"
                "    pivot = medianOf3(arr, lo, mid, hi)\n"
                "    partition; recurse with depthLimit - 1"
            ),
            "time_complexity": {
                "Introsort": "O(n log n) worst case",
                "Dual-Pivot QuickSort": "O(n log n) expected, better constants",
                "BFPRT Selection": "O(n) worst case",
                "BFPRT practical overhead": "~5-10x slower than QuickSelect despite O(n) guarantee",
                "Java Arrays.sort(int[]) ": "Dual-Pivot QuickSort"
            },
            "space_complexity": "O(log n) for introsort; O(n) for BFPRT (groups).",
            "applications": (
                "• Standard library sorting (Java Arrays.sort, C++ std::sort = introsort)\n"
                "• Real-time systems needing worst-case guarantees\n"
                "• Cache-conscious data sorting\n"
                "• Competitive programming custom comparators\n"
                "• In-place data shuffling for streaming algorithms"
            ),
            "advantages": (
                "• Introsort combines best of Quick Sort, Heap Sort, and Insertion Sort\n"
                "• Dual-pivot performs fewer comparisons on average\n"
                "• BFPRT provides theoretical O(n) guarantee for any input"
            ),
            "disadvantages": (
                "• BFPRT's constant factor makes it slower than QuickSelect in practice\n"
                "• Introsort loses Quick Sort's cache friendliness when falling back to Heap Sort\n"
                "• Dual-pivot only benefits primitives — Java uses Merge Sort for objects"
            ),
            "interview_notes": (
                "★ Know that Java Arrays.sort(int[]) uses Dual-Pivot QuickSort (unstable).\n"
                "★ Java Arrays.sort(Object[]) uses Timsort (stable merge sort variant).\n"
                "★ BFPRT guarantees O(n) but interviewers rarely ask to implement it.\n"
                "★ Introsort = Quick + Heap + Insertion hybrid — name this in sorting discussions."
            ),
            "java": """\
import java.util.*;

public class AdvancedQuickSort {
    // Simplified Introsort (Quick + Insertion fallback)
    static int THRESHOLD = 16;

    static void introsort(int[] arr, int lo, int hi, int depthLimit) {
        if (hi - lo + 1 <= THRESHOLD) { insertionSort(arr, lo, hi); return; }
        if (depthLimit == 0) { heapSort(arr, lo, hi); return; }
        // median-of-3 pivot
        int mid = lo + (hi - lo) / 2;
        if (arr[lo] > arr[mid]) { int t = arr[lo]; arr[lo] = arr[mid]; arr[mid] = t; }
        if (arr[lo] > arr[hi]) { int t = arr[lo]; arr[lo] = arr[hi]; arr[hi] = t; }
        if (arr[mid] > arr[hi]) { int t = arr[mid]; arr[mid] = arr[hi]; arr[hi] = t; }
        int pivot = arr[mid];
        int i = lo, j = hi;
        while (i <= j) {
            while (arr[i] < pivot) i++; while (arr[j] > pivot) j--;
            if (i <= j) { int t = arr[i]; arr[i] = arr[j]; arr[j] = t; i++; j--; }
        }
        introsort(arr, lo, j, depthLimit - 1);
        introsort(arr, i, hi, depthLimit - 1);
    }
    static void insertionSort(int[] arr, int lo, int hi) {
        for (int i = lo+1; i <= hi; i++) {
            int key = arr[i], j = i-1;
            while (j >= lo && arr[j] > key) { arr[j+1] = arr[j]; j--; }
            arr[j+1] = key;
        }
    }
    static void heapSort(int[] arr, int lo, int hi) {
        // Simple heap sort on subarray
        Arrays.sort(arr, lo, hi + 1); // placeholder; real impl uses heapify
    }

    public static void main(String[] args) {
        int[] arr = {64, 25, 12, 22, 11, 50, 3, 99, 7};
        int depthLimit = 2 * (int) (Math.log(arr.length) / Math.log(2));
        introsort(arr, 0, arr.length - 1, depthLimit);
        System.out.println("Introsorted: " + Arrays.toString(arr));
    }
}"""
        }
    }
}
# ==============================
# API ROUTES
# ==============================

@app.get("/module/{module}/{level}")
def get_module(module: str, level: str):
    if module in DSA_CONTENT and level in DSA_CONTENT[module]:
        return DSA_CONTENT[module][level]
    return {"error": f"Content not found for module='{module}' level='{level}'"}

@app.get("/modules")
def list_modules():
    return {
        "modules": list(DSA_CONTENT.keys()),
        "levels": ["Beginner", "Intermediate", "Advanced"]
    }

@app.get("/health")
def health():
    return {"status": "ok", "message": "DSA Learning API is running"}

# --- VISUALIZATION API ---
class VisualizeRequest(BaseModel):
    algorithm: str
    input: Any
    code: Optional[str] = None

import re

def parse_code_for_visualizer(algorithm: str, code: str, default_input: Any):
    """Attempt to extract logic/data from user code for the simulator."""
    if not code or not code.strip():
        return default_input
        
    code_clean = re.sub(r'//.*', '', code) # Remove comments
    code_clean = re.sub(r'/\*.*?\*/', '', code_clean, flags=re.DOTALL)

    if algorithm == "stack":
        ops = []
        # Support push(10), stack.push(20), s.add(30)
        matches = re.finditer(r"\b(push|pop|add|remove|peek)\s*\(\s*([^()]*?)\s*\)", code_clean, re.IGNORECASE)
        for m in matches:
            action = m.group(1).lower()
            val = m.group(2).strip()
            if action in ["push", "add"]:
                if not val: val = "X"
                ops.append({"action": "push", "value": val})
            elif action in ["pop", "remove"]:
                ops.append({"action": "pop", "value": None})
        return ops if len(ops) > 0 else default_input

    if algorithm == "queue":
        ops = []
        matches = re.finditer(r"\b(enqueue|dequeue|add|remove|offer|poll)\s*\(\s*([^()]*?)\s*\)", code_clean, re.IGNORECASE)
        for m in matches:
            action = m.group(1).lower()
            val = m.group(2).strip()
            if action in ["enqueue", "add", "offer"]:
                if not val: val = "X"
                ops.append({"action": "enqueue", "value": val})
            elif action in ["dequeue", "remove", "poll"]:
                ops.append({"action": "dequeue", "value": None})
        return ops if len(ops) > 0 else default_input

    if algorithm in ["bubble_sort", "insertion_sort", "binary_search"]:
        # Match arrays/lists: [1, 2, 3] or {1, 2, 3} with many items to avoid empty [] function sigs
        m = re.search(r"([\[\{])\s*(-?\d+[\d\s,]*)[\]\}]", code_clean)
        if m:
            nums = [int(n.strip()) for n in re.split(r'[\s,]+', m.group(2)) if n.strip().lstrip('-').isdigit()]
            if len(nums) >= 2: # At least 2 elements to count as data
                if algorithm == "binary_search":
                    # Fallback to search for 'target = X' or similar
                    target = nums[-1] # Default to last
                    target_m = re.search(r"(target|find|search|val)\s*[:=]\s*(-?\d+)", code_clean, re.I)
                    if target_m: target = int(target_m.group(2))
                    return {"arr": sorted(nums), "target": target}
                return nums
        return default_input

    if algorithm == "arrays":
        ops = []
        # Support arr[idx] = val, arr.get(idx), search(val)
        upd = re.finditer(r"\[\s*(\d+)\s*\]\s*=\s*(-?\d+)", code_clean)
        for m in upd: ops.append({"action": "update", "index": int(m.group(1)), "value": int(m.group(2))})
        acc = re.finditer(r"\[\s*(\d+)\s*\](?!\s*=)", code_clean)
        for m in acc: ops.append({"action": "access", "index": int(m.group(1))})
        src = re.search(r"\bsearch\s*\(\s*(-?\d+)\s*\)", code_clean, re.I)
        if src: ops.append({"action": "search", "value": int(src.group(1))})
        
        arr_m = re.search(r"(\[|\{)\s*(-?\d+[\d\s,]*)[\]\}]", code_clean)
        initial_arr = [int(n.strip()) for n in re.split(r'[\s,]+', arr_m.group(2)) if n.strip().lstrip('-').isdigit()] if arr_m else [1,2,3,4,5]
        return {"arr": initial_arr, "ops": ops if ops else [{"action":"access", "index":0}]}

    if algorithm == "strings":
        action = "reverse"
        if "palindrome" in code_clean.lower(): action = "palindrome"
        m = re.search(r'"([^"]*)"', code_clean)
        s = m.group(1) if m else "radar"
        return {"s": s, "action": action}

    if algorithm == "hashing":
        m = re.findall(r"\d+", code_clean)
        keys = [int(x) for x in m if len(x) < 5][:10] if m else [10, 20, 30]
        return {"keys": keys, "size": 7}

    if algorithm == "heap":
        action = "extract"
        val = None
        if "insert" in code_clean.lower() or "add" in code_clean.lower():
            action = "insert"
            m = re.search(r"(?:insert|add)\s*\(\s*(\d+)\s*\)", code_clean, re.I)
            val = int(m.group(1)) if m else 50
        m = re.search(r"(\[|\{)\s*(-?\d+[\d\s,]*)[\]\}]", code_clean)
        arr = [int(n.strip()) for n in re.split(r'[\s,]+', m.group(2)) if n.strip().lstrip('-').isdigit()] if m else [10, 20, 30]
        return {"arr": arr, "action": action, "val": val}

    if algorithm == "backtracking":
        m = re.search(r"(\d+)", code_clean)
        n = int(m.group(1)) if m and int(m.group(1)) < 10 else 4
        return n

    if algorithm == "linked_lists":
        action = "insert"
        val, pos = 10, 0
        if "delete" in code_clean.lower() or "remove" in code_clean.lower():
            action = "delete"
            m = re.search(r"(?:delete|remove)\s*\(\s*(\d+)\s*\)", code_clean, re.I)
            pos = int(m.group(1)) if m else 0
        else:
            m = re.search(r"(?:insert|add)\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)", code_clean, re.I)
            if m: val, pos = int(m.group(1)), int(m.group(2))
        
        m = re.search(r"(\[|\{)\s*(-?\d+[\d\s,]*)[\]\}]", code_clean)
        arr = [int(n.strip()) for n in re.split(r'[\s,]+', m.group(2)) if n.strip().lstrip('-').isdigit()] if m else [1, 2, 3]
        return {"arr": arr, "action": action, "val": val, "pos": pos}

    if algorithm == "greedy_algorithms":
        amount = 55
        m = re.search(r"(?:amount|val|n)\s*[:=]\s*(\d+)", code_clean, re.I)
        if m: amount = int(m.group(1))
        coins = [10, 5, 1]
        cm = re.search(r"(\[|\{)\s*(-?\d+[\d\s,]*)[\]\}]", code_clean)
        if cm: coins = [int(n.strip()) for n in re.split(r'[\s,]+', cm.group(2)) if n.strip().lstrip('-').isdigit()]
        return {"amount": amount, "coins": coins}

    if algorithm == "dynamic_programming":
        m = re.search(r"\b(fib|fibonacci|dp)\s*\(\s*(\d+)\s*\)", code_clean, re.I)
        n = int(m.group(2)) if m and int(m.group(2)) < 15 else 6
        return n

    if algorithm == "bit_manipulation":
        op = "AND"
        if "OR" in code_clean: op = "OR"
        elif "XOR" in code_clean: op = "XOR"
        elif "LSHIFT" in code_clean or "<<" in code_clean: op = "SHIFT"
        
        val = 15
        m = re.search(r"(?:val|n|a)\s*[:=]\s*(\d+)", code_clean, re.I)
        if m: val = int(m.group(1))
        
        mask = 1
        mask_m = re.search(r"(?:mask|b|m)\s*[:=]\s*(\d+)", code_clean, re.I)
        if mask_m: mask = int(mask_m.group(1))
        
        return {"val": val, "op": op, "mask": mask}

    if algorithm == "tries":
        m = re.findall(r'"([^"]*)"', code_clean)
        words = m if m else ["code", "cool"]
        return words

    if algorithm == "segment_trees":
        m = re.search(r"(\[|\{)\s*(-?\d+[\d\s,]*)[\]\}]", code_clean)
        arr = [int(n.strip()) for n in re.split(r'[\s,]+', m.group(2)) if n.strip().lstrip('-').isdigit()] if m else [1, 2, 3, 4]
        return arr

    if algorithm == "disjoint_set_union":
        n = 5
        m = re.search(r"new\s+DSU\s*\(\s*(\d+)\s*\)", code_clean, re.I)
        if m: n = int(m.group(1))
        ops = []
        u_m = re.finditer(r"\bunion\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)", code_clean, re.I)
        for m in u_m: ops.append(("union", int(m.group(1)), int(m.group(2))))
        f_m = re.finditer(r"\bfind\s*\(\s*(\d+)\s*\)", code_clean, re.I)
        for m in f_m: ops.append(("find", int(m.group(1)), None))
        return {"n": n, "ops": ops if ops else [("union", 0, 1)]}

    if algorithm == "factorial":
        m = re.search(r"\b(fact|factorial)\s*\(\s*(\d+)\s*\)", code_clean, re.I)
        if m: return int(m.group(2))
        return default_input

    return default_input

@app.post("/visualize")
def visualize(req: VisualizeRequest):
    alg = req.algorithm
    data = parse_code_for_visualizer(alg, req.code, req.input)
    
    try:
        steps = []
        if alg == "bubble_sort":
            steps = ve.simulate_bubble_sort(data)
        elif alg == "insertion_sort":
            steps = ve.simulate_insertion_sort(data)
        elif alg == "binary_search":
            steps = ve.simulate_binary_search(data["arr"], data["target"])
        elif alg == "factorial":
            val = int(data) if isinstance(data, (int, str)) and str(data).isdigit() else 5
            steps = ve.simulate_factorial(val)
        elif alg == "stack":
            steps = ve.simulate_stack(data)
        elif alg == "queue":
            steps = ve.simulate_queue(data)
        elif alg == "dfs":
            steps = ve.simulate_dfs(data["adj"], data["start"])
        elif alg == "bfs":
            steps = ve.simulate_bfs(data["adj"], data["start"])
        elif alg == "arrays":
            steps = ve.simulate_arrays(data["arr"], data["ops"])
        elif alg == "strings":
            steps = ve.simulate_strings(data["s"], data["action"])
        elif alg == "hashing":
            steps = ve.simulate_hashing(data["keys"], data["size"])
        elif alg == "heap":
            steps = ve.simulate_heap(data["arr"], data["action"], data["val"])
        elif alg == "backtracking":
            steps = ve.simulate_backtracking(data)
        elif alg == "linked_lists":
            steps = ve.simulate_linked_list(data["arr"], data["action"], data["val"], data["pos"])
        elif alg == "greedy_algorithms":
            steps = ve.simulate_greedy(data["amount"], data["coins"])
        elif alg == "dynamic_programming":
            steps = ve.simulate_dp(data)
        elif alg == "bit_manipulation":
            steps = ve.simulate_bit_manipulation(data["val"], data["op"], data["mask"])
        elif alg == "tries":
            steps = ve.simulate_trie(data)
        elif alg == "segment_trees":
            steps = ve.simulate_segment_tree(data)
        elif alg == "disjoint_set_union":
            steps = ve.simulate_dsu(data["n"], data["ops"])
        else:
            return {"error": f"Algorithm '{alg}' not supported yet.", "steps": []}
            
        if not steps:
            return {"error": "Simulator generated 0 steps for this code/input.", "steps": []}
            
        return {"steps": steps}
    except Exception as e:
        import traceback
        return {"error": f"Execution Error: {str(e)}", "trace": traceback.format_exc(), "steps": []}
    
    return {"error": "End of visualization block reached unexpectedly."}

import os
import uvicorn
client = None
db = None

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))