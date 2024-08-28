
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# List of 1 country from each continent to lower search size
country_list = ['Algeria', 'Albania', 'Afghanistan', 'Bahamas', 'Argentina', 'Australia']

# All countrys from each continent
africa = ['Algeria','Angola','Benin','Botswana','Burkina','Faso','Burundi','Cabo','Verde','Cameroon','Central','African','Republic','Chad','Comoros','Congo','Cote',"d’ Ivoire",'Djibouti','Egypt','Equatorial','Guinea','Eritrea','Eswatini','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea-Bissau','Kenya','Lesotho','Liberia','Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria','Rwanda','Sao','Tome','and','Principe','Senegal','Seychelles','Sierra','Leone','Somalia','South','Africa','South','Sudan','Sudan','Tanzania','Togo','Tunisia','Uganda','Zambia','Zimbabwe']
europe= ['Albania','Andorra','Armenia','Austria','Azerbaijan','Belarus','Belgium','Bosnia and Herzegovina','Bulgaria','Croatia','Cyprus','Czechia','Denmark','Estonia','Finland','France','Georgia','Germany','Greece','Hungary','Iceland','Ireland','Italy','Kazakhstan','Kosovo','Latvia','Liechtenstein','Lithuania','Luxembourg','Malta','Moldova','Monaco','Montenegro','Netherlands','North','Macedonia','Norway','Poland','Portugal','Romania','Russia','San Marino','Serbia','Slovakia','Slovenia','Spain','Sweden','Switzerland','Turkey','Ukraine','United Kingdom','Vatican City']
asia = ['Afghanistan','Armenia','Azerbaijan','Bahrain','Bangladesh','Bhutan','Brunei','Cambodia','China','Cyprus','Georgia','India','Indonesia','Iran','Iraq','Israel','Japan','Jordan','Kazakhstan','Kuwait','Kyrgyzstan','Laos','Lebanon','Malaysia','Maldives','Mongolia','Myanmar','Nepal','North Korea','Oman','Pakistan','Palestine','Philippines','Qatar','Russia','Saudi Arabia','Singapore','South Korea','Sri Lanka','Syria','Taiwan','Tajikistan','Thailand','Timor-Leste','Turkey','Turkmenistan','United Arab Emirates','Uzbekistan','Vietnam','Yemen']
north_america = ['Antigua and Barbuda','Bahamas','Barbados','Belize','Canada','Costa Rica','Cuba','Dominica','Dominican Republic','El Salvador','Grenada','Guatemala','Haiti','Honduras','Jamaica','Mexico','Nicaragua','Panama','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Trinidad','USA']
south_america = ['Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador','Guyana','Paraguay','Peru','Suriname','Uruguay','Venezuela']
oceania = ['Australia','Fiji','Kiribati','Marshall Islands','Micronesia','Nauru','New Zealand','Palau','Papua New Guinea','Samoa','Solomon Islands','Tonga','Tuvalu','Vanuatu']

# Initialize chrome driver on Globle-game.com

PATH = "Path To Chrome Driver"

driver = webdriver.Chrome(PATH)
driver.get('https://globle-game.com/')
driver.maximize_window()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# Click Play
play_globe = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[2]/div[1]/a/div/div/div/div/div/canvas').click()

time.sleep(5)
enter_country = driver.find_element(By.XPATH, '//*[@id="guesser"]')

# Enter one country from each continent
i = 0
while i < len(country_list):
  enter_country.send_keys(country_list[i] + Keys.RETURN)
  i = i + 1

# Locate whihc continent the country is in by using the games "hot cold" system
closest_guess = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/ul/li[1]/button/span').text

# Enter all of the countrys in the correct continent based on the closest_guess
if closest_guess in europe:
    for item in range(500):
        enter_country.send_keys(random.choice(tuple(europe)) + Keys.RETURN)     
else:
    pass

if closest_guess in africa:
    for item in range(500):
        enter_country.send_keys(random.choice(tuple(africa)) + Keys.RETURN)
else:
    pass

if closest_guess in asia:
    for item in range(500):
        enter_country.send_keys(random.choice(tuple(asia)) + Keys.RETURN)
else:
    pass

if closest_guess in north_america:
    for item in range(500):
        enter_country.send_keys(random.choice(tuple(north_america)) + Keys.RETURN)
else:
    pass

if closest_guess in south_america:
    for item in range(500):
        enter_country.send_keys(random.choice(tuple(south_america)) + Keys.RETURN)
else:
    pass

if closest_guess in oceania:
    for item in range(500):
        enter_country.send_keys(random.choice(tuple(oceania)) + Keys.RETURN)
else:
    pass