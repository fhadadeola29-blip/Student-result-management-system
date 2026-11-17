"""storage.py - save and load data using a JSON file."""
import json
import os
from student import Student

DATA_FILE = os.path.join("data", "students.json")


def load_students():
    """Return a list of Student objects. Empty list if file is missing."""
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Data file is damaged. Starting with an empty list.")
        return []
    else:
        return [Student.from_dict(d) for d in data]


def save_students(students):
    os.makedirs("data", exist_ok=True)
    try:
        with open(DATA_FILE, "w") as f:
            json.dump([s.to_dict() for s in students], f, indent=4)
    except OSError as e:
        print("Could not save data:", e)
