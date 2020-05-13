#!/usr/bin/env python
# coding: utf8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
# from selenium.webdriver.common.exceptions.NoSuchElementException import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time, datetime
from pyvirtualdisplay import Display

import argparse
parser = argparse.ArgumentParser(description='')
parser.add_argument('--stores', dest='stores', default='all', help="name of stores to check. 'all' for all")
parser.add_argument('--withtest', action='store_true', help="set this if positive tests should be done for available products")
parser.add_argument('--visible', action='store_true', help="set this if the process should run in a visible window")

args = parser.parse_args()
stores = args.stores
withtest = args.withtest
visible = args.visible

check_positive = withtest

# Start virtual display
display = Display(visible=(1 if visible else 0), size=(1920, 1080))  
display.start()

chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu") 
if not visible:
    chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")


amazon_url_grey = "https://www.amazon.de/Nintendo-Switch-Konsole-Grau-2019/dp/B07W13KJZC"
mm_url_grey = "https://www.mediamarkt.de/de/product/_switch-grau-neue-edition-nintendo-switch-konsolen-2584584.html"
saturn_url_grey = "https://www.saturn.de/de/product/_nintendo-switch-grau-neue-edition-2584584.html"
lidl_url_grey = "https://www.lidl.de/de/nintendo-switch-konsole-grau/p311460"
otto_url_grey = "https://www.otto.de/p/nintendo-switch-neues-modell-959859613/#variationId=959859614"
conrad_url_grey = "https://www.conrad.de/de/p/switch-konsole-grau-v2-2019-2163187.html"

amazon_url_rb = "https://www.amazon.de/Nintendo-Switch-Konsole-Neon-Rot-Neon-Blau/dp/B07WKNQ8JT"
mm_url_rb = "https://www.mediamarkt.de/de/product/_switch-neon-rot-neon-blau-neue-edition-nintendo-switch-konsolen-2584585.html"
saturn_url_rb = "https://www.saturn.de/de/product/_nintendo-switch-neon-rot-neon-blau-neue-edition-2584585.html"
lidl_url_rb = "https://www.lidl.de/de/nintendo-switch-konsole-neon-rot-neon-blau/p311463"
otto_url_rb = "https://www.otto.de/p/nintendo-switch-neues-modell-941579551/#variationId=941579552"
conrad_url_rb = "https://www.conrad.de/de/p/switch-konsole-grau-neonblau-neonrot-v2-2019-2163186.html"


def check_general(url, 
    availability_text, 
    button_search_criterion=None, 
    button_search_value=None, 
    scroll_down=False,
    cart_url=None):

    try:

        # Create driver
        driver = webdriver.Chrome('./chromedriver', options=chrome_options)
        
        # Call website
        driver.get(url)

        time.sleep(5)

        if button_search_criterion is not None:

            if button_search_criterion is 'class':
                button = driver.find_element_by_class_name(button_search_value)

            elif button_search_criterion is 'id':
                button = driver.find_element_by_id(button_search_value)

            if button is None:
                driver.quit()
                return None

            if scroll_down:
                driver.execute_script("arguments[0].scrollIntoView()", button); 

                # actions = ActionChains(driver)
                # actions.move_to_element(button)
                # for i in range(10):
                #     actions.key_down(Keys.DOWN)

                # actions.perform()
                # time.sleep(5)

            button.click()
            time.sleep(5)

        if cart_url is not None:
            driver.get(cart_url)
            time.sleep(5)

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

def print_html_header():
    print("<html><head></head><body><h2>"+ str(datetime.datetime.now()) +"</h2>")
    print("<table>")

def print_html_footer():
    print("</table></body></html>")

def print_html_for_vendor(name, avail_grey, avail_grey_url, avail_rb, avail_rb_url, test):
    print("<tr>")
    
    print("<td>")
    print("<b>"+name+" </b>", end='')
    print("</td>")
    
    # GREY
    print("<td>")
    if test is not True or avail_grey is None:
        print("<p style='color: yellow'>not sure</p>")

    else:
        if avail_grey is True:
            print("<a href="+avail_grey_url+" style='color: green' target='_'>grey AVAILABLE</a>")
        else:
            print("<a href="+avail_grey_url+" style='color: red' target='_'>grey not available</p>")
    print("</td>")

    # RED BLUE
    print("<td>")
    if test is not True or avail_rb is None:
        print("<p style='color: yellow'>not sure</p>")

    else:
        if avail_rb is True:
            print("<a href="+avail_rb_url+" style='color: green' target='_'>red-blue AVAILABLE</a>")
        else:
            print("<a href="+avail_rb_url+" style='color: red' target='_'>red-blue not available</p>")
    print("</td>")

    print("</tr>")

#==============================================
#==============================================
# MAIN PROGRAM 
#==============================================
#==============================================
print_html_header()

# Amazon
# print("Checking amazon...")
if 'amazon' in stores or 'all' in stores:
    avail_amazon_grey = not check_general(
        url=amazon_url_grey,
        availability_text="diesen Anbietern")

    avail_amazon_rb = not check_general(
        url=amazon_url_rb,
        availability_text="diesen Anbietern")

    avail_amazon_positive = True
    if check_positive:
        avail_amazon_positive = not check_general(
            url="https://www.amazon.de/Dr-Kawashimas-Gehirn-Jogging-Nintendo-Switch/dp/B07Z52WCLL",
            availability_text="diesen Anbietern")

    print_html_for_vendor("Amazon", avail_amazon_grey, amazon_url_grey, avail_amazon_rb, amazon_url_rb, avail_amazon_positive)


# # Media Markt
# print("Checking Media Markt...")
if 'mm' in stores or 'all' in stores:
    avail_mm_grey = not check_general(
        url=mm_url_grey,
        availability_text="Online leider nicht mehr verfügbar",
        button_search_criterion='class', 
        button_search_value="bBMQBs",
        scroll_down=True,
        cart_url="https://www.mediamarkt.de/checkout")

    avail_mm_rb = not check_general(
        url=mm_url_rb,
        availability_text="Dieser Artikel ist aktuell nicht verfügbar",
        # button_search_criterion='class', 
        # button_search_value="IRVNX",
        # scroll_down=True,
        # cart_url="https://www.mediamarkt.de/checkout"
    )

    avail_mm_positive = True
    if check_positive:
        avail_mm_positive = not check_general(
            url="https://www.mediamarkt.de/de/product/_sandisk-ultra%C2%AE-microsdxc%E2%84%A2-uhs-i-2317003.html",
            availability_text="Online leider nicht mehr verfügbar",
            button_search_criterion='class', 
            button_search_value="IRVNX",
            scroll_down=True,
            cart_url="https://www.mediamarkt.de/checkout")

    print_html_for_vendor("Media Markt", avail_mm_grey, mm_url_grey, avail_mm_rb, mm_url_rb, avail_mm_positive)


# Saturn
#print("Checking Saturn...")
if 'saturn' in stores or 'all' in stores:
    avail_saturn_grey = not check_general(
        url=saturn_url_grey,
        availability_text="In ausgewählten Märkten verfügbar"
        # availability_text="Eine Lieferung ist nicht möglich, da der Artikel online ausverkauft ist",
        # button_search_criterion='id', 
        # button_search_value="pdp-add-to-cart",
        # cart_url="https://www.saturn.de/webapp/wcs/stores/servlet/MultiChannelDisplayBasket?langId=-3"
    )

    avail_saturn_rb = not check_general(
        url=saturn_url_rb,
        availability_text="In ausgewählten Märkten verfügbar"
        # availability_text="Eine Lieferung ist nicht möglich, da der Artikel online ausverkauft ist",
        # button_search_criterion='id', 
        # button_search_value="pdp-add-to-cart",
        # cart_url="https://www.saturn.de/webapp/wcs/stores/servlet/MultiChannelDisplayBasket?langId=-3"
    )

    avail_saturn_positive = True
    if check_positive:
        avail_saturn_positive = not check_general(
            url="https://www.saturn.de/de/product/_animal-crossing-new-horizons-simulation-2626931.html",
            availability_text="In ausgewählten Märkten verfügbar"
            # button_search_criterion='id', 
            # button_search_value="pdp-add-to-cart",
            # cart_url="https://www.saturn.de/webapp/wcs/stores/servlet/MultiChannelDisplayBasket?langId=-3"
        )

    print_html_for_vendor("Saturn", avail_saturn_grey, saturn_url_grey, avail_saturn_rb, saturn_url_rb, avail_saturn_positive)


# Lidl
#print("Checking LIDL...")
if 'lidl' in stores or 'all' in stores:
    avail_lidl_grey = not check_general(
        url=lidl_url_grey,
        availability_text="Dieser Artikel ist demnächst für Sie verfügbar",
        button_search_criterion='class', 
        button_search_value="cookie-alert-extended-button")

    avail_lidl_rb = not check_general(
        url=lidl_url_rb,
        availability_text="Dieser Artikel ist demnächst für Sie verfügbar",
        button_search_criterion='class', 
        button_search_value="cookie-alert-extended-button")

    avail_lidl_positive = True
    if check_positive:
        avail_lidl_positive = not check_general(
            url="https://www.lidl.de/de/nintendo-dr-kawashimas-gehirn-jogging-nintendo-switch/p319510",
            availability_text="Dieser Artikel ist demnächst für Sie verfügbar",
            button_search_criterion='class', 
            button_search_value="cookie-alert-extended-button")

    print_html_for_vendor("LIDL", avail_lidl_grey, lidl_url_grey, avail_lidl_rb, lidl_url_rb, avail_lidl_positive)


# Otto
#print("Checking Otto...")
if 'otto' in stores or 'all' in stores:
    avail_otto_grey = not check_general(
        url=otto_url_grey,
        availability_text="lieferbar Ende Juni")

    avail_otto_rb = not check_general(
        url=otto_url_rb,
        availability_text="lieferbar Ende Juni")

    avail_otto_positive = True
    if check_positive:
        avail_otto_positive = not check_general(
            url="https://www.otto.de/p/nintendo-switch-lite-967565701/#variationId=967565702",
            availability_text="lieferbar Ende Juni")

    print_html_for_vendor("Otto", avail_otto_grey, otto_url_grey, avail_otto_rb, otto_url_rb, avail_otto_positive)


# Conrad
#print("Checking Conrad...")
if 'conrad' in stores or 'all' in stores:
    avail_conrad_grey = not check_general(
        url=conrad_url_grey,
        availability_text="Der gewünschte Artikel ist leider nicht verfügbar")

    avail_conrad_rb = not check_general(
        url=conrad_url_rb,
        availability_text="Der gewünschte Artikel ist leider nicht verfügbar")

    avail_conrad_positive = True
    if check_positive:
        avail_conrad_positive = not check_general(
            url="https://www.conrad.de/de/p/nintendo-switch-konsole-32-gb-tuerkis-2162597.html",
            availability_text="Der gewünschte Artikel ist leider nicht verfügbar")

    print_html_for_vendor("Conrad", avail_conrad_grey, conrad_url_grey, avail_conrad_rb, conrad_url_rb, avail_conrad_positive)

# End of Store processing
print_html_footer()
display.stop()

