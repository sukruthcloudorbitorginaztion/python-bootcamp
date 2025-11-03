## 🧩 **Assignment Set: Git Amend, Reset, Restore, and Diff**

---

### **Assignment 1 — Understanding `git commit --amend`**

**Goal:** Modify your last commit without creating a new one.

1. Create a new folder and initialize a Git repo:

   ```bash
   mkdir git-amend-demo && cd git-amend-demo
   git init
   ```
2. Create a file:

   ```bash
   echo "Version 1" > file.txt
   git add file.txt
   git commit -m "Initial commit"
   ```
3. Edit the file:

   ```bash
   echo "Version 2" >> file.txt
   git add file.txt
   ```
4. **Task:**
   Amend the previous commit to include this change without creating a new commit.

   ```bash
   git commit --amend --no-edit
   ```
5. Verify that only one commit exists and includes both changes:

   ```bash
   git log --oneline
   git show
   ```

**Extra:** Try changing the commit message while amending (`git commit --amend -m "Updated initial commit"`).

---

### **Assignment 2 — Exploring `git reset`**

**Goal:** Learn the difference between `soft`, `mixed`, and `hard` resets.

1. Continue in the same repo. Create two commits:

   ```bash
   echo "Line A" >> file.txt
   git add .
   git commit -m "Added Line A"

   echo "Line B" >> file.txt
   git add .
   git commit -m "Added Line B"
   ```

2. Run:

   ```bash
   git log --oneline
   ```

3. **Task 1:** Undo the last commit **but keep the changes staged**:

   ```bash
   git reset --soft HEAD~1
   ```

   Verify using `git status`.

4. **Task 2:** Undo the last commit **and unstage the changes**, but keep them in the working directory:

   ```bash
   git reset --mixed HEAD~1
   ```

5. **Task 3:** Undo the last commit **and remove all changes completely**:

   ```bash
   git reset --hard HEAD~1
   ```

6. Note the effect of each type of reset using:

   ```bash
   git status
   git log --oneline
   ```

---

### **Assignment 3 — Using `git restore --staged`**

**Goal:** Learn how to unstage files without removing the changes from your working directory.

1. Add a few files:

   ```bash
   echo "A" > a.txt
   echo "B" > b.txt
   git add .
   ```
2. **Task:** Unstage `b.txt` only:

   ```bash
   git restore --staged b.txt
   ```
3. Confirm:

   ```bash
   git status
   ```

   You should see `a.txt` staged and `b.txt` unstaged (but modified).

---

### **Assignment 4 — Investigating Changes with `git diff`**

**Goal:** Compare working directory, staged area, and commits.

1. Modify a tracked file:

   ```bash
   echo "New line" >> file.txt
   ```
2. View changes not yet staged:

   ```bash
   git diff
   ```
3. Stage the file and compare again:

   ```bash
   git add file.txt
   git diff --staged
   ```
4. Make another change to the same file (without staging) and compare:

   ```bash
   echo "Another line" >> file.txt
   git diff
   ```
5. Compare with previous commits:

   ```bash
   git diff HEAD~1 HEAD
   ```

---


