"""This module contains the Book class."""

class Page():

    """Page base class"""
    def __init__(self):
        """ Initialize Page."""
        self.nextpage = []
        self.text = ""

    def play(self, player):
        """ Print Text"""
        print(self.text)

class PageNexus(Page):

    """A Page that just leads to other pages"""

    def __init__(self):
        """ Initialize Page with options."""
        self.options = {"blah":232, "blahblah":3223, "baskl":323}
        self.text = ""

class Book():

    """Books contain pages."""

    def __init__(self):
        """ Initialize Book."""
        self.pages = []

    def play_book(self, player, pageno=0):
        """Combatant subtracts damage from stamina."""
        page = self.pages[pageno]
        while not player.dead():
            page = self.pages[page.play(player)]
