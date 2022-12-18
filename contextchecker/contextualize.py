from imports import *
from dot_product_attention import *
from embeddings_generator import *
from text_preprocessor import *

def context_weights(sentence):
    words = tokenizer(sentence)
    word_embeddings, words = get_word2vec_embedding(words)
    weights, context_vectors = dot_product_attention(word_embeddings, word_embeddings)
    return words, weights

def wordwise_weight_list(sentence):

    words, weights = context_weights(sentence)

    weights_lists = []

    for word_list_1,i in zip(words,range(len(words))):

        for word_list_2,j in zip(words,range(len(words))):

            weights_lists.append([[word_list_1, word_list_2], weights[i][j]])

    return weights_lists


def check_context_weight(sentence, word_one, word_two):
    
    weights_lists = wordwise_weight_list(sentence)

    for weights_list in weights_lists:

        if weights_list[0] == [str(word_one).lower(), str(word_two).lower()]:

            return weights_list[0], weights_list[1]

    else:

        raise ValueError("Word(s) not found in a sentence") 