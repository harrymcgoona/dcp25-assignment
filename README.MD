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


# List of files in the project

| Files | Source |
|-----------|-----------|
| main.py | Self written |
| test.py | Modified from [reference]() |
| test.py | From [reference]() |

# References
* Item 1
* Item 2

# What I am most proud of in the assignment

Bla bla bla

# What I learned

Bla bla bla

## Below is how to use Markdown. You can delete this:

## This is how to markdown text:

This is *emphasis*

This is a bulleted list

- Item
- Item

This is a numbered list

1. Item
1. Item

This is a [hyperlink](http://bryanduggan.org)

# Headings
## Headings
#### Headings
##### Headings

This is code:

```Java
public void render()
{
	ui.noFill();
	ui.stroke(255);
	ui.rect(x, y, width, height);
	ui.textAlign(PApplet.CENTER, PApplet.CENTER);
	ui.text(text, x + width * 0.5f, y + height * 0.5f);
}
```

So is this without specifying the language:

```
public void render()
{
	ui.noFill();
	ui.stroke(255);
	ui.rect(x, y, width, height);
	ui.textAlign(PApplet.CENTER, PApplet.CENTER);
	ui.text(text, x + width * 0.5f, y + height * 0.5f);
}
```

This is an image using a relative URL:

![An image](images/p8.png)

This is an image using an absolute URL:

![A different image](https://bryanduggandotorg.files.wordpress.com/2019/02/infinite-forms-00045.png?w=595&h=&zoom=2)

This is a youtube video:

[![YouTube](http://img.youtube.com/vi/J2kHSSFA4NU/0.jpg)](https://www.youtube.com/watch?v=J2kHSSFA4NU)

This is a table:

| Heading 1 | Heading 2 |
|-----------|-----------|
|Some stuff | Some more stuff in this column |
|Some stuff | Some more stuff in this column |
|Some stuff | Some more stuff in this column |

|Some stuff | Some more stuff in this column |






