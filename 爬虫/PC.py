import requests
from lxml import html
#导入request
target_url= "https://www.tiobe.com/tiobe-index/"
response=requests.get(target_url)
#print(response.text)
document=html.fromstring(response.text)
doc1_list=document.xpath("//table[@id='top20']/thead/tr/th/text()")
print(doc1_list)
print(len(document.xpath("//table")))
doc2_list=document.xpath("//table[@id='top20']/tbody/tr")
for i in doc2_list:
    doc3_list=i.xpath("./td/text()")
    print(doc3_list)