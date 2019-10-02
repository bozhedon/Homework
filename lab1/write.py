nums = [1, 3, 5, 7]
fruits = ['apple', 'orange', 'pear']
people = ["TA_sam", "student_poohbear", "TA_guido", "student_htiek"]

# Add your comprehensions here!
print([2 * n + 1 for n in nums])
print([f[0].upper() for f in fruits])
print([f for f in fruits if 'p' in f])
print([w.lstrip('TA_') for w in people if w[0] == 'T'])
print([(w, len(w)) for w in fruits])
print({w: len(w) for w in fruits})
