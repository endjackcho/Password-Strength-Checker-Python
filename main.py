sc = "`~!@#$%^&*)(-_=+\|][}[};':\"\",./?><"

def checker(p):
    score = 0
    if "123456789" in p or "123" in p or "1234" in p or "12345" in p or "123456" in p or "1234567" in p : score -= 5
    if "abcd" in p or "abc" in p : score -= 3
    for i in p :
        if p.count(i) > 10 and len(p) / 2 < p.count(i): score -= 3
        if i.isnumeric() :
            score += 1.5
        elif i.isupper() :
            score += 1.5
        elif i.islower() :
            score += 1
        elif i in sc :
            score += 2
    return "Low" if score < 20 else "High"

def main() :
    while True :
        password = input("\nEnter Your Password : ")
        if password == "" : break
        print(checker(password))

if __name__ == "__main__":
    main()
    print(f"\n~ Thanks for choosing us ;)\n")