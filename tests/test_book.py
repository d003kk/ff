import unittest
import book
import play
from unittest.mock import patch, call

class TestBook(unittest.TestCase):


    def test_init(self):
        b = book.Book()
        self.assertEqual(b.pages, [])

    @patch('book.Page', autospec=True)
    @patch('book.play.Player', autospec=True)
    def test_combat(self, mock_player, mock_page):
        b = book.Book()
        b.pages.append(mock_page)
        b.pages.append(mock_page)
        mock_player.dead.returnvalue = True
        b.play_book(mock_player, 0)
        mock_page.play.assert_not_called()

