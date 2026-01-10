
import re

with open("resume.txt", encoding="utf-8") as file:
    resume = file.read().lower()
with open("job_description.txt", encoding="utf-8") as file:
    job = file.read().lower()
keywords = set(re.findall(r"\b[a-zA-Z][a-zA-Z+#.]{1,}\b", job))
matched = sorted(word for word in keywords if word in resume)
missing = sorted(keywords - set(matched))
print("Matched keywords:", matched)
print("Potentially missing keywords:", missing)
