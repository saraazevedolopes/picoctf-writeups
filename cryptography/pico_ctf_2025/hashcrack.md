### hashcrack

**Description:**  
We are given access to a remote service through **netcat**. The service provides us with a series of cryptographic hash values (**MD5**, **SHA-1**, and **SHA-256**) and asks us to input the corresponding plaintext password that produces each hash. The goal is to successfully crack each hash to eventually obtain the flag.

**Approach:**

1. **Connect to the remote service:**
   ```bash
   nc verbal-sleep.picoctf.net 53299
   ```

2. **First hash (MD5):**
   ```
   We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
   Enter the password for identified hash:
   ```
   I used the script `md5_cracker.py` located in the `resources` folder with the `rockyou.txt` wordlist.

   ```bash
   python3 resources/md5_cracker.py
   ```

   Output:
   ```
   [+] Password found: password123
   ```

   ```
   Correct! You've cracked the MD5 hash with no secret found!
   ```

3. **Second hash (SHA-1):**

   ```
   Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
   Enter the password for the identified hash:
   ```
   I used the script `sha1_cracker.py` in the `resources` folder.

   ```bash
   python3 resources/sha1_cracker.py
   ```

   Output:
   ```
   [+] Password found: letmein
   ```

   ```
   Correct! You've cracked the SHA-1 hash with no secret found!
   ```

4. **Third hash (SHA-256):**

   ```
   Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
   Enter the password for the identified hash:
   ```
   I used the script `sha256_cracker.py` from the `resources` folder.

   ```bash
   python3 resources/sha256_cracker.py
   ```

   Output:
   ```
   [+] Password found: qwerty098
   ```

   ```
   Correct! You've cracked the SHA-256 hash with a secret found.
   The flag is: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_23622a7e}
   ```

5. **Flag found:**
   ```
   picoCTF{UseStr0nG_h@shEs_&PaSswDs!_23622a7e}
   ```

**How the scripts work:**

All the Python scripts in the `resources` folder (`md5_cracker.py`, `sha1_cracker.py`, `sha256_cracker.py`) follow the same structure:

1. A **target hash** is hardcoded in the script.
2. The script loads passwords from the `rockyou.txt` wordlist.
3. Each password is hashed using the relevant algorithm (**MD5**, **SHA-1**, **SHA-256**).
4. If a match is found, the script prints the password.

These scripts are minimal by design to allow fast testing in CTF scenarios.

**About `rockyou.txt`:**

* `rockyou.txt` is a famous password wordlist compiled from real password leaks.
* It contains millions of common passwords used by real users.
* Hash cracking is often possible because users choose predictable passwords that appear in such lists.
* You can download `rockyou.txt` manually using the following command:
  ```bash
  wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
  ```

**Takeaways:**

* All the hashes were breakable because the passwords were **weak and common**, easily guessed using public wordlists.
* No **salt** was applied, making offline dictionary attacks straightforward.
* This highlights the importance of using **modern password hashing algorithms** (e.g., **bcrypt**, **argon2**) together with **salts** and **strong passwords** to resist attacks like this.
