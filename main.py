from bs4 import BeautifulSoup
import requests

site=requests.get("https://internshala.com/internships/work-from-home-civil,electrical,electronics,information%20technology,mechanical-jobs/part_time-true")
soup=BeautifulSoup(site.text,'lxml')
intern_detail=[]
internship=soup.findAll('div',class_="container-fluid individual_internship")
for i in internship:
    comany =i.find('div',class_="company")

    detail = i.find('div', class_="individual_internship_details")
    btn = i.find('a', class_="view_detail_button")
    data={
        "internship":comany.select('a')[0].text.strip(),
        "company":comany.select('a')[1].text.strip(),
        "location":detail.select('a')[0].text.strip(),
        "start_date":detail.select('span')[2].text.strip(),
        "duration":detail.select('div.item_body')[1].text.strip(),
        "stipend":detail.select('span')[6].text.strip(),
        "apply_by":detail.select('div.item_body')[3].text.strip(),
        "apply_link":"https://internshala.com"+btn.get('href').strip(),
    }
    intern_detail.append(data)
for i in intern_detail:
    print(i)

