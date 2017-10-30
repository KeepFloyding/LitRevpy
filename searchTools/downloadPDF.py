# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 17:28:13 2016

@author: ap4409
"""

import requests

def downloadPDF(url,saveFile):

    r = requests.get(url, stream=True)
    
    with open(saveFile, 'wb') as fd:
        fd.write(r.content)
        print('Saved under '+saveFile)
        
urlList = {};

urlList['Thrombin activatable fibrinolysis inhibitor and the risk for deep vein thrombosis'] = 'http://www.bloodjournal.org/content/95/9/2855.full.pdf'
urlList['A study of the mechanism of inhibition of fibrinolysis by activated thrombin-activable fibrinolysis inhibitor'] = 'http://www.jbc.org/content/273/42/27176.full.pdf'

for url in urlList:
        
        downloadPDF(urlList[url],url + '.pdf');
