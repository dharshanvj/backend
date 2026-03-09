import re

def main():
    with open('main.py', 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.splitlines()
    with open('topics.txt', 'w', encoding='utf-8') as out:
        for i, line in enumerate(lines[:8500]):
            if re.match(r'^\s+"[A-Za-z0-9 /\-]+": \{', line):
                out.write(f"Line {i+1}: {line.strip()}\n")

if __name__ == '__main__':
    main()
