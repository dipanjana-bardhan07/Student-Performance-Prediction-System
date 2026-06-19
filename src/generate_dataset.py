import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

students = 2500

data = {
    "StudentID": range(1, students + 1),
    "Age": np.random.randint(15, 22, students),
    "Gender": np.random.choice(["Male", "Female"], students),
    "AttendancePercentage": np.random.randint(50, 101, students),
    "StudyHoursPerWeek": np.random.randint(1, 41, students),
    "AssignmentCompletionRate": np.random.randint(40, 101, students),
    "PreviousExamScore": np.random.randint(35, 96, students),
    "ParticipationScore": np.random.randint(1, 11, students),
    "ExtracurricularActivities": np.random.choice(["Yes", "No"], students),
    "InternetAccessAtHome": np.random.choice(["Yes", "No"], students),
    "ParentEducationLevel": np.random.choice(
        ["High School", "Graduate", "Postgraduate"], students
    ),
}

df = pd.DataFrame(data)

# Calculate Final Exam Score based on features
df["FinalExamScore"] = (
    0.25 * df["AttendancePercentage"]
    + 0.20 * df["StudyHoursPerWeek"]
    + 0.25 * df["AssignmentCompletionRate"]
    + 0.20 * df["PreviousExamScore"]
    + 2 * df["ParticipationScore"]
    + np.random.normal(0, 5, students)
)

df["FinalExamScore"] = df["FinalExamScore"].clip(0, 100).round(2)

# ==========================================
# NEW: INTRODUCING MESSY DATA FOR YOUR TEACHER
# ==========================================

# 1. Inject random Null (NaN) values into a few columns
# We will introduce missing data in Age, AttendancePercentage, and ParentEducationLevel
for col in ["Age", "AttendancePercentage", "ParentEducationLevel"]:
    # Randomly pick 40 rows per column to set as NaN
    nan_indices = np.random.choice(df.index, size=40, replace=False)
    df.loc[nan_indices, col] = np.nan

# 2. Inject Duplicate Rows
# We will grab 20 random rows and duplicate them completely
duplicate_rows = df.sample(n=20, random_state=42)
df = pd.concat([df, duplicate_rows], ignore_index=True)

# 3. Shuffle the dataset so the duplicates aren't all at the bottom
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# ==========================================

# Save the messy dataset
df.to_csv("data/student_performance_dataset.csv", index=False)

print("Messy Dataset created successfully for preprocessing!")
print(f"Total Rows (including duplicates): {df.shape[0]}")