from .engine import _transform_word


def transform(text: str):
    """
    No bitches?

    :param text: the text to convert.
    :return: the gay text.
    """
    return " ".join([_transform_word(i) for i in text.split(" ")])
