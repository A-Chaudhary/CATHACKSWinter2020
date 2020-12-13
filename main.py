from GoogleNews import GoogleNews

import numpy as np
import tensorflow as tf
from tensorflow import keras


reconstructed_model = keras.models.load_model("model")

googlenews = GoogleNews()
print('Sentiment Analysis (-1 to 1, Negative to Positive Sentiment)')

ticker = input('Enter in Stock Ticker (Blank to Quit): ')
sort = True

while ticker != '':
    titles = []

    googlenews.search(ticker + ' Stock')
    news = googlenews.results(sort=sort)

    googlenews.clear()

    for articles in news:
        titles.append(articles['title'])

    predictions = []
    for title in titles:
        # print(title)
        predictions.append( reconstructed_model.predict(np.array([title]))[0][0] )

    sentiment = 0
    for prediction in predictions:
        if prediction > 0:
            sentiment +=1
        elif prediction < 0:
            sentiment -=1
    sentiment /= 10

    # print(predictions)
    print(ticker +': '+ str(sentiment))

    ticker = input('Enter in Stock Ticker (Blank to Quit): ')
