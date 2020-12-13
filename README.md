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


### References
* [Text Classification](https://www.tensorflow.org/tutorials/text/text_classification_rnn)
* [Google News API PyPI](https://pypi.org/project/GoogleNews/)
* [Google News API Documentation](https://github.com/Iceloof/GoogleNews/blob/master/GoogleNews/__init__.py)
