from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from pymongo import MongoClient
import os

MONGO_URI = os.environ.get("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["dsa_database"]
collection = db["modules"]
# ==============================
# DSA CONTENT DATABASE
# ==============================

DSA_CONTENT = {

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

    # ==================== BUBBLE SORT ====================
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
import os
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))