"""Post class.

Sample HTML structure of a NUF post:

```html
<li id="post-360506" class="message" data-author="DCLXVI">
  <div class="messageUserInfo">...</div>
  <div class="messageInfo primaryContent">
    <div class="messageContent">
      <article>
        <blockquote class="messageText SelectQuoteContainer ugc baseHtml">
          {{ POST CONTENT }}
          <div class="messageTextEndMarker">...</div>
        </blockquote>
      </article>
    </div>
    <div class="messageMeta ToggleTriggerAnchor">...</div>
    <div id="likes-post-360506">...</div>
  </div>
</li>
```

Sample HTML structure of a BBCode [quote][/quote] block:

```html
<div class="bbCodeBlock bbCodeQuote" data-author="nrvn qsr">
  <aside>
    <div class="attribution type">
      nrvn qsr said:
    </div>
    <blockquote class="quoteContainer">
      <div class="quote">
        <span style="font-size: 22px">
          {{ QUOTE CONTENT }}
        </span>
      </div>
      <div class="quoteExpand">
        Click to expand...
      </div>
    </blockquote>
  </aside>
</div>
```

"""

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
        """Construct a single post given a BeautifulSoup <li> Tag object.

        Args:
            soup (bs4.Tag): BeautifulSoup Tag object.

        """
        self.id = soup['id']
        self.author = soup['data-author']
        self.text = soup.find('blockquote', 'messageText')

    def __str__(self):
        """Print string representation of the post."""
        return self.id

    def get_id(self):
        """Print the numeric integer of the id of this post."""
        return int(self.id.split('-')[1])

    def get_text(self, remove_quotes=True, remove_tags=False):
        """Print the text body of the post.

        Args:
            remove_quotes (bool): Remove BBCode [quote][/quote] blocks.
            remove_tags (bool): Removes all html tags and print only text.

        Return:
            (str) The post text.

        """
        # Deep copy is needed to prevent modifying self.text
        text_copy = copy.copy(self.text)

        # Remove <div class="messageTextEndMarker">...</div>
        text_copy.find('div', 'messageTextEndMarker').decompose()

        if remove_quotes:
            # Remove all incidences of <div class="bbCodeQuote">...</div>
            for quote in text_copy.find_all('div', 'bbCodeQuote'):
                quote.decompose()

        if remove_tags:
            # Insert a newline after </div> tags
            for div in text_copy.find_all('div'):
                div.insert_after('\n')
            return text_copy.get_text().strip()

        # Print HTML with extra whitespace stripped
        text_contents = ''.join(str(i).strip() for i in text_copy.contents)
        return text_contents.replace('\n', '').replace('\t', '')

    def get_lines(self, remove_quotes=True):
        """Return the text body line-by-line with HTML stripped.

        Args:
            remove_quotes (bool): Remove BB Code quote blocks if True.

        Return:
            str[] Returns a list of strings.

        """
        text = self.get_text(remove_quotes, remove_tags=True)
        return text.split('\n')
