# Write a program to read a 3 text files on any technical concept with at least
# 20 sentences and 150 words. Implement one-hot encoding. 


from sklearn.preprocessing import MultiLabelBinarizer
# Step 1: File names (assuming they already exist in the same folder)
file_names = ['ml.txt', 'blockchain.txt', 'cloudcomputing.txt']
# Step 2: Read files
texts = []
for file_name in file_names:
    with open(file_name, 'r') as f:
        texts.append(f.read())
# Step 3: Preprocess text (basic tokenization)
tokenized_texts = []
for text in texts:
    tokens = text.lower().replace('.', '').replace(',', '').split()
    tokenized_texts.append(tokens)
# Step 4: Create vocabulary
vocab = set()
for tokens in tokenized_texts:
    vocab.update(tokens)
vocab = sorted(vocab)  # Sorting helps maintain consistent encoding
print(f"Vocabulary Size: {len(vocab)}")
print(f"Vocabulary: {vocab}\n")
# Step 5: One-Hot Encoding
mlb = MultiLabelBinarizer(classes=vocab)
one_hot_encoded_texts = mlb.fit_transform(tokenized_texts)
# Display One-Hot Encoded Output
for i, encoded in enumerate(one_hot_encoded_texts):
    print(f"One-Hot Encoding for file '{file_names[i]}':\n{encoded}\n")
