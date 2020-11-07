#!/usr/bin/env python3
import logging
import yaml

from app.providers.zonaprop import Zonaprop
from app.providers.argenprop import Argenprop
from app.providers.mercadolibre import Mercadolibre
from app.providers.properati import Properati
from app.providers.inmobusqueda import Inmobusqueda


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    with open("configuration.yml", 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)

    providers_cfg = cfg['providers']

    for p in ['zonaprop', 'argenprop', 'mercadolibre', 'properati', 'inmobusqueda']:
        try:
            provider = Zonaprop(p, providers_cfg[p])
            [print(prop) for prop in provider.next_prop()]
        except KeyError:
            pass
