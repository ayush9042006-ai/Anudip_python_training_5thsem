'''5. Product Review Analyzer 
Problem Statement
A customer submits a review: This product is excellent excellent excellent and very useful Tasks Write a program to: 
1. Count total words.  
2. Create a dictionary containing word frequencies.  
3. Find the most frequently used word.  
4. Find all words appearing only once.  
5. Count words having more than 5 characters.  
6. Display words in reverse order.  
7. Create a list of unique words.  '''




review = "This product is excellent excellent excellent and very useful"

# Convert review into list of words
words = review.split()
# 1. Count total words
print("Total Words :", len(words))
# 2. Create dictionary of word frequencies
freq = {}

for i in words:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Word Frequencies :", freq)

# 3. Find most frequently used word
max_count = 0
most_word = ""

for word in freq:
    if freq[word] > max_count:
        max_count = freq[word]
        most_word = word

print("Most Frequent Word :", most_word)

# 4. Find words appearing only once
once_words = []

for i in freq:
    if freq[i] == 1:
        once_words.append(i)

print("Words Appearing Once :", once_words)

# 5. Count words having more than 5 characters
count = 0
for i in words:
    if len(i) > 5:
        count += 1

print("Words with more than 5 characters :", count)

# 6. Display words in reverse order
print("Words in Reverse Order :")
for word in words[::-1]:
    print(word, end=" ")
# 7. Create list of unique words
unique_words = []
for i in words:
    if word not in unique_words:
        unique_words.append(i)

print("Unique Words :", unique_words)