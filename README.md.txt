# 📱 Python Phonebook Programs

This repository contains three progressively advanced Python programs that simulate a phonebook. Each version builds upon the last, adding more functionality and better data handling using dictionaries.

---

## 📂️ Program 1: Basic Phonebook Entry

### 📄 Description:

This is the most basic version of the phonebook. It takes the name and contact number of one person and stores it in a dictionary.

### 💡 Features:

- Add a single contact (name + phone number)
- Displays the stored contact

### 🧐 Concepts Used:

- Dictionaries
- `input()` function
- Simple print formatting

### 💻 Sample Input:

```
Enter the name of the contact: Alice
Enter the contact number: 9876543210
```

### 📸 Output:

```
The contact details are: {'Alice': '9876543210'}
```

---

## 📂️ Program 2: Full Contact Details with Nested Dictionary

### 📄 Description:

This version stores additional information for each contact, such as:

- Primary & Secondary Phone Numbers
- Email Address
- Address
- Instagram and LinkedIn URLs

Each contact is stored using a **nested dictionary**.

### 💡 Features:

- Takes multiple data fields for one contact
- Uses a dictionary inside a dictionary for better structure

### 💻 Sample Input:

```
Enter the name of the contact: Shreya
Enter the primary contact number: 9876543210
Enter the secondary contact number: 9876543211
Enter the email address: shreya@email.com
Enter the address: 11 Garden Lane, Delhi
Enter the Instagram URL: @shreya_insta
Enter the LinkedIn URL: linkedin.com/in/shreya
```

### 📸 Output:

```python
{
  'Shreya': {
    'primary_phone_number': '9876543210',
    'secondary_phone_number': '9876543211',
    'email_adrdress': 'shreya@email.com',
    'address': '11 Garden Lane, Delhi',
    'instagram url': '@shreya_insta',
    'linked_IN': 'linkedin.com/in/shreya'
  }
}
```

---

## 📂️ Program 3: Interactive Phonebook with Menu, Search, and View All

### 📄 Description:

This is the most advanced version of the phonebook. It includes a **menu-based interface** and lets the user:

- Add multiple contacts
- View all stored contacts
- Search for a specific contact by name

### 💡 Features:

- Menu-driven loop
- Search contact functionality
- Structured storage with nested dictionaries
- Easy-to-read output

### 💻 Sample Menu:

```
📱 Phonebook Menu:
1. Add Contact
2. View All Contacts
3. Search Contact
4. Exit
Choose an option (1–4):
```

### 💻 Sample Search Output:

```
Enter the name to search: Shreya

🔍 Contact Found: Shreya
Primary Phone: 9876543210
Secondary Phone: 9876543211
Email: shreya@email.com
Address: 11 Garden Lane, Delhi
Socials:
  Instagram: @shreya_insta
  LinkedIn: linkedin.com/in/shreya
```

### 🧐 Concepts Used:

- Functions
- Looping with `while`
- Menu-based user interface
- Nested dictionaries
- Input validation and graceful exits

---

## 🚀 How to Run These Programs

1. Download or clone this repository.
2. Run the programs in a Python environment (Python 3.x):
   ```bash
   python program1.py
   python program2.py
   python program3.py
   ```

---

## 📌 Notes

- These programs are designed to run in the terminal/command line.
- Data does not persist after the program ends. You can add JSON or file storage to keep it.
- Variable naming in Program 2 has minor typos (`email_adrdress`, `linked_IN`) — these can be corrected for consistency.


## 👨‍💼 Author

Created with ❤️ by Shreya Pachauri\
Feel free to use, learn from, or contribute to this project!

