"""A Markov chain based toki pona chatbot written in Python."""

import pprint
import src.weights

def main() -> None:
    """
    The main function for ilo jan.
    """
    ilo_jan = src.weights.read_corpus('ilo-jan/data/corpus.txt', context_length=3)
    with open('brain.dump', 'w') as f:
        pprint.pprint(ilo_jan.model, width=1, stream=f)

    print(ilo_jan.generate_text('toki Inli li'))

if __name__ == "__main__":
    main()
