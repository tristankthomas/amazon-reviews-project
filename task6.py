import pandas as pd
import re
import json
import nltk
from nltk.corpus import stopwords
from nltk import ngrams
from task2 import get_scores

def task6():
    data = pd.read_csv('dataset.csv', index_col=False)
    
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
    pattern = fr'(?<="review_star":)(?: ?")((?:.|\n)*?)(?=",)'
    matches = re.findall(pattern, product)
    return matches

def get_review_body(product):
    # gets a list of review body's
    pattern = r'(?<="review_body":)(?: ?")((?:.|\n)*?)(?="})'
    matches = re.findall(pattern, product)
    return matches

def processing(review):
    MIN_WORD_LEN = 3
    stop_words = set(stopwords.words('english'))
    # removes all non alphabetic chars (not spacing chars) and international chars
    review = re.sub(r'([^A-Za-z\\]|\\u)', ' ', review)
    # replaces spacing chars with a single space (since back slash still included from above)
    review = re.sub(r'(\\[nt])', ' ', review)
    # goes through again to only keep letters
    review = re.sub(r'([^A-Za-z])', ' ', review)
    # replaces any instances of two or more spaces with a single space
    review = re.sub(r' {2,}', ' ', review)
    # makes all chars lowercase
    review = review.lower()
    # tokenises the review
    review = nltk.word_tokenize(review)
    # removes any stop words and words less than 3 chars
    review = [w for w in review if not w in stop_words]
    review = [w for w in review if len(w) >= MIN_WORD_LEN]

    # creates list of ngrams
    review = list(ngrams(review, 2))
    
    return review



