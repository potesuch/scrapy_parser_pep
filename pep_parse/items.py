# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PepParseItem(scrapy.Item):
    """
    Класс элемента для хранения данных PEP.

    Этот класс определяет поля для собираемых элементов PEP.
    """
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
