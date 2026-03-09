from typing import List, Dict, Any

def simulate_bubble_sort(arr: List[int]):
    steps = []
    n = len(arr)
    temp_arr = list(arr)
    
    # Initial state
    steps.append({
        "line": 1,
        "variables": {"i": 0, "j": 0, "swapped": "False"},
        "array": list(temp_arr),
        "pointers": {},
        "stack": [],
        "explanation": "Starting Bubble Sort"
    })
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            steps.append({
                "line": 4, 
                "variables": {"i": i, "j": j, "swapped": str(swapped)},
                "array": list(temp_arr),
                "pointers": {"j": j, "j+1": j+1},
                "stack": [],
                "explanation": f"Comparing {temp_arr[j]} and {temp_arr[j+1]}"
            })
            
            if temp_arr[j] > temp_arr[j+1]:
                temp_arr[j], temp_arr[j+1] = temp_arr[j+1], temp_arr[j]
                swapped = True
                steps.append({
                    "line": 6,
                    "variables": {"i": i, "j": j, "swapped": str(swapped)},
                    "array": list(temp_arr),
                    "pointers": {"j": j, "j+1": j+1},
                    "stack": [],
                    "explanation": f"Swapping {temp_arr[j+1]} and {temp_arr[j]}"
                })
        if not swapped:
            break
            
    steps.append({
        "line": 10,
        "variables": {"i": n, "swapped": str(swapped)},
        "array": list(temp_arr),
        "pointers": {},
        "stack": [],
        "explanation": "Sort complete!"
    })
    return steps

def simulate_binary_search(arr: List[int], target: int):
    steps = []
    arr = sorted(arr)
    low = 0
    high = len(arr) - 1
    
    steps.append({
        "line": 1,
        "variables": {"low": low, "high": high, "target": target},
        "array": list(arr),
        "pointers": {"low": low, "high": high},
        "stack": [],
        "explanation": f"Starting binary search for {target}"
    })
    
    while low <= high:
        mid = (low + high) // 2
        steps.append({
            "line": 4,
            "variables": {"low": low, "high": high, "mid": mid, "target": target},
            "array": list(arr),
            "pointers": {"low": low, "high": high, "mid": mid},
            "stack": [],
            "explanation": f"Checking mid element {arr[mid]}"
        })
        
        if arr[mid] == target:
            steps.append({
                "line": 6,
                "variables": {"low": low, "high": high, "mid": mid, "target": target},
                "array": list(arr),
                "pointers": {"mid": mid},
                "stack": [],
                "explanation": f"Target {target} found at index {mid}!"
            })
            return steps
        elif arr[mid] < target:
            low = mid + 1
            steps.append({
                "line": 8,
                "variables": {"low": low, "high": high, "mid": mid, "target": target},
                "array": list(arr),
                "pointers": {"low": low, "high": high},
                "stack": [],
                "explanation": f"{arr[mid]} < {target}, moving low to {low}"
            })
        else:
            high = mid - 1
            steps.append({
                "line": 10,
                "variables": {"low": low, "high": high, "mid": mid, "target": target},
                "array": list(arr),
                "pointers": {"low": low, "high": high},
                "stack": [],
                "explanation": f"{arr[mid]} > {target}, moving high to {high}"
            })
            
    steps.append({
        "line": 12,
        "variables": {"low": low, "high": high, "target": target},
        "array": list(arr),
        "pointers": {},
        "stack": [],
        "explanation": f"Target {target} not found."
    })
    return steps

def simulate_factorial(n: int):
    steps = []
    
    def fact(val, stack_frames):
        # Push frame
        current_stack = list(stack_frames)
        current_stack.append(f"fact({val})")
        
        steps.append({
            "line": 1,
            "variables": {"n": val},
            "array": [],
            "pointers": {},
            "stack": list(current_stack),
            "explanation": f"Calling factorial({val})"
        })
        
        if val <= 1:
            steps.append({
                "line": 3,
                "variables": {"n": val, "return": 1},
                "array": [],
                "pointers": {},
                "stack": list(current_stack),
                "explanation": f"Base case fact({val}) returns 1"
            })
            return 1
        
        res = val * fact(val - 1, current_stack)
        
        steps.append({
            "line": 5,
            "variables": {"n": val, "return": res},
            "array": [],
            "pointers": {},
            "stack": list(current_stack),
            "explanation": f"Factorial({val}) returning {res}"
        })
        return res
        
    fact(n, [])
    return steps

def simulate_stack(ops: List[Dict]):
    steps = []
    stack_data = []
    
    for i, op in enumerate(ops):
        action = op.get("action")
        val = op.get("value")
        
        if action == "push":
            stack_data.append(val)
            explanation = f"Pushed {val} onto stack"
        elif action == "pop":
            if stack_data:
                popped = stack_data.pop()
                explanation = f"Popped {popped} from stack"
            else:
                explanation = "Stack underflow!"
        
        steps.append({
            "line": i + 1,
            "variables": {"action": action, "value": val, "size": len(stack_data)},
            "array": list(stack_data),
            "pointers": {"top": len(stack_data) - 1 if stack_data else -1},
            "stack": [],
            "explanation": explanation
        })
    return steps

def simulate_dfs(adj_list, start):
    steps = []
    visited = set()
    stack = [start]
    
    steps.append({
        "line": 1,
        "variables": {"current": None, "stack": str(stack)},
        "array": sorted(list(visited)), # show visited set
        "pointers": {"start": start},
        "stack": list(stack),
        "explanation": f"Starting DFS from {start}"
    })
    
    while stack:
        curr = stack.pop()
        explanation = f"Popped {curr} from stack"
        
        if curr not in visited:
            visited.add(curr)
            explanation += f", exploring it now"
            
            # For visualization, we'll show neighbors being pushed
            neighbors = adj_list.get(str(curr), [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    
            steps.append({
                "line": 5,
                "variables": {"current": curr, "visited": str(visited)},
                "array": list(visited),
                "pointers": {"current": curr},
                "stack": list(stack),
                "explanation": explanation
            })
    
    steps.append({
        "line": 10,
        "variables": {},
        "array": list(visited),
        "pointers": {},
        "stack": [],
        "explanation": "DFS complete!"
    })
    return steps

def simulate_queue(ops: List[Dict]):
    steps = []
    queue_data = []
    
    for i, op in enumerate(ops):
        action = op.get("action")
        val = op.get("value")
        
        if action == "enqueue":
            queue_data.append(val)
            explanation = f"Enqueued {val} to queue"
        elif action == "dequeue":
            if queue_data:
                dequeued = queue_data.pop(0)
                explanation = f"Dequeued {dequeued} from queue"
            else:
                explanation = "Queue underflow!"
        
        steps.append({
            "line": i + 1,
            "variables": {"action": action, "value": val, "size": len(queue_data)},
            "array": list(queue_data),
            "pointers": {"front": 0 if queue_data else -1, "rear": len(queue_data) - 1 if queue_data else -1},
            "stack": [],
            "explanation": explanation
        })
    return steps

def simulate_insertion_sort(arr: List[int]):
    steps = []
    n = len(arr)
    temp_arr = list(arr)
    
    steps.append({
        "line": 1,
        "variables": {"i": 1},
        "array": list(temp_arr),
        "pointers": {},
        "stack": [],
        "explanation": "Starting Insertion Sort"
    })
    
    for i in range(1, n):
        key = temp_arr[i]
        j = i - 1
        steps.append({
            "line": 3,
            "variables": {"i": i, "key": key},
            "array": list(temp_arr),
            "pointers": {"i": i, "key": i},
            "stack": [],
            "explanation": f"Picking {key} as key"
        })
        
        while j >= 0 and temp_arr[j] > key:
            steps.append({
                "line": 5,
                "variables": {"i": i, "key": key, "j": j},
                "array": list(temp_arr),
                "pointers": {"j": j, "key": i},
                "stack": [],
                "explanation": f"{temp_arr[j]} > {key}, shifting {temp_arr[j]}"
            })
            temp_arr[j + 1] = temp_arr[j]
            j -= 1
            
        temp_arr[j + 1] = key
        steps.append({
            "line": 8,
            "variables": {"i": i, "key": key, "j": j},
            "array": list(temp_arr),
            "pointers": {"j+1": j+1},
            "stack": [],
            "explanation": f"Placed key {key} at index {j+1}"
        })
        
    steps.append({
        "line": 10,
        "variables": {},
        "array": list(temp_arr),
        "pointers": {},
        "stack": [],
        "explanation": "Insertion sort complete!"
    })
    return steps

def simulate_bfs(adj_list, start):
    steps = []
    visited = {str(start)}
    queue = [str(start)]
    
    steps.append({
        "line": 1,
        "variables": {"queue": str(queue), "visited": str(visited)},
        "array": sorted(list(visited)),
        "pointers": {"front": 0, "rear": 0},
        "stack": [],
        "explanation": f"Starting BFS from {start}"
    })
    
    while queue:
        curr = queue.pop(0)
        explanation = f"Dequeued {curr} from queue"
        
        # Neighbor exploration
        neighbors = adj_list.get(str(curr), [])
        for neighbor in neighbors:
            if str(neighbor) not in visited:
                visited.add(str(neighbor))
                queue.append(str(neighbor))
                explanation += f", neighbor {neighbor} discovered"
                
        steps.append({
            "line": 5,
            "variables": {"current": curr, "queue": str(queue)},
            "array": sorted(list(visited)),
            "pointers": {"current": curr},
            "stack": [],
            "explanation": explanation
        })
                
    steps.append({
        "line": 10,
        "variables": {},
        "array": sorted(list(visited)),
        "pointers": {},
        "stack": [],
        "explanation": "BFS complete!"
    })
    return steps

def simulate_arrays(arr: List[int], ops: List[Dict]):
    steps = []
    current_arr = list(arr)
    
    for i, op in enumerate(ops):
        action = op.get("action")
        idx = op.get("index")
        val = op.get("value")
        
        explanation = f"Op {i+1}: {action}"
        if action == "access":
            explanation = f"Accessed array at index {idx}: value {current_arr[idx] if 0 <= idx < len(current_arr) else 'Out of bounds'}"
        elif action == "update":
            if 0 <= idx < len(current_arr):
                current_arr[idx] = val
                explanation = f"Updated index {idx} to {val}"
        elif action == "search":
            found_idx = -1
            for j, v in enumerate(current_arr):
                steps.append({
                    "line": 4, "variables": {"target": val, "curr": v, "i": j},
                    "array": list(current_arr), "pointers": {"searching": j},
                    "explanation": f"Checking if {v} == {val}"
                })
                if v == val:
                    found_idx = j
                    break
            explanation = f"Searching for {val}: Found at {found_idx}" if found_idx != -1 else f"{val} not found"
            
        steps.append({
            "line": 2, "variables": {"action": action, "idx": idx, "val": val},
            "array": list(current_arr), "pointers": {"active": idx} if action != "search" else {},
            "explanation": explanation
        })
    return steps

def simulate_strings(s: str, action: str):
    steps = []
    chars = list(s)
    
    if action == "reverse":
        left, right = 0, len(chars) - 1
        while left < right:
            steps.append({
                "line": 3, "variables": {"l": left, "r": right, "leftChar": chars[left], "rightChar": chars[right]},
                "array": list(chars), "pointers": {"left": left, "right": right},
                "explanation": f"Swapping {chars[left]} and {chars[right]}"
            })
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        steps.append({
            "line": 10, "variables": {"result": "".join(chars)},
            "array": list(chars), "pointers": {},
            "explanation": f"String reversal complete: {''.join(chars)}"
        })
    elif action == "palindrome":
        left, right = 0, len(chars) - 1
        is_pal = True
        while left < right:
            steps.append({
                "line": 3, "variables": {"l": left, "r": right},
                "array": list(chars), "pointers": {"checkL": left, "checkR": right},
                "explanation": f"Comparing {chars[left]} and {chars[right]}"
            })
            if chars[left] != chars[right]:
                is_pal = False
                break
            left += 1
            right -= 1
        steps.append({
            "line": 10, "variables": {"isPalindrome": is_pal},
            "array": list(chars), "pointers": {},
            "explanation": f"Palindrome check result: {is_pal}"
        })
    return steps

def simulate_backtracking(n: int):
    # Simulate N-Queens setup for n x n board
    # Simplified: Show placement steps for the first few queens
    steps = []
    board = [-1] * n # board[row] = col
    
    def solve(row):
        if row == n:
            steps.append({
                "line": 10, "variables": {"row": row}, "array": list(board),
                "pointers": {}, "explanation": "Found a valid solution!"
            })
            return True
        
        for col in range(n):
            # Check if valid (simplified check for visualization)
            is_valid = True
            for prev_row in range(row):
                if board[prev_row] == col or abs(board[prev_row] - col) == abs(prev_row - row):
                    is_valid = False
                    break
            
            board[row] = col
            steps.append({
                "line": 5, "variables": {"row": row, "col": col, "valid": is_valid},
                "array": list(board), "pointers": {"current": row},
                "explanation": f"Trying to place Queen at row {row}, col {col}... {'Valid' if is_valid else 'Conflict'}"
            })
            
            if is_valid:
                if solve(row + 1): return True
            
            board[row] = -1 # backtrack
            if not is_valid: # Only show explicit backtrack for conflicts or after a fail
                 steps.append({
                    "line": 8, "variables": {"row": row, "col": col},
                    "array": list(board), "pointers": {"backtrack": row},
                    "explanation": f"Backtracking from row {row}, col {col}"
                })
        return False

    solve(0)
    return steps[:50] # Limit steps

def simulate_heap(arr: List[int], action: str, val: int = None):
    steps = []
    heap = list(arr)
    
    if action == "insert":
        heap.append(val)
        curr = len(heap) - 1
        steps.append({
            "line": 2, "variables": {"val": val}, "array": list(heap),
            "pointers": {"inserted": curr}, "explanation": f"Inserted {val} at index {curr}"
        })
        
        while curr > 0:
            parent = (curr - 1) // 2
            steps.append({
                "line": 5, "variables": {"curr": heap[curr], "parent": heap[parent]},
                "array": list(heap), "pointers": {"curr": curr, "parent": parent},
                "explanation": f"Checking if {heap[curr]} > parent {heap[parent]}"
            })
            if heap[curr] > heap[parent]:
                heap[curr], heap[parent] = heap[parent], heap[curr]
                curr = parent
            else:
                break
        steps.append({
            "line": 10, "variables": {}, "array": list(heap),
            "pointers": {}, "explanation": "Heapify complete"
        })
    elif action == "extract":
        if not heap: return steps
        root = heap[0]
        last = heap.pop()
        if heap:
            heap[0] = last
            steps.append({
                "line": 2, "variables": {"root": root, "new_top": last},
                "array": list(heap), "pointers": {"root": 0},
                "explanation": f"Extracted {root}, moved {last} to root"
            })
            # Sift down (simplified)
            curr = 0
            while True:
                left = 2 * curr + 1
                right = 2 * curr + 2
                largest = curr
                if left < len(heap) and heap[left] > heap[largest]: largest = left
                if right < len(heap) and heap[right] > heap[largest]: largest = right
                
                if largest != curr:
                    heap[curr], heap[largest] = heap[largest], heap[curr]
                    curr = largest
                else: break
        explanation = f"Extracted {root}"
        steps.append({ "line": 10, "array": list(heap), "explanation": explanation })
        
    return steps

def simulate_hashing(keys: List[int], size: int = 7):
    steps = []
    table = [None] * size
    
    for key in keys:
        h = key % size
        steps.append({
            "line": 2, "variables": {"key": key, "hash": h}, "array": list(table),
            "pointers": {"target": h}, "explanation": f"Key {key} hashes to index {h}"
        })
        
        # Linear probing for collision
        curr = h
        while table[curr] is not None:
             steps.append({
                "line": 5, "variables": {"collisionAt": curr}, "array": list(table),
                "pointers": {"collision": curr}, "explanation": f"Collision at {curr}, probing next..."
            })
             curr = (curr + 1) % size
             
        table[curr] = key
        steps.append({
            "line": 8, "variables": {"placedAt": curr}, "array": list(table),
            "pointers": {"placed": curr}, "explanation": f"Placed {key} at index {curr}"
        })
    return steps

def simulate_linked_list(arr: List[int], action: str, val: int = None, pos: int = 0):
    steps = []
    nodes = list(arr)
    
    if action == "insert":
        nodes.insert(pos, val)
        steps.append({
            "line": 2, "variables": {"val": val, "pos": pos}, "array": list(nodes),
            "pointers": {"new_node": pos}, "explanation": f"Inserted {val} at position {pos}"
        })
    elif action == "delete":
        if 0 <= pos < len(nodes):
            old = nodes.pop(pos)
            steps.append({
                "line": 2, "variables": {"old": old, "pos": pos}, "array": list(nodes),
                "pointers": {"deleted_at": pos}, "explanation": f"Deleted value {old} at position {pos}"
            })
    return steps
