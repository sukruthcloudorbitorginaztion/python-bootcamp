## 🧩 **Assignment 1: Exploring Git History**

**Objective:** Understand and explore the commit history of a repository.

**Tasks:**

1. Create a new Git repository and make at least **five commits**.
2. Use `git log` to view all commits.
3. Try different log options:

   * `git log --oneline`
   * `git log --graph --decorate`
   * `git log -p`
4. Identify a specific commit and use `git show <commitID>` to inspect details.
5. Write a short note explaining how Git history helps in debugging or reviewing changes.

**Deliverables:**

* Screenshots or terminal output of logs.
* A short explanation (150–200 words).

---

## 🧰 **Assignment 2: Using Git Stash**

**Objective:** Learn how to temporarily save uncommitted work using Git stash.

**Tasks:**

1. Create or open a project and make some changes without committing.
2. Run `git stash save "Temporary changes for feature X"`.
3. Verify using `git stash list`.
4. Make new commits or pull updates from remote.
5. Apply the stashed changes back with `git stash apply`.
6. Delete the stash once applied (`git stash drop`).
7. Explain a real-world situation where stashing is useful.

**Deliverables:**

* Screenshot of stash list and applied changes.
* A written explanation of use cases for `git stash`.

---

## 🏷️ **Assignment 3: Tagging and Version Control**

**Objective:** Practice creating and managing tags to mark specific project versions.

**Tasks:**

1. Create at least five commits in a repository.
2. Tag the third commit as `v1.0` (annotated tag).
3. Tag the latest commit as `v2.0` (lightweight tag).
4. Use `git tag` to list all tags.
5. Show detailed info for one tag using `git show v1.0`.
6. Push all tags to GitHub using `git push origin --tags`.
7. Explain the difference between annotated and lightweight tags.

**Deliverables:**

* Screenshot showing both tags in the repository.
* A short write-up on when to use annotated vs lightweight tags.

---

## 🧠 **Assignment 4: Getting Help with Git**

**Objective:** Use Git’s built-in help commands effectively.

**Tasks:**

1. Run `git help` and list 5 Git commands you haven’t used before.
2. Open detailed help for one command (e.g., `git help stash`).
3. Use `git help -a` and `git help -g` to explore available guides.
4. Find one plumbing command (low-level command) and describe what it does.
5. Explain how `git help` differs from using online documentation.

**Deliverables:**

* Screenshot of terminal output.
* A 100–150 word reflection on how `git help` can improve productivity.

---

## 🧪 **Assignment 5: Combining Git Tag, Stash, and History**

**Objective:** Apply multiple Git concepts in a single workflow.

**Scenario:**
You are developing a project where you release version `v1.0`, start new work, stash some incomplete features, then release version `v2.0`.

**Tasks:**

1. Make 3 commits → tag as `v1.0`.
2. Make changes but **stash them** instead of committing.
3. Make a few more commits → tag as `v2.0`.
4. Apply the stash and commit those changes as part of a new version.
5. Use `git log --oneline --graph` to show the full project history.
6. Explain how tagging, stashing, and viewing history can help in team collaboration.

**Deliverables:**

* Screenshot of graph view (`git log --oneline --graph`).
* Tags list and stash output.
* Summary paragraph on how these tools work together in real projects.

---
