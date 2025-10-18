## Chapter: Clone a GitHub Repository Using SSH Key

This guide walks you through generating an SSH key, adding it to GitHub, and configuring your system to clone repositories securely using SSH.

---

### 1. Prerequisites

Before starting, ensure:

* **Git** is installed.
  You can verify by running:

  ```powershell
  git --version
  ```

* You have access to your **GitHub account**.

---

### 2. Generate an SSH Key

1. Open **PowerShell** or **Command Prompt**.

2. Navigate to your desired working directory, for example:

   ```powershell
   cd C:\workspace\Experiments\git_learning
   ```

3. Run the following command to generate a new SSH key:

   ```powershell
   ssh-keygen -t ed25519 -C "GitHub Sukruth Cloud Orbit" -f id_ed25519
   ```

4. When prompted:

   * Press **Enter** to skip passphrase (optional), or
   * Enter a secure **passphrase** for extra protection.

You should see an output similar to:

```
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in id_ed25519
Your public key has been saved in id_ed25519.pub
```

The files `id_ed25519` (private key) and `id_ed25519.pub` (public key) will be created in your current directory.

---

### 3. Add the SSH Key to GitHub

1. Open GitHub in your browser and navigate to:
   [https://github.com/settings/keys](https://github.com/settings/keys)

2. In the left pane, click **SSH and GPG keys**.

3. Click **New SSH key**.

4. Enter a title — for example:
   **GitHub Sukruth Cloud Orbit**

5. Open the public key file you just generated:

   ```powershell
   notepad id_ed25519.pub
   ```

6. Copy the entire content and paste it into the **Key** field on GitHub.

7. Click **Add SSH key** to save.

---

### 4. Configure SSH on Your Local System

To ensure Git uses your private key correctly, configure your SSH client.

1. Open or create the SSH configuration file:

   ```
   %USERPROFILE%\.ssh\config
   ```

   Example full path:
   `C:\Users\sukru\.ssh\config`

2. Add the following configuration:

   ```text
   Host github.com
       HostName github.com
       User git
       IdentityFile C:\workspace\Experiments\git_learning\ssh\id_ed25519
   ```

> 💡 **Tip:** Make sure the path to `id_ed25519` is correct.

---

### 5. Test Your SSH Connection

Run the following command to verify the SSH connection to GitHub:

```powershell
ssh -T git@github.com
```

If everything is set up correctly, you’ll see a message like:

```
Hi sukruth! You've successfully authenticated, but GitHub does not provide shell access.
```

---

### 6. Clone the Repository

Now you can clone your repository using SSH:

```powershell
git clone git@github.com:sukruthcloudorbitorginaztion/python-bootcamp.git
```

---

## ✅ You’re Done!

You have successfully:

* Generated an SSH key
* Added it to GitHub
* Configured your local SSH client
* Cloned your GitHub repository securely using SSH

---