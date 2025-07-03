import hashlib

target_hash = "b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3"
wordlist_path = "rockyou.txt"

with open(wordlist_path, "r", encoding="latin-1") as file:
    for line in file:
        password = line.strip()
        hash_test = hashlib.sha1(password.encode()).hexdigest()
        if hash_test == target_hash:
            print(f"[+] Password found: {password}")
            break
    else:
        print("[-] Password not found in wordlist.")
