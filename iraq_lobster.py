
name = "Customer X"
score1 = 85
score2 = 92
average = score1 + score2 / 2  # Bug: missing parentheses; only score2 is divided
print("Average satisfaction for", name, ":", average)