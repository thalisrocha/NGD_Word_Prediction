# Kolmogorov Complexity-Based Word Predictor (NGD_Word_Prediction)

## Description

This Python program utilizes a pre-trained GPT-2 model along with Normalized Google Distance (NGD) and Normalized Compression Distance (NCD) to generate predictions for a given incomplete input phrase.

The code is structured into 4 Python scripts: `main.py`, `ngd.py`, `ncd.py`, and `predict.py`.

## Requirements

Before running the program, ensure you have the following software and libraries installed on your machine:

- **Python:** The program was developed using Python 3.7.4. While it should work on most recent versions of Python, it has not been tested on versions other than 3.7.4.

- **Libraries:** You will need several Python libraries, including:
  - `numpy`
  - `math`
  - `nltk`
  - `urllib`
  - `googleapiclient`
  - `sklearn`
  - `lzma`
  - `gzip`
  - `tensorflow.compat.v1`
  - `gpt_2_simple`

You can install the above Python libraries using pip:

```ruby
pip install numpy nltk sklearn tensorflow lzma gzip google-api-python-client google-auth google-auth-httplib2 google-auth-oauthlib gpt-2-simple
```

- **Google Custom Search JSON API Key and Search Engine ID:** The `ngd.py` file requires a Google Custom Search JSON API key and Search Engine ID to calculate NGD scores. Please replace the placeholders in the code with your own API key and Search Engine ID.

- **GPT-2 Model:** The `predict.py` file needs a pre-trained GPT-2 model to generate predictions. The model name and directory are specified in the `main.py` file.

## Running the Program

To run the program, execute `main.py`. You will be prompted to enter an incomplete phrase and the number of word predictions you want the program to generate.

```ruby	
python main.py
```

The program will provide the top word predictions and then ask if you want to continue with another prediction. Enter `y` to continue or `n` to stop the program. 

## Note 

This code is designed for educational and research purposes. Please ensure to abide by the terms of service of the Google Custom Search API and the usage policies of the GPT-2 model.

## Model's construction

### Pre-processing

The initial idea of directly using NGD for predictions faced scalability issues. As a solution, the GPT-2 model was employed for initial predictions, followed by the application of NGD to rank these predictions. Various challenges, such as dealing with Google's API limits and ensuring correct search query formulation, were addressed during this phase.

### Method evaluation

Post pre-processing, two main methodologies were explored:

1. Calculating NGD between the entire input phrase and each predicted word.
2. Computing the average NCD in a similar manner.

A variety of test phrases were used to evaluate the efficacy of these methods.

## Discussion and Conclusions

While the NGD ranking generally aligns with anticipated predictions, it struggles with high-frequency, closed-class words. Moreover, the GPT-2 predictions sometimes deviate from the expected outcomes, indicating a limitation of the model. The model's prolonged response time also makes it unsuitable for real-time applications.


