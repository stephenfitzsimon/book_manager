# Notes for book cli ap
- Goal of ap: build an ap that can manage a personal library and hold notes on the books
- Learning goals:
    - be able to implement a CLI app with multiple commands
    - save data
    - allow for user configuration
    - learn argparse, sql integration, and file access
- implement the following:
    - argparse
    - a relational database to manage saved books
- later goals:
    - add subparsers with different actions (add, print all, edit record, etc)
    - allow for producing a .bib file
        - maybe add flags for inclusion
    - GUI version
    - browser app version
    - use worldcat or google books api to populate information

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

## 13 May 2022
- made subparsers for add and print commands
- added a delete function to the DAO csv object
    - need to implement this in the cli class
- changed the save file to csv.  JSON was giving problem.  CSV is more straighforward.
    - pros for csv : csv module made it a lot easier to manage the file, csv is less space
    - cons for csv : limited information in it at this point
- notes: make lots more commments so it is easier to follow what going on in the code after a break from the project!
- next goals:
    - implement a delete command in the cli class
    - implement an update command in the cli class
    - both of these will require finding an object in the list
        - probably will need to override the __eq__ and __ne__ class functions
