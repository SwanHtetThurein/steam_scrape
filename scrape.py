import requests
import lxml.html

html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content)

#Extract the divs that have an id of "tab_newreleases_content" from the explore/new page 
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

#Extract Titles(item_name) and Price(discount_final_price) under new_releases  
titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')


tags = []#Declare a list of tags 
#Iterate over the list of extracted tags 
for tag in new_releases.xpath('.//div[@class="tab_item_top_tags"]'):
    tags.append(tag.text_content())#Extract the text from the tags using text_content method 

tags = [tag.split(', ') for tag in tags]#Separate each tag with ',' so that each tag is a separate element 

#Extract item_details under new_releases 
platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []


for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)

output = []
for info in zip(titles, prices, tags, total_platforms):
    resp = {}
    resp['title'] = info[0]
    resp['price'] = info[1]
    resp['tags'] = info[2]
    resp['platforms'] = info[3]
    output.append(resp)

print(output)
