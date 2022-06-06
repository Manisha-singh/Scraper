import requests
from bs4 import BeautifulSoup
from csv import writer

main_url="https://clutch.co"
url="https://clutch.co/directory/mobile-application-developers"

r=requests.get(url)
soup=BeautifulSoup(r.content, 'html.parser')
anchors=soup.select(".company_info a")
all_links=set()

for link in anchors:
      new_link=main_url+link.get('href')
      all_links.add(new_link)

with open('clutch.csv', 'w', encoding='utf8', newline='') as f:     
      thewriter=writer(f)
      header=['Company', 'Website', 'Location', 'Contact', 'Rating', 'Review', 'Hourly Rate', 'Min Project Size', 'Employee Size'] 
      thewriter.writerow(header)
      for link in all_links:
            req=requests.get(link)
            htmlContent2=req.content
            soup2=BeautifulSoup(htmlContent2, 'html.parser')

            Company=soup2.find("h1", class_="header-company--title").find("a",class_="website-link__item").text.replace('\n', '').replace(' ','')
            Websites=soup2.find("a", class_="web_icon website-link__item").get('href').rsplit('?', 1)[0]
            Address=soup2.find("span", class_="locality").text.replace('\n', '')
            Contacts=soup2.find("a", class_="contact phone_icon").text.replace('\n', '')
            Rating=soup2.find("span",class_="rating sg-rating__number").text.replace('\n', '')
            ReviewCount=soup2.find("a", class_="reviews-link sg-rating__reviews").text.replace('\n', '').replace('Â','')
            Hourly_Count=soup2.find("div", class_="list-item custom_popover").text.replace('\n', '')
            MinProjectSize=soup2.find("div", class_="list-item custom_popover custom_popover__left").text.replace('\n', '')    
            EmployeeSize=soup2.find_all("div", class_="list-item custom_popover")[1].find('span').string.replace('\n', '').replace(' ','')
           
                  
            info=[Company, Websites, Address, Contacts,Rating, ReviewCount, Hourly_Count, MinProjectSize, EmployeeSize ]
            thewriter.writerow(info)
      
      
