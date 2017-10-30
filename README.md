# LiteratureReviewTools
Python tools used to extract publication information from the web and performing data analysis. 

PREREQUISITES
Anaconda with Python 3.X
pip install untangle

TOOLS FOR EXTRACTING PUBLICATION INFORMATION

1) Science Direct; limited to 200 results per query request. Need an API key to access the database. This can be found by registering at
http://dev.elsevier.com/index.html

2) PubMed; limited to 1000 results per query. No authentication needed as URL accessed with urllib.request.

3) Google Scholar; no limit on number of results, but at some point, Google will block the IP address if calling too much. 
URL is accessed with BeautifulSoup, and html tags are extracted relating to article content. 

All results are saved in a csv file under the name of the query keywords. 

DEVELOPMENT

1) Try to retrieve results from Web of Science database. Should be possible by using BeautifulSoup (Weekend)

2) Unsupervised learning algorithm to classify each research article in a cluster. Possible options for classification include:

  - Topic modelling algorithms such as LDA (Latent Dirichlet Analysis) or LSA (Latent Semantic Analysis)
  - Gensim Doc2Vec algorithm to represent each document as a set of vectors. Then maybe run clustering algorithm on it. Visualise with pyLDAVis. 
  
Interested in contributing? Email me at andris.piebalgs14@outlook.com
