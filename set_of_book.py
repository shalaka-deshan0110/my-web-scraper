with open('books.txt', 'r') as f:
    lines = [line.strip() for line in f if not line.startswith('BOOKS RECOMMENDED BY')]
    
lines = list(set(lines))

with open('set_of_books.txt', 'w') as f:
    for line in lines:
        f.write(line + '\n')