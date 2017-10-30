# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 17:03:24 2016

@author: Andris Piebalgs

INPUTS
    - search_terms
    - numRes: number of results to be returned
    - saveDir: name of folder to save CSV files

OUTPUTS
    - title,authors,date,abstract
    - saved csv file under the name 'saveDir/Pubmed_($search_terms)'

"""

# ----------------------------------------------------------------------------
# HEADERS
# ----------------------------------------------------------------------------

import requests
import json
from helpTool import printToCSV
import untangle


def pubmedSearch(search_terms,numRes, saveDir):
    
    # ----------------------------------------------------------------------------
    # INPUTS
    # ----------------------------------------------------------------------------
    
    count = numRes;
    
    # Finding ID codes
    search_url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax='+str(count)+'&sort=relevance&term='+search_terms;
    page_request = requests.get(search_url);
    
    print(page_request.status_code)
    
    page = json.loads(page_request.content.decode("utf-8"));
    idList = page["esearchresult"]["idlist"]
    
    # Retrieving information for each id code
    fetch_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id='+','.join(idList);
    
    fetch_request = requests.get(fetch_url);
    print(fetch_request.status_code)
    
    obj = untangle.parse(fetch_url)
    
    titleStore      = [];
    authorsStore    = [];
    abstractStore   = [];
    IDStore         = [];
    dateStore       = [];
    
    try:
        L1 = len(obj.PubmedArticleSet.PubmedArticle);
        
    except:
        L1 = 1;
    
    
    for it in range(L1):
    
        # Retrieve Article    
        article = obj.PubmedArticleSet.PubmedArticle[it].MedlineCitation.Article
        
        # Retrieve Title    
        title = article.ArticleTitle.cdata;
        titleStore.append(title);
        
        # Retrieve Abstract
        try:
            abstract = article.Abstract.AbstractText;
            text = [];
        
            try:    
                for inner in range(len(abstract)-1):
                    text.append(abstract[inner].cdata);
                   
                abstractStore.append(' '.join(text))                   
                   
            except:
                text = abstract.cdata;
                abstractStore.append(text);
        
        except:
            
            abstractStore.append('N/A')
        
        # Retrieve Date
    
        date = article.Journal.JournalIssue.PubDate
        try:
            dateStore.append(date.Year.cdata)
        
        except:
            dateStore.append('Error Retrieving')
        
        
        # Retrieve Authors
        
        try:
    
            authorList = article.AuthorList;
            emptyList = [];
    
            try:
                for loop in range(len(authorList.Author)):
                    emptyList.append(authorList.Author[loop].LastName.cdata + ', '+authorList.Author[loop].ForeName.cdata)
                
            except:
                emptyList = [authorList.Author.LastName.cdata,authorList.Author.ForeName.cdata];

            authorsStore.append(emptyList);
            
        except:
            authorsStore.append('Error Retrieving')
        
        # Retrieve Article ID List
    
        articleIDList = obj.PubmedArticleSet.PubmedArticle[it].PubmedData.ArticleIdList
        IDStore.append(articleIDList)
    
    # ----------------------------------------------------------------------------
    # SAVING RESULTS
    # ----------------------------------------------------------------------------
        
    printToCSV(saveDir+'/Pubmed_'+search_terms+'.csv',['Title','Abstract','Date','Authors'],
               titleStore,abstractStore,dateStore,authorsStore)
               
               
    return titleStore, abstractStore, authorsStore, dateStore
                   
                   
                   
                   
    
    
    
    
