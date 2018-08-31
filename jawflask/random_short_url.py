#!/usr/bin/python3

from jawflask.storage import urlstore
import string
import random
import sys


def url_generator(sourceUrl):
    chars = string.ascii_uppercase + string.ascii_lowercase
    size = 6
    rng_string = ''.join(random.choice(chars) for i in range(size))
    urlstore.urldict[rng_string] = sourceUrl
    del_string = ''.join(random.choice(chars) for i in range(size + 1))
    urlstore.deldict[del_string] = rng_string
    urlstore.save()
    return ({rng_string: sourceUrl, "delstring": del_string})





if __name__ == '__main__':
    print(url_generator())
