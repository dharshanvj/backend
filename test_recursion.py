import re

def main():
    with open('main.py', 'r', encoding='utf-8') as f:
        text = f.read()
        
    start = text.find('"Recursion": {')
    if start == -1:
        print("Not found")
        return
        
    # extract around 3000 chars from start to see the content
    print(text[start:start+3000])

if __name__ == "__main__":
    main()
