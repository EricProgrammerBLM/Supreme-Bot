from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import datetime, time
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


print ('Below you will be asked personal information specifically for the checkout page on Supremes website.')
CreditCard = input('Enter your Credit/Debit Card Number Here: ')
print (CreditCard)
ExpMonth = input('Enter your Cards Expiration Month (Numbers Only. May would be 05, March would be 03, December would be 12 etc): ')
print (ExpMonth)
ExpYear = input('Enter your Cards Expiration Year: ')
print (ExpYear)
TheCVV = input('Enter your CVV Number: ')
print (TheCVV)
Merch = input ("Enter the Exact Name of the Merchandise/Clothing You Plan to Buy from Supremes website. Go there and copy and paste the namehere. PLEASE...Do not include the color, and no extra spaces: ")
print (Merch)

#---------------------Link Names----------------------------------



jackets = "https://www.supremenewyork.com/shop/all/jackets"
shirts = "https://www.supremenewyork.com/shop/all/shirts"
tops = "https://www.supremenewyork.com/shop/all/tops_sweaters"
sweaters = "https://www.supremenewyork.com/shop/all/tops_sweaters"
sweatshirts = "https://www.supremenewyork.com/shop/all/sweatshirts"
pants = "https://www.supremenewyork.com/shop/all/pants"
shorts = "https://www.supremenewyork.com/shop/all/shorts"
hats = "https://www.supremenewyork.com/shop/all/hats"
bags = "https://www.supremenewyork.com/shop/all/bags"
accessories = "https://www.supremenewyork.com/shop/all/accessories"
shoes = "https://www.supremenewyork.com/shop/all/shoes"
sneakers = "https://www.supremenewyork.com/shop/all/shoes"
skate = "https://www.supremenewyork.com/shop/all/skate"

#Get these links from the preview section. They allow you to preview future releases
print ('Category: jackets(1), shirts(2), tops/sweaters(3), sweatshirts(4), pants(5), shorts(6), hats(7), bags(8), accessories(9), shoes(10), sneakers(11), skate(12)')
Category = input('Which Category is Your Merch Under? Enter the Number next to the name of the Category only: ')
print (Category)


#------------------------End---------------------------------

Name = input('Enter your First and Last Name: ')
print (Name)
Email = input('Enter your email: ')
print (Email)
Phone = input('Enter your Phone Number: ')
print (Phone)
Address = input('Enter your street address. DO NOT include city, state, or zipcode.')
print (Address)
Unit = input('Enter your Apartment or Unit Number. If none, put 1: ')
print (Unit)
Zipcode = input('Enter your Zipcode: ')
print (Zipcode)
City = input('Enter your City: ')
print (City)
State = input('Enter your State Abbreviation (Example: New York would be NY): ')
State = State.upper()
print (State)
print ('')
print ('This bot has a Schedule feature. Below you will be asked at which hour, minute and second of the day you would like the bot to start. This bot uses military time, 6:00PM = 18:00:00, and 10:00AM = 10:00:00. Be as specific as you want.')
Hour = int(input('Which hour of the day would you like this bot to start: '))
print (Hour)
Min = int(input('Which minute of the hour would you like this bot to start: '))
print (Min)
Sec = int(input('Which second of the minute would you like this bot to start: '))
print (Sec)
    
AddProxy = input('Do you have a Proxy: ')
if AddProxy == 'yes' or AddProxy == 'Yes':
    print ('Your proxy should look like this: 109.98.36.23:38474 - Basically enter the IP:PORT or HOST:PORT')
    PROXY = input('Enter your Proxy Here: ') # IP:PORT or HOST:PORT
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    #the code here before was simple webdriver code pointing to the path of where
    #the webdriver chrome was on my computer, if ever a problem, download chrome webdriver
    #put path here, and leave ,chrome_options as is
    #This new code basically calls to update the chrome if it is ever outdated
    #Make sure to 'pip install webdriver-manager' first
else:
    print ('Continuing without Proxy...')
    driver = webdriver.Chrome(ChromeDriverManager().install())

#Supreme Bot written by Eric Byam @therealericny


#----------------------------------------THERE ARE 4 STEPS




Slow = 0 #CHANGE THIS TO ZERO 0 BEFORE YOU USE - #STEP 1
#NO EXTRA SPACE SHOULD BE INCLUDED
#This should be the name of the merch you're getting. Color not included
#STEP 2

#----------------------Starting-------------------

driver.get('https://www.bing.com/')

#-------------------------Time-------------------------
def Schedule(hour1, min2, sec3):
    hour1 = int(hour1)
    min2 = int(min2)
    sec3 = int(sec3)
    today = datetime.datetime.now()
    Activate = (datetime.datetime(today.year, today.month, today.day, hour1, min2, sec3) - today).seconds     #STEP 3 CHOOSE THE TIME YOU WANT IT TO CONTINUE AT AFTER LAUNCHING THE BROWSER
#Uses Military Time 23, 25, 0 = 11:25:00PM                                                       #STEP 4 MAKE SURE YOUR NIKE CART IS COMPLETELY EMPTY
    print('Waiting for ' + str(datetime.timedelta(seconds=Activate)))
    time.sleep(Activate)
#Rest of the code will activate at the correct time that you set it

#Schedule() #Uncomment this

StartUp = input('Would you like this bot to start at the scheduled time? ')
if StartUp == 'yes' or StartUp == 'Yes':
    Schedule(Hour, Min, Sec)
else:
    print ('Scheduled timing not needed...continuing without')
    StartBot = input('Press the Enter Key when you are ready to run the bot.')

#--------------------Category
#Category: jackets(1), shirts(2), tops/sweaters(3), sweatshirts(4), pants(5), shorts(6), hats(7), bags(8), accessories(9), shoes(10), sneakers(11), skate(12)
if Category =='1':
    driver.get(jackets)
elif Category =='2':
    driver.get(shirts)
elif Category =='3':
    driver.get(tops)
elif Category =='4':
    driver.get(sweatshirts)
elif Category =='5':
    driver.get(pants)
elif Category =='6':
    driver.get(shorts)
elif Category =='7':
    driver.get(hats)
elif Category =='8':
    driver.get(bags)
elif Category =='9':
    driver.get(accessories)
elif Category =='10':
    driver.get(shoes)
elif Category =='11':
    driver.get(sneakers)
elif Category =='12':
    driver.get(skate)
else:
    print('Category was entered incorrectly')

#-------------------Category
#STEP 4
#Change this to the link of the general name
#of where the merch you will be buying from
#The link of where the jackets, shorts, hats are on the Supreme site.

driver.implicitly_wait(900)
driver.find_element_by_link_text(Merch).send_keys(Keys.RETURN)

driver.implicitly_wait(900)


Cart = ("//input[@name='commit' and @value='add to cart']")
driver.find_element_by_xpath(Cart).click()
#Clicks add to cart
    

#driver.implicitly_wait(900) Was here before explicit wait

wait = WebDriverWait(driver,900)
wait.until(EC.presence_of_element_located((By.ID, 'items-count')))

checkout = "//a[@data-no-turbolink='true']"
driver.find_element_by_xpath(checkout).click()

driver.implicitly_wait(20)
driver.find_element_by_id('order_billing_name').send_keys(Name)
driver.find_element_by_id('order_email').send_keys(Email)
driver.find_element_by_id('order_tel').send_keys(Phone)
driver.find_element_by_id('bo').send_keys(Address)
driver.find_element_by_id('oba3').send_keys(Unit)
driver.find_element_by_id('order_billing_zip').send_keys(Zipcode)
driver.find_element_by_id('order_billing_city').send_keys(City)
opt = driver.find_element_by_id('order_billing_state')
dropdown = Select(opt)
dropdown.select_by_visible_text(State)
driver.find_element_by_id('store-address').click()
Input = "//input[@placeholder='number']"
CVV = "//input[@placeholder='CVV']"
driver.find_element_by_xpath(Input).send_keys(CreditCard)
driver.find_element_by_xpath(CVV).send_keys(TheCVV)
driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()

opt2 = driver.find_element_by_id('credit_card_month')
dropdown2 = Select(opt2)
dropdown2.select_by_visible_text(ExpMonth)

opt3 = driver.find_element_by_id('credit_card_year')
dropdown3 = Select(opt3)
dropdown3.select_by_visible_text(ExpYear)
sleep(Slow) #CHANGE TO THE NUMBER ZERO 0 BEFORE U USE
Pay = "//input[@value='process payment']"
driver.find_element_by_xpath(Pay).click()

