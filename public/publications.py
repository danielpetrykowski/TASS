import scholarly
from bs4 import BeautifulSoup
import requests
BASE = 'https://scholar.google.com'
pathPatentsAuthors = "patent_authors.txt"


def elementExist(tab, element):
    for e in tab:
        if(e==element):
            return 1
    return 0

def scraperName():
    names=[]
    f = open(pathPatentsAuthors, "rt", encoding='utf-8')
    text = f.read()
    
    idStart = text.find("'inventor_name': '")
    while(idStart!=-1):
        idStart = idStart+18
        idEnd = text.find("'",idStart)
        name = text[idStart:idEnd]
        if(elementExist(names,name)==0):
            names.append(name)
        idStart = text.find("'inventor_name': '", idEnd)
    return names



if __name__ == '__main__':
    
    result = []
    correct = []
    wrong = []
    names = scraperName()
    numberNames = len(names)
    processedNames = 0
    id = -1
    
    for i in range(1601, 16000):

        try:
            authorMeta = next(scholarly.search_author(names[i]))
            req = requests.get('%s/citations?hl=pl&user=%s' % (BASE, authorMeta.id))
            soup = BeautifulSoup(req.content, 'html.parser')
            article = soup.find_all('tr', {'class': 'gsc_a_tr'})
            print("Found results for user %s" % names[i])
            
            id = id + 1
            result.append([])
            for a in article:
                try:
                    authorsDiv = a.find('td', {'class': 'gsc_a_t'}).find('div')
                    authorsLine = authorsDiv.text.strip()
                    authorTab = authorsLine.split(",")
                    for i in range(len(authorTab)):
                        a = authorTab[i].strip()
                        if(elementExist(result[id], a)==0):
                            result[id].append(a)
            
                except Exception as e:
                    print(e)        
            
            correct.append(authorMeta.name)
            print(result[id])
            
        except Exception as e:
            print(e)
            wrong.append(names[i])
            print("Error for user %s" % names[i])
            

        processedNames = processedNames + 1
        print("progress:", (processedNames * 100) / numberNames, "%")
        
        
        
    with open("coperations_authors6.txt", "w+", encoding='utf-8') as f:
            for i in range(len(result)):
                f.write("{}:{}\n".format(correct[i],result[i]))
    with open("wrong_coperations_authors6.txt", "w+", encoding='utf-8') as f:
            for a in wrong:
                f.write("%s\n" % a)      
    
    
    


