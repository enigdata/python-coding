import datetime 

#Store the next available id for all new notes
last_id = 0 

class Note:
    #Represent a note in the notebook. Match against a string in searches and store tags for each note.#

    def __init__(self, memo, tags = ''):
        '''
        Initialize a note with memo and optional space-separated tags.
        Automatically set the note's creation date and a unique id.
        ''' 

        self.memo = memo 
        self.tags = tags 
        self.creation_date = datetime.date.today()
        global last_id 
        last_id += 1 
        self.id = last_id 

    def match(self, search_text):
        '''
        Determine if this note matches the filter text.
        Return true if matches, False otherwise
        '''
        return search_text in self.memo or search_text in self.tags  

class Notebook:
    "Represent a collection of notes that can be tagged, modified and searched"
    def __init__(self):
        '''
        Initialize a notebook with an empty list.
        '''
        self.notes = [] 

    def add_note(self, memo, tags = ""):
        '''
        Create a new note and add it to the list.
        '''
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        '''
        Find the note with the given id and change its memo to the given value.
        '''
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo 
                break 

    def modify_tags(self, note_id, tags):
        '''
        Find the note with the given id and change its tags to the given value.
        '''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags 
                break 

    def search(self, search_text):
        '''
        Find all notes that match the given search text
        '''
        return [note for note in self.notes if note.match(search_text)]
    
#### Improve the above code
# modify_tags and modify_memo methods are almost identical.  Not good coding practice 
# 

def _find_note(self, note_id):
    '''
    Locate the note with the given id.
    '''
    for note in self.notes:
        if str(note.id) == str(note_id):
            return note 
    return None 

def modify_memo(self, note_id, memo):
    '''
    Find the note with the given id and change its memo to the given value
    '''
    if self._find_note(note_id):
        self._find_note(note_id).memo = memo 
        return True
    else:
        return False 

def modify_tags(self, note_id, tags):
    '''
    Find the note with the given id and change its tags to the given value
    '''
    if self._find_note(note_id):
        self._find_note(note_id).tags = tags
        return True
    else:
        return False 

#### In a separate code file let's create a menu interface
import sys 
#from notebook import Notebook

class Menu:
    '''
    Display a menu and respond to choices when run.
    '''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            '1': self.show_notes,
            '2': self.search_notes,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.quit
        }

    def display_menu(self):
        print(
            """
Notebook Menu

1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
"""
        )

    def run(self):
        '''
        Display the menu and respond to choices.
        '''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice, None)
            if action:
                action()
            else:
                print(f'{choice} is not a valid choice.')
    
    def show_notes(self, notes = None):
        if not notes:
            notes = self.notebook.notes 
        for note in notes:
            print('{}: {}\n{}'.format(note_id, note.tags, note.memo))

    def search_notes(self):
        search_text = input('Search for: ')
        notes = self.notebook.search(search_text)
        self.show_notes(notes)

    def add_note(self):
        memo = input('Enter a memo: ')
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        id_ = input('Enter a note id: ')
        memo = input('Enter a memo: ')
        tags = input('Enter tags: ')
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print('Thank you for using your notebook today.')
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()

    





    





