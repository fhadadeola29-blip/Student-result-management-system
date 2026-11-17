"""student.py - the Student class."""
from datetime import datetime


class Student:
    def __init__(self, student_id, name, class_name, gender, dob, scores=None, date_entered=None):
        self.student_id = student_id
        self.name = name
        self.class_name = class_name
        self.gender = gender
        self.dob = dob
        self.scores = scores if scores else {}      # e.g. {"Maths": 80}
        self.date_entered = date_entered            # date the result was recorded

    def set_scores(self, scores):
        self.scores = scores
        self.date_entered = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "class_name": self.class_name,
            "gender": self.gender,
            "dob": self.dob,
            "scores": self.scores,
            "date_entered": self.date_entered,
        }

    @staticmethod
    def from_dict(d):
        return Student(d["student_id"], d["name"], d["class_name"], d["gender"],
                       d["dob"], d.get("scores", {}), d.get("date_entered"))
