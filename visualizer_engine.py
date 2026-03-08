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

