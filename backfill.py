import os
import random
import subprocess
from datetime import datetime, timedelta

DAYS_BACK = 30
START_HOUR = 9
END_HOUR = 21

def commits_for_day():
    return random.choice([2, 3, 3, 4, 4, 5])

MESSAGES = [
    "update progress log",
    "dsa prep update",
    "semester revision note",
    "daily study tracking",
    "consistency update",
    "prep progress update"
]

os.makedirs("progress", exist_ok=True)

if not os.path.exists("progress/log.txt"):
    with open("progress/log.txt", "w") as f:
        f.write("start\n")

today = datetime.now()

for i in range(DAYS_BACK, 0, -1):
    day = today - timedelta(days=i)

    if random.random() < 0.15:
        continue

    num_commits = commits_for_day()

    for c in range(num_commits):
        commit_time = day.replace(
            hour=random.randint(9, 21),
            minute=random.randint(0, 59),
            second=random.randint(0, 59)
        )

        with open("progress/log.txt", "a") as f:
            f.write(f"{commit_time}\n")

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = commit_time.strftime("%Y-%m-%dT%H:%M:%S")
        env["GIT_COMMITTER_DATE"] = commit_time.strftime("%Y-%m-%dT%H:%M:%S")

        subprocess.run(["git", "add", "."], env=env)
        subprocess.run(["git", "commit", "-m", random.choice(MESSAGES)], env=env)

print("DONE")