import tensorflow.compat.v1 as tf
import gpt_2_simple as gpt2

def generate_word_predictions(input_phrase, num_predictions, model_name, model_dir):
    tf.reset_default_graph()
    sess = gpt2.start_tf_sess()
    
    with tf.Session() as sess:
        gpt2.load_gpt2(sess, model_name=model_name, model_dir=model_dir)

        generated_words = []
        while len(generated_words) < num_predictions:
            generated_word = gpt2.generate(sess, model_name=model_name,
                                            model_dir=model_dir, prefix=input_phrase,
                                            nsamples=num_predictions+20, 
                                            length=1, temperature=0.5, 
                                            return_as_list=True)
            
            for phrase in generated_word:
                generated_words.append(phrase.strip().split()[-1])
            
            generated_words = list(set(generated_words))
            print(generated_words)

    return generated_words[:num_predictions]