"""
rest fast api output.
"""
from fastapi import FastAPI
from apps import apis

app = FastAPI()


@app.get("/")
def names_root():
    """
    rest api default
    :return:
    """
    return {"hello": "moto"}


@app.get("/names")
def names_root(limit: str = '1000', regex: str = r'\w*at\w*a\w*'):
    """
    rest api calling apps names function
    :param limit: optional limit param
    :param regex: optional different regex
    :return:
    """
    return apis.amount_match_names(limit, regex)


@app.get("/species")
def species_root(pokemon: str = 'raichu'):
    """
    rest api calling apps species function
    :param pokemon: pokemon name or id
    :return:
    """
    return apis.amount_breeding_especies(pokemon)


@app.get("/weights")
def weights_root(gen_limit: int = 151, filter_type: str = 'fighting'):
    """
    rest api calling apps weights function
    :param gen_limit: amount of register to receive
    :param filter_type: pokemon type to filter
    :return:
    """
    return apis.minmax_weights(gen_limit, filter_type)
