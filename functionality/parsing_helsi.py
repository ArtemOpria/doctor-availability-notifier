import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .driver import Driver
from .message import Message


class HelsiSlots:

    def __init__(self, driver: Driver):
        self._driver = driver
        self.exception_days = []
        self.slots_dict = {}

    @classmethod
    def create_instance(cls, driver: Driver):
        instance = cls(driver)
        instance._driver.open_page()
        return instance

    def get_helsi_slots(self):
        self.click_show_more_slots()
        self.fill_slots_dictionary()
        return str(Message(self._driver, self.slots_dict))

    def click_show_more_slots(self):
        self._driver.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[class='ShowMoreBtn_btnWrapper__brKhH']"))
        ).click()

    def click_arrow_right(self):
        self._driver.find_element(By.CLASS_NAME, value="arrow-right").click()

    def get_columns(self):
        return self._driver.find_elements(By.CSS_SELECTOR, 'div[data-index]')

    @staticmethod
    def get_slot_date(column):
        pattern_title = r"\d+\s\w+"
        match_title = re.search(pattern_title, column.text)
        return match_title.group(0) if match_title else None

    @staticmethod
    def find_available_slots(column):
        return column.find_elements(
            By.CSS_SELECTOR,
            value=f"div[class*=slot_available]")

    def fill_slots_dictionary(self):
        columns = self.get_columns()[:14]

        for idx, column in enumerate(columns):
            available_slots = HelsiSlots.find_available_slots(column)
            slot_date = HelsiSlots.get_slot_date(column)
            exception_days_lower = list(map(lambda el: el.lower(), self.exception_days))

            if slot_date.lower() not in exception_days_lower:
                self.slots_dict[slot_date] = [available_slot.text for available_slot in available_slots]

            if idx + 1 < len(columns):
                next_column = columns[idx + 1]
                next_slot_date = HelsiSlots.get_slot_date(next_column)

                if next_slot_date is None:
                    self.click_arrow_right()
