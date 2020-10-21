# IMDb Scrapper By Muhammad Hanan Asghar
# IMDb Scrapper
# Muhammad Hanan Asghar
import requests
from bs4 import BeautifulSoup as Soup
print("[*] IMDb Scrapper By Muhammad Hanan Asghar [*]")
print("")
print("1. Search Movie")
print("2. Top Chart")
choice = int(input("> "))
if choice ==1:
  url = input("Enter Movie Name : ")
  URL = f"https://www.imdb.com/find?q={url}"
  r = requests.get(URL).content
  soup = Soup(r,"html.parser")
  results = soup.find_all("td",class_="result_text")
  number = 0
  print("")
  print("[*] {} Results Found".format(len(results)))
  data_links = []
  for i in results:
    number += 1
    print(str(number)+" "+i.find("a").text)
    data_links.append((number,i.find("a").text,"https://www.imdb.com/"+i.find("a").get("href")+"?ref_=fn_al_tt_1"))
  option = int(input("[+] Enter Choice Number : "))
  for i in data_links:
    if option == i[0]:
      r2 = requests.get(i[-1]).content
      soup2 = Soup(r2,"html.parser")
      try:
        text = soup2.find_all("div",class_="summary_text")[0].text.strip()
        text = text.replace("See full summary\xa0»","").strip()
        text = text.replace("Add a Plot\xa0»","").strip()
        links = soup2.find_all("div",class_="credit_summary_item")
        images = soup2.find_all("div",class_="mediastrip")
        cast_table = soup2.find_all("table",class_="cast_list")
        print("")
        print("Summary:")
        if text == "":
          print("No Summary Found!")
        else:
          print(text)
        if links == []:
          print("No Stars Found!")
        else:
          for i in links:
            i = i.text.replace("See full cast & crew\xa0»","")
            print(i)
        print(" ")
        print("Images:")
        if images[0].find_all("img") == []:
          print("No Images Found!")
        else:
          for img in images[0].find_all("img"):
            print(img.get("loadlate"))
        print("")
        print("Cast:")
        if cast_table == []:
          print("No Cast Found!")
        else:
          for i in cast_table[0].find_all("img"):
            if str(i) == "None":
              pass
            else:
              print(i.get("title"))
      except:
        print("No Result Found!")
    else:
      pass
elif choice == 2:
  soup = Soup(requests.get("https://www.imdb.com/chart/top").content,"html.parser")
  topchart = []
  for i in soup.find_all("td"):
    if str(i.find("a")) == "None":
      pass
    else:
      if "<img" in str(i.find("a")):
        pass
      else:
        topchart.append(i.find("a").text)
  ratings = []
  for i in soup.find_all("td"):
    if str(i.find("strong")) == "None":
      pass
    else:
      ratings.append(i.find("strong").get("title"))
  print("")
  print("Top Movies: ")
  for x,y in zip(topchart,ratings):
    print(x,"-",y)
else:
  print("Please Enter Correct Choice.Closing Program!")
