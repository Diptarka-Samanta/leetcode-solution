# leetcode-solution
I save the leetcode daily solution and another solutions also

---

## How to Upload Daily Solutions

Follow these step-by-step instructions to upload your daily LeetCode solutions:

### Step 1: Save your code locally
Save your Python solution file (e.g., `june9#1234.py`) inside the `python/` folder:
`d:\coding\leetcode-solution\python\`

### Step 2: Open the Terminal
Open a terminal in your project directory (`d:\coding\leetcode-solution`).

### Step 3: Run the Git Commands
Run these three commands in your terminal:
```bash
# 1. Add your new file to staging
git add python/june9#1234.py

# 2. Commit the changes with a message
git commit -m "Add June 9 LeetCode solution (#1234)"

# 3. Push the commit to GitHub
git push
```

For more tips and troubleshooting (such as changing a commit message or renaming files after pushing), see the [HOW_TO_UPLOAD.md](./HOW_TO_UPLOAD.md) guide.

## Quick Git Tips

- **Change your last commit message (even if already pushed):**
  ```bash
  git commit --amend -m "Your new correct message"
  git push --force
  ```
- **Rename a file (even if already pushed):**
  ```bash
  git mv python/old-name.py python/new-name.py
  git commit -m "Rename old-name.py to new-name.py"
  git push
  ```
