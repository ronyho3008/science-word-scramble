# 🔬 Science Word Scramble Game

A simple Python project where players try to unscramble biology and chemistry related words.
This project is based on an earlier assignment and was converted into a standalone repository.

---
## 🎮 How to Play
In order to play the game you only need to Make sure you have Python 3.8+ installed ☑️
Run the game:

```bash
python word_scramble.py
```

You will see a scrambled scientific word.
Try to guess the original word!

Type quit anytime to exit the game.


![PIC](https://c8.alamy.com/comp/F2H55X/biology-word-representing-plant-life-and-wildlife-F2H55X.jpg)


## 🔧 Improvements Added

This project includes several enhancements beyond the original assignment:

### 1. Loading Words from a File  
The game now loads scientific words from an external file (`words.txt`).  
If the file is missing or empty, the game automatically falls back to a built-in word list.

### 2. High Score System  
A new `highscore.txt` file stores the highest score ever achieved.  
When a player beats the previous record, the game saves the new high score.

### 3. Better Error Handling  
The game continues to run smoothly even if files are missing, corrupted, or empty.

### 4. Cleaner and More Organized Code  
Functions are separated clearly, making the project easier to read, maintain, and extend.

These improvements use real file-handling techniques, as requested in the assignment.



