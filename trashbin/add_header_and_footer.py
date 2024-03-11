import os
filenamelist = ['life','life_acad','life_h+t','rsch','TBD',]
for filename in filenamelist:
    
    infile01 = open(filename+'.html','r', encoding='utf-8')
    infile02 = open('website_header.html', 'r', encoding='utf-8')
    infile03 = open('website_footer.html', 'r', encoding='utf-8')
    outfile1 = open(filename+'_temp.html','w', encoding='utf-8')
    
    # for sen in infile01:
    #     # TypeError: a bytes-like object is required, not 'str'
    #     strg = sen[:-2]
    #     ReplacementStarted = False
    
    #     if ReplacementStarted==False:
    #         outfile1.write(sen)
            
    #     if strg == :
    #         ReplacementStarted = True
    
    #         for sen2 in infile02:
    #             outfile1.write(sen2)
                
                
    #     elif ReplacementStarted==True:
    #         ReplacementEnded = False
            
    #         if strg == :
    #             ReplacementEnded = True
                
    #         if ReplacementEnded==True:
    #             outfile1.write(sen)
    
    lines1 = infile01.readlines()
    lines2 = infile02.readlines()
    # lines1 = [byte.decode('utf-8') for byte in lines1]
    # lines2 = [byte.decode('utf-8') for byte in lines2]
    print(lines1[31], type(lines1[31]))
    line1 = '<!-- [To Python] Replace header html from here      -->' + '\n'
    line2 = '<!-- [To Python] Replacement of header html ends here -->' + '\n'
    print(line1,      type(line1))
    index1 = lines1.index(line1)
    index2 = lines2.index(line2)
    
    infile01.close()
    infile02.close()
    infile03.close()
    outfile1.close()
    print('Header done...')
    
    infile01 = open(filename+'.html','rb')
    infile02 = open('website_header.html', 'rb')
    infile03 = open('website_footer.html', 'rb')
    outfile1 = open(filename+'_temp.html','wb')
    for sen in infile01:
        # TypeError: a bytes-like object is required, not 'str'
        strg = sen.decode('utf-8')[:-2]
        outfile1.write(sen)
        if strg == '<!-- [To Python] Replace footer html from here      -->':
            for sen3 in infile03:
                outfile1.write(sen3)
            break
                
    print('Footer done...')
    
    infile01.close()
    infile02.close()
    infile03.close()
    outfile1.close()
    
    os.remove(filename+'.html')
    os.rename(filename+'_temp.html', filename+'.html')
    print('Done: '+filename)