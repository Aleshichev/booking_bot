# Booking bot
Парсинг веб-страниц с помощью Selenium и Beautiful Soup.
Была создана гугл форма в Google Forms с тремя вопросами. Бот автоматически вводит данные, считывает информацию и заполняет Google форму.
## Используемые ресурсы
-	Beautiful Soup, 
-	Selenium, 
-	Google forms,
-	www.booking, 
## Модули и библиотеки 
bs4, reqests, os, time, selenium.webdriver

## Структура проекта
Для удобства  управления данными создано 2 класса:
1.	HotelData - отвечает за сбор данных с сайта, имеет 2 функции **def get_price_list()** и **def get_addres_link()**
2.	Bot Brain – отвечает за ввод данных, имеет 2 функции **def enter_data()**   и  **def fill_form()**

## Процесс программы
1.	С помощью **selenium**  через функцию **def enter_data()**  бот открывает страницу **booking** и вводит заданные параметры **город**, **дату прибытия**, **дату отъезда**. Нажимает кнопку найти. 
2.	Затем в открывшемся окне выбирает класс отеля (вводи количество звёзд 2/3/4/5).
3.	 С помощью **Beautiful Soup**( функции **def get_price_list()** и **def get_addres_link()**) бот считывает информацию и создаёт список отелей с названием, ценой и ссылкой на отель (для примера установлен лимит списка 5 отелей).  
4.	Затем бот открывает Google форму, функция **def fill_form()** ,  и заполняет три строки соответствующей информацией.
<img src="https://github.com/Aleshichev/booking_bot/blob/main/booking_bot.gif" width="600">




