"""
functions for the poke api
"""
from queue import Queue
import re
import threading
import numpy
from .utils import http_get


BASE_URL = 'https://pokeapi.co/api/v2'
dest_url = {
    'names': BASE_URL + '/pokemon?limit=%s',
    'species': BASE_URL + '/pokemon-species/%s'
}


def amount_match_names(limit='10000', match_regex=r'\w*at\w*a\w*'):
    """
    function that requests names api, and match names with a reges criteria
    :param match_regex: regex criteria to apply filter
    :param limit: limit for the pokemon api returning of values
    :return: integer of the matching criteria pokemon names
    """
    out = http_get(dest_url['names'] % limit)
    names = re.findall(match_regex, ' '.join([x['name'] for x in out['results']]))
    return len(names)


def amount_breeding_especies(pokemon: str = 'raichu'):
    """
    function that request especies api of an especific
    pokemon and filter species that are egg group related
    :param pokemon: string pokemon name or number
    :return: integer of unique especies that could breed
    with the entered pokemon
    """
    out = http_get(dest_url['species'] % pokemon)
    pokemon_species = [http_get(x['url'])['pokemon_species'] for x in out['egg_groups']]
    name_lists = set(numpy.concatenate([[y['name'] for y in x] for x in pokemon_species]))
    return len(name_lists)


def weight_queue_filler(url: int, queue: Queue, filter_type: str = 'fighting'):
    """
    thread function that request pokemon information and
    filter by pokemon type and save its weight to a queue
    :param url: url requests
    :param queue: queue used
    :param filter_type: string used to filter
    :return:
    """
    out = http_get(url)
    if {tipo['type']['name'] for tipo in out['types'] if tipo['type']['name'] == filter_type}:
        queue.put(out['weight'])


def minmax_weights(gen_limit: int = 151, filter_type:str='fighting'):
    """
    function that uses threads to handle request that return values in a queue
    :param gen_limit: int input param that delimiter limit request by its number
    :return: list of max and min values
    """
    out = http_get(dest_url['names'] % gen_limit)
    queue = Queue()
    thread = []
    [thread.append(threading.Thread(target=weight_queue_filler, args=(url, queue, filter_type)))
        for url in [result['url'] for result in out['results']]]
    [_.start() for _ in thread]
    [_.join() for _ in thread]
    weights = list(queue.queue)
    return [max(weights), min(weights)]
