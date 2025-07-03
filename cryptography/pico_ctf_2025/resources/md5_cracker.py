import hashlib

target_hash = "482c811da5d5b4bc6d497ffa98491e38"
wordlist_path = "rockyou.txt"

with open(wordlist_path, "r", encoding="latin-1") as file:
    for line in file:
        password = line.strip()
        hash_test = hashlib.md5(password.encode()).hexdigest()
        if hash_test == target_hash:
            print(f"[+] Password found: {password}")
            break
    else:
        print("[-] Password not found in wordlist.")
