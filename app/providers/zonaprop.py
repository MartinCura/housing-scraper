import logging
from difflib import ndiff

from bs4 import BeautifulSoup

from app.providers.base_provider import BaseProvider


class Zonaprop(BaseProvider):
    def props_in_source(self, source):
        page_link = self.provider_data['base_url'] + source
        page = 0
        # previous_page = None

        while(True):
            logging.info(f"Requesting {page_link}")
            page_response = self.request(page_link)

            if page_response.status_code != 200:
                break

            page_content = BeautifulSoup(page_response.content, 'lxml')
            # logging.info(page_content)
            # logging.info('********')

            # if previous_page:
            #     diff = ndiff(str(previous_page), str(page_content))
            #     logging.info(type(diff))
            #     # logging.info(''.join(diff))
            #     if not diff:
            #         logging.info("hey! this page is just like the last!!")
            #         break
            #     # for d in diff:
            #     #     logging.info(d)
            #     # while (d := next(diffs)):
            #     #     logging.info(d)
            # previous_page = page_content

            properties = page_content.find_all('div', class_='postingCard')

            for prop in properties:
                title = prop.find('a', class_='go-to-posting').get_text().strip()
                price_section = prop.find('span', class_='firstPrice')
                if price_section is not None:
                    title += ' ' + price_section['data-price']
                location_section = prop.find('span', 'postingCardLocation')
                if location_section:
                    title += f' ~ ({location_section.span.get_text().strip()})'

                yield {
                    'title': title,
                    'url': self.provider_data['base_url'] + prop['data-to-posting'],
                    'internal_id': prop['data-id'],
                    'provider': self.provider_name
                }

            page += 1
            # TODO: currently fails to realize when there's only 1 page;
            # this is a hack to fix it but would leave out results with more than 3 pages
            if page > 3:
                break
            page_link = f"{self.provider_data['base_url']}{source[:-5]}--pagina-{page}.html"
