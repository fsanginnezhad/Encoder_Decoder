# 🔐 ROT13 Text Encoder/Decoder

A minimal yet effective **command-line tool** written in Python that uses the classic [ROT13 cipher](https://en.wikipedia.org/wiki/ROT13) to encode and decode messages. 🔁

---

## ✨ Features

- 🔤 Transforms input using the ROT13 substitution cipher
- 🧠 Decodes automatically with the same command
- 🔁 Runs in a loop for continuous encoding
- ❓ Exit confirmation for accidental quits
- 🧼 Clean and simple terminal interface

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.x  
- No external libraries needed

### ▶️ Run the Program

```bash
python rot13.py
💬 Sample Usage
text
Copy
Edit
Enter Your Text: Hello World
Uryyb Jbeyq

Enter Your Text: q
Are You Sure to EXIT? no
D

Enter Your Text: exit
Are You Sure to EXIT? yes
# Program exits
🔍 What is ROT13?
ROT13 ("rotate by 13 places") is a simple letter substitution cipher that replaces a letter with the letter 13 positions after it in the alphabet.
It's a special case of the Caesar cipher and is its own inverse—applying it twice returns the original text.

For example:

Input	ROT13 Output
Hello	Uryyb
Python	Clguba
Uryyb	Hello

📁 Project Structure
css
Copy
Edit
📦 rot13-cli/
 ┣ 📄 rot13.py         ← Main script
 ┗ 📄 README.md        ← Project documentation
📌 Exit Conditions
To exit the program, enter any of the following:

bash
Copy
Edit
q, quit, e, exit
You'll be asked to confirm before exiting.

📝 License
This project is licensed under the MIT License.
Feel free to use, modify, and share.

❤️ Acknowledgments
Made with love using Python 🐍
Inspired by curiosity for classic cryptography.
