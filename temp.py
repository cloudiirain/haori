"""Testing."""

from haori.models.bot import Bot

haori = Bot('haori')
page = haori.get('https://forum.novelupdates.com/threads/word-chain-pokemon-edition.3880/')

print(page.title)
print(page.base_url)
print(page.url)
print(page.next_url)
print(page.prev_url)
