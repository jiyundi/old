infile01 = open('index.html','rb')
infile02 = open('website_header.html', 'rb')
outfile1 = open('index_temp.html','wb')

for sen in infile01:
    # TypeError: a bytes-like object is required, not 'str'
    strg = sen.decode('utf-8')[:-2]
    if strg == '<!-- [To Python] Go add website header html here -->':
        
        for sen2 in infile02:
            outfile1.write(sen2)
            
    else:
        outfile1.write(sen)
    
infile01.close()
infile02.close()
outfile1.close()

import os
os.remove('index.html')
os.rename('index_temp.html', 'index.html')
print('Done.')