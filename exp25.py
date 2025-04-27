# Write a program to read a 3 text files on a movie review with at least 20
# sentences and 150 words. Implement bag of words. 
from sklearn.feature_extraction.text import CountVectorizer
# Step 1: File names (assuming you already have the text files)
file_names = ['review1.txt', 'review2.txt', 'review3.txt']
# Step 2: Read files
texts = []
for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as f:
        texts.append(f.read())
# Step 3: Bag of Words (using CountVectorizer)
vectorizer = CountVectorizer(lowercase=True, stop_words='english')  # remove common words like 'the', 'is', 'and'
X = vectorizer.fit_transform(texts)
# Step 4: Display vocabulary
print("Vocabulary:")
print(vectorizer.get_feature_names_out())
print()
# Step 5: Show Bag of Words matrix
print("Bag of Words Matrix:")
print(X.toarray())
# Optional: Display using a table (more readable)
import pandas as pd
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out(), index=file_names)
print("\nBag of Words Table:\n")
print(df)
