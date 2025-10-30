### **Assignment 1: Getting Started with Git**

**Reference:** [W3Schools – Git Getting Started](https://www.w3schools.com/git/git_getstarted.asp?remote=github)

**Tasks:**

1. Initialize a new Git repository in a folder of your choice.

   ```bash
   git init
   ```
2. Check the current repository status.

   ```bash
   git status
   ```
3. Write a short note (150–250 words) on:

   * What happens when you run `git init`.
   * Why version control is important in software development.
   * The significance of `.git` folder.

**Deliverables:**

* Screenshot or text output of commands.
* Written note.

---

### **Assignment 2: Creating and Tracking New Files**

**Reference:** [W3Schools – Git New Files](https://www.w3schools.com/git/git_new_files.asp?remote=github)

**Tasks:**

1. Create two new files, for example:

   ```bash
   echo "This is file1" > file1.txt
   echo "This is file2" > file2.md
   ```
2. Run and capture:

   ```bash
   git status
   ```
3. Add both files to the staging area:

   ```bash
   git add file1.txt file2.md
   git status
   ```
4. Write a short note (150–250 words) explaining:

   * What untracked files are.
   * How `git add` changes a file’s state.
   * When a file becomes part of Git version control.

**Deliverables:**

* Output of commands.
* Written note.

---

### **Assignment 3: Understanding the Staging Environment**

**Reference:** [W3Schools – Git Staging Environment](https://www.w3schools.com/git/git_staging_environment.asp?remote=github)

**Tasks:**

1. Modify one of the files created earlier.
2. Check differences and stage the modified file:

   ```bash
   git diff
   git add file1.txt
   git status
   ```
3. Write a short note (150–250 words) on:

   * The purpose of the staging area.
   * Difference between the working directory, staging area, and repository.
   * How to view and compare unstaged vs staged changes.

**Deliverables:**

* Output of commands.
* Written note.

---

### **Assignment 4: Making Commits**

**Reference:** [W3Schools – Git Commit](https://www.w3schools.com/git/git_commit.asp?remote=github)

**Tasks:**

1. Commit your staged changes:

   ```bash
   git commit -m "Initial commit with two files"
   ```
2. Modify one of the files again, add the changes, and commit with a new message.
3. View the commit history:

   ```bash
   git log --oneline
   ```
4. Write a short note (150–250 words) on:

   * What a commit represents.
   * The importance of meaningful commit messages.
   * How to check commit history and previous versions.

**Deliverables:**

* Output of commands.
* Written note.

---

