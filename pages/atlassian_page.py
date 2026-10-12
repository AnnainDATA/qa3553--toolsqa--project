from selenium.webdriver.common.by import By

POPUP_POSITIVE_MESSAGE = (By.XPATH,"//div[@class = '_11c8fhey _1reo1wug _18m91wug _c71l53f4 _1i4qfg65']")
ERROR_MESSAGE_FIRST = (By.XPATH,"//*[]")

def has_message(self,message:str)->bool:
    return self.is_text_present(self.POPUP_POSITIVE_MESSAGE,message)
