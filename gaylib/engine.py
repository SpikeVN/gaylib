import random

from .dictionary import CONTENT

MODIFICATIONS = [
    lambda x: x.replace("h", "k"),
    lambda x: x.replace("ị", "j"),
    lambda x: x + x[-1],
    lambda x: x.replace("r", "g"),
    lambda x: x.replace("l", "n"),
    lambda x: x.replace("c", "k"),
    lambda x: x.replace("s", "x"),
    lambda x: x.replace("y", "i"),
    lambda x: x.replace("tr", "ch"),
    lambda x: x.replace("qu", "w"),
    lambda x: x.replace("g", "q"),
    lambda x: x.replace("ê", "i"),
    lambda x: x.replace("ng", "g"),
    lambda x: x.replace("l", "n"),
    lambda x: x + "k",
    lambda x: x.replace("ph", "f"),
]


def _transform_word(word: str):
    """
    Transform a world into its gay counterpart.

    :param word:
    :return:
    """
    output = CONTENT.get(word, word)
    mods = random.choices(MODIFICATIONS, k=2)
    output = mods[0](output)
    output = mods[1](output)
    return output




