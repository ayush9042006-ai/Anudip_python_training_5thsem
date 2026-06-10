message = "AAABBBCCCDDDAAA"
 
# 1. Count occurrences of each character
freq = {}
 
for char in message:
    freq[char] = freq.get(char, 0) + 1
 
print("Character Frequencies:")
for char, count in freq.items():
    print(f"{char}: {count}")
 
# 2. Dictionary of character frequencies
print("\nFrequency Dictionary:")
print(freq)
 
# 3. Display unique characters
print("\nUnique Characters:")
print(list(freq.keys()))
 
# 4. Find the most frequent character
most_frequent = max(freq, key=freq.get)
print("\nMost Frequent Character:", most_frequent)
print("Frequency:", freq[most_frequent])
 
# 5. Create compressed output (Run-Length Encoding)
compressed = ""
count = 1
 
for i in range(1, len(message)):
    if message[i] == message[i - 1]:
        count += 1
    else:
        compressed += message[i - 1] + str(count)
        count = 1
 
compressed += message[-1] + str(count)
 
print("\nCompressed Output:", compressed)
 
# 6. Calculate compression ratio
original_size = len(message)
compressed_size = len(compressed)
 
compression_ratio = compressed_size / original_size
 
print("\nOriginal Length:", original_size)
print("Compressed Length:", compressed_size)
print("Compression Ratio:", round(compression_ratio, 2))