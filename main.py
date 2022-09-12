from hotel_data import HotelData
from bot_brain import BotBrain

hotel = HotelData()
bot_brain = BotBrain()


current_url = bot_brain.enter_data()
price_list = hotel.get_price_list(current_url)
link_list, addres_list = hotel.get_address_link(current_url)
bot_brain.fill_form(link_list, addres_list, price_list)

