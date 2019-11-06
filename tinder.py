from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
class tinder:
  def Link_Connect(self):
      tindprofile = webdriver.FirefoxProfile('C:/Users/Ongund/AppData/Roaming/Mozilla/Firefox/Profiles/7tv74fmp.tinderpro') 
      browser = webdriver.Firefox(tindprofile)
      browser.get('https://tinder.com/')
      time.sleep(10)
      people_count = 0
      new_matches = 0
      mess_cnt = 0
      while True: 
        try:
          likebutton = browser.find_element_by_css_selector("button[aria-label='Like']").click()
          people_count += 1
          time.sleep(3)
        except:
          try: 
            browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/button[2]").click() #click no thanks button
            people_count = people_count - 1
            break 
          except: 
            browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/a").click()
            new_matches += 1
      print("---Liked, " +str(people_count)+ " people. Got " +str(new_matches)+ " new matches." ) 
      all_new_matches = browser.find_elements_by_css_selector("div[class='P(8px) Ta(c)']")
      for i in range(1,len(all_new_matches)):
        browser.find_element_by_css_selector("div[class='Cur(p)']").click() 
        all_new_matches[i].click()
        time.sleep(3)
        name = browser.find_element_by_css_selector("span[class='Fz($xl) Fw($bold) Fxs($flx1) Flw(w) Pend(8px)']") 
        age = browser.find_element_by_css_selector("span[class='Whs(nw) Fz($l)']") 
        first_message = ""
        second_message = " "
        third_message = ""
        message_array = [first_message,second_message,third_message]
        text_box = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[2]/form/textarea")
        text_box.clear() 
        text_box.send_keys(message_array[random.randint(1,len(message_array)-1)])
        mess_cnt += 1
        text_box.send_keys(Keys.RETURN)
      print("---Messaged: " +str(mess_cnt)+ " new people.")


start_time = time.time() 
ed = tinder()
ed.Link_Connect()
print ("---Took: " +str(round((time.time() - start_time)/60))+ " minute(s).") 
