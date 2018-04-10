"""Post class."""

__author__ = 'cloudiirain'
__version__ = '0.0.1'
__status__ = 'development'

import copy


class Post(object):
    """Represents a post in a NUF thread.

    Attributes:
        id: (unicode) The NUF id for the post.
        author: (unicode) The author's username.
        text: (bs4.Tag) The content of the post.

    """

    def __init__(self, soup):
        """Construct a single post given a BeautifulSoup Tag object.

        Args:
            soup (bs4.Tag): BeautifulSoup Tag object.

        """
        self.id = soup['id']
        self.author = soup['data-author']
        self.text = soup.find('blockquote', 'messageText')

    def __str__(self):
        """Print string representation of the post."""
        return self.id

    def __repr__(self):
        """Print computer representation of the post."""
        return self.id

    def get_id(self):
        """Print the numeric integer of the id of this post."""
        return int(self.id.split('-')[1])

    def get_text(self, remove_quotes=True, remove_tags=False):
        r"""Print the text body of the post.

        Args:
            remove_quotes (bool): Remove BB Code quote blocks if True.
            remove_tags (bool): Removes all html tags if True and replaces
                `<br>` with `\n`.

        Return:
            (str) Returns the parsed post text body.

        """
        text_copy = copy.copy(self.text)
        if remove_quotes:
            for quote in text_copy.find_all('div', 'bbCodeQuote'):
                quote.decompose()
        if remove_tags:
            # Temporarily mark <br /> tags
            for newline in text_copy.find_all('br'):
                newline.replace_with('\\NEWLINE')

            # Strip all tags from text
            text = ''
            for string in text_copy.stripped_strings:
                text = text + string.strip() + ' '

            # Split text on NEWLINES, strip extra whitespace, and return
            result = ''
            for line in text.split('\\NEWLINE'):
                result = result + line.strip() + '\n'
            return result
        return str(text_copy)

    def get_lines(self, remove_quotes=True, remove_tags=True):
        """Return the text body line-by-line.

        Args:
            remove_quotes (bool): Remove BB Code quote blocks if True.
            remove_tags (bool): Removes all html tags if True.

        Return:
            str[] Returns a list of strings.

        """
        text = self.get_text(remove_quotes, remove_tags)
        if remove_tags:
            # Remove the newline at EOF
            return text.split('\n')[:-1]
        return text.split('<br/>')
