
import urllib.request
import re
import gzip


q=re.compile("domainSelect\(\"([A-Za-z]+)\.bit\"\)")
expired=[]


for pnumber in range(50,60):
    pagestring="https://dotbit.me/get_expired_domains.php?s=date&w=desc&p={}&_=1546548861087".format(pnumber)
    print ("Retreiving: " + pagestring)    
    page = urllib.request.Request(pagestring)
    page.add_header("Host", "dotbit.me")
    page.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0")
    page.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    page.add_header("Accept-Language", "sv,en-US;q=0.7,en;q=0.3")
    page.add_header("Accept-Encoding",  "gzip, deflate, br")
    page.add_header("DNT", "1")
    page.add_header("Connection", "keep-alive")
    page.add_header("Cookie", "dotbit-session=m3mg8gpst7kll0r470pd4of1r2")
    page.add_header("Upgrade-Insecure-Requests", "1")
    page.add_header("Cache-Control",  "max-age=0" )   
    readable = gzip.decompress(urllib.request.urlopen(page).read())

    for link in q.findall(readable.decode("utf8")): 
        expired.append(link)

thelist = open("/home/magnus/dotbitexpired.txt", "w")
for dom in expired:
    print (dom  + ".bit")
    thelist.write(dom + ".bit\n")

thelist.close
          