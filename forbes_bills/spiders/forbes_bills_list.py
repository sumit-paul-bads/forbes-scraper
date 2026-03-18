import scrapy
import json

class ForbesSpider(scrapy.Spider):
    name = "forbes"

    def start_requests(self):
        for start in range(0, 500, 50):
            url = f"https://www.forbes.com/forbesapi/person/billionaires/2026/rank/true.json?limit=50&start={start}"
            
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                headers={"User-Agent": "Mozilla/5.0"}
            )

    def parse(self, response):
        data = json.loads(response.text)

        persons = data.get('personList', {}).get('personsLists', [])

        for person in persons:
            yield {
                'name': person.get('personName'),
                'net_worth': person.get('finalWorth'),
                'rank': person.get('rank'),
                'age': person.get('age'),
                'country': person.get('countryOfCitizenship'),
                'source': person.get('source'),
                'industry': person.get('category'),
            }