from imports import *
from contextualize import check_context_weight, context_weights
from visualizer import plot_attention_weight_matrix


def main(sentence,word_one, word_two):

    sentence_copy,word_one_copy,word_two_copy = sentence, word_one, word_two
   
    #get all the weights from the
    words, weights = context_weights(sentence)

    # plot the weights matrix
    plot_attention_weight_matrix(weights, words, words)

    # extract weights from the weights matrix pairwise
    words_passed, weight = check_context_weight(sentence, word_one, word_two)

    print("Context weight between \'{}\' and \'{}\' in a sentence \'{}\' is {:.2f}".format(word_one_copy, word_two_copy, sentence_copy, weight))

def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a frequency) and one optional argument,
    preceded by "-s" (the value to use as the sentence).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("s", type=str, help="a sentence")
    parser.add_argument("w1", type=str,help="the first word")
    parser.add_argument("w2", type=str,help="the second word")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.s, args.w1, args.w2)

