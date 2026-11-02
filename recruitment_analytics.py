
candidates = {
    "Aman": [85, 3],
    "Riya": [92, 5],
    "Kiran": [74, 2],
    "Neha": [89, 4]
}

for name, data in candidates.items():
    score, experience = data
    status = "Shortlisted" if score >= 80 and experience >= 3 else "Not Shortlisted"
    print(name, "-", status)

print("Total Candidates:", len(candidates))
