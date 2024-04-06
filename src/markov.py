"""A library for processing Markov chains."""

import random

class Model:
    """
    A Markov chain based chatbot model.
    """

    def __init__(self, context_length: int = 2) -> None:
        self.context_length = context_length
        self.model: dict[tuple[str, ...], dict[str, float]] = {}

    def sample_next(self, context: list[str]):
        """
        Samples the next word from the model based on the given context.

        `context` The context to sample the word based on.
        """

        context = context[-self.context_length:]
        if self.model.get(tuple(context)) is None:
            return " "

        return random.choices(
            list(self.model[tuple(context)].keys()),
            weights = list(self.model[tuple(context)].values())
        )[0]

    def generate_text(self, context: str, max_output_length:int = 200) -> str:
        """
        Generate text with the model based on the given context.\n

        `context` Context to generate text on.\n
        `max_output_length` Maximum length of outputted string.\n
        """

        sentence: list[str] = context.split(' ')
        unfinished_word = sentence[-max_output_length:]

        for _ in range(max_output_length):
            next_prediction = self.sample_next(unfinished_word)
            sentence.append(next_prediction)
            unfinished_word = sentence[-self.context_length:]

        finished_sentence = str()
        for word in sentence:
            finished_sentence += f'{word} '

        return finished_sentence
