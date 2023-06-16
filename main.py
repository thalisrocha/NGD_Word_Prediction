from ngd import ngd, get_top_words
from predict import generate_word_predictions

def main():
    # Set the model name and checkpoint directory
    # Set the model name and checkpoint directory
    model_name = "124M"
    model_dir = r"C:\Users\rocha\OneDrive\Área de Trabalho\IA225\IA225_Project\NGD_Word_Prediction\gpt-2\models"

    while True:
        # Get input phrase from the user
        input_phrase = input("Enter your input phrase: ")
        num_predictions = int(input("Enter the number of word predictions: "))

        # Generate word predictions using the NGD function
        word_predictions = generate_word_predictions(input_phrase, num_predictions, model_name, model_dir)

        # Print the generated words
        # Print the generated words
        print("Word predictions:")
        for idx, word in enumerate(word_predictions):
            print("Word", idx+1, ":", word)
        
        # Get the top 5 words with the smallest NGD scores
        top_words = get_top_words(input_phrase, word_predictions, 5)
        
        # Print the top words
        print("Top words:")
        for idx, word in enumerate(top_words):
            print("Word", idx+1, ":", word)

        # Ask if the user wants to continue or exit
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
