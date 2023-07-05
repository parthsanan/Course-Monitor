# Program monitors course and returns all sections that are available to register 

def Course_Monitor():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    from discordwebhook import Discord

    discord = Discord(url="<web hook url>")
    service = Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    printcount = 0

    courses = {"Department Abbreviation": "Course Number"}

    for dept, course in courses.items():

        url = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept="+dept+"&course="+course
        driver.get(url)

        table_locator = (By.CLASS_NAME, "section-summary")
        wait = WebDriverWait(driver, 10)
        table = wait.until(EC.visibility_of_element_located(table_locator))

        rows = table.find_elements(By.TAG_NAME, "tr")
        
        for row in rows:
            
            columns = row.find_elements(By.TAG_NAME, "td")
            
            if len(columns) >= 5:
                status = columns[0].text.strip()
                section = columns[1].text.strip()
                type = columns[2].text.strip()
                term = columns[3].text.strip()
                days = columns[6].text.strip()
                time = columns[7].text.strip()+" - "+columns[8].text.strip()

                if term == "1" and type == "Lecture" and status == '':
                    
                    printcount+=1                    
                    
                    discord.post(content ="Section: "+ section)
                    discord.post(content ="Type: "+ type)
                    discord.post(content ="Term: "+ term)
                    discord.post(content ="Days: "+ days)
                    discord.post(content = "Time: "+ time)
                    discord.post(content ="-----------------------------------")
                
        if printcount > 0:
        
            print("\nCOURSES FOUND FOR", dept, course)
            discord.post(content = "\n\nALL SECTIONS AVAILABLE FOR " + dept + " " + course)
            discord.post(content = "-----------------------------------")
    
        else:
            print("\nNO COURSES FOUND FOR", dept, course)


    

    
    
 
