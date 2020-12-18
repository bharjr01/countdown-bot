import json
from typing import List, Tuple, Dict, Union


def find_anagrams(selection: List[str]):
    selection_model = __create_model(selection)

    anagrams = []
    for word, model in __MODELS.items():
        if all(item in selection_model for item in model):
            anagrams.append(word)

    return sorted(anagrams, key=len)[-5:]


def __create_model(selection: Union[str, List[str]]) -> List[Tuple[str, int]]:
    return [(char, selection.count(char)) for char in set(selection)]


def __get_english_words() -> List[str]:
    # https://github.com/dwyl/english-words
    with open('./src/words_dictionary.json') as f:
        content = json.load(f)

    return [k.upper() for k, v in content.items()
            if 3 < len(k) < 10]


def __get_english_words_models() -> Dict[str, List[Tuple[str, int]]]:
    models = {}
    for word in __get_english_words():
        models[word] = __create_model(word)

    return models


__MODELS = __get_english_words_models()
