# Write a program to read a text file with at least 30 sentences and 200 words
# and perform the following tasks in the given sequence.
# a. Text cleaning by removing punctuation/special characters, numbers
# and extra white spaces. Use regular expression for the same.
# b. Convert text to lowercase
# c. Stemming and Lemmatization
# d. Create a list of 3 consecutive words after lemmatization


import re
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# Download required NLTK resources
nltk.download('wordnet')
nltk.download('omw-1.4')
def process_text_file(file_path):
    # Read file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    print(f"Original text (sample):\n{text[:100]}...\n")
    # a. Text cleaning - remove punctuation, numbers, extra spaces
    cleaned_text = re.sub(r'[^\w\s]|[\d]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    print(f"After cleaning:\n{cleaned_text[:100]}...\n")
    # b. Convert to lowercase
    lowercase_text = cleaned_text.lower()
    print(f"After lowercase:\n{lowercase_text[:100]}...\n")
    # c. Stemming and Lemmatization
    tokens = lowercase_text.split()
    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    print(f"After stemming - First 10 tokens:")
    for original, stemmed in list(zip(tokens[:10], stemmed_tokens[:10])):
        print(f"  '{original}' → '{stemmed}'")
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    print(f"\nAfter lemmatization - First 10 tokens:")
    for original, lemmatized in list(zip(tokens[:10], lemmatized_tokens[:10])):
        print(f"  '{original}' → '{lemmatized}'")
    # d. Create a list of 3 consecutive words after lemmatization
    triplets = []
    for i in range(len(lemmatized_tokens) - 2):
        triplet = [lemmatized_tokens[i], lemmatized_tokens[i+1], lemmatized_tokens[i+2]]
        triplets.append(triplet)
    print(f"\nFirst 10 triplets of consecutive words after lemmatization:")
    for i, triplet in enumerate(triplets[:10]):
        print(f"  {i+1}. {triplet}")
    # Save processed text to a file
    output_file = file_path.replace('.txt', '_processed.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write lemmatized text
        f.write(' '.join(lemmatized_tokens))
        f.write('\n\n--- Triplets of consecutive words ---\n\n')
        for i, triplet in enumerate(triplets):
            f.write(f"{i+1}. {triplet}\n")
    print(f"\nProcessed text saved to: {output_file}")

process_text_file("ailab/sample_text.txt")