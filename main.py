import time
import os

def get_report_path():
    # This solves the [Errno 13] Permission denied error on Android
    # by using the app's internal home directory.
    return os.path.join(os.path.expanduser("~"), "mbzuai_psych_report.txt")

def start_assessment():
    os.system('clear')
    print("==============================================")
    print("   🧠 NEURO-LOGIC v2.0 | MBZUAI PORTFOLIO   ")
    print("==============================================\n")
    
    name = input("Enter Candidate Name: ")
    
    questions = [
        "1. Prefer (a) math puzzles or (b) creative stories?",
        "2. Coding style: (a) Plan first or (b) Jump in?",
        "3. View of AI: (a) High-risk/Extreme or (b) Useful tool?",
        "4. Knowledge: (a) Want to know future or (b) Surprise?",
        "5. Role: (a) Data Organizer or (b) Strategic Visionary?",
        "6. Wins: (a) Small/Guaranteed or (b) Big/Risky?",
        "7. World view: (a) Numbers or (b) Experiences?",
        "8. Preference: (a) Optimize old or (b) Build new?"
    ]

    score_a = 0
    for q in questions:
        print("\n" + q)
        ans = input("Your choice (a/b): ").lower()
        while ans not in ['a', 'b']:
            ans = input("Error: Please type 'a' or 'b': ").lower()
        if ans == 'a': score_a += 1

    print("\n[RUNNING HEURISTIC CLASSIFICATION...]")
    time.sleep(2)

    # Logic to decide the profile
    if score_a >= 6:
        profile = "THE PRECISION ANALYST"
        desc = "Focuses on high-accuracy and logical consistency."
    elif score_a <= 2:
        profile = "THE DISRUPTIVE INNOVATOR"
        desc = "Focuses on high-risk, creative problem solving."
    else:
        profile = "THE ADAPTIVE ENGINEER"
        desc = "Balances logical structure with creative adaptation."

    print(f"\nFINAL DIAGNOSIS: {profile}")
    print(f"Analysis: {desc}")

    # Save to file safely
    try:
        path = get_report_path()
        with open(path, "a") as f:
            f.write(f"Name: {name} | Result: {profile}\n")
        print(f"\n✅ Report securely saved to: {path}")
    except Exception as e:
        print(f"\n❌ Logging failed: {e}")

if __name__ == "__main__":
    start_assessment()
      
