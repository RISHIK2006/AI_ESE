# Define universe
universe = [1, 2, 3, 4, 5]

# Example membership values for Set A
A = {1: 0.2, 2: 0.5, 3: 0.8, 4: 1.0, 5: 0.7}

# Example membership values for Set B
B = {1: 0.9, 2: 0.6, 3: 0.3, 4: 0.1, 5: 0.4}

# Example membership values for Set C
C = {1: 0.1, 2: 0.3, 3: 0.6, 4: 0.9, 5: 0.2}

# Union (max)
union_ab = {x: max(A[x], B[x]) for x in universe}
union_bc = {x: max(B[x], C[x]) for x in universe}
union_ac = {x: max(A[x], C[x]) for x in universe}

# Intersection (min)
intersection_ab = {x: min(A[x], B[x]) for x in universe}
intersection_bc = {x: min(B[x], C[x]) for x in universe}
intersection_ac = {x: min(A[x], C[x]) for x in universe}

# Complement (1 - value)
complement_a = {x: 1 - A[x] for x in universe}
complement_b = {x: 1 - B[x] for x in universe}
complement_c = {x: 1 - C[x] for x in universe}

# Print results
print("--- Fuzzy Set A ---")
print("A:", A)

print("\n--- Fuzzy Set B ---")
print("B:", B)

print("\n--- Fuzzy Set C ---")
print("C:", C)

print("\n--- Union Results ---")
print("A ∪ B:", union_ab)
print("B ∪ C:", union_bc)
print("A ∪ C:", union_ac)

print("\n--- Intersection Results ---")
print("A ∩ B:", intersection_ab)
print("B ∩ C:", intersection_bc)
print("A ∩ C:", intersection_ac)

print("\n--- Complement Results ---")
print("¬A:", complement_a)
print("¬B:", complement_b)
print("¬C:", complement_c)