import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

gdtotCookies = [
    {
        "name": "PHPSESSID",
        "value": "9c6gkcp8nfh308868u3bgvu3ak"
    },
    {
        "name": "_ga",
        "value": "GA1.2.330343945.1664316149"
    },
    {
        "name": "_gid",
        "value": "GA1.2.2067489530.1664477704"
    },
    {
        "name": "crypt",
        "value": "NzFCSExFUjB1ZFRITExFZTZRKzE4NUwxSCswbzVPRUw0MGxrbnpTdnl3cz0%3D"
    }
]

def getProperLink(link):
    half = link.split('=')[1].split('&')[0]
    full = f'https://drive.google.com/file/d/{half}/view?usp=sharing'
    return full

async def getGDToT(url):
    
    driver = uc.Chrome(use_subprocess=True)
    driver.get("https://new.gdtot.cfd")
    
    for x in range(len(gdtotCookies)):
        try:
            driver.add_cookie(gdtotCookies[x])
        except Exception as e:
            pass
        
    driver.refresh()
    driver.get("https://new.gdtot.cfd/upload-link")
    driver.find_element(By.CLASS_NAME, "form-control").send_keys(url)
    driver.find_element(By.XPATH, "//*[@id='storeli']").click()
    await asyncio.sleep(5)
    final = driver.find_element(By.XPATH, "//*[@id='card-link']/div/a").get_attribute("textContent")
    driver.quit()
    return final
