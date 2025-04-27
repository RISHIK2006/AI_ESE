# Write a program to read a 3 text files a tourist place with at least 20
# sentences and 150 words. Implement TF-IDF. 


from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
# Step 1: File names
file_names = ['place1.txt', 'place2.txt', 'place3.txt']
# Step 2: Read files
texts = []
for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as f:
        texts.append(f.read())
# Step 3: Apply TF-IDF
vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
X = vectorizer.fit_transform(texts)
# Step 4: Display Vocabulary
print("Vocabulary:")
print(vectorizer.get_feature_names_out())
print()
# Step 5: Show TF-IDF Matrix
print("TF-IDF Matrix:")
print(X.toarray())
# Step 6: Optional: Display using a DataFrame (pretty table)
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out(), index=file_names)
print("\nTF-IDF Table:\n")
print(df)
