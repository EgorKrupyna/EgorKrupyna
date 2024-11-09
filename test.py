from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Ініціалізація драйвера для Google Chrome
driver = webdriver.Chrome()  # Переконайтеся, що у вас встановлений ChromeDriver і він у PATH

# Відкриваємо Google
driver.get("http://www.google.com")

# Перевіряємо, що сторінка Google завантажилася
assert "Google" in driver.title

# Знаходимо поле пошуку за допомогою імені (name) елемента
search_box = driver.find_element(By.NAME, "q")

# Вводимо пошуковий запит
search_box.send_keys("wowpowers.com")

# Натискаємо Enter, щоб виконати пошук
search_box.send_keys(Keys.RETURN)

# Очікуємо кілька секунд для завантаження результатів
time.sleep(2)

# Перевіряємо, чи з'явилося посилання на wowpowers.com
if "wowpowers.com" in driver.page_source:

# Знаходимо посилання і натискаємо на нього
link = driver.find_element(By.PARTIAL_LINK_TEXT, "wowpowers.com")
link.click()  # Клік на посилання

# Додатково можна додати паузу, щоб перевірити, що сторінка завантажилася
time.sleep(2)

# Шукаємо посилання "Forgot your password?" і натискаємо на нього
reset_password_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot your password?")
reset_password_link.click()  # Клік на "Forgot your password?"

# Додаткова пауза, щоб перевірити, що сторінка завантажилася
time.sleep(2)

# Знаходимо поле "Email or Username" за допомогою атрибута placeholder
email_or_username_field = driver.find_element(By.XPATH, "//input[@placeholder='Email or Username']")

# Вводимо текст "test@gmail" в поле
email_or_username_field.send_keys("test@gmail.com")

# Знаходимо елемент з текстом "Reset Password"
reset_password_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Reset Password')]")

# Клік на елемент з текстом "Reset Password"
reset_password_element.click()

# Закриваємо браузер
driver.quit()