#Original script made by https://twitter.com/s_hiburizu
#The King of Fighter XIII CSV to wikitext
#For use with MoveData and AttackData at DreamCancel, or any other wiki with similar syntax
#First row of your CSV should have headers that are part of 'n' list, and the last row of your data should be indicated with 'END DATA' in the first column.
#Add section headers to the first column and denote them in c to have headers inserted at your desired points on the CSV.
#usage: kofwiiwiki.py [csv] [name]
#example usage: python kofxiiwiki.py yourfile.csv King

import csv,sys

def wikitext(f,l,s):
    if s != '':
        f.write("%s%s\n" % (l,s))
    else:
        pass

n = ['Name','Damage','Startup','Active','Recovery','Hit Adv','Block Adv.'] #header rows
e = 'END DATA' #end data keyword
c = ['Normals','DM','SDM/NeoMAX']
f = open("kofxii.txt","w+",encoding='utf-8')
curChar = sys.argv[2]
f.write('{{TOClimit|2}}\n\n')
with open(sys.argv[1],'r',encoding='utf-8') as file:
    for i in csv.DictReader(file):
        d = dict(i)
        if d['Name'] == e: #end keyword
            break
        elif d['Name'] in c: #Check for Headers
            f.write('== %s ==\n\n' % d['Name'])
        else:
            f.write('=====<font style="visibility:hidden; float:right">%s</font>=====\n' % d['Name'])
            f.write('{{MoveData\n')
            f.write('|image=KOFIII_%s_%s.png\n' % (curChar,d['Name'].replace('>','')))
            f.write('|caption=\n')
            f.write('|name=\n')
            f.write('|input=%s\n' % d['Name'])
            f.write('|data=\n')
            f.write('{{AttackData-KOFXIII\n')
            #wikitext(f,'|Damage=', d['Damage'])
            wikitext(f,'|Startup=', d['Startup'])
            wikitext(f,'|Active=', d['Active'])
            wikitext(f,'|Recovery=', d['Recovery'])
            wikitext(f,'|Adv. Hit=', d['Hit Adv'])
            wikitext(f,'|On Block=', d['Block Adv.'])
            f.write('}}\n}}\n\n')
f.write('[[Category:The King of Fighters XIII]]\n{{The King of Fighters XIII}}')
f.close()
