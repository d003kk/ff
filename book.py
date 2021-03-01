"""This module contains the Book class."""
import play

class Page(object):

    """Books contain pages."""
    def __init__(self):
        """ Initialize Book."""
        self.nextPage = []
        self.text = "Blahblah"
    def play(self, player):
        print(self.text)

class PageNexus(Page):

    """Books contain pages."""
    def __init__(self):
        """ Initialize Book."""
        self.options= {"blah":232, "blahblah":3223, "baskl":323}
        self.text = "Blahblah"
    def play(self, player):
        print(self.text)

class Book(object):

    """Books contain pages."""

    def __init__(self):
        """ Initialize Book."""
        self.pages = []

    def play_book(self, player, pageNo=0):
        """Combatant subtracts damage from stamina."""
        page = self.pages[pageNo]
        while not player.dead():
            page = self.pages[page.play(player)]
