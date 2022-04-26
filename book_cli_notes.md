# Notes for book cli ap
- Goal of ap: build an ap that can manage a personal library and hold notes the books
- implement the following:
    - argparse
    - a relational database to manage saved books
- later goals:
    - add subparsers with different actions (add, print all, edit record, etc)
    - allow for producing a .bib file
        - maybe add flags for inclusion
    - GUI version
    - browser app version

## 25 April 2022
- work on the following functionality
    - set up a book object with book info
    - allow for the user to add a book on the CL
    - save to file

## 26 April 2022
- achieved the goals from 25 Apr
- save file is currently a json. Is there a better way of doing this?
    - could the user add a INI file setting to decide how to save data?
- current goals:
    - make subparsers for add and print commands
        - add = add a book object to the save file
        - print = print all books in current save file