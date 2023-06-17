import lzma 
import gzip

def compressed_size(str):
    return len(gzip.compress(str.encode()))

def ncd(str1, str2):
    return (compressed_size(str1 + str2) - 
            min(compressed_size(str1), compressed_size(str2))) / max(
                compressed_size(str1), compressed_size(str2))

def get_top_words_v3(input_phrase, predictions, num_words):
    ncd_scores = [(word, ncd(input_phrase, word)) for word in predictions]

    sorted_words = sorted(ncd_scores, key=lambda x: x[1])

    top_words = [word for word, _ in sorted_words[:num_words]]

    return top_words