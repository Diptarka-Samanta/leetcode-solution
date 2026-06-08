# How to Upload Your Daily LeetCode Solutions to GitHub

Follow these step-by-step instructions to upload your daily LeetCode solutions from your local computer to your GitHub repository.

---

## Step 1: Create the Python File
Write or paste your LeetCode solution into a Python file inside your local repository.

1. Open VS Code (or your editor of choice) to the repository folder: `d:\coding\leetcode-solution\`.
2. Inside the `python` folder, create a new file named after the date and question number/title.
   - *Example file name format:* `june8#2161.py` or `june9#1234.py`
3. Paste your LeetCode solution inside this file and **save the file** (`Ctrl + S`).

---

## Step 2: Open your Terminal
You need to run a few commands in the terminal to push the files to GitHub.

1. In VS Code, open the integrated terminal:
   - Press **Ctrl + `** (backtick) or go to **Terminal** -> **New Terminal** at the top menu.
2. Make sure you are in the correct repository directory. The prompt should show:
   ```powershell
   D:\coding\leetcode-solution>
   ```
   *If it doesn't, run the command:*
   ```powershell
   cd D:\coding\leetcode-solution
   ```

---

## Step 3: Run the Git Commands
Run the following three commands in your terminal one by one:

### 1. Stage your changes
This tells Git to prepare your new file to be committed.
```bash
git add python/june9#1234.py
```
*(Tip: You can also use `git add .` to stage all new and changed files at once).*

### 2. Commit your changes
This saves a snapshot of your staged files locally with a descriptive message.
```bash
git commit -m "Add June 9 LeetCode solution (#1234)"
```

### 3. Push to GitHub
This uploads your local commit to your GitHub repository.
```bash
git push
```

---

## Troubleshooting & Tips
- **Check Git Status:** If you want to see which files are modified or ready to be added, run:
  ```bash
  git status
  ```
- **Syncing remote changes:** Before starting to write a new solution, it's always a good habit to pull any changes from GitHub (if you edited README on the website, for example):
  ```bash
  git pull
  ```
