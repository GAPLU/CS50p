import time
import io

from PIL import Image
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


PATH = "C:\Code\chromedriver.exe"
options = Options()
options.binary_location = (
    "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"
)


def get_images_from_google(delay, max_images, queries):
    wd = webdriver.Chrome(options=options, executable_path=PATH)
    for query in queries:
        find = query["word"]
        id = query["id"]
        find = find.replace(" ", "+")
        url = f"https://www.freepik.com/search?format=search&last_filter=orientation&last_value=landscape&orientation=landscape&query={find}&selection=1&type=photo"
        wd.get(url)

        image_urls = set()
        skips = 0

        while len(image_urls) + skips < max_images:
            thumbnails = wd.find_elements(By.CLASS_NAME, "js-detail-data-link")

            for img in thumbnails[len(image_urls) + skips : max_images]:
                try:
                    img.click()
                    time.sleep(delay)
                except:
                    continue

                images = wd.find_elements(By.CLASS_NAME, "thumb")
                for image in images:
                    if image.get_attribute("src") in image_urls:
                        max_images += 1
                        skips += 1
                        break

                    if image.get_attribute("src") and "http" in image.get_attribute(
                        "src"
                    ):
                        image_urls.add(image.get_attribute("src"))

        image_urls = list(image_urls)

        try:
            image_content = requests.get(image_urls[0]).content
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file)

            original_width, original_height = image.size
            if original_width > 390 and original_height > 260:
                ratio = original_height / original_width
                new_height = 390 * ratio
                image = image.resize((390, int(new_height)), Image.ANTIALIAS)

            file_path = f"images/{str(id)}.jpg"

            with open(file_path, "wb") as f:
                image.save(f, "JPEG")

        except Exception as e:
            print("FAILED -", e)
