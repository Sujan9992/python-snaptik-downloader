from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from link_parser import parse_links


def main(links_list: list[str], driver: WebDriver) -> None:
    for i in range(len(links_list)):
        driver.get("https://snaptik.app/")
        search_box: WebElement = driver.find_element(By.ID, "url")
        search_box.send_keys(links_list[i])
        search_box.submit()
        try:
            download_button: WebElement = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "download-file"))
            )
        except Exception:
            print("Timeout")
            continue
        else:
            download_button.send_keys(Keys.CONTROL, Keys.ENTER)
            sleep(5)


if __name__ == "__main__":
    # Path to the text file containing links
    file_path: str = "text.txt"

    # Parse links from the text file
    parsed_links: list[str] = parse_links(file_path)
    print(f"Found {len(parsed_links)} links in file")
    driver: WebDriver = webdriver.Chrome()

    main(parsed_links, driver)
    driver.quit()
