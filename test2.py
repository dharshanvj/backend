import re

def main():
    with open('main.py', 'r', encoding='utf-8') as f:
        text = f.read()

    # Find all topics inside DSA_CONTENT
    lines = text.splitlines()
    for i, line in enumerate(lines[:8200]):
        if re.match(r'^\s+"[A-Za-z0-9 /\-]+": \{', line):
            print(f"Line {i+1}: {line.strip()}")

if __name__ == '__main__':
    main()
