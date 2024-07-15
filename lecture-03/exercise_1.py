score = [
    int(input("Enter score 1: ")),
    int(input("Enter score 2: ")),
    int(input("Enter score 3: ")),
]

avg = sum(score) / len(score)

print(f"Average score: {avg:.2f}")

if avg > 95:
    print("Congratulations!")