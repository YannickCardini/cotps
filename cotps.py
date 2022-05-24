from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import DesiredCapabilities


class Cotps(object):
    def __init__(self):
        self.delay = 7
        self.driver = self.launchBrowser()
        self.phoneNumber = ''

    def launchBrowser(self,headless=True):
        
        options = Options()
        options.add_argument("--window-size=1920,1080")
        if(headless):
            options.add_argument('--headless')  # example
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # print("Connecting to the wed-driver...")
        # driver = webdriver.Remote("http://0.0.0.0:4444/wd/hub", options=options )
        # print("Diver connected !")

        """Start web driver"""
        # d = DesiredCapabilities.CHROME
        # d['loggingPrefs'] = {'performance': 'ALL'}
        # opt = webdriver.ChromeOptions()
        # if(headless):
        #     opt.add_argument("--headless")
        # opt.add_argument("--disable-xss-auditor")
        # opt.add_argument("--disable-web-security")
        # opt.add_argument("--allow-running-insecure-content")
        # opt.add_argument("--no-sandbox")
        # opt.add_argument("--disable-setuid-sandbox")
        # opt.add_argument("--disable-webgl")
        # opt.add_argument("--disable-popup-blocking")
        # opt.add_argument("--window-size=1920,1080")

        # driver = webdriver.Chrome(options=opt,desired_capabilities=d)

        return driver

    def get_country_xpath(self,country):
        france = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[73]'
        thailand = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[201]'
        germany = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[79]'
        united_kingdom = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[214]'
        canada = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[39]'
        spain = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[40]'
        switzerland =  '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[196]'
        belgium =  '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[24]'
        return {
            'fr': france,
            '33':france,
            '+33':france,
            'be': belgium,
            '32':belgium,
            '+32':belgium,
            'th': thailand,
            '66':thailand,
            '+66':thailand,
            'de': germany,
            '49':germany,
            '+49':germany,
            'uk': united_kingdom,
            'gb': united_kingdom,
            '44':united_kingdom,
            '+44':united_kingdom,
            'ca':canada,
            "1":canada,
            '+1':canada,
            'es':spain,
            "34":spain,
            '+34':spain,
            'ch':switzerland,
            "41":switzerland,
            '+41':switzerland,
        }[country]

    def login_process(self,country,phoneNumber,password):

        self.driver.get('https://www.cotps.com/#/pages/phonecode/phonecode?from=login')
        self.phoneNumber = phoneNumber

        #Variable for Xpath buton and input
        mobile_number_xpath = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-input/div/input'
        password_xpath = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-input/div/input'
        login_xpath = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-button'
        transaction_xpath = '/html/body/uni-app/uni-tabbar/div[1]/div[3]'

        country_xpath = self.get_country_xpath(country)
        #Click on the country code
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,country_xpath)))
        self.driver.find_element(by=By.XPATH, value=country_xpath).click()
       
        #Fill the phonenumber & password details and login
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, mobile_number_xpath)))
        self.driver.find_element(by=By.XPATH, value=mobile_number_xpath).send_keys(phoneNumber)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, password_xpath)))
        self.driver.find_element(by=By.XPATH, value=password_xpath).send_keys(password)

        #Login
        self.wait(self.delay)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,login_xpath)))
        self.driver.find_element(by=By.XPATH, value=login_xpath).click()
        # self.driver.find_element(by=By.XPATH, value=login_xpath).click()
        
        #Click on the transaction bar tab
        try:
            self.wait(self.delay)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,transaction_xpath)))
            print("Connected to account: "+phoneNumber[:3]+"*****"+phoneNumber[-2:])
            self.driver.find_element(by=By.XPATH, value=transaction_xpath).click()
        except:
            print("Wrong password or phone number: ", phoneNumber)

    #Sleep for a certain delay
    def wait(self,delay):
        self.action = webdriver.ActionChains(self.driver)
        self.action.pause(delay)
        self.action.perform()

    def sell(self):

        commande_xpath = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-button'
        sell_xpath = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]'
        confirm_xpath = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button'
        solde_xpath = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]'
        montant_command_xpath = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[5]/uni-text[2]/span'
        profit_xpath = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-view[4]/uni-text[2]/span'

        #Try 10 time to sell or until solde is below 5$
        for _ in range(10):

            #Click on command buton
            self.wait(self.delay)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,commande_xpath)))
            self.driver.find_element(by=By.XPATH, value=commande_xpath).click()

            #try if sell buton appear
            try:

                self.wait(self.delay)
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,solde_xpath)))
                price = self.driver.find_element_by_xpath(solde_xpath).text
                print("Wallet balance: ",price,"$")
        
                if(float(price) >= 10):

                    self.wait(self.delay)
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,sell_xpath)))
                    # Transaction amount print
                    montant_command = self.driver.find_element_by_xpath(montant_command_xpath).text
                    print("Transaction amount:",montant_command,"$")
                    self.driver.find_element(by=By.XPATH, value=sell_xpath).click()

                    self.wait(self.delay)
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,confirm_xpath)))
                    # Profit print
                    profit = self.driver.find_element_by_xpath(profit_xpath).text
                    print("Profit:",profit,"$")
                    self.driver.find_element(by=By.XPATH, value=confirm_xpath).click()
                
                else:
                    print("Your balance is under 10 $")
                    break

            except:
                print("Your balance is under 10 $")
                break

    def kill(self):
        
        last_transaction_period_xpath = '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[3]/uni-view[1]'
        # Transaction amount print
        try:
            self.wait(self.delay)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,last_transaction_period_xpath)))
            last_transaction = self.driver.find_element_by_xpath(last_transaction_period_xpath).text
            print("Last transaction period:",last_transaction)
        except:
            pass
        print("Logging out of the", self.phoneNumber,"account...\n")
        self.driver.quit()





