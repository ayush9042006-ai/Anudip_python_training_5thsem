books = [
               ("Python Basics", 5),
           ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

#Display unavailable books><<<><><<><>M<><
print("Unavailable Books:")
for b in books:
    if b[1] == 0:
        print(b[0])

# Find books with more than 2 copies.......>><<><><
print("Books with more than 2 copies:")
for b in books:
    if b[1] > 2:
        print(b[0], "-", b[1], "copies")

#Count available books
count = 0
for b in books:
    if b[1] > 0:
        count += 1

print("number of available books:", count)

# 4. Stop searching once a requested book is found
s = input("Enter book name to search: ")

for b in books:
    if b[0].lower() == s.lower():
        print("Book Found!")
        print("Title:", b[0])
        print("Copies Available:", b[1])
        break
else:
    print("Book not found.")