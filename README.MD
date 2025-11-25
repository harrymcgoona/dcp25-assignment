# Data Centric Programming Assignment 2025

- [Assignment Brief](assignment.md)

Name: Harry McGoona

Student Number: C24342003 

# Screenshots
Processing Book 1...
![](images/Screenshot%202025-11-25%20180809.png)
Processing Book 2...
![](images/Screenshot%202025-11-25%20180821.png)
Displays the user interface...
![](images/Screenshot%202025-11-25%20180834.png)
Choose option 1 [Show tunes by book]...
![](images/Screenshot%202025-11-25%20180904.png)
Display output of "Enter book number: 2"...
![](images/Screenshot%202025-11-25%20180930.png)
Choose option 2 [Show tunes by type]...
![](images/Screenshot%202025-11-25%20180954.png)
Display output of "Enter tune type: jig"...
![](images/Screenshot%202025-11-25%20181019.png)
Choose option 3 [Search tunes by title]...
![](images/Screenshot%202025-11-25%20181037.png)
Display output of "Enter search term: girl"...
![](images/Screenshot%202025-11-25%20181104.png)
Choose option 4 [Show tunes by key]...
![](images/Screenshot%202025-11-25%20181120.png)
Display output of "Enter key (e.g., G, Dm): Em"...
![](images/Screenshot%202025-11-25%20181159.png)
Display (a sample of) output of choosing option 5 [Show all tunes]...
![](images/Screenshot%202025-11-25%20181249.png)
Show program stopping after choosing option 0 [Exit]...
![](images/Screenshot%202025-11-25%20181339.png)

# Description of the project
Connects to the "abc_books" database and allows a user to prompt a program to show samples of the data contained within through search terms such as filtering by book number, tune type, title, key, and showing all tunes with a sixth option allowing the user to end the program.

# Instructions for use
1. Run the program.
2. Wait for Book 1 & 2 to finish processing.
3. Press either 1, 2, 3, 4, 5 depending on what way you wish to filter the listed tunes. Alternatively, skip to step 6.
4. Enter a search term (differing dependent on which filter was chosen).
5. Repeat steps 3 & 4 if you wish.
6. Enter 0 to end the program.

# How it works:
The program scans through the abc_books files, extracts tune information, stores everything in an SQLite database, loads it into Pandas, and then lets the user search and browse the tunes with a simple menu.

READING AND PARSING:
- Looks inside the abc_books folder.
- Opens every .abc file.
- Reads line-by-line looking for T:, R:, M:, and K:.
- each time it encounters T: it logs a new tune.

SAVING TO SQLITE DATABASE:
- Before inserting anything the program drops the old tunes table, preventing duplicates from piling up every time the program is run.
- Recreates the table with columns for id, title, type, meter, key, and book number.

LOADING THE DATA INTO PANDAS:
- Once the database is filled the program loads the entire table into a pandas dataframe.

USER INTERFACE:
- The program includes functions that filter the dataframe.
- The user gets a simple text menu with options to show tunes by book, show tunes by type, search tunes by title, show tunes by key, show all tunes, and exit.

# List of files in the project

| Files | Source |
|-----------|-----------|
| abc_books | Pre-made |
| images | Pre-made |
| .gitignore | Pre-made |
| LICENSE | Pre-made |
| README.MD | Pre-made |
| assignment.md | Pre-made |
| assignment_code.py | Self written |
| starter_code.py | Pre-made |
| tunes.db | Pre-made |

# References
* Item 1
* Item 2

# What I am most proud of in the assignment
I am most proud of the user interaction menu and the code linked to it to make it work.

# What I learned
I learnt how to show all of the database entries when prompted as opposed to only showing only the first 3 and last 3 entries of the dataset sample.
