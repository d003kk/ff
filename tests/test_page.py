import unittest
import book
import play
from unittest.mock import patch, call

class TestPage(unittest.TestCase):


    def test_init(self):
        page = book.Page()
        self.assertEqual(page.nextPage, [])
        self.assertEqual(page.text, "")

    @patch('book.play.Player', autospec=True)
    @patch('builtins.print')
    def test_page_play_prints_txt(self, mock_print, mock_player):
        page = book.Page()
        page.play(mock_player)
        mock_print.assert_called_with(page.text)

