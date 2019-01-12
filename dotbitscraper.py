import urllib.request
import re
import gzip
import time

# compile regex to find .bit domain names, create regex object
q = re.compile("domainSelect\(\"([A-Za-z]+)\.bit\"\)")
expired = []


for pnumber in range(60, 63):
    pagestring = "https://dotbit.me/get_expired_domains.php?s=date&w=desc&p={}&_=1546548861087".format(pnumber)
    print ("Retreiving: " + pagestring)
    page = urllib.request.Request(pagestring)
# add headers from Firefox to trick .bit registration site
    page.add_header("Host", "dotbit.me")
    page.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0")
    page.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    page.add_header("Accept-Language", "sv,en-US;q=0.7,en;q=0.3")
    page.add_header("Accept-Encoding",  "gzip, deflate, br")
    page.add_header("DNT", "1")
    page.add_header("Connection", "keep-alive")
    page.add_header("Upgrade-Insecure-Requests", "1")
    page.add_header("Cache-Control",  "max-age=0" )
    readable = gzip.decompress(urllib.request.urlopen(page).read())

# run the regex on decoded page and append all domains
    for link in q.findall(readable.decode("utf8")):
        expired.append(link)
# and throttle the requests
    time.sleep(2)

# write the list to a file and console
thelist = open("/home/magnus/dotbitexpired.txt", "w")
for dom in expired:
    print (dom + ".bit")
    thelist.write(dom + ".bit\n")
thelist.close
