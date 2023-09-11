# Booking bot
Parsing web pages using Selenium and Beautiful Soup.
A google form was created in Google Forms with three questions. The bot automatically enters the data, reads the information and fills out the google form.
## Resources used
- Beautiful Soup, 
- Selenium, 
- Google forms,
- www.booking, 
## Modules and libraries 
bs4, reqests, os, time, selenium.webdriver

## Project structure
For the convenience of data management we created 2 classes:
1. HotelData - responsible for collecting data from the site, has 2 functions **def get_price_list()** and **def get_addres_link()**
2. Bot Brain - responsible for entering data, has 2 functions **def enter_data()** and **def fill_form()**

## Programme Process
1.	Using **selenium** via **def enter_data()** function, the bot opens the **booking** page and enters the given parameters **city**, **date of arrival**, **date of departure**. It clicks the find button. 
2.	Then in the opened window it selects the hotel class (enter the number of stars 2/3/4/5).
3.	 Using **Beautiful Soup**( functions **def get_price_list()** and **def get_addres_link()**) the bot reads the information and creates a list of hotels with the name, price and hotel link (for example the list limit is set to 5 hotels).  
4.	The bot then opens a Google form, function **def fill_form()** , and fills three lines with relevant information.
<img src="https://github.com/Aleshichev/booking_bot/blob/main/booking_bot.gif" width="600">




