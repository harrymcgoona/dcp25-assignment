import os
import sqlite3
import pandas as pd

# I'm enabling these Pandas settings so I can actually SEE all the rows during testing. Without this, Pandas keeps hiding most of the entries.
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', None)

BOOKS_DIR = "abc_books"
DB_NAME = "tunes.db"

# 1. READ ABC FILES FROM MULTIPLE FOLDERS & 2. PARSE AND STORE TUNES INTO A LIST OF DICTIONARIES
def parse_abc_file(file_path):
    tunes = []
    current_tune = {}

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            # Every time the function hits a title, it starts a new tune.
            if line.startswith("T:"):
                if current_tune:
                    # I had a bug here early on where I forgot to save the previous tune, so now I'm careful to append before resetting.
                    tunes.append(current_tune)
                    current_tune = {}
                current_tune["title"] = line[2:].strip()
            elif line.startswith("R:"):
                current_tune["type"] = line[2:].strip()
            elif line.startswith("M:"):
                current_tune["meter"] = line[2:].strip()
            elif line.startswith("K:"):
                current_tune["key"] = line[2:].strip()
        # I kept forgetting this part early in development. Without this, the very last tune in each file was getting lost.
        if current_tune:
            tunes.append(current_tune)

    return tunes


# 3. STORE THE DATA IN AN SQL DATABASE
def create_database():
    # This function originally only created the table once, but I noticed every time I reran the script the number of entries kept growing. The program just kept adding duplicates each time it was ran.
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Using "DROP TABLE" to fully reset the table each rerun seemed to work in fixing the issue I mentioned last comment.
    cursor.execute("DROP TABLE IF EXISTS tunes")

    cursor.execute("""CREATE TABLE tunes (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, type TEXT, meter TEXT, key TEXT, book_number INTEGER)""")
    conn.commit()
    conn.close()

def insert_tune(conn, tune, book_number):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO tunes (title, type, meter, key, book_number) VALUES (?, ?, ?, ?, ?)""", (tune.get("title"), tune.get("type"), tune.get("meter"), tune.get("key"), book_number))
    conn.commit()

def load_books_into_db():
    conn = sqlite3.connect(DB_NAME)

    for folder_name in os.listdir(BOOKS_DIR):
        folder_path = os.path.join(BOOKS_DIR, folder_name)
        # Checking the folder name is numeric is a simple but surprisingly effective filter.
        if os.path.isdir(folder_path) and folder_name.isdigit():
            book_number = int(folder_name)
            print(f"Processing Book {book_number}...")
            for filename in os.listdir(folder_path):
                if filename.endswith(".abc"):
                    file_path = os.path.join(folder_path, filename)
                    tunes = parse_abc_file(file_path)
                    # This used to be nested incorrectly, fixed it once I noticed weird grouping.
                    for tune in tunes:
                        insert_tune(conn, tune, book_number)

    conn.close()


# 4. LOAD DATA INTO PANDAS FOR ANALYSIS
def load_dataframe():
    # Pretty straightforward: read the whole table into a DataFrame.
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql("SELECT * FROM tunes", conn)
    conn.close()

    # Quick cleanup fix — SQLite sometimes tried to treat book numbers as floats.
    df["book_number"] = df["book_number"].fillna(0).astype(int)
    return df

def get_tunes_by_book(df, book_number):
    # Get all tunes form a specific book.
    return df[df["book_number"] == book_number]


def get_tunes_by_type(df, tune_type):
    # Get tunes with a specific key.
    # Lowercasing here avoids subtle mismatches.
    return df[df["type"].str.lower() == tune_type.lower()]


def search_tunes(df, term):
    # Get tunes by title.
    # Fixed crashes by adding "na=False".
    return df[df["title"].str.lower().str.contains(term.lower(), na=False)]


def get_tunes_by_key(df, key_term):
    # Search by tune key.
    # Exact match only. I didn’t want "G" to match "Gm" or "Gmix".
    mask = df["key"].str.lower() == key_term.lower()
    return df[mask]


# 5. CREATE A SIMPLE USER INTERFACE FOR QUERYING
def menu():
    # I learned pretty fast that reloading the DataFrame in every loop was slow, so now I load it once here.
    df = load_dataframe()

    while True:
        print("\n--- ABC Tune Database ---")
        print("1. Show tunes by book")
        print("2. Show tunes by type")
        print("3. Search tunes by title")
        print("4. Show tunes by key")
        print("5. Show all tunes")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            book = int(input("Enter book number: "))
            results = get_tunes_by_book(df, book)
            print(results if not results.empty else f"No tunes found for book {book}.")
        elif choice == "2":
            ttype = input("Enter tune type: ")
            results = get_tunes_by_type(df, ttype)
            print(results if not results.empty else f"No tunes found of type {ttype}.")
        elif choice == "3":
            term = input("Enter search term: ")
            results = search_tunes(df, term)
            print(results if not results.empty else "No tunes found matching that term.")
        elif choice == "4":
            key_term = input("Enter key (e.g., G, Dm): ")
            results = get_tunes_by_key(df, key_term)
            print(results if not results.empty else f"No tunes found with key {key_term}.")
        elif choice == "5":
            print(df)
        elif choice == "0":
            break
        else:
            print("Invalid option. Try again.")


# MAIN PROGRAM
if __name__ == "__main__":
    # Running the DB creation first ensures a clean slate every time.
    create_database()
    # Load the two book folders into SQLite.
    load_books_into_db()
    # Finally drop into the menu UI.
    menu()
