# Character-Map-Generation-using Machine Learning Techniques

**Overview**

Psychological bias is the tendency to make decisions or take action in an unknowingly irrational way. Naturally, a human will be biased towards a particular option while taking a decision based on the interest. Through this project, implementation of a system that maps these biases are done. It is an approach to build the core part of an AGI(Artificial General Intelligence) system. 
 
As an initial phase of the whole project, we are implementing a program which generates a radar graph based on a person’s interest. The initial dataset is collected from the Instagram ad-data. The ad-data consists of labels from various fields that are generated based on the activity. These labels are processed using Word2Vec and a hierarchical clustering algorithm. The output generated is be a dendrogram. It is then converted into a simple understandable radar graph collection that is interlinked.** 


**Methodology**

The main steps that include are: 

• Fetches Instagram ads information.
• Instagram’s each ad interest data is considered as a label. Top 5 URL regarding that label is extracted. 
• Cleaning is performed on the data of that URLs and is tokenized. 
• Training is performed using fastText.  
• The tokenized data is given as the input of Word2Vec and fastText. Both of them convert the words into vectors as the machine-understandable format.  
• The output of the Word2Vec and fastText are fed into a hierarchical clustering system and the output will be a dendrogram. 
• From the dendrogram, an interlinked collection of radar graphs can be generated. 
• The radar graph represents a bias towards different areas. The output will be different for different persons. 
 
**Data fetching part **

Data containing page is a dynamic one, hence simply taking the source code of the page won't be enough to collect the data. The data is tracked and collected using "Selenium", a popular library which is used for web automation - scraping purposes. Selenium needs the corresponding browser's driver (Here it is Google's Chrome web driver) to do the automation.  
 
Running the fetching part of the code will trigger Google Chrome to open a new window which is directed to the Instagram home page. User needs to enter the login credentials, from there the page will be redirected to the “Ads Interest” tab. 
 
Since the website is a dynamic one, scrolling is required to get all data. The class which contains the interest text data is processed and the data is stored to a file. Users can either wait to get all the data or can end the processing using a keyboard interrupt. The program will store all the data which is currently visible in the window.  
 
The “Ads interest” data contains labels that have a collective meaning but when they are treated separately most of them appear to be quite unrelated. To indicate a bias towards a specific area of interest, they need to be classified. For that relation between each of the input labels have to be calculated.   

**Incremental training**

Since the labels stored are not recognizable by the computer, the conversion is needed for further processing. Using Natural Language Processing (NLP) corresponding vector information can be generated. Specifically, word embedding techniques are used for this. Models like Word2Vec (gensim) and Spacey are initially tested for this, these are fast models but the main disadvantage was the lack of ability to train the dataset incrementally.  
 
Incremental training adds labels and corresponding vectors to the trained output whenever a new label occurs. Because of the presence of multiple users, incremental training is an important feature here. The same corpus can grow bigger incrementally. Facebook’s FastText is a word embedding system that supports incremental training and has similar features of Word2Vec. Hence it is used.

**Preprocessing and training **

Labels collected are unrelated mostly and most of them are simply independent words. Because of that, there is no way to find the meaning of them or to find out the vector values of them. The words can appear in a suitable context in a related document, but all of the necessary documents have to be collected individually from the internet. 
 
Labels are fetched from the stored location. Information required to vectorize them is collected from the internet using the “google search” library. It returns links to the pages which contain exactly the labels that searched for. It is done by quoting the labels which enable Google’s “must include” feature. It ensures that the search result will contain information related to the searched label. 
 
Returned links are accessed using the “urllib” library which is commonly used to parse and process HTTP requests. The Source of the webpage is collected and the text data is scraped using the “BeautifulSoup” library. Then regular expressions are used to filter out numbers, dates, single words. Word embedding systems need a collection of sentences to vectorize each of the tokens. Specifically, in the Skip-gram model, it takes every word and also takes the surrounding words within a defined window and then feeds a neural network that after training will predict the probability for each word to appear in the window. 
 
The output of the preprocessing stage is a collection of tokens that are separated from the scraped sentences. Then it is fed to the fasttext model. But before that it needs to be trained with a vectorized dataset, it can be downloaded from the fasttext documentation page(many general datasets are available on the internet). It helps the system to gain much more accuracy. After all labels are trained, the trained output will have a large collection of labels which includes the user’s Ads data as well as the tokens from all the pages that are used to accurately vectorize these input labels. 
 
**Processing**

As per each of the users, vectors of required labels have to be taken from the trained vectorized data. It can be taken by comparing the input data file and the dictionary of the trained data. Then these vectors associated with the labels are copied into a new file with the same name as the user. This information is fed into a hierarchical clustering algorithm that plots a dendrogram corresponding to it.  
 
Clustering is done by using sklearn’s “AgglomerativeClustering” method and plotting of dendrogram can be done by using Scipy’s dendrogram and linkage methods. 
 
The radar graph is generated using matplotlib’s pyplot library. Manual clustering is used to separate clusters because radar graphs corresponding to each of the users. After all, the same number of clusters is needed for comparison. 

**Conclusion **
 
Information collected from users is quite like an asset for a company. Powerful recommender systems are used by companies like Netflix, TikTok, Instagram, etc for gaining more users and to provide the best overall experience. The proposed system predicts biases based on the interests of users. 
 
Generation of character map is a step towards building an Artificial General Intelligence which can control Narrow AIs by giving proper guidelines. The generated character map can be used to implement a system that can act as individuals and take decisions or reshape itself to work with different people based on their preferences.  
 
 

 
