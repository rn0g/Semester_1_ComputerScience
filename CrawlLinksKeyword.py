from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import time
import re

leave = True
stay = True
while stay == True:
    while leave:
        enter_site = input("[*] Type a domain [http://example.com]: ")

        try:
            html = urlopen(enter_site)
            soup = BeautifulSoup(html, "html.parser")
            leave = False
        except URLError as u:

            print("\nCould not access URL. Try again and check the domain.")
            leave = True

        except HTTPError as u:
            print("\nCould not find page. Try again.")    
            leave = True
        
        except ValueError as u:
            print("\nURL unknown. Please try again and follow the format.")
            leave = True
        
    existing_links = set()

    if leave == False:

        
        keyword = input("[*] Define a keyword to look for links at %s :"%enter_site)
        print("Here's a list of all the links containing %s:" %keyword)
        print("\n")
        for i in soup.select_one("body"):
            for i in soup.findAll("a", href=re.compile("%s" %keyword)):
                if "href" in i.attrs:
                    new_link = i.attrs["href"]
                    if new_link not in existing_links:
                        print("[*] Found:",new_link)
                        existing_links.add(new_link)
                        

        if len(soup.findAll("a", href=re.compile("%s" %keyword))) == 0:
            print("No link was found.")

        if len(soup.findAll("a", href=re.compile("%s" %keyword))) > 0:
            print("\n[*] Count: ", len(existing_links))

        leave_or_nah = input("Leave? y/n")
        if leave_or_nah == 'n':

            leave = True
            print("restarting...")
            while leave:
                enter_site = input("[*] Type a domain [http://example.com]: ")

                try:
                    html = urlopen(enter_site)
                    soup = BeautifulSoup(html, "html.parser")
                    leave = False
                except URLError as u:

                    print("\nCould not access URL. Try again and check the domain.")
                    leave = True

                except HTTPError as u:
                    print("\nCould not find page. Try again.")    
                    leave = True
                
                except ValueError as u:
                    print("\nURL unknown. Please try again and follow the format.")
                    leave = True
        else:
            print("bye")
            stay = False
        
        time.sleep(2)

        
        


                
        




