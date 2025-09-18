import re

def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@$!%*?&]", password):
        score += 1

    if score == 5:
        return "Strong 💪"
    elif score >= 3:
        return "Medium ⚠️"
    else:
        return "Weak ❌"

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    print("Password Strength:", password_strength(pwd))
