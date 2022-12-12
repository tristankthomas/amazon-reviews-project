import pandas as pd
import re
import json
import nltk
from nltk.corpus import stopwords
from nltk import ngrams
from task2 import get_scores

def task6():
    data = pd.read_csv('data/dataset.csv', index_col=False)
    
    # replacing the review section with a list of review bodys for each product
    review_body = data['REVIEWLIST'].apply(lambda x: get_review_body(x))
    review_star = data['REVIEWLIST'].apply(lambda x: get_review_score(x))

    scores = []
    reviews = []

    # iterates through each review body in each product
    for i in range(len(review_body)):
        for j in range(len(review_body[i])):   
            review_body[i][j] = processing(review_body[i][j])
            # only appends valid reviews and scores
            if len(review_body[i][j]) != 0 and len(review_star[i][j]) != 0:
                scores.append(review_star[i][j])
                reviews.append(review_body[i][j])

    scores = [int(get_scores(x)[0]) for x in scores]

    df = pd.DataFrame({'score': scores, 'bigrams': reviews})
    json_str = df.to_json(orient='records')
    json.dump(json.loads(json_str), open("task6.json", "w"))

    return df

def get_review_score(product):
    # gets a list of review scores
    scores = []
    for review in json.loads(product):
        scores.append(review['review_star'])

    return scores

def get_review_body(product):
    # gets a list of review body's
    bodies = []
    for review in json.loads(product):
        bodies.append(review['review_body'])

    return bodies

def processing(review):
    eng_stopwords = stopwords.words('english')
    # remove non-alphabetic characters
    review_processed = re.sub('[^a-zA-Z]', ' ', review)
    # replace multiple spaces with single space
    review_processed = re.sub('\s+', ' ', review_processed)
    # lower case
    review_processed = review_processed.lower()
    # tokenize
    review_words = review_processed.split()
    # stopwords removal
    review_words = [word for word in review_words if not word in eng_stopwords]
    # remove words 2 characters or less
    review_words = [word for word in review_words if not len(word) <= 2] 
    
    review_pairs = []
    for i in range(len(review_words) - 1):
        review_pairs.append(review_words[i] + ' ' + review_words[i + 1])
        
    return review_pairs
    



