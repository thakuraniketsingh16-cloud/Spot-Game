# 📝 Project Statement: Python Slot Machine Simulation

## 1. Introduction
The objective of this project is to develop a simplified, text-based simulation of a casino slot machine. Using Python, the application replicates the core mechanics of a game of chance—betting, spinning reels, and calculating payouts—providing users with a risk-free environment to test their luck.

---

## 2. Objective
The primary goal was to build an interactive command-line application that manages the user’s session balance while ensuring true randomness in outcomes.  
This project demonstrates Python concepts such as:

- Control flow  
- User input validation  
- Modular programming  
- Randomization  

---

## 3. Core Features

### 🎮 Virtual Economy  
The player begins with a fixed balance of *$100* and must manage funds strategically.

### 🎰 Randomized Mechanics  
The game uses Python’s random library to generate symbols from:  
🌟 🍎 🍌 👻 🐪

### 🏆 Tiered Payout System  
Multipliers vary by symbol:  
- *1×* – Camel 🐪  
- *2×* – Ghost 👻  
- *3×* – Banana 🍌  
- *4×* – Apple 🍎  
- *5×* – Star 🌟  

### 🛡 Input Validation  
The program prevents:  
- Over-betting  
- Negative bets  
- Non-numeric input  

---

## 4. Technical Implementation

### 🔧 spin_slots()
Generates a random list of three slot symbols.

### 🔧 payout(row, bet)
Checks if the symbols match and applies the correct multiplier.

### 🔧 main() Game Loop
Maintains the game state until:  
- User quits (q)  
- Or the balance reaches zero  

---

## 5. Conclusion
The Slot Machine Simulation demonstrates how basic programming concepts can be combined to build an interactive and engaging user experience. It also provides a strong foundation for future enhancements like:

- GUI version  
- Sound effects  
- Save/load system  
- More symbols and animations
