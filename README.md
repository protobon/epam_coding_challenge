# epam_coding_challenge

### Description
This script simulates a file system CLI program to create, delete, move and list files in a directory.

**to run the program, execute the following command in the console at the root of this project:**

 `python main.py`
 
Available commands:

`CREATE path/to/file` -> creates a new 'file' in the system if the path is valid, otherwise prints an error

`DELETE path/to/file` -> deletes a 'file' given the path provided, if path is invalid prints an error

`MOVE path/to/target path/to/destination` -> moves a 'file' from target to destination, both paths must be valid otherwise prints an error

`LIST` -> standalone command, prints 'directory' contents as a tree

### Functionality
It uses a python dictionary as hierarchical tree.