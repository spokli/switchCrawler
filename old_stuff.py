
# def check_mediamarkt(url):

#     driver = webdriver.Chrome(options=chrome_options)
#     # driver = webdriver.Chrome()
#     driver.get(url)

#     button = driver.find_element_by_class_name("IRVNX")

#     actions = ActionChains(driver)
#     touch_actions = TouchActions(driver)

#     actions.move_to_element(button)
#     for i in range(10):
#         actions.key_down(Keys.DOWN)

#     actions.perform()

#     time.sleep(1)
#     button.click()
    
#     driver.get("https://www.mediamarkt.de/checkout")

#     time.sleep(1)

#     try:
#         not_available = driver.find_elements_by_xpath("//*[contains(text(), '')]")
#     except:
#         # Not found -> might be available!
#         result = None
    
#     if len(not_available) > 0:
#         # Found -> not available
#         result = False
#     else:
#         # Not found -> available
#         result = True

#     driver.quit()
#     return result

# def check_saturn(url):
#     # Create driver
#     driver = webdriver.Chrome(options=chrome_options)
    
#     # Call website
#     driver.get(url)

#     # Add to cart button
#     button = driver.find_element_by_id("pdp-add-to-cart")
#     button.click()
    
#     time.sleep(1)

#     # Call cart website
#     driver.get("https://www.saturn.de/webapp/wcs/stores/servlet/MultiChannelDisplayBasket?langId=-3")

#     time.sleep(1)

#     # Check availability text
#     try:
#         not_available = driver.find_elements_by_xpath("//*[contains(text(), 'Eine Lieferung ist nicht möglich, da der Artikel online ausverkauft ist.')]")
#     except:
#         # Not found -> might be available!
#         result = None
    
#     if len(not_available) > 0:
#         # Found -> not available
#         result = False
#     else:
#         # Not found -> available
#         result = True

#     driver.quit()
#     return result

# def check_lidl(url):
#     # Create driver
#     driver = webdriver.Chrome(options=chrome_options)
    
#     # Call website
#     driver.get(url)

#     time.sleep(2)

#     button = driver.find_element_by_class_name("cookie-alert-extended-button")

#     button.click()

#     time.sleep(1)

#     # Check availability text
#     try:
#         not_available = driver.find_elements_by_xpath("//*[contains(normalize-space(), 'Dieser Artikel ist demnächst für Sie verfügbar')]")

#         if len(not_available) > 0:
#             # Found -> not available
#             result = False
#         else:
#             # Not found -> available
#             result = True

#     except:
#         # Not found -> might be available!
#         result = None
    
#     finally:
#         driver.quit()

#     return result
