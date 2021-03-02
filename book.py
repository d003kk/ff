"""This module contains the Book class."""
import play

class Page(object):

    """Page base class"""
    def __init__(self):
        """ Initialize Page."""
        self.nextPage = []
        self.text = ""

    def play(self, player):
        """ Print Text"""
        print(self.text)

class PageNexus(Page):

    """A Page that just leads to other pages"""

    def __init__(self):
        """ Initialize Page with options."""
        self.options= {"blah":232, "blahblah":3223, "baskl":323}
        self.text = ""

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
