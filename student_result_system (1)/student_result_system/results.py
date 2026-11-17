"""results.py - total, average and grade calculations."""

SUBJECTS = ["English", "Mathematics", "Physics", "Chemistry", "Biology"]


def get_total(student):
    return sum(student.scores.values())


def get_average(student):
    if len(student.scores) == 0:
        return 0.0
    return get_total(student) / len(student.scores)


def get_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    else:
        return "F"
