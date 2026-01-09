
# Assignment 1: Data Handling, Visualization & Database Management

**Submitted by:** Harshwardhan Ahire  
**Date:** January 2026

## 📌 Project Overview
This repository contains the solution for Assignment 1, which consists of three distinct Python tasks:
1.  **API Data Retrieval:** Fetching book data from the Open Library API and storing it in SQLite.
2.  **Data Visualization:** Analyzing student test scores and generating a bar chart.
3.  **CSV Import:** Reading user data from a CSV file and migrating it to a database.

---

## ⚙️ Prerequisites & Installation

Ensure you have **Python 3.x** installed. You will also need to install the required third-party libraries.

### 1. Install Dependencies
Run the following command in your terminal/command prompt:

```bash
pip install requests matplotlib pandas

```

---

## 📂 File Structure

```text
Assignment_1/
│
├── problem1_api.py        # Code for fetching API data and saving to DB
├── problem2_visuals.py    # Code for Student Score visualization
├── problem3_csv.py        # Code for importing CSV data to DB
├── users.csv              # (Auto-generated) Sample input for Problem 3
├── library.db             # (Generated) Database file for Problem 1
├── user_data.db           # (Generated) Database file for Problem 3
└── README.md              # This documentation file

```

---

## 🚀 How to Run the Scripts

### Problem 1: API to SQLite

Fetches Science Fiction books from the Open Library API and saves them into `library.db`.

**Command:**

```bash
python problem1_api.py

```

**Expected Output:** - Console message: `[-] Successfully saved 5 books.`

* A table of books printed in the terminal.

---

### Problem 2: Data Visualization

Fetches student scores (or uses fallback data) and displays a bar chart.

**Command:**

```bash
python problem2_visuals.py

```

**Expected Output:** - Console message: `Average Score: XX.XX`

* A pop-up window displaying a **Bar Chart** with Green/Red bars.

---

### Problem 3: CSV to Database Import

Reads `users.csv` (creates it if missing) and inserts unique users into `user_data.db`.

**Command:**

```bash
python problem3_csv.py

```

**Expected Output:** - Console message: `[-] Successfully processed X rows.`

* A printed table of users currently stored in the database.

---

## ⚠️ Troubleshooting

* **Error: `Module not found`** Make sure you ran the `pip install` command listed in the Prerequisites section.
* **Error: `Database locked`** Ensure you don't have the database file open in another program (like 'DB Browser for SQLite') while running the script.
* **Connection Error** Problem 1 requires an active internet connection to reach `openlibrary.org`.

```

```