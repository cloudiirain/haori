"""Test models/post.py module."""

__author__ = 'cloudiirain'
__version__ = '0.0.1'
__status__ = 'development'

import os
import unittest

from bs4 import BeautifulSoup

from haori.models.post import Post


class PostTest(unittest.TestCase):
    """Test case for general post object methods."""

    def setUp(self):
        """Set up test case."""
        dir = os.path.dirname(__file__)
        with open(os.path.join(dir, 'fixtures', 'thread_post.html')) as f:
            soup = BeautifulSoup(f, 'html.parser')
            self.post = Post(soup.find('li'))

    def test_init(self):
        """Test instance variables from Post object constructor."""
        self.assertEqual(self.post.id, 'post-360506')
        self.assertEqual(self.post.author, 'DCLXVI')

    def test_str_repr(self):
        """Test __str__() and __repr__() methods."""
        self.assertEqual(str(self.post), 'post-360506')
        self.assertEqual(repr(self.post), 'post-360506')

    def test_get_id(self):
        """Test get_id() method."""
        self.assertEqual(self.post.get_id(), 360506)

    def test_get_text(self):
        """Test that bbcode quotes are removed in get_text() output."""
        text = self.post.get_text()
        self.assertNotIn('bbCodeQuote', text)

    def test_get_text_remove_quotes_false(self):
        """Test that bbcode quotes can be retained in get_text() output."""
        text = self.post.get_text(remove_quotes=False)
        self.assertIn('bbCodeQuote', text)

    def test_get_text_remove_tags(self):
        """Test that HTML tags can be removed in get_text() output."""
        text = self.post.get_text(remove_tags=True)
        self.assertNotIn('<b>', text)

    def test_get_lines(self):
        """Test get_lines() method."""
        self.assertEqual(len(self.post.get_lines()), 23)
        self.assertEqual(len(self.post.get_lines(remove_tags=False)), 23)


if __name__ == '__main__':
    unittest.main()
