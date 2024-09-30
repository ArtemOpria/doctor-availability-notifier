from .driver import Driver
from selenium.webdriver.common.by import By


class DoctorInfo:

    def __init__(self, driver: Driver, doctor_name: str = None, doctor_speciality: str = None):
        self._doctor_name = doctor_name
        self._doctor_speciality = doctor_speciality
        self._driver = driver
        self.parse_doctor_name()
        self.parse_doctor_speciality()

    @property
    def doctor_name(self):
        return self._doctor_name

    @property
    def doctor_speciality(self):
        return self._doctor_speciality

    def parse_doctor_name(self):
        self._doctor_name = self._driver.find_element(By.CSS_SELECTOR, 'h1[class*="doctor-name"]').text

    def parse_doctor_speciality(self):
        self._doctor_speciality = self._driver.find_element(By.CSS_SELECTOR, 'div[class*="doctor-speciality_"]').text
