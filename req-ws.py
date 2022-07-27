import requests
import re


#put the url below
url = 'http://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d=1394-01-14'

#pattern of our RegEx
date_extract_pattern = "([0-9]{4})-(1[0-2]|0[1-9])-(3[01]|[12][0-9]|0[1-9])$"
    


j = '01'
z = '01'

for i in range(1395 , 1402):
    
    s = re.sub(date_extract_pattern , str(i)+'-'+(j)+'-' + (z) , url)
    
    r = requests.get(s, allow_redirects=True)

    


    
    for j in range(1,13):
    
    
        if j<10:
            j = '0' + str(j)
            s = re.sub(date_extract_pattern , str(i)+'-'+(j)+'-' + (z) , url)
            
            r = requests.get(s, allow_redirects=True)

            open(str(i)+'-'+(j)+'-' + (z) + '.csv', 'wb').write(r.content)
        else:
            j = str(j)
            s = re.sub(date_extract_pattern , str(i)+'-'+(j)+'-' + (z) , url)
            
            r = requests.get(s, allow_redirects=True)

            open(str(i)+'-'+(j)+'-' + (z) + '.csv', 'wb').write(r.content)

        for z in range(1,32):
            if z<10:
                 z = '0' + str(z)
                 s = re.sub(date_extract_pattern , str(i)+'-'+(j)+'-' + (z) , url)
            
                 r = requests.get(s, allow_redirects=True)

                 open(str(i)+'-'+(j)+'-' + (z) + '.csv', 'wb').write(r.content)
            else:
                 z = str(z)
                 s = re.sub(date_extract_pattern , str(i)+'-'+(j)+'-' + (z) , url)
            
                 r = requests.get(s, allow_redirects=True)

                 open(str(i)+'-'+(j)+'-' + (z) + '.csv', 'wb').write(r.content)
        
            
    





