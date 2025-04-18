
class Node:
    """
    A class to represent a node in the tree.
    """
    def __init__(self, word, meaning):
        '''Initialzes Node, or key/value pair'''
        
        self.word = word
        self.meaning = meaning
        self._left = None
        self._right = None
        self._height = 0

class DictionaryBST:
    """
    A class to represent a dictionary using self-balancing trees.
    
    Methods:
        insert(word, meaning): Insert a word and its meaning into the dictionary.
        search(word): Search for a word in the dictionary and return its meaning.
        print_alphabetical(): Return all dictionary entries in alphabetical order.
    """
    def __init__(self, entries: dict[str, str] | None = None):
        """
        Parameters:
        entries (dict[str, str] | None, optional): A dictionary with string words and meanings.
                                                  Defaults to None if not provided.
        """
        self.entries = entries
        self._root = None
        self._height = 0
        if self.entries is not None:
            for key, val in entries.items():
                self.insert(key, val)
    
    def insert(self, word, meaning):
        """
        Insert a word and its meaning into the tree. If inserting a duplicate word updates the meaning.
        
        Args:
            word (str): The word to insert.
            meaning (str): The meaning of the word.
        """
    
        self._root = self._insert(word, meaning, self._root)

    def _insert(self, word, meaning, current):
        '''Helper function that searches but allows user to only enter word/meaning'''

        if current is None:
            return Node(word, meaning)
        
        if current.word == word:
            current.meaning = meaning
        elif word < current.word:
            current._left = self._insert(word, meaning, current._left)
        else:
            current._right = self._insert(word, meaning, current._right)
        
        self._update_height(current)
        balance = self._find_balance_factor(current)

        if balance > 1:
            if word > current._left.word:
                current._left = self._rotate_left(current._left)
            return self._rotate_right(current)
        elif balance < -1:
            if word < current._right.word:
                current._right = self._rotate_right(current._right)
            return self._rotate_left(current)
        
        return(current)

    def search(self, word):
        """
        Search for a word in the tree and return its meaning.
        
        Args:
            word (str): The word to search for.
        
        Returns:
            str: The meaning of the word if found, else return None'
        """

        if self._root is None:
            return(None)
        current = self._root
        return(self._search(word, current))

    def _search(self, word, current):
        '''Private function to search on basis of left and right'''

        if word == current.word:
            return(current.meaning)
        if word < current.word:
            if current._left is None:
                return(None)
            return(self._search(word, current._left))
        if word > current.word:
            if current._right is None:
                return(None) 
            return(self._search(word, current._right))
            
    def print_alphabetical(self):
        """
        Retrieve all dictionary entries in alphabetical order.
        
        Returns:
            list of tuple: List of tuples, each containing (word, meaning).
        """
        
        if self._root is None:
            return([])
        current = self._root
        return(list(self._print_alphabet(current)))
    
    def _print_alphabet(self, current):
        '''Helper function for printing alphabet'''

        if current is not None:
            yield from self._print_alphabet(current._left)
            yield (current.word, current.meaning)
            yield from self._print_alphabet(current._right)

    def _get_height(self, current):
        '''Returns height of object, if none returns -1'''

        return current._height if current else -1 #returns -1 if there is no node, otherwise returns height

    def _update_height(self, current):
        '''Returns height of subtree on basis of root(current) given'''

        current._height = 1 + max(self._get_height(current._left), self._get_height(current._right)) #finds max height

    def _find_balance_factor(self, current):
        '''Finds balance factor'''
        if current is None:
            return(0)
        return(self._get_height(current._left) - self._get_height(current._right))

    def is_balanced(self):
        """Public method to check if the entire tree is balanced."""
        return self._check_balanced(self._root)

    def _check_balanced(self, current):
        '''Private method to see if tree is balanced'''
        if current is None:
            return True
        balance = self._find_balance_factor(current)
        if abs(balance) > 1:
            return False
        return self._check_balanced(current._left) and self._check_balanced(current._right)

    def _rotate_left(self, parent):
        '''Rotates left on basis that parent's right child' left can be middle of parent and right child'''

        if parent is None or parent._right is None:
            return parent 
        new_root = parent._right
        parent._right = new_root._left
        new_root._left = parent
        self._update_height(parent)
        self._update_height(new_root)
        return(new_root)

    def _rotate_right(self, parent):
        '''Rotates right to balance tree more'''

        if parent is None or parent._left is None:
            return parent
        new_root = parent._left
        parent._left = new_root._right
        new_root._right = parent
        self._update_height(parent)
        self._update_height(new_root)
        return(new_root)