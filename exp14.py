universe = [1, 2, 3, 4, 5]

print("--- Fuzzy Set A ---")
A = {1: 0.2, 2: 0.5, 3: 0.8, 4: 1.0, 5: 0.7}
print("A:", A)

print("\n--- Fuzzy Set B ---")
B = {1: 0.9, 2: 0.6, 3: 0.3, 4: 0.1, 5: 0.4}
print("B:", B)


# Union (max)
union_ab = {x: max(A[x], B[x]) for x in universe}

# Intersection (min)
intersection_ab = {x: min(A[x], B[x]) for x in universe}

# Complement (1 - value)
complement_a = {x: 1 - A[x] for x in universe}
complement_b = {x: 1 - B[x] for x in universe}

# --- Demonstrate De Morgan's Law (Complement of Intersection) ---

# Left side of De Morgan's Law: Complement of (A Intersection B)
lhs = {x: 1 - intersection_ab[x] for x in universe}

# Right side of De Morgan's Law: (Complement of A) Union (Complement of B)
rhs = {x: max(complement_a[x], complement_b[x]) for x in universe}

# --- Print Results ---

print("\n--- Union (A ∪ B) ---")
print("A ∪ B:", union_ab)

print("\n--- Intersection (A ∩ B) ---")
print("A ∩ B:", intersection_ab)

print("\n--- Complement of A (¬A) ---")
print("¬A:", complement_a)

print("\n--- Complement of B (¬B) ---")
print("¬B:", complement_b)

print("\n--- De Morgan's Law Demonstration (Complement of Union) ---")
print("\nLeft Side: ")
print(lhs)

print("\nRight Side: ")
print(rhs)

# Verify De Morgan's Law
if lhs == rhs:
    print("\nDe Morgan's Law (Complement of Intersection) is verified for these fuzzy sets.")
else:
    print("\nDe Morgan's Law (Complement of Intersection) is NOT verified for these fuzzy sets.")