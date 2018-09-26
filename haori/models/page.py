"""Page class.

Sample HTML structure of a NUF page:

```html
<html>
  <head>
    <title>...</title>
    <link rel="canonical" href="..." />
    <link rel="prev" href="..." />
    <link rel="next" href="..." />
  </head>
  <body>
    <div id="loginBar">
      <div class="pageWidth">
        <div class="pageContent">
          <h3 id="loginBarHandle">...</h3>
          <span class="helper"></span>
          <form id="login">...</form>
        </div>
      </div>
    </div>
    <div class="topHelper"></div>
    <div id="headerMover">
      <div id="headerProxy"></div>
      <div id="content">
        <div class="pageWidth">
          <div class="pageContent">
            <!-- main content area -->
            <div class="mainContainer">...</div>
            <!-- sidebar -->
            <aside>...</aside>
            <div class="breadBoxBottom">...</div>
          </div>
        </div>
      </div>
      <header>
        <div id="header">
          <div id="logoBlock">...</div>
          <div id="navigation" class="pageWidth widthSearch">
            <div class="pageContent">
              <nav>
                <div class="navTabs">
                  <ul class="publicTabs">...</ul>
                  <ul class="visitorTabs">
                    <li class="navTab account Popup PopupControl">
                      <a class="navLink accountPopup" rel="Menu">
                        <strong class="accountUsername">
                          <i class="fa fa-chevron-down">...</i>
                          " lychee"
                        </strong>
                        <strong id="VisitorExtraMenu_Counter">...</strong>
                      </a>
                    </li>
                    <li class="navTab inbox Popup PopupControl"></li>
                    <li class="navTab alerts Popup PopupControl"></li>
                  </ul>
                </div>
                <span class="helper"></span>
              </nav>
            </div>
          </div>
          <div id="searchBar" class="pageWidth">...</div>
        </div>
      </header>
    </div>
    <footer>...</footer>
    <script>...</script>
  </body>
</html>
```

The `loginBar` div is only shown when not logged in.

The 'visitorTabs' ul is only shown when logged in

"""

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
