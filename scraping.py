from lxml import html
import requests
import simplejson as json

page = requests.get('https://www.xataka.com/categoria/inteligencia-artificial')
tree = html.fromstring(page.content)


articles = tree.xpath('//a/text()')
res_titles = [x for x in articles if "inteligencia" in x]
dict_titles = { i : 2 for i in res_titles}
new_json_data = json.dumps(dict_titles, indent=4)

print(new_json_data)
#print('articles: ', res_titles)