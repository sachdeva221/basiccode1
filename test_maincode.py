from selenium.webdriver.common.by import By

from new_projec_test.Base import Base


class Test_maincode(Base):
    def test_initialcode(self):
        self.Driver.find_element(By.ID, "search-input").click()
        self.Driver.find_element(By.NAME, 'search_query').send_keys("python basic")
        self.Driver.find_element(By.CSS_SELECTOR, 'button[class="style-scope ytd-searchbox"]').click()

