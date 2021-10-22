
from bs4 import BeautifulSoup
download_url = []

def download_file(url):
    local_filename = 'love/'
    #
    #NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush() #commented by recommendation from J.F.Sebastian
    return local_filename

for x in range(31,40):
    response = requests.get('http://www.hdwallpapernew.in/romantic-couple/?galleryPage=%s'% x)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('dt', {'class': 'gallery-icon'}):
        #print link.contents
        thumburl = link.find('img')['src']
        # print thumburl
        full_imgurl = thumburl.replace('-270x170', '')
        print (full_imgurl)
        print ('Download Started :' + full_imgurl)
        download_file(full_imgurl)
        print ('Download Completed : ')
