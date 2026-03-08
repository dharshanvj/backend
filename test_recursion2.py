import json

def main():
    with open('main.py', 'r', encoding='utf-8') as f:
        text = f.read()

    start = text.find('"Recursion": {')
    if start == -1: return

    end = text.find('"Backtracking": {')
    if end == -1: end = len(text)
    
    recursion_text = text[start:end]
    
    with open('out_recursion.txt', 'w', encoding='utf-8') as f:
        f.write(recursion_text)

if __name__ == "__main__":
    main()
