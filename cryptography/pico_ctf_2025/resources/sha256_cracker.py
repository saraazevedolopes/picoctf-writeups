import hashlib

# Target SHA-256 hash to crack
target_hash = "916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745"
wordlist_path = "rockyou.txt"

with open(wordlist_path, "r", encoding="latin-1") as file:
    for line in file:
        password = line.strip()
        hash_test = hashlib.sha256(password.encode()).hexdigest()
        if hash_test == target_hash:
            print(f"[+] Password found: {password}")
            break
    else:
        print("[-] Password not found in wordlist.")
