"""Page class.

Sample HTML structure of a NUF page:

```html
<html>
  <head>
    <title>...</title>
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
        title: (bs4.Tag) The title of the page.

    """

    def __init__(self, html):
        """Construct a page given html source code."""
        self.soup = BeautifulSoup(html, 'html5lib')
        self.title = self.soup.title
        self.isLoggedIn = bool(self.soup.find('ul', class_='visitorTabs'))
