# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 17:03:24 2016

@author: Andris Piebalgs
"""

# ----------------------------------------------------------------------------
# HEADERS
# ----------------------------------------------------------------------------
import sys
import requests
import json
from helpTool import printToCSV

sys.path.append('toolbox');

def scienceDirectSearch(search_terms,numRes,APIKEY, saveDir):
    
    # ----------------------------------------------------------------------------
    # INPUTS
    # ----------------------------------------------------------------------------
    
    MY_API_KEY = APIKEY;
    count = numRes; # results returned
    
    #Other useful search macros
    # abs() for abstract
    # tak() for abstract, title and keywords
    # authors()
    
    # ----------------------------------------------------------------------------
    # ARTICLE SEARCH/ABSTRACT RETRIEVAL
    # ----------------------------------------------------------------------------

    # API inputs
    search_url = 'http://api.elsevier.com/content/search/scidir?count='+ str(count) + '&query=' + search_terms;
    headers = {'Accept':'application/json', 'X-ELS-APIKey': MY_API_KEY}
    
    # API request
    page_request = requests.get(search_url, headers=headers)
    print(page_request.status_code)
    
    # Unpack json
    page = json.loads(page_request.content.decode("utf-8"))
    store = page['search-results']['entry'];
    
    # Cycle through each paper, retrieve information
    it = -1;
    title = []; authors = []; date = []; link = []; eid = []; abstract = [];
    for paper in store:
        
        try: 
            
            it += 1;
            titleCur   = paper['dc:title'];
            authorsCur = paper['authors'];
            dateCur    = paper['prism:coverDisplayDate']
            linkCur    = paper['link'][0]['@href'];
            eidCur     = paper['eid']
                    
            title.append(titleCur)
            authors.append(authorsCur)
            date.append(dateCur)
            link.append(linkCur)
            eid.append(eidCur) 
            
            # Retrieve abstract
            abstract_request = requests.get(linkCur, headers=headers);
            abstractjson = json.loads(abstract_request.content.decode("utf-8"))
            
            try:            
                abstract.append(abstractjson['full-text-retrieval-response']['coredata']['dc:description'])
            
            except:
                abstract.append('N/A');
             
        except:
            
            # Specify where it failed
            print('Failed at paper # ' + str(it))
            
            continue;
            
    # ----------------------------------------------------------------------------
    # SAVING RESULTS
    # ----------------------------------------------------------------------------
    
    printToCSV(saveDir + '/science_direct_'+search_terms+'.csv',['title','abstract','date','authors','link','eid'],
               title, abstract,date,authors,link,eid)
               
    return title, abstract,date,authors,link,eid
               
               
               
                   
                   
    
    
    
