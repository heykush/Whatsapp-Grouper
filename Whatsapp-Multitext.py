from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\gkush\Downloads\chromedriver.exe")
driver.maximize_window()                        
driver.get('https://web.whatsapp.com/')

# if __name__ == "__main__":
#     while True:
        # input('Enter anything after scanning QR code..  Hit ENTER to start')

cl_no = [] 
# names = []  
client=[]
client.sort(reverse=True)
na=input("Enter your Friend's name and Number: ")
# cap=na.title()                                      
# names.extend(na.split(","))                         
msg = str(input("Enter your message: "))
# count = int(input("How many times: "))
sleep(2)
user = driver.find_element_by_xpath(f'//span[@title = "{na}"]').click()
sleep(2)
user_msg=driver.find_element_by_xpath(f'(//span[@title = "{na}"])[2]').click()
client=driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span').get_attribute("innerHTML")
client=str(client)       
cl_no.extend(client.split(", "))   
print(cl_no)  

count=0
scroll=driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div')
for cl in cl_no:   
    sleep(2)
    user = driver.find_element_by_xpath(f'//span[@title = "{na}"]').click()
    user_msg=driver.find_element_by_xpath(f'(//span[@title = "{na}"])[2]').click()
    sleep(2)
    driver.find_element_by_xpath('//span[@data-icon="down"]').click()
    sleep(3) 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", scroll)
    sleep(2)
    client_user=driver.find_element_by_xpath(f'//span[@title = "{cl}"]').click()
    sleep(2)
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    #for i in range(count):
    msg_box.send_keys(msg)
    sleep(2)
    button = driver.find_element_by_xpath('//button[@class="_1U1xa"]').click()
    count+=1
    print(count)
    
   
