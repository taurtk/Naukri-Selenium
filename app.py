from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
from selenium.webdriver import Chrome
class Naukri:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get('http://www.naukri.com/')
        self.applied_success=[]
        self.applied_failure={}
        self.pages = []
    def LOGIN(self):
        
        log =self.driver.find_element_by_id('login_Layer')
        log.click()

        email = self.driver.find_element_by_name('email')
        email.clear()
        email.send_keys('taurtk@gmail.com')
        
        passw = self.driver.find_element_by_name('PASSWORD')
        passw.clear()
        passw.send_keys('Hamida@123')
        
        #prob = driver.find_element_by_class_name("//button[@class='blueBtn']")
        self.driver.find_element_by_css_selector("button[value='Login']").click()
        
    def search(self):
        time.sleep(5)
        #field =self.driver.find_element_by_id('qsbClick')
        #field.click()
        search_field =self.driver.find_element_by_name('qp')
        #search_field = self.driver.find_element_by_xpath("//input[@class = 'sugInp']")
        #search_field.clear()
        search_field.send_keys("machine learning" + Keys.TAB)
        #search_field.send_keys(Keys.TAB)
        #search_field = self.driver.find_element_by_xpath("//*[@id='sugDrp_qsb-keyskill-sugg']/ul/li/div")
        
        #search_field.click()
        search_field =self.driver.find_element_by_name('ql')
        search_field.clear()
        search_field.send_keys("bangalore")
        
#         search_field.click()
        search_field.submit()
#         submit_button = self.driver.find_element_by_xpath("//button[@class='col search l2 btn btn-mid']")
#         submit_button.click()
        products = self.driver.find_elements_by_xpath("//li[@class='desig']/a")
        time.sleep(5)
       
        
       # for product in products:
       #     print(product.text)
    
        
    def open_job(self):
        listed_jobs = self.driver.find_elements_by_xpath("//div[@type = 'tuple']")
        print('number of jobs listed in current page ', len(listed_jobs))
        print(type(listed_jobs))
        try:
            for job in listed_jobs:
                job.click()
                self.applyAndClose()
                self.driver.execute_script("window.scrollTo(0, 500)") 
        except Exception as ex:
            print('exception in open_job ', ex)
        
        #self.clean_up()
    
            
   
        
           
    def applyAndClose(self):
        
        time.sleep(2)
        obs = self.driver.find_element_by_css_selector("button[class='btn waves-effect waves-light btn-large']").click()
        handles = N.driver.window_handles
        print('number of pages opened ',len(handles))
        csv_writer = csv.writer(open("C://Users//star//Desktop//question.csv",'a+'))
        #start from 1st job opened page, infact there is only one job that is opened 
        for handle in handles[1:]:
            i=0
            self.driver.switch_to.window(handle)
            #self.driver.maximize_window()
            print('title of page ', self.driver.title)
            try:
                
                #//*[@id="closeLB1"]
                apply_button = self.driver.find_element_by_xpath("//button[@class='waves-effect waves-ripple btn apply-button']")
                apply_button.click()
                i+=1
                try:
                    element = self.driver.find_element_by_xpath("//*[@id='applyRelevanceFormSubmit']")
                    element.click()
                except:
                    element = self.driver.find_element_by_class_name("skipLink")
                    element.click()
                try:
                    time.sleep(1)
                    source = self.driver.find_elements_by_xpath("//form[@id='qusFrm']/div/label")
                    
                    
                    for q in source:
                       a = []              
                       for q in source:
                           a.append(q.text)
                           print(q.text)
                    csv_writer.writerow("".join(a))
                #    file.write("\n")
                except Exception as ex:
                    print(ex)
                    self.applied_failure[self.driver.title] = str(ex)
                print('Successfully applied for :', self.driver.title)
                self.applied_success.append(self.driver.title)
            except Exception as ex:
                print(ex)
                self.applied_failure[self.driver.title] = str(ex)
            try:
                apply_button1 = self.driver.find_element_by_xpath("//button[@class='waves-effect waves-ripple btn company-site-button']")
                apply_button1.click()
            except Exception as ex:
                print(ex)
                self.applied_failure[self.driver.title] = str(ex)
            try:
                apply_button2 = self.driver.find_element_by_id("loginApply")
                apply_button2.click()
                try:
                    element = self.driver.find_element_by_xpath("//*[@id='applyRelevanceFormSubmit']")
                    element.click()
                except:
                    element = self.driver.find_element_by_class_name("skipLink")
                    element.click()
                    
                print('Successfully applied for :', self.driver.title)
                self.applied_success.append(self.driver.title)
            except Exception as ex:
                print(ex)
                self.applied_failure[self.driver.title] = str(ex)
            try:
               # obs = self.driver.find_element_by_css_selector("button[class='btn waves-effect waves-light btn-large']").click()
                apply_button3 = self.driver.find_element_by_class_name("blueBtn")
                apply_button3.click()                
            except Exception as ex:
                print(ex)
                self.applied_failure[self.driver.title] = str(ex)
            
            #self.clean_up(start_position=1):\
        
        time.sleep(2)
        self.clean_up(start_position=1)
        self.driver.switch_to.window(handles[0])
        
    def clean_up_beforelogin(self, start_position):
        self.clean_up(start_position)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        
    def clean_up(self, start_position=0):
        #close the opened browser
        handles = self.driver.window_handles
        for handle in handles[start_position:]:
            self.driver.switch_to.window(handle)
            self.driver.close()        
    def page(self):
        time.sleep(5)
        try:
            obs = self.driver.find_element_by_css_selector("button[class='btn waves-effect waves-light btn-large']").click()
        except Exception as ex:
                print(ex)
                self.applied_failure[self.driver.title] = str(ex)
            
        flag = True
        self.open_job()
        while flag:
            obs = self.driver.find_element_by_css_selector("button[class='btn waves-effect waves-light btn-large']").click()
            if flag:    
                page = self.driver.find_element_by_link_text("Next")
                self.pages.append(self.driver.current_url)
                page.click()
                flag = True
            else:
                flag = False
            self.open_job()
        
            
    def print_result(self):
        print('Success in jobs applied')
        print('-'*50)
        for j in self.applied_success:
            print(j)
        print('-'*50)
        print('Failure in jobs applied')
        for key, value in self.applied_failure.items():
            print(key, ' failed because of ', value)
        print('-'*50)
        

N = Naukri()
N.clean_up_beforelogin(1)
N.LOGIN()
N.search()
#N.page()
N.open_job()
# N.print_result()
