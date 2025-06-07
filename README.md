# 🎱 AUSTRALIAN POWERBALL NUMBER GENERATOR

A cryptographically secure, animated number generator for the Australian Powerball lottery game. Built in Python with `tkinter`, this app generates fresh, random Powerball entries each time — with animated draws, styled number balls, and a polished visual interface.

---

## 🔑 What It Does

- 🎲 Generates **4 complete Powerball games** per draw
- 🔐 Uses **cryptographically secure randomness** (`secrets.SystemRandom`)
- 🌀 Animated number reveal (like real lottery machines)
- 🎱 Displays numbers as styled “balls”
- 🟣 Distinct Powerball display (1–20)
- 🟨 Yellow background for arcade-like presentation
- 🖥️ Always opens centered on screen
- 🧱 Frameless window (no OS title bar)

---

## 🎯 Modeled After

This generator follows the rules of **Australian Powerball**:

- **7 main numbers** drawn from 1–35
- **1 Powerball number** drawn from 1–20
- 4 sets (games) generated per session

This is a **number generator only**, not a full lottery simulator. It does **not simulate draw odds, winnings, or tickets**.

---

## 🔐 Secure Randomness

- Uses Python’s `secrets.SystemRandom()` — same as used in security, password managers, and encryption tools
- Does **not** reuse seeds or allow prediction
- Ideal for fair-number generation (though not for gambling)

---

## 💻 Interface Preview

| Feature           | Description                                  |
|------------------|----------------------------------------------|
| 🎱 White number balls | Bold, styled, animated labels                |
| 🟣 Powerball       | Purple standout ball                          |
| 🌀 Animation       | Each number flickers before being revealed    |
| 🟨 Theme           | Yellow background, green accents              |
| 🎛️ Controls        | "Draw Numbers" and "Exit" buttons             |

---

## ▶️ How to Run

### 🛠 Prerequisites

Install `tkinter` if not already installed:

```bash
sudo apt install python3-tk -y


🧠 How It Works
Uses secrets.SystemRandom() to draw 7 unique numbers (1–35)

Uses randint() to generate 1 Powerball (1–20)

Results are styled and animated before final display

App window is centered using screen dimensions

overrideredirect(True) removes the OS window frame

🚫 What It Is Not
Not a simulator of real draws

Does not calculate winnings or simulate odds

Not connected to any official lottery service




