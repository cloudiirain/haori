"""Testing."""

from haori.models.bot import Bot

haori = Bot('haori')
page = haori.get('https://forum.novelupdates.com/threads/word-chain-pokemon-edition.3880/')

print(str(page.soup))
