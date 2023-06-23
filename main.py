from ngd import ngd, get_top_words_v1, get_top_words_v2
from predict import generate_word_predictions
from ncd import get_top_words_v3

from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.preprocessing import MultiLabelBinarizer
from nltk.translate.bleu_score import sentence_bleu

def main():
    
    model_name = "124M"
    model_dir = r"C:\Users\rocha\OneDrive\Área de Trabalho\IA225\IA225_Project\NGD_Word_Prediction\gpt-2\models"

    while True:
        input_phrase = input("Enter your input phrase: ")
        num_predictions = int(input("Enter the number of word predictions: "))

        word_predictions = generate_word_predictions(input_phrase, num_predictions, model_name, model_dir)

        print("Word predictions:")
        for idx, word in enumerate(word_predictions):
            print("Word", idx+1, ":", word)
        
        print("Top words considering the entire input phrase:")
        top_words = get_top_words_v1(input_phrase, word_predictions, 5)
        for idx, word in enumerate(top_words):
            print("Word", idx+1, ":", word)
            
        print("Top words considering the NCD:")
        top_words = get_top_words_v3(input_phrase, word_predictions, 5) 
        for idx, word in enumerate(top_words):
            print("Word", idx+1, ":", word)     

        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
