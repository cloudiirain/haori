"""Testing."""

import re
import sys
from haori.models.bot import Bot
from haori.models.post import Post

dictionary = {}

haori = Bot('dice')
haori.login(sys.argv[1])
page = haori.get('https://forum.novelupdates.com/threads/word-association.3094')
while(page.next_url):
    posts = page.soup.find('ol', class_='messageList')
    for post in posts.children:
        if post.name == u'li':
            p = Post(post)
            text = p.get_text(remove_tags=True)
            words = text.lower().strip().replace('\n', ' ').split(' ')
            if len(words) == 1:
                word = re.sub('[^a-zA-Z]', '', words[0])
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    page = haori.get(page.next_url)

for key in sorted(dictionary.iterkeys()):
    print(key + '\t' + str(dictionary[key]))
