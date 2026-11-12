# 🔐 Password Strength Checker

A lightweight Python-based password strength checker that evaluates passwords using a custom scoring algorithm.

This project analyzes different password characteristics, assigns scores based on their complexity, and identifies potentially weak patterns to estimate password strength.

## ✨ Features

- **Character Analysis:** Evaluates uppercase letters, lowercase letters, numbers, and special characters.
- **Pattern Detection:** Detects common sequential patterns such as `123`, `1234`, and `abcd`.
- **Repetition Detection:** Reduces the score when a password contains excessive character repetition.
- **Custom Scoring System:** Uses a weighted algorithm to calculate password strength.
- **Interactive CLI:** Allows users to check multiple passwords in one session.

## ⚙️ How It Works

The checker assigns different scores to password characters:

| Character Type | Score |
|---|---:|
| Lowercase letters | +1 |
| Uppercase letters | +1.5 |
| Numbers | +1.5 |
| Special characters | +2 |

It also applies penalties for predictable sequences and excessive character repetition.

### Strength Classification

- **High:** Score of 20 or above.
- **Low:** Score below 20.

## 🚀 Getting Started

### Requirements
- Python 3.x

### Installation

Clone the repository:

```bash
git clone https://github.com/endjackcho/Password-Strength-Checker.git
```

Navigate to the project directory:

```bash
cd Password-Strength-Checker
```

Run the program:

```bash
python main.py
```

## 💻 Example

```text
Enter Your Password : MyPassword123!
High

Enter Your Password : abc123
Low
```

## 🛠️ Technologies

- Python
- String Manipulation
- Conditional Logic
- Loops
- Custom Scoring Algorithms

## 📌 Project Goals

This project was developed to practice Python programming, string processing, logical conditions, and algorithm design through a practical security-related application.

---

**Developed by [endjackcho](https://github.com/endjackcho)**
