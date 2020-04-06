#!/usr/bin/env python
# coding: utf8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
# from selenium.webdriver.common.exceptions.NoSuchElementException import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from pyvirtualdisplay import Display

# Start virtual display
display = Display(visible=0, size=(1920, 1080))  
display.start()

chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu") 
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")

def check_general(url, 
    availability_text, 
    button_search_criterion=None, 
    button_search_value=None, 
    scroll_down=False,
    cart_url=None):

    # Create driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Call website
    driver.get(url)

    time.sleep(2)

    if button_search_criterion is not None:

        if button_search_criterion is 'class':
            button = driver.find_element_by_class_name(button_search_value)

        elif button_search_criterion is 'id':
            button = driver.find_element_by_id(button_search_value)            

        if scroll_down:
            actions = ActionChains(driver)
            actions.move_to_element(button)
            for i in range(10):
                actions.key_down(Keys.DOWN)

            actions.perform()
            time.sleep(5)

        button.click()
        time.sleep(5)

    if cart_url is not None:
        driver.get(cart_url)
        time.sleep(5)

    try:
        text_occurences = driver.find_elements_by_xpath("//*[contains(normalize-space(), '" + availability_text + "')]")

        if len(text_occurences) > 0:
            # Found
            result = True
        else:
            # Not found
            result = False

    except:
        # Not found -> unsure
        result = None
    
    finally:
        driver.quit()

    return result

# Amazon
print("Checking amazon...")
avail_amazon = not check_general(
    url="https://www.amazon.de/Nintendo-Switch-Konsole-Grau-2019/dp/B07W13KJZC",
    availability_text="diesen Anbietern")

# Media Markt
print("Checking Media Markt...")
avail_mm = not check_general(
    url="https://www.mediamarkt.de/de/product/_switch-grau-neue-edition-nintendo-switch-konsolen-2584584.html",
    availability_text="Online leider nicht mehr verfügbar",
    button_search_criterion='class', 
    button_search_value="IRVNX",
    scroll_down=True,
    cart_url="https://www.mediamarkt.de/checkout")

# Saturn
print("Checking Saturn...")
avail_saturn = not check_general(
    url="https://www.saturn.de/de/product/_nintendo-switch-grau-neue-edition-2584584.html",
    availability_text="Eine Lieferung ist nicht möglich, da der Artikel online ausverkauft ist",
    button_search_criterion='id', 
    button_search_value="pdp-add-to-cart",
    cart_url="https://www.saturn.de/webapp/wcs/stores/servlet/MultiChannelDisplayBasket?langId=-3")

# Lidl
print("Checking LIDL...")
avail_lidl = not check_general(
    url="https://www.lidl.de/de/nintendo-switch-konsole-grau/p311460",
    availability_text="Dieser Artikel ist demnächst für Sie verfügbar",
    button_search_criterion='class', 
    button_search_value="cookie-alert-extended-button")

# Otto
print("Checking Otto...")
avail_otto = not check_general(
    url="https://www.otto.de/p/nintendo-switch-neues-modell-959859613/#variationId=959859614",
    availability_text="lieferbar Ende Juni")

# Conrad
print("Checking Conrad...")
avail_conrad = not check_general(
    url="https://www.conrad.de/de/p/switch-konsole-grau-v2-2019-2163187.html",
    availability_text="Der gewünschte Artikel ist leider nicht verfügbar")


print("Availabilities:")
print("Amazon:", avail_amazon)
print("Media Markt: ", avail_mm)
print("Saturn: ", avail_saturn)
print("Lidl: ", avail_lidl)
print("Otto: ", avail_otto)
print("Conrad: ", avail_conrad)


# # ===========================
# # Positive tests
# # ===========================

# Amazon
avail_amazon_positive = not check_general(
    url="https://www.amazon.de/Dr-Kawashimas-Gehirn-Jogging-Nintendo-Switch/dp/B07Z52WCLL",
    availability_text="diesen Anbietern")

# # Media Markt
avail_mm_positive = not check_general(
    url="https://www.mediamarkt.de/de/product/_sandisk-ultra%C2%AE-microsdxc%E2%84%A2-uhs-i-2317003.html",
    availability_text="Online leider nicht mehr verfügbar",
    button_search_criterion='class', 
    button_search_value="IRVNX",
    scroll_down=True,
    cart_url="https://www.mediamarkt.de/checkout")

# # Saturn
avail_saturn_positive = not check_general(
    url="https://www.saturn.de/de/product/_animal-crossing-new-horizons-simulation-2626931.html",
    availability_text="Eine Lieferung ist nicht möglich, da der Artikel online ausverkauft ist",
    button_search_criterion='id', 
    button_search_value="pdp-add-to-cart",
    cart_url="https://www.saturn.de/webapp/wcs/stores/servlet/MultiChannelDisplayBasket?langId=-3")

# # Lidl
avail_lidl_positive = not check_general(
    url="https://www.lidl.de/de/nintendo-dr-kawashimas-gehirn-jogging-nintendo-switch/p319510",
    availability_text="Dieser Artikel ist demnächst für Sie verfügbar",
    button_search_criterion='class', 
    button_search_value="cookie-alert-extended-button")

# # Otto
avail_otto_positive = not check_general(
    url="https://www.otto.de/p/nintendo-switch-lite-967565701/#variationId=967565702",
    availability_text="lieferbar Ende Juni")

# Conrad
avail_conrad_positive = not check_general(
    url="https://www.conrad.de/de/p/nintendo-switch-konsole-32-gb-tuerkis-2162597.html",
    availability_text="Der gewünschte Artikel ist leider nicht verfügbar")

print()
print("POSITIVE TESTS")
print("Amazon:", avail_amazon_positive)
print("Media Markt: ", avail_mm_positive)
print("Saturn: ", avail_saturn_positive)
print("Lidl: ", avail_lidl_positive)
print("Otto: ", avail_otto_positive)
print("Conrad: ", avail_conrad_positive)


# müller https://www.mueller.de/search/?q=Nintendo+Switch&filter.from_PRICE=7&filter.to_PRICE=379&price_range_changed=false&sortBy=pricedesc
# expert https://www.expert.de/suche?q=Nintendo+Switch&sort=price_desc
# euronics https://www.euronics.de/spiele-und-konsolen-film-und-musik/spiele-und-konsolen/nintendo-switch/spielkonsole/
