### DISKO 1 

**Description:**  
We are given a `.gz` compressed file containing a disk image. After extracting it, we get a `.dd` file — a bit-by-bit image of a disk, which preserves the exact structure and contents of the original drive. This kind of image can be mounted and explored like a real filesystem.

**Approach:**

1. **Extract the image:**
   ```bash
   gunzip disko-1.dd.gz
   ```

2. **Try to find the flag directly using `grep`:**
   ```bash
   grep "picoCTF" disko-1.dd
   ```
   Output:
   ```
   grep: disko-1.dd: binary file matches
   ```
   This means `grep` found the string `"picoCTF"` inside the binary, but doesn't print it by default due to the file being binary.

3. **Extract printable strings and search again:**
   ```bash
   strings disko-1.dd | grep "picoCTF"
   ```

4. **Flag found:**
   ```
   picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}
   ```
