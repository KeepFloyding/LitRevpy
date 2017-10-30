# LiteratureReviewTools
Python tools used to extract publication information from any of the following serach engines.

* Science Direct; limited to 200 results per query request. Need an API key to access the database. This can be found by registering at
http://dev.elsevier.com/index.html

* PubMed; limited to 1000 results per query. No authentication needed as URL accessed with urllib.request.

* Google Scholar; no limit on number of results, but at some point, Google will block the IP address if calling too much. 
URL is accessed with BeautifulSoup, and html tags are extracted relating to article content. 

All results are saved in a csv file under the name of the query keywords within a specified folder. 

## Getting Started

### Prerequisites

* Anaconda with Python 3.X
* pip install untangle

### Running 

Main script is in runAll.py

Inputs are search terms, number of results desired and the folder where results are to be saved.

```
search_terms = 'abdominal aortic aneurysm'
numRes = 100;
saveDir = 'testResults2
```

Main source files are located in searchTools. 





