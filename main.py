from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class GoogleKeywordScreenshooter():
    def __init__(self,keyword,screenshots_dir):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())  
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir

    def start(self):
        self.browser.get("http://google.com")
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)

        try:
            shitty_element = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.CLASS_NAME, "g-blk")))

            self.browser.execute_script(
                """
                const shitty = arguments[0]
                console.log(shitty)
                shitty.parentElement.removeChild(shitty)
            """,shitty_element)
        except:
            pass

        search_results = self.browser.find_elements_by_class_name("g")

        for index,search_result in enumerate(search_results):
            class_name = search_result.get_attribute("class")
            if "kno-kp mnr-c g-blk" not in class_name:
                search_result.screenshot(f"{self.screenshots_dir}/{self.keyword}x{index}.png")
    
    def end(self):
        self.browser.quit()


googleKeyword_Screenshooter = GoogleKeywordScreenshooter("python book","screenshots")
googleKeyword_Screenshooter.start()
googleKeyword_Screenshooter.end()