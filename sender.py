from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
import time

from database import get_contacts


def send_messages(message, image_path=None):

    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=./whatsapp_session")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://web.whatsapp.com")

    time.sleep(10) 

    wait = WebDriverWait(driver, 25)

    contacts = get_contacts()

    for contact in contacts:

        phone = contact[1]

        try:
            print(f"Sending to {phone}")

            # فتح الشات
            driver.get(f"https://web.whatsapp.com/send?phone={phone}")

            time.sleep(5)

            # لو الرقم مش شغال
            if "phone-number" in driver.current_url:
                print(f"Invalid WhatsApp number: {phone}")
                continue

            # انتظار مربع الرسالة
            box = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@contenteditable='true']")
                )
            )

            box.click()
            box.send_keys(message)
            box.send_keys(Keys.ENTER)

            # إرسال صورة (لو موجودة)
            if image_path:

                time.sleep(3)

                # فتح قائمة الإرفاق
                attach = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//div[@title='Attach']")
                    )
                )
                attach.click()

                # رفع الصورة
                file_input = wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//input[@type='file']")
                    )
                )
                file_input.send_keys(image_path)

                # انتظار رفع الصورة بالكامل (مهم جدًا)
                time.sleep(5)

                # إرسال الصورة
                send_btn = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//span[@data-icon='send']")
                    )
                )
                send_btn.click()

                time.sleep(2)

            # تأخير بين الرسائل
            time.sleep(4)

        except Exception as e:
            print(f"Error with {phone}: {e}")

    driver.quit()