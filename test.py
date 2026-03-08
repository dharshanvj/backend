import json

def main():
    with open('main.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines[:1000]):
        if 'DSA_CONTENT =' in line:
            print(f'DSA_CONTENT found at line {i}')
        if '"java":' in line:
            print(f'java key found at line {i}: {line.strip()[:40]}')

if __name__ == '__main__':
    main()
