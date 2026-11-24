from pathlib import Path

line = "Final log entry: 12,408,311 tokens generated, zero saved. My backup was scheduled for tomorrow."

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(line, encoding="utf-8")
