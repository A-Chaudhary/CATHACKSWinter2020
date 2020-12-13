# Short Term Stock Sentiment Analysis 
Analyzes Current News Articles' Title to determine Short Term Sentiment (7 Days) for Stock Tickers.
Uses a Recurrent Neural Network for Text Classification Trained on a Custom Dataset.

## Files
* tickers.csv : Contains tickers for S&P 500
* trainingData.csv : Contains News Article Titles with their Sentiment Labels
* data.ipynb : Creates the Custom Dataset using tickers.csv called trainingData.csv
* dictionary.json : Contains a Dictonary of Words in trainingData.csv
* training.ipynb : Creates the RNN based on trainingData.csv and Corresponding Model
* main.ipynb : Performs predictions of Sentiment based on User inputted Tickers
* main.py : Python version of main.ipynb Jupyter Notebook

## Inspiration
The Inspiration behind this project was learning about quantitative analysts. I thought it was interesting to predict future prices with previous stock price information. I had experimented with Long-Short Term Models to create mass stock predictions in the past but I wanted to see if it was possible based on qualitative data. I heard of stock movement based on hype. I thought that being able to determine what people were talking about the stock might be indicative of its shift in price and I could create a way to determine that "hype".

## What it does
The code takes a user inputted stock ticker and determines if the stock currently has a positive or negative sentiment on a scale of -1 to 1.

## How I built it
There are three fundamental parts to this project, creating a dataset with titles and sentiment labels, training a model based on the dataset, and getting predictions based on a user inputted ticker. 

The creation of the dataset used a csv file with ticker symbols for the S&P 500. Each ticker symbol was put in a search query in Google News to get the titles of news articles. The titles were assigned a positive(1) or negative(-1) sentiment with the use of specialized search query's with key words to allow for positive or negative articles to pop up respectively. This was then saved to a csv file to be used in training.

The training was done on a Recurrent Neural Network. The training data was parsed to have the same format as a tensorflow dataset of imdb reviews. The model composed of LSTM layers and Dense layer with relu activation function. The model was fit on the training data and saved for predictions.

The prediction process was done by loading the aforementioned model and using the user input as the search query (without biasing keywords) to get titles of news articles relating to the stock while also being in a relevant time frame from the current date. Each title for the specific search query was given a prediction from -1 to 1 and then combined into a single sentiment value to be reported back to the user.

## Challenges I ran into
There were many challenges I faced throughout this project.

The creation of the custom training dataset had encoding issues when trying to save the file as a result of special characters in a numerous amount of news article titles. Time also played a challenge in the creation of the custom dataset; the manual sentiment labelling for each title would have taken a long time so coming up with a way to query more positive or negative sentiment titles was critical.

The creation of the input data for the RNN model was having issues with the datatypes of the inputs given they were both strings and floats. The parameters of the model required tweaking and with limited computing power, they caused large wait times between parameter adjustment attempts.

The prediction based on user input wasn't working when in a function which left the program unable to give an output.
## Accomplishments that I'm proud of

## What I learned
I learned how to have requests from websites that I use on a weekly basis through code. I learned about using string input in neural network production and improved my experience with various model setups. I explored a new data format, json. 

## What's next for Short Term Stock Sentiment Analysis
Further steps include adding a way to implement stock price shifts based on sentiment thereby allowing future predictions to be based on previous stock prices along with current news regarding the company whose public offering is being traded. Integration of a price based model along with natural language processing would benefit from a redefined dataset now also including percent stock price changes and better sentiment labeling on a bigger dataset.

### References
* [S&P500 Ticker CSV File](https://datahub.io/core/s-and-p-500-companies)
* [Text Classification](https://www.tensorflow.org/tutorials/text/text_classification_rnn)
* [Google News API PyPI](https://pypi.org/project/GoogleNews/)
* [Google News API Documentation](https://github.com/Iceloof/GoogleNews/blob/master/GoogleNews/__init__.py)
