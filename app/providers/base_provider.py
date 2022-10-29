import logging
from abc import ABC, abstractmethod

import cloudscraper


class BaseProvider(ABC):
    def __init__(self, provider_name, provider_data):
        self.provider_name = provider_name
        self.provider_data = provider_data
        self.__scraper = cloudscraper.create_scraper()

    @abstractmethod
    def props_in_source(self, source):
        pass

    def request(self, url):
        return self.__scraper.get(url)

    def next_prop(self):
        logging.info(f"Sources: {self.provider_data['sources']}")
        for source in self.provider_data['sources']:
            logging.info(f'Processing source {source}')
            yield from self.props_in_source(source)
