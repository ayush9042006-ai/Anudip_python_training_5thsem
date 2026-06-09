'''3. Chat Message Analytics 
Problem Statement 
A chat application stores a message: Python is awesome and Python is easy to learn Tasks 
Write a program to: 1. Count total characters. 
 2. Count total words.  
 3. Find the longest word. 
   4. Find the shortest word. 
     5. Count how many times the word "Python" appears.  
     6. Create a list of words having more than 4 characters.  
     7. Display all words starting with a vowel.  
     8. Count the number of vowels and consonants.'''


message = "Python is awesome and Python is easy to learn"

# Count total characters...............................................................
total_characters = len(message)

#Count total words.....................................................................
words = message.split()
total_words = len(words)

#Find the longest word.............................................................
longest_word = max(words, key=len)

#Find the shortest word............................................................
shortest_word = min(words, key=len)

#Count how many times "Python" appears..............................................
python_count = words.count("Python")

#List of words having more than 4 characters
more_than_4 = []

for word in words:
    if len(word) > 4:
        more_than_4.append(word)

# 7. Display words starting with a vowel
vowel_words = []

for word in words:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

# 8. Count vowels and consonants
vowels = 0
consonants = 0

for ch in message:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Output
print("Message:", message)

print("\nTotal Characters:", total_characters)
print("Total Words:", total_words)

print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)

print("Python Appears:", python_count, "times")

print("Words with more than 4 characters:", more_than_4)

print("Words starting with a vowel:", vowel_words)

print("Total Vowels:", vowels)
print("Total Consonants:", consonants)