import tensorflow.compat.v1 as tf
import gpt_2_simple as gpt2


def generate_word_predictions(input_phrase, num_words, model_name, model_dir):
    tf.reset_default_graph()
    
    # Create a TensorFlow session
    sess = gpt2.start_tf_sess()

    # Load the GPT-2 model
    gpt2.load_gpt2(sess, model_name=model_name, model_dir=model_dir)

    # Generate word predictions
    generated_words = []
    for _ in range(num_words):
        # Generate one word at a time
        generated_word = gpt2.generate(sess, model_name=model_name, model_dir=model_dir, prefix=input_phrase, length=1, temperature=0.7, return_as_list=True)[0]
        generated_word = generated_word.strip().split()[-1]
        generated_words.append(generated_word.strip())

    return generated_words


# # Create a TensorFlow session
# sess = gpt2.start_tf_sess()

# # Load the GPT-2 model
# gpt2.load_gpt2(sess, model_name=model_name, model_dir=model_dir)

# # Generate word predictions
# # Your code for generating predictions goes here


# # generated_text = gpt2.generate(sess, model_name=model_name, model_dir=model_dir, prefix=input_phrase, length=1, temperature=0.7, return_as_list=True)[0]
# # print(generated_text)

# # Generate 5 individual words

# generated_words = []
# for _ in range(num_words):
#     # Generate one word at a time
    



