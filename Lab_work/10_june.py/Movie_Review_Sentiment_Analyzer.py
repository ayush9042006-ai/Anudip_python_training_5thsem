'''3. Movie Review Sentiment Analyzer 
Problem Statement 
Movie reviews are stored as follows: 
reviews = ["excellent movie","average story","excellent acting","poor direction","excellent visuals","poor screenplay","good music","excellent climax",
          "average performance","good cinematography" ] 
Requirements Create the following functions: 
1. count_sentiments(reviews) Counts: • Excellent  • Good  • Average  • Poor reviews  
2. most_common_word(reviews) Returns the most frequently occurring word. 
3. longest_review(reviews) Returns the review containing the maximum number of characters. 
4. reviews_with_keyword(reviews, keyword) Displays all reviews containing a given keyword. '''



reviews = ["excellent movie","average story","excellent acting","poor direction","excellent visuals","poor screenplay","good music","excellent climax",
          "average performance","good cinematography" ] 


#Count sentiments
def count_sentiments(reviews):
    excellent = 0
    good = 0
    average = 0
    poor = 0

    for i in reviews:
        if "excellent" in i:
            excellent += 1
        elif "good" in i:
            good += 1
        elif "average" in i:
            average += 1
        elif "poor" in i:
            poor += 1
    print("Excellent Reviews :", excellent)
    print("Good Reviews      :", good)
    print("Average Reviews   :", average)
    print("Poor Reviews      :", poor)


#Most common word
def most_common_word(reviews):
    words = []
    for i in reviews:
        words.extend(i.split())
    max_count = 0
    common_word = ""
    for word in words:
        count = words.count(word)
        if count > max_count:
            max_count = count
            common_word = word

    return common_word

# 3. Longest review
def longest_review(reviews):
    longest = reviews[0]

    for review in reviews:
        if len(review) > len(longest):
            longest = review
    return longest


# 4. Reviews with a given keyword
def reviews_with_keyword(reviews, keyword):
    print(f"Reviews containing '{keyword}':")
    found = False
    for review in reviews:
        if keyword.lower() in review.lower():
            print(review)
            found = True
    if not found:
        print("No review found.")

count_sentiments(reviews)
print("Most Common Word :", most_common_word(reviews))
print("Longest Review   :", longest_review(reviews))
reviews_with_keyword(reviews, "excellent")
    
            
