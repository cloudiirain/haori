"""Bot class.

This class represents a bot object that can be utilized programatically.

Sample HTML structure of a login page:

```html
<div id="content" class="login">
<div class="pageWidth">
<div class="pageContent">
  <div class="breadBoxTop">...</div>
  <div class="titleBar">...</div>
  <form action="login/login" method="post" id="pageLogin" class="xenForm">
    <h2 class="textHeading">Log in or Sign up</h2>
    <dl class="ctrlUnit">
      <dt><label for="ctrl_pageLogin_login">...</label></dt>
      <dd><input type="text" name="login" id="ctrl_pageLogin_login"></dd>
    </dl>
    <dl class="ctrlUnit">
      <dt><label for="ctrl_pageLogin_password">...</label></dt>
      <dd>
        <input type="password" name="password" id="ctrl_pageLogin_password">
        <div><a href="lost-password/">Forgot your password?</a></div>
      </dd>
    </dl>
    <dl class="ctrlUnit submitUnit">
      <dt></dt>
      <dd>
        <input type="submit" class="button primary" value="Log in">
        <label class="rememberPassword">
          <input type="checkbox" name="remember" id="ctrl_pageLogin_remember">
          Stay logged in
        </label>
      </dd>
    </dl>
    <input type="hidden" name="cookie_check" value="1">
    <input type="hidden" name="_xfToken" value="">
    <input type="hidden" name="redirect" value="...">
  </form>
  <script>...</script>
  <div class="breadBoxBottom">...</div>
</div>
</div>
</div>
```

"""

__author__ = 'cloudiirain'
__version__ = '0.0.1'
__status__ = 'development'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from haori.models.page import Page

LOGIN_URL = 'http://forum.novelupdates.com/login'
LOGOUT_URL = 'https://forum.novelupdates.com/logout'


class Bot(object):
    """Represents a bot that can interact with NUF.

    Attributes:
        username: (unicode) The username for the bot (default: guest).
        driver:

    """

    def __init__(self, username='guest'):
        """Construct a bot object."""
        self.username = username
        c_opt = Options()
        c_opt.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path='chromedriver',
                                       chrome_options=c_opt)

    def __str__(self):
        """Print string representation of the bot."""
        return self.username

    def get(self, url):
        """Send a GET request a return a Page object."""
        self.driver.get(url)
        return Page(self.driver.page_source)

    def login(self, password):
        """Log the bot into NUF."""
        # self.logout()
        self.driver.get(LOGIN_URL)
        usr_input = self.driver.find_element_by_id('ctrl_pageLogin_login')
        pswd_input = self.driver.find_element_by_id('ctrl_pageLogin_password')
        submit = self.driver.find_element_by_css_selector(
            '#pageLogin input[type="submit"]'
        )
        usr_input.send_keys(self.username)
        pswd_input.send_keys(password)
        submit.click()

    def logout(self):
        """Log the bot out of NUF."""
        self.driver.get(LOGOUT_URL)
        return self.driver.page_source

    def post(self):
        """Post to a thread."""
        pass
