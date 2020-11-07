#!/usr/bin/env python3
import sys
import yaml
import logging

from app.providers.processor import process_properties
from app.notifier import Notifier


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    with open("configuration.yml", 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)

    notifier = Notifier.get_instance(cfg['notifier'])

    new_properties = []

    for provider_name, provider_data in cfg['providers'].items():
        try:
            logging.info(f"Processing provider {provider_name}")
            new_properties += process_properties(provider_name, provider_data)
        except:
            logging.exception(f"Error processing provider {provider_name}.\n{sys.exc_info()[0]}")

    if len(new_properties) > 0:
        logging.info('* Found new properties *')
        for prop in new_properties:
            text = f"[{prop['title']}]({prop['url']})"
            logging.info(text)
        notifier.notify(new_properties)


if __name__ == "__main__":
    main()
