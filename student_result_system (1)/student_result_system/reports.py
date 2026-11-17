"""reports.py - report card, class list, statistics and saving to file."""
import os
from datetime import datetime
from results import get_total, get_average, get_grade


def report_card(student):
    lines = ["=" * 40,
             f"REPORT CARD - {student.name}",
             "=" * 40,
             f"ID: {student.student_id}   Class: {student.class_name}",
             f"Gender: {student.gender}   DOB: {student.dob}",
             "-" * 40]
    for subject, score in student.scores.items():
        lines.append(f"{subject:<15} {score}")
    avg = get_average(student)
    lines += ["-" * 40,
              f"Total   : {get_total(student)}",
              f"Average : {avg:.2f}",
              f"Grade   : {get_grade(avg)}",
              f"Date entered: {student.date_entered}",
              "=" * 40]
    return "\n".join(lines)


def class_list(students, sort_by="average"):
    if sort_by == "average":
        ordered = sorted(students, key=get_average, reverse=True)   # highest first
    else:
        ordered = sorted(students, key=lambda s: s.name.lower())    # A-Z
    lines = [f"{'ID':<8}{'Name':<22}{'Total':>7}{'Average':>9}{'Grade':>7}",
             "-" * 53]
    for s in ordered:
        avg = get_average(s)
        lines.append(f"{s.student_id:<8}{s.name:<22}{get_total(s):>7}{avg:>9.2f}{get_grade(avg):>7}")
    return "\n".join(lines)


def class_statistics(students):
    scored = [s for s in students if s.scores]
    if not scored:
        return "No scores recorded yet."
    all_scores = [score for s in scored for score in s.scores.values()]
    averages = [get_average(s) for s in scored]
    best = max(scored, key=get_average)
    return "\n".join([
        f"Number of students : {len(scored)}",
        f"Highest score      : {max(all_scores)}",
        f"Lowest score       : {min(all_scores)}",
        f"Class average      : {sum(averages) / len(averages):.2f}",
        f"Top student        : {best.name} ({get_average(best):.2f})",
    ])


def save_report_to_file(students, filename="class_report.txt"):
    os.makedirs("data", exist_ok=True)
    path = os.path.join("data", filename)
    try:
        with open(path, "w") as f:
            f.write("STUDENT RESULT MANAGEMENT SYSTEM\n")
            f.write("Created by Fhad Balogun | Contributor: Khidir Segun Aileru\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(class_list(students) + "\n\n")
            f.write(class_statistics(students) + "\n")
        return path
    except OSError as e:
        print("Could not write report:", e)
        return None
