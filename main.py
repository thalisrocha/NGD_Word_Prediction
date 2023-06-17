from ngd import ngd, get_top_words_v1, get_top_words_v2
from predict import generate_word_predictions

def main():
    # Set the model name and checkpoint directory
    # Set the model name and checkpoint directory
    model_name = "124M"
    model_dir = r"C:\Users\rocha\OneDrive\Área de Trabalho\IA225\IA225_Project\NGD_Word_Prediction\gpt-2\models"

    while True:
        input_phrase = input("Enter your input phrase: ")
        num_predictions = int(input("Enter the number of word predictions: "))

        word_predictions = generate_word_predictions(input_phrase, num_predictions, model_name, model_dir)

        print("Word predictions:")
        for idx, word in enumerate(word_predictions):
            print("Word", idx+1, ":", word)
        
        top_words = get_top_words_v1(input_phrase, word_predictions, 5)
        
        print("Top words considering the entire input phrase:")
        for idx, word in enumerate(top_words):
            print("Word", idx+1, ":", word)
            
        print("Top words considering the tokenized input phrase:")
        top_words = get_top_words_v2(input_phrase, word_predictions, 5)
        for idx, word in enumerate(top_words):
            print("Word", idx+1, ":", word)
            

        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
