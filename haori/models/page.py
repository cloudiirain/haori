"""Page class."""

__author__ = 'cloudiirain'
__version__ = '0.0.1'
__status__ = 'development'

from bs4 import BeautifulSoup


class Page(object):
    """Represents an HTML page on the NUF forum.

    Attributes:
        soup: (bs4.BeautifulSoup) The BeautifulSoup representation of the page.
        title: (unicode) The title of the page.
        base_url: (unicode) The base url of the NUF site.
        url: (unicode) The url of the current page, or else None.
        next_url: (unicode) The url of the next page in sequence, or else None.
        prev_url: (unicode) The url of the prev page in sequence, or else None.

    """

    def __init__(self, html):
        """Construct a NUF page given html source code."""
        self.soup = BeautifulSoup(html, 'html5lib')
        self.title = self.soup.title.string
        self.base_url = self.soup.base['href']
        try:
            self.url = self.soup.find('link', rel='canonical')['href']
            if self.base_url not in self.url:
                # If the url is a relative url, convert to an absolute url
                self.url = self.base_url + self.url
        except:
            self.url = None
        try:
            self.next_url = self.soup.find('link', rel='next')['href']
            if self.base_url not in self.next_url:
                self.next_url = self.base_url + self.next_url
        except:
            self.next_url = None
        try:
            self.prev_url = self.soup.find('link', rel='prev')['href']
            if self.base_url not in self.prev_url:
                self.prev_url = self.base_url + self.prev_url
        except:
            self.prev_url = None

    def __str__(self):
        """Print string representation of the page."""
        return str(self.soup)

    def isUserLoggedIn(self):
        """Check if the bot is logged in.

        Return:
            (bool) True if a user is logged in on this page.

        """
        return bool(self.soup.find('ul', class_='visitorTabs'))

    def getUser(self):
        """Return the logged in user.

        Return:
            (unicode) The logged in username, or else None.

        """
        if self.isUserLoggedIn():
            return self.soup.select(
                '#header .visitorTabs .accountUsername'
            ).string
        return None
