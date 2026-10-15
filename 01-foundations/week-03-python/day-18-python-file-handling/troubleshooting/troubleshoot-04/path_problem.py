"""
Path Problem issue

"""

from pathlib import Path

file_path = Path("troubleshoot-04") / "servers.txt"
print("Looking for:", file_path.resolve())

with open(file_path, "r", encoding="utf-8") as file:
    file_path.read_text()

print("File operation done")