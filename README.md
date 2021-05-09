# Overview

This is a SQLite program in python that creates a SQL database of D&D magic items. It's a command line program that allows users to add, search, modify, delete and view all the items in the items table. My husband and I play a lot of D&D so I thought it would be cool to have a database of magic items that we could use in our campaigns and this is a cool starter project that I can invest some time into to add in more features (like a description column in the items table) and some changes in the code to make it harder to have inputs that will cause issues in the data or the code.

[Software Demo Video](https://youtu.be/npTPVrsn1HQ)

# Relational Database

Currently my database is made up of three tables: items, rarity, and type. The items table has an id primary key, the name of the item, the rarity of the item (which is a foreign key to the rarity table however I had problems implementing this in the code), the type of item (foreign key to the type table) and attunement which is a yes or no binary column (I was planning on doing Y or N, but I accidentally typed out No and I don't want to recreate my database from scratch). The rarity table has an id primary key and the name column with 6 values between Common and Artifact. The type table has an id primary key and a name column with 9 different types of items.

# Development Environment

- Python 3.9.0
- SQLite 3

# Useful Websites

* [Python Standard Library SQLite](https://docs.python.org/3.8/library/sqlite3.html)
* [SQLite Tutorial](https://www.sqlitetutorial.net/)
* [W3Schools SQL Tutorials](https://www.w3schools.com/sql/default.asp)
* [Magic Items Page I used](https://donjon.bin.sh/5e/magic_items/)

# Future Work

* I wanted to implement the join for the item search, however I ran into issues and for awhile I couldn't figure out what was wrong before I realized that the rarity and type columns in my items table were strings because I uploaded them into the table using inputs and the rarity_id and type_id columns were integers so when I tried to do an inner join it wouldn't return anything and I only figured it out after I tried a left join and it say I had nulls which helped me figure it out so I'll need to fix that by either rewriting the inputs so it will upload integers to the tables and delete and reupload the current items in the items table or I could use the alter table function to make the id columns in the rarity and type tables strings so I can get the joins to work.
* Also I didn't spend a significant amount of time writing the code that protects the database from having incorrect data put in it. I normally take a bit of time to write code that makes sure inputs are only what I want them to be but to save time I would say to input an integer between 1 and 6, however if they didn't it wouldn't flag so you can probably do some funny things with the database for now until I go in and fix it.
* I would also like to eventually two more columns in the items table for the description of the item and the sourcebook it's from (and a sourcebook table) however I think the easiest way to do that would be to recreate the database and add those in when I recreate it so I probably won't get around to it for a bit.
* Finish commenting the code