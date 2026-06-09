'''3. Chat Message Analytics 
Problem Statement 
A chat application stores a message: Python is awesome and Python is easy to learn Tasks 
Write a program to:
 1. Count total characters. 
 2. Count total words.  
 3. Find the longest word. 
 4. Find the shortest word. 
 5. Count how many times the word "Python" appears.  
 6. Create a list of words having more than 4 characters.  
 7. Display all words starting with a vowel.  
 8. Count the number of vowels and consonants.'''


message = "Python is awesome and Python is easy to learn"

# Count total characters...............................................................
characters = len(message)

#Count total words.....................................................................
words = message.split()
total = len(words)

#Find the longest word.............................................................
longest_word = words[0]
for i in words:
    if len(i) > len(longest_word):
        longest_word = i

#Find the shortest word............................................................
shortest_word = words[0]
for i in words:
    if len(i) < len(shortest_word):
        shortest_word = i

#Count how many times "Python" appears..............................................
python_count = words.count("Python")

#List of words having more than 4 characters
words4 = []

for i in words:
    if len(i) > 4:
        words4.append(i)

# 7. Display words starting with a vowel
vowel_words = []
for i in words:
    if i[0].lower() in "aeiou":
        vowel_words.append(i)

# 8. Count vowels and consonants
vowels = 0
consonants = 0

for i in message:
    if i.isalpha():
        if i.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Output
print("Message:", message)
print("Total Characters:", characters)
print("Total Words:", total)
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print("Python Appears:", python_count, "times")
print("Words with more than 4 characters:", words4)
print("Words starting with a vowel:", vowel_words)
print("Total Vowels:", vowels)
print("Total Consonants:", consonants)