from lxml import html

import requests

page = requests.get('http://www.litecoinrate.co.uk')

tree = html.fromstring(page.content)

price = tree.xpath('//*[@id="tablepress-1"]/tbody/tr[1]/td/strong/text()')

print price[0]