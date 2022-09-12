from bs4 import BeautifulSoup
import requests

header = {
        "User-Agent": 'USER_AGENT',
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8"
}

class HotelData():
     """This class is responsible for collecting information from the booking site"""
    def __init__(self):
        self.price_list = []
        self.addres_list = []
        self.link_list = []

    def get_price_list(self, current_url):
        """Function converts data to price list"""
        response = requests.get(current_url, headers=header)
        soup = BeautifulSoup(response.content, "html.parser")
        print(response)
        price_data = soup.find_all("span", class_="fcab3ed991 bd73d13072", limit=5)
        for price in price_data:
                new_price = price.get_text()[3:].replace(' ', '')
                out = "".join(new_price.split())
                self.price_list.append(out)

        return self.price_list

    def get_address_link(self, current_url):
        """Function converts data to address list and link list"""
        response = requests.get(current_url, headers=header)
        soup = BeautifulSoup(response.content, "html.parser")
        link_data = soup.find_all('div', class_="d20f4628d0", limit=5)
        for link in link_data:
            new_link = link.find('img').get('alt')
            self.addres_list.append(new_link)

        for link in link_data:
            new_link = link.find('a').get('href')
            self.link_list.append(new_link)

        return self.link_list, self.addres_list
