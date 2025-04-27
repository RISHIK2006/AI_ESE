# Write a program to read a text file with at least 30 sentences and 200 words
# and perform the following tasks in the given sequence.
# a. Text cleaning by removing punctuation/special characters, numbers
# and extra white spaces. Use regular expression for the same.
# b. Convert text to lowercase
# c. Tokenization
# d. Remove stop words
# e. Correct misspelled words

import re
from spellchecker import SpellChecker
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
    # c. Tokenization (simple split on spaces)
    tokens = lowercase_text.split()
    print(f"Tokenization - {len(tokens)} tokens. First 10:\n{tokens[:10]}\n")
    # d. Remove stop words (common English stop words)
    # Simplified approach - using a string of common stop words separated by spaces
    stop_words_str = "a an the and or but if of in on at by for with to from as i me my we us our you your he him his she her it its they them their this that these those am is are was were be been being have has had do does did can could would should will shall must might"
    stop_words = set(stop_words_str.split())
    filtered_tokens = [word for word in tokens if word not in stop_words]
    print(f"After stop word removal - {len(filtered_tokens)} tokens. First 10:\n{filtered_tokens[:10]}\n")
    # e. Correct misspelled words
    spell = SpellChecker()
    misspelled = spell.unknown(filtered_tokens)
    corrected_tokens = []
    corrections = {}
    for word in filtered_tokens:
        if word in misspelled:
            correction = spell.correction(word)
            if correction != word and correction is not None:
                corrections[word] = correction
                corrected_tokens.append(correction)
            else:
                corrected_tokens.append(word)
        else:
            corrected_tokens.append(word)
    print(f"Spelling corrections - {len(corrections)} words corrected. Examples:")
    for word, correction in list(corrections.items())[:5]:
        print(f"  '{word}' → '{correction}'")
    # Final processed text
    final_text = ' '.join(corrected_tokens)
    print(f"\nFinal text (sample):\n{final_text[:100]}...\n")
    # Save to file
    output_file = file_path.replace('.txt', '_processed.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_text)
    print(f"Processed text saved to: {output_file}")
    

process_text_file("ailab\sample_text.txt")