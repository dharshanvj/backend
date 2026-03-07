from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os

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
import java.util.Scanner;
import java.util.Stack;

public class StackCalculator {
    // Simple calculator using stack to evaluate expressions
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        
        System.out.println("Simple Stack Calculator");
        System.out.println("Enter numbers to push, or + - * / to operate:");
        
        while (true) {
            System.out.print("Enter value or operator (q to quit): ");
            String input = scanner.next();
            
            if (input.equals("q")) break;
            
            // Check if input is a number
            try {
                int num = Integer.parseInt(input);
                stack.push(num);
                System.out.println("Pushed: " + num);
            } catch (NumberFormatException e) {
                // Input is an operator
                if (stack.size() < 2) {
                    System.out.println("Need at least 2 numbers in stack!");
                    continue;
                }
                
                int b = stack.pop();
                int a = stack.pop();
                int result = 0;
                
                switch (input) {
                    case "+": result = a + b; break;
                    case "-": result = a - b; break;
                    case "*": result = a * b; break;
                    case "/": 
                        if (b == 0) {
                            System.out.println("Cannot divide by zero!");
                            stack.push(a); stack.push(b);
                            continue;
                        }
                        result = a / b; 
                        break;
                    default:
                        System.out.println("Unknown operator!");
                        stack.push(a); stack.push(b);
                        continue;
                }
                
                stack.push(result);
                System.out.println("Result: " + result);
            }
            
            System.out.println("Current stack: " + stack);
        }
        
        scanner.close();
    }
}"""
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
import java.util.Scanner;

public class DecimalToBinaryStack {
    // Custom Stack implementation
    static class Stack {
        int[] arr;
        int top;
        int capacity;
        
        Stack(int size) {
            arr = new int[size];
            top = -1;
            capacity = size;
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
        
        boolean isEmpty() {
            return top == -1;
        }
    }
    
    // Convert decimal to binary using stack
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a decimal number: ");
        int decimal = scanner.nextInt();
        int original = decimal;
        
        Stack stack = new Stack(32); // 32 bits max
        
        // Push remainders to stack
        while (decimal > 0) {
            stack.push(decimal % 2);
            decimal = decimal / 2;
        }
        
        // Pop and display binary representation
        System.out.print("Binary representation of " + original + ": ");
        while (!stack.isEmpty()) {
            System.out.print(stack.pop());
        }
        System.out.println();
        
        scanner.close();
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
import java.util.Scanner;
import java.util.Stack;

public class TowerOfHanoi {
    // Solve Tower of Hanoi using stack (iterative)
    static class Move {
        int n;
        char from, to, aux;
        
        Move(int n, char from, char to, char aux) {
            this.n = n;
            this.from = from;
            this.to = to;
            this.aux = aux;
        }
    }
    
    public static void solveHanoi(int disks) {
        Stack<Move> stack = new Stack<>();
        stack.push(new Move(disks, 'A', 'C', 'B'));
        
        while (!stack.isEmpty()) {
            Move current = stack.pop();
            
            if (current.n == 1) {
                System.out.println("Move disk 1 from " + current.from + " to " + current.to);
            } else {
                // Push in reverse order (to simulate recursion)
                stack.push(new Move(current.n - 1, current.aux, current.to, current.from));
                stack.push(new Move(1, current.from, current.to, current.aux));
                stack.push(new Move(current.n - 1, current.from, current.aux, current.to));
            }
        }
    }
    
    // Calculate factorial using stack (iterative)
    public static long factorial(int n) {
        Stack<Integer> stack = new Stack<>();
        for (int i = 1; i <= n; i++) {
            stack.push(i);
        }
        
        long result = 1;
        while (!stack.isEmpty()) {
            result *= stack.pop();
        }
        return result;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter number of disks for Tower of Hanoi: ");
        int disks = scanner.nextInt();
        System.out.println("Steps to solve Tower of Hanoi with " + disks + " disks:");
        solveHanoi(disks);
        
        System.out.print("\\nEnter a number to find factorial: ");
        int num = scanner.nextInt();
        System.out.println("Factorial of " + num + " = " + factorial(num));
        
        scanner.close();
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
import java.util.Scanner;

public class TicketCounter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Queue<String> queue = new LinkedList<>();
        
        System.out.println("Ticket Counter Simulation");
        System.out.println("Commands: add <name>, serve, display, quit");
        
        while (true) {
            System.out.print("Enter command: ");
            String command = scanner.nextLine();
            String[] parts = command.split(" ");
            
            if (parts[0].equals("quit")) {
                break;
            }
            
            switch (parts[0]) {
                case "add":
                    if (parts.length < 2) {
                        System.out.println("Please provide a name");
                    } else {
                        queue.add(parts[1]);
                        System.out.println(parts[1] + " added to queue");
                    }
                    break;
                    
                case "serve":
                    if (queue.isEmpty()) {
                        System.out.println("No customers in queue");
                    } else {
                        System.out.println("Now serving: " + queue.remove());
                    }
                    break;
                    
                case "display":
                    if (queue.isEmpty()) {
                        System.out.println("Queue is empty");
                    } else {
                        System.out.println("Current queue: " + queue);
                    }
                    break;
                    
                default:
                    System.out.println("Unknown command");
            }
        }
        
        scanner.close();
    }
}"""
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
import java.util.Scanner;

public class ProcessScheduler {
    // Circular Queue implementation
    static class CircularQueue {
        int[] arr;
        int front, rear, size, capacity;
        
        CircularQueue(int cap) {
            capacity = cap;
            arr = new int[capacity];
            front = rear = -1;
            size = 0;
        }
        
        boolean enqueue(int processId) {
            if (isFull()) {
                System.out.println("Queue is full! Process " + processId + " rejected");
                return false;
            }
            
            if (isEmpty()) {
                front = rear = 0;
            } else {
                rear = (rear + 1) % capacity;
            }
            
            arr[rear] = processId;
            size++;
            System.out.println("Process " + processId + " added to queue");
            return true;
        }
        
        int dequeue() {
            if (isEmpty()) {
                System.out.println("No processes to execute");
                return -1;
            }
            
            int processId = arr[front];
            
            if (front == rear) {
                front = rear = -1;
            } else {
                front = (front + 1) % capacity;
            }
            
            size--;
            return processId;
        }
        
        boolean isEmpty() {
            return front == -1;
        }
        
        boolean isFull() {
            return (rear + 1) % capacity == front;
        }
        
        void display() {
            if (isEmpty()) {
                System.out.println("No processes in queue");
                return;
            }
            
            System.out.print("Processes in queue: ");
            int i = front;
            while (i != rear) {
                System.out.print(arr[i] + " ");
                i = (i + 1) % capacity;
            }
            System.out.println(arr[rear]);
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        CircularQueue queue = new CircularQueue(5);
        int processCounter = 1;
        
        System.out.println("Process Scheduler Simulation");
        System.out.println("Commands: add, execute, display, quit");
        
        while (true) {
            System.out.print("Enter command: ");
            String command = scanner.nextLine();
            
            switch (command) {
                case "add":
                    queue.enqueue(processCounter++);
                    break;
                    
                case "execute":
                    int executed = queue.dequeue();
                    if (executed != -1) {
                        System.out.println("Executing process " + executed);
                    }
                    break;
                    
                case "display":
                    queue.display();
                    break;
                    
                case "quit":
                    scanner.close();
                    return;
                    
                default:
                    System.out.println("Unknown command");
            }
        }
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

public class ShortestPathBFS {
    // BFS to find shortest path in grid (like in maze)
    static class Point {
        int x, y, dist;
        Point(int x, int y, int dist) {
            this.x = x; this.y = y; this.dist = dist;
        }
    }
    
    public static int shortestPath(int[][] grid, int startX, int startY, int endX, int endY) {
        int rows = grid.length;
        int cols = grid[0].length;
        
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        boolean[][] visited = new boolean[rows][cols];
        
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(startX, startY, 0));
        visited[startX][startY] = true;
        
        while (!queue.isEmpty()) {
            Point current = queue.poll();
            
            if (current.x == endX && current.y == endY) {
                return current.dist;
            }
            
            for (int[] dir : directions) {
                int newX = current.x + dir[0];
                int newY = current.y + dir[1];
                
                if (newX >= 0 && newX < rows && newY >= 0 && newY < cols && 
                    !visited[newX][newY] && grid[newX][newY] == 1) {
                    queue.add(new Point(newX, newY, current.dist + 1));
                    visited[newX][newY] = true;
                }
            }
        }
        
        return -1; // No path found
    }
    
    // Level-order traversal of binary tree to find sum at each level
    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) { this.val = val; }
    }
    
    public static List<Integer> levelOrderSum(TreeNode root) {
        List<Integer> sums = new ArrayList<>();
        if (root == null) return sums;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            int levelSum = 0;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                levelSum += node.val;
                
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            
            sums.add(levelSum);
        }
        
        return sums;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Create a sample grid (1 = path, 0 = obstacle)
        int[][] grid = {
            {1, 1, 0, 1},
            {1, 0, 1, 1},
            {1, 1, 1, 0},
            {0, 1, 1, 1}
        };
        
        System.out.print("Enter start position (x y): ");
        int startX = scanner.nextInt();
        int startY = scanner.nextInt();
        
        System.out.print("Enter end position (x y): ");
        int endX = scanner.nextInt();
        int endY = scanner.nextInt();
        
        int distance = shortestPath(grid, startX, startY, endX, endY);
        if (distance != -1) {
            System.out.println("Shortest path distance: " + distance);
        } else {
            System.out.println("No path found!");
        }
        
        // Build a sample binary tree
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);
        
        List<Integer> levelSums = levelOrderSum(root);
        System.out.println("Sum at each level: " + levelSums);
        
        scanner.close();
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
import java.util.Scanner;

public class ArrayOperations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read number of elements
        System.out.print("Enter number of elements: ");
        int n = scanner.nextInt();
        
        int[] numbers = new int[n];
        
        // Read array elements
        System.out.println("Enter " + n + " numbers:");
        for (int i = 0; i < n; i++) {
            numbers[i] = scanner.nextInt();
        }
        
        // Find largest among 3 numbers (first 3 elements)
        if (n >= 3) {
            int largest = numbers[0];
            for (int i = 1; i < 3; i++) {
                if (numbers[i] > largest) {
                    largest = numbers[i];
                }
            }
            System.out.println("Largest among first 3 numbers: " + largest);
        }
        
        // Calculate sum and average
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        double average = (double) sum / n;
        System.out.println("Sum: " + sum);
        System.out.println("Average: " + average);
        
        // Check even or odd for each element
        System.out.println("Even/Odd check:");
        for (int num : numbers) {
            if (num % 2 == 0) {
                System.out.println(num + " is even");
            } else {
                System.out.println(num + " is odd");
            }
        }
        
        scanner.close();
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
import java.util.Scanner;

public class MatrixOperations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read matrix dimensions
        System.out.print("Enter number of rows: ");
        int rows = scanner.nextInt();
        System.out.print("Enter number of columns: ");
        int cols = scanner.nextInt();
        
        int[][] matrix = new int[rows][cols];
        
        // Read matrix elements
        System.out.println("Enter matrix elements:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }
        
        // Display matrix
        System.out.println("\\nMatrix:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        
        // Find largest in each row
        System.out.println("\\nLargest in each row:");
        for (int i = 0; i < rows; i++) {
            int max = matrix[i][0];
            for (int j = 1; j < cols; j++) {
                if (matrix[i][j] > max) {
                    max = matrix[i][j];
                }
            }
            System.out.println("Row " + (i+1) + ": " + max);
        }
        
        // Calculate sum of each column
        System.out.println("\\nSum of each column:");
        for (int j = 0; j < cols; j++) {
            int sum = 0;
            for (int i = 0; i < rows; i++) {
                sum += matrix[i][j];
            }
            System.out.println("Column " + (j+1) + ": " + sum);
        }
        
        // Transpose matrix
        int[][] transpose = new int[cols][rows];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                transpose[j][i] = matrix[i][j];
            }
        }
        
        System.out.println("\\nTranspose:");
        for (int i = 0; i < cols; i++) {
            for (int j = 0; j < rows; j++) {
                System.out.print(transpose[i][j] + " ");
            }
            System.out.println();
        }
        
        scanner.close();
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
import java.util.Scanner;

public class ArrayAlgorithms {
    // GCD using Euclidean algorithm
    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    // LCM using GCD
    public static int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }
    
    // Check if number is prime
    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
    
    // Display all prime numbers from 1 to N
    public static void displayPrimes(int n) {
        System.out.print("Prime numbers from 1 to " + n + ": ");
        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }
    
    // Check if number is Armstrong (e.g., 153 = 1³ + 5³ + 3³)
    public static boolean isArmstrong(int n) {
        int original = n;
        int sum = 0;
        int digits = String.valueOf(n).length();
        
        while (n > 0) {
            int digit = n % 10;
            sum += Math.pow(digit, digits);
            n /= 10;
        }
        
        return sum == original;
    }
    
    // Check if number is Neon (sum of digits of square equals number)
    public static boolean isNeon(int n) {
        int square = n * n;
        int sum = 0;
        
        while (square > 0) {
            sum += square % 10;
            square /= 10;
        }
        
        return sum == n;
    }
    
    // Check leap year
    public static boolean isLeapYear(int year) {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }
    
    // Calculate compound interest
    public static double compoundInterest(double principal, double rate, int time, int n) {
        return principal * Math.pow(1 + rate/(n*100), n*time) - principal;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // GCD and LCM
        System.out.print("Enter two numbers for GCD/LCM: ");
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        System.out.println("GCD of " + a + " and " + b + ": " + gcd(a, b));
        System.out.println("LCM of " + a + " and " + b + ": " + lcm(a, b));
        
        // Prime numbers
        System.out.print("\\nEnter limit for prime numbers: ");
        int limit = scanner.nextInt();
        displayPrimes(limit);
        
        // Armstrong number
        System.out.print("\\nEnter number to check Armstrong: ");
        int arm = scanner.nextInt();
        System.out.println(arm + " is Armstrong? " + isArmstrong(arm));
        
        // Neon number
        System.out.print("\\nEnter number to check Neon: ");
        int neon = scanner.nextInt();
        System.out.println(neon + " is Neon? " + isNeon(neon));
        
        // Leap year
        System.out.print("\\nEnter year to check leap year: ");
        int year = scanner.nextInt();
        System.out.println(year + " is leap year? " + isLeapYear(year));
        
        // Compound interest
        System.out.print("\\nEnter principal, rate, time, compoundings per year: ");
        double p = scanner.nextDouble();
        double r = scanner.nextDouble();
        int t = scanner.nextInt();
        int n = scanner.nextInt();
        System.out.println("Compound Interest: " + compoundInterest(p, r, t, n));
        
        scanner.close();
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
import java.util.Scanner;

public class StringBasics {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read input from user
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        
        // Check vowel or consonant
        System.out.println("\\nVowel/Consonant check:");
        for (int i = 0; i < input.length(); i++) {
            char c = Character.toLowerCase(input.charAt(i));
            if (c >= 'a' && c <= 'z') {
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    System.out.println(c + " is a vowel");
                } else {
                    System.out.println(c + " is a consonant");
                }
            }
        }
        
        // Count vowels and consonants
        int vowels = 0, consonants = 0;
        for (int i = 0; i < input.length(); i++) {
            char c = Character.toLowerCase(input.charAt(i));
            if (c >= 'a' && c <= 'z') {
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    vowels++;
                } else {
                    consonants++;
                }
            }
        }
        System.out.println("\\nTotal vowels: " + vowels);
        System.out.println("Total consonants: " + consonants);
        
        // Reverse string
        StringBuilder reversed = new StringBuilder(input).reverse();
        System.out.println("Reversed string: " + reversed);
        
        // Check if palindrome
        if (input.equalsIgnoreCase(reversed.toString())) {
            System.out.println("It is a palindrome");
        } else {
            System.out.println("It is not a palindrome");
        }
        
        scanner.close();
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
import java.util.Scanner;
import java.util.HashMap;

public class StringAnagram {
    // Check if two strings are anagrams
    public static boolean areAnagrams(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        
        int[] count = new int[26];
        
        // Count characters in first string
        for (char c : s1.toCharArray()) {
            count[c - 'a']++;
        }
        
        // Decrement for second string
        for (char c : s2.toCharArray()) {
            if (count[c - 'a'] == 0) return false;
            count[c - 'a']--;
        }
        
        return true;
    }
    
    // Add two binary strings
    public static String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();
        int carry = 0;
        int i = a.length() - 1;
        int j = b.length() - 1;
        
        while (i >= 0 || j >= 0 || carry > 0) {
            int sum = carry;
            if (i >= 0) sum += a.charAt(i--) - '0';
            if (j >= 0) sum += b.charAt(j--) - '0';
            
            result.append(sum % 2);
            carry = sum / 2;
        }
        
        return result.reverse().toString();
    }
    
    // Check if string has all unique characters
    public static boolean hasUniqueChars(String s) {
        boolean[] seen = new boolean[256]; // ASCII
        for (char c : s.toCharArray()) {
            if (seen[c]) return false;
            seen[c] = true;
        }
        return true;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Anagram check
        System.out.print("Enter first string: ");
        String s1 = scanner.nextLine().toLowerCase();
        System.out.print("Enter second string: ");
        String s2 = scanner.nextLine().toLowerCase();
        
        if (areAnagrams(s1, s2)) {
            System.out.println("The strings are anagrams");
        } else {
            System.out.println("The strings are not anagrams");
        }
        
        // Binary addition
        System.out.print("\\nEnter first binary string: ");
        String bin1 = scanner.nextLine();
        System.out.print("Enter second binary string: ");
        String bin2 = scanner.nextLine();
        System.out.println("Sum: " + addBinary(bin1, bin2));
        
        // Check unique characters
        System.out.print("\\nEnter string to check unique characters: ");
        String unique = scanner.nextLine();
        System.out.println("Has all unique characters? " + hasUniqueChars(unique));
        
        scanner.close();
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
import java.util.Scanner;

public class StringPatternMatching {
    // KMP Pattern Search
    public static int[] computeLPS(String pattern) {
        int m = pattern.length();
        int[] lps = new int[m];
        int len = 0;
        int i = 1;
        
        lps[0] = 0;
        
        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }
    
    public static int kmpSearch(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        
        int[] lps = computeLPS(pattern);
        
        int i = 0; // index for text
        int j = 0; // index for pattern
        
        while (i < n) {
            if (pattern.charAt(j) == text.charAt(i)) {
                i++;
                j++;
            }
            
            if (j == m) {
                return i - j; // pattern found
            } else if (i < n && pattern.charAt(j) != text.charAt(i)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return -1; // pattern not found
    }
    
    // Check if string is a valid number (integer/float)
    public static boolean isValidNumber(String s) {
        try {
            Integer.parseInt(s);
            return true;
        } catch (NumberFormatException e1) {
            try {
                Double.parseDouble(s);
                return true;
            } catch (NumberFormatException e2) {
                return false;
            }
        }
    }
    
    // Count occurrences of pattern in text
    public static int countOccurrences(String text, String pattern) {
        int count = 0;
        int index = 0;
        
        while ((index = text.indexOf(pattern, index)) != -1) {
            count++;
            index += pattern.length();
        }
        
        return count;
    }
    
    // Remove all occurrences of a substring
    public static String removeAll(String text, String toRemove) {
        StringBuilder result = new StringBuilder();
        int i = 0;
        int len = toRemove.length();
        
        while (i < text.length()) {
            if (i <= text.length() - len && 
                text.substring(i, i + len).equals(toRemove)) {
                i += len;
            } else {
                result.append(text.charAt(i));
                i++;
            }
        }
        
        return result.toString();
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // KMP Pattern Search
        System.out.print("Enter text: ");
        String text = scanner.nextLine();
        System.out.print("Enter pattern to search: ");
        String pattern = scanner.nextLine();
        
        int pos = kmpSearch(text, pattern);
        if (pos != -1) {
            System.out.println("Pattern found at position: " + pos);
        } else {
            System.out.println("Pattern not found");
        }
        
        // Count occurrences
        int occurrences = countOccurrences(text, pattern);
        System.out.println("Pattern occurs " + occurrences + " times");
        
        // Check if valid number
        System.out.print("\\nEnter a string to check if it's a number: ");
        String numStr = scanner.nextLine();
        System.out.println("Is a valid number? " + isValidNumber(numStr));
        
        // Remove substring
        System.out.print("\\nEnter substring to remove from original text: ");
        String toRemove = scanner.nextLine();
        String result = removeAll(text, toRemove);
        System.out.println("Result after removal: " + result);
        
        scanner.close();
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
                "Access": "O(n) — must traverse from head",
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
import java.util.Scanner;

public class LinkedListOperations {
    // Node class for linked list
    static class Node {
        int data;
        Node next;
        Node(int d) {
            data = d;
            next = null;
        }
    }
    
    static Node head;
    
    // Insert at end
    public static void insert(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node last = head;
        while (last.next != null) {
            last = last.next;
        }
        last.next = newNode;
    }
    
    // Display list
    public static void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
    
    // Search for an element
    public static boolean search(int key) {
        Node current = head;
        while (current != null) {
            if (current.data == key) {
                return true;
            }
            current = current.next;
        }
        return false;
    }
    
    // Delete a node
    public static void delete(int key) {
        if (head == null) return;
        
        if (head.data == key) {
            head = head.next;
            return;
        }
        
        Node current = head;
        while (current.next != null && current.next.data != key) {
            current = current.next;
        }
        
        if (current.next != null) {
            current.next = current.next.next;
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Linked List Operations");
        System.out.println("Commands: insert <num>, delete <num>, search <num>, display, quit");
        
        while (true) {
            System.out.print("Enter command: ");
            String command = scanner.nextLine();
            String[] parts = command.split(" ");
            
            if (parts[0].equals("quit")) {
                break;
            }
            
            switch (parts[0]) {
                case "insert":
                    if (parts.length < 2) {
                        System.out.println("Please provide a number");
                    } else {
                        insert(Integer.parseInt(parts[1]));
                        System.out.println("Inserted " + parts[1]);
                    }
                    break;
                    
                case "delete":
                    if (parts.length < 2) {
                        System.out.println("Please provide a number");
                    } else {
                        delete(Integer.parseInt(parts[1]));
                        System.out.println("Deleted " + parts[1]);
                    }
                    break;
                    
                case "search":
                    if (parts.length < 2) {
                        System.out.println("Please provide a number");
                    } else {
                        boolean found = search(Integer.parseInt(parts[1]));
                        System.out.println(parts[1] + " found? " + found);
                    }
                    break;
                    
                case "display":
                    display();
                    break;
                    
                default:
                    System.out.println("Unknown command");
            }
        }
        
        scanner.close();
    }
}"""
        }
    }
}

# Continue with all remaining data structures following the same pattern...
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
client = None
db = None

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))