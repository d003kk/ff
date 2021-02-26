"""This module contains the Book class."""
import player

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
        self.options= {:, :, :}
        self.text = "Blahblah"
    def play(self, player):
        print(self.text)

class Book(object):

    """Books contain pages."""

    def __init__(self):
        """ Initialize Book."""
        self.pages = []

    def play_book(self, damage, pageNo=0):
        """Combatant subtracts damage from stamina."""
        page = self.page[pageNo]
        while(!player.isDead())
            page = self.pages[page.play(player)]
