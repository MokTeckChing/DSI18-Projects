 ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Reddit Classification

### Problem Statement

A psychology professor is interested in gauging maliciousness via language. Being a frequent surfer of reddit, he has chanced upon two subreddits that would provide him a good metric for comparison: r/pettyrevenge and r/prorevenge. 

However, this psychology professor has no background in language processing via code, and has thus hired me, a freelance data analyst, to use scraped data from both these subreddits to build a model that would determine if a person was less (r/pettyrevenge) or more (r/prorevenge) malicious, as well as do a simple analysis of any significant words found.

The professor has stated that for the purpose of his research, the model needs to achieve an accuracy score of over 70%.

### Executive Summary

The subreddits r/pettyrevenge and r/prorevenge were scraped for about 800 posts each via the PushshiftAPI. The "selftext" and "title" data categories were then extracted and combined into a "text" category. The text was run through a function removing stopwords, punctuation and short words (len < 3), and then lemmatized using the WordNet Lemmatizer. 

The text was transformed using a Count Vectorizer, and the top scoring words for both reddits were removed before running the data through three classifiers: Multinomial Naive Bayes, K-Nearest-Neighbors and Random Forest, each with minor optimisation via GridSearchCV. Random Forest scored the best in accuracy overall, and was then further optimised, resulting in a model with 72.7% accuracy. 


### Data Dictionary

As this is a classification model based on natural language processing, there is no data dictionary available.


### Conclusion

After examination of the highest weighted features, it was theorized that there were several themes that significantly factored into causing someone to increase their maliciousness. Presence of hostile intent from the offending party is one such factor. Place of work/school was also another significant theme that was seen.

Further research was suggested using several other "revenge" subreddits, such as r/nuclearrevenge, so that one's maliciousness can be determined on a scale rather than as a binary function.

