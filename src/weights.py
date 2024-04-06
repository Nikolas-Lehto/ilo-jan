"""A library for extracting, calculating and/or saving weights from corpora."""

import src.markov

def read_corpus(file_path: str, context_length: int = 2) -> src.markov.Model:
    """
    Automagically reads weights from corpus.

    `file_paths`: Paths for the corpus.\n
    `context_length`: Context length for the model in words.\n
    """

    model = src.markov.Model(context_length)
    weights: dict[tuple[str, ...], dict[str, int]] = {}
    converted_weights = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        words = []
        for line in file.readlines():
            for word in line.split(' '): words.append(word)

        weights = generate_weights(words, context_length)
        converted_weights = calculate_probabilities(weights)

    model.model = converted_weights

    return model

def generate_weights(words: list[str], context_length: int = 2)\
    -> dict[tuple[str, ...], dict[str, int]]:
    """
    Generate weights from text.\n
    
    `text` The text to generate the weights from.\n
    `weights` A previously generated weights to append the new ones to.\n
    `context_length` Context length for the model in words.\n
    """

    weights = {}

    for word in range(len(words) - context_length):

        # `current_words` is the elements form `words`
        # that are in the range of word to word + context length.
        current_words = tuple(words[word : word + context_length])
        next_word = words[word + context_length]

        if weights.get(current_words) is None:
            weights[current_words] = {next_word: 1}

        else:
            if weights[current_words].get(next_word) is None:
                weights[current_words][next_word] = 1

            else:
                weights[current_words][next_word] += 1

    return weights

def calculate_probabilities(weights: dict[tuple[str, ...], dict[str, int]])\
    -> dict[tuple[str, ...], dict[str, float]]:
    """
    Calculates the probabilities of potential next words from the frequencies 
    they appeared in the corpus text.\n

    `weights` The previously generated weights to calculate the probabilities from.\n
    """

    converted_weights: dict[tuple[str, ...], dict[str, float]] = {}

    for current_words in weights.keys():

        # How many times the current word appeared in the corpus
        word_appearance_count = float(sum(weights[current_words].values()))

        converted_weights[current_words] = {}
        for possible_next_word in weights[current_words].keys():

            # How likely is it for a possible next word to appear after current words
            converted_weights[current_words][possible_next_word] = \
            weights[current_words][possible_next_word] / word_appearance_count

    return converted_weights
