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
    def test_book_player_dead(self, mock_player, mock_page):
        b = book.Book()
        b.pages.append(mock_page)
        b.pages.append(mock_page)
        mock_player.dead.returnvalue = True
        b.play_book(mock_player, 0)
        mock_page.play.assert_not_called()

    @patch('book.Page', autospec=True)
    @patch('book.play.Player', autospec=True)
    def test_book_player_dies_2nd_page(self, mock_player, mock_page):
        b = book.Book()
        b.pages.append(mock_page)
        b.pages.append(mock_page)
        mock_player.dead.side_effect = [False, True]
        b.play_book(mock_player, 0)
        mock_page.play.assert_called_with(mock_player)
        self.assertEqual(mock_page.play.call_count, 1)
