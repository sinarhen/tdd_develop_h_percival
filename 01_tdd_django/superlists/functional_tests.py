from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """Тест нового посетителя"""

    def setUp(self):
        """установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """Демонтаж"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Тест: можно начать список и получить его позже"""
        # Эдит слышала про крутое новое онлайн приложение
        # со списком неотложных дел
        # она решает оценить его домашнюю страницу
        self.browser.get('http://127.0.0.1:8000')

        # Она видит что заголовок и шапка страницы говорят о списках
        # неотложных дел
        self.assertIn('The', self.browser.title)
        self.fail('Закончить тест!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
