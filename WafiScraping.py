import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define a list of URLs to scrape
url = 'https://wafi.housing.gov.sa/ar/projects-map'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
#Extract links for project 
project_links = []
for element in soup.find_all('table', class_='views-table cols-2 table table-hover table-striped'):
    for a_tag in element.find_all('a'):
        project_links.append(a_tag['href'])

# Create a session object to maintain a persistent connection to the website
session = requests.Session()

# Create an empty list to store the data
data = []

# Loop over each URL in the list
for url in project_links:
        # Send a GET request to the website and get the HTML content
        URL_HOME ='https://wafi.housing.gov.sa'
        response = session.get(URL_HOME+url)

        # Parse the HTML content using the lxml parser
        soup = BeautifulSoup(response.content, 'lxml')
        #Selecting the div parent ##title_project a specific class
        parent_div_title_project = soup.find('div', class_='field field-name-title-field field-type-text field-label-above')
        if parent_div_title_project:
            Title_Project = parent_div_title_project.find('div', class_='field-item even').text.strip()
        else:
            Title_Project =None  
        #Selecting the div parent ##Description_Project aspecific class
        parent_div_Description_Project = soup.find('div', class_='field field-name-body field-type-text-with-summary field-label-above')
        if parent_div_Description_Project:        
            Description_Project =parent_div_Description_Project.find('div', class_='field-item even').text.strip()
        else:
            Description_Project=None
            
        # Select the div parent ##license_number aspecific class
        parent_div_license_number = soup.find('div', class_='field field-name-field-license-number-new field-type-text field-label-above')
        if parent_div_license_number:
            license_number = parent_div_license_number.find('div', class_='field-item even').text.strip()
        else:
            license_number = None

        #Selecting the div parent ##project_state aspecific class
        parent_div_project_state = soup.find('div', class_='field field-name-field-project-state field-type-list-text field-label-above')
        if parent_div_project_state:
            project_state= parent_div_project_state.find('div', class_='field-item even').text.strip()
        else:
            project_state=None 
            
        # Select the div parent ##developer_name aspecific class
        parent_div_developer_name = soup.find('div', class_='field field-name-field-developer-name field-type-text field-label-above')
        if parent_div_developer_name:
            developer_name = parent_div_developer_name.find('div', class_='field-item even').text.strip()
        else:
            developer_name = None

        # Select the div parent City aspecific class
        parent_div_City = soup.find('div', class_='field field-name-field-city field-type-list-text field-label-above')
        if parent_div_City:
            City = parent_div_City.find('div', class_='field-item even').text.strip()
        else:
            City = None
        #Selecting the div parent ##Banck_name aspecific class
        parent_div_Banck_name = soup.find('div', class_='field field-name-field-bank-name field-type-text field-label-above')
        if parent_div_Banck_name:
            Banck_name = parent_div_Banck_name.find('div', class_='field-item even').text.strip()
        else:
            Banck_name=None 
            
        #Selecting the div parent ##account_number aspecific class
        parent_div_account_number = soup.find('div', class_='field field-name-field-bank-account-number field-type-text field-label-above')
        if parent_div_account_number:
            Account_num =parent_div_account_number.find('div', class_='field-item even').text.strip()
        else:
            Account_num=None

        #Selecting the div parent ##Project_type aspecific class
        parent_div_Project_type = soup.find('div', class_='field field-name-field-project-type field-type-entityreference field-label-above')
        if parent_div_Project_type :
            Project_type =parent_div_Project_type.find('div', class_='field-item even').text.strip()
        else:
            Project_type=None 

        #Selecting the div parent ##thedate_of_issuance aspecific class
        parent_div_thedate_of_issuance = soup.find('div', class_='field field-name-field-the-date-of-issuance-of-th field-type-datetime field-label-above')
        if parent_div_thedate_of_issuance:
            the_date_of_issuance=parent_div_thedate_of_issuance .find('span', class_='date-display-single') or parent_div_thedate_of_issuance.find('div', class_='field-item even')
        else:
            the_date_of_issuance=None 


        #Selecting the div parent ##Num_UnitOFProject aspecific class
        parent_div_Num_UnitOFProject = soup.find('div', class_='field field-name-field-number-of-units-of-the-pro field-type-number-integer field-label-above')
        if parent_div_Num_UnitOFProject :
            Num_UnitOFProject = parent_div_Num_UnitOFProject.find('div', class_='field-item even').text.strip()
        else :
            Num_UnitOFProject=None
            
        # Select the div parent ##Start_date_Pro aspecific class
        parent_div_Start_date_Pro = soup.find('div', class_='field field-name-field-the-start-date-of-the-proj field-type-datetime field-label-above')
        if parent_div_Start_date_Pro:
            Start_date_Pro = parent_div_Start_date_Pro.find('span', class_='date-display-single') or parent_div_Start_date_Pro.find('div', class_='field-item even')
        else:
            Start_date_Pro = None

        #Selecting the div parent End_date_Pro aspecific class
        parent_div_End_date_Pro = soup.find('div', class_='field field-name-field-the-start-date-of-the-proj field-type-datetime field-label-above')
        if parent_div_End_date_Pro:
            End_date_Pro =parent_div_End_date_Pro.find('span', class_='date-display-single') or parent_div_End_date_Pro.find('div', class_='field-item even') 
        else:
            End_date_Pro=None



        #Selecting div parent ## LInkofvideo  &&Extract value 
        parent_div_Link_video = soup.find('div', class_='field field-name-field-video-album field-type-youtube field-label-hidden')
        if parent_div_Link_video:
            try:
                Link_video = parent_div_Link_video.select_one('#document').text.strip()
            except AttributeError:
                Link_video = None
        else:
            Link_video = None


        #Selecting the div parent_div_percentage_project a specific class && Extracting the value of percentage_project
        parent_div_percentage_project = soup.find('div', class_='field field-name-field-percentage-project-text field-type-text field-label-above') 
        if parent_div_percentage_project:                 
            percentage_project = parent_div_percentage_project.find('div', class_='field-item even').text.strip()
        else:
            percentage_project=None 

        #Selecting the div parent_div_percentage_project a specific class && Extracting the value of percentage_project
        parent_div_planned_ratio = soup.find('div', class_='field field-name-field-planned-ratio-text field-type-text field-label-above')    
        if parent_div_planned_ratio:     
            planned_ratio = parent_div_planned_ratio.find('div', class_='field-item even').text.strip()
        else:
            planned_ratio=None


        #Selecting the div parent_div_Account_administratora specific class && Extracting the value of percentage_project
        parent_div_Account_administrator = soup.find('div', class_='field field-name-field-account-administrator field-type-text field-label-above') 
        if parent_div_Account_administrator :
            Account_administrator = parent_div_Account_administrator.find('div', class_='field-item even').text.strip()
        else:
            Account_administrator= None
            

        #Selecting the div parent_div_Account_administratora specific class && Extracting the value of percentage_project
        parent_div_No_escrow_account = soup.find('div', class_='field field-name-field-no-escrow-account field-type-text field-label-above');
        if  parent_div_No_escrow_account :
            div_No_escrow_account = parent_div_No_escrow_account.find('div', class_='field-item even').text.strip()
        else :
            div_No_escrow_account = None 



   



        # Create a dictionary with the data
        project_data = {
        
         'Developer_Name': developer_name,
            'City': City,
            'Start_Date_Pro': Start_date_Pro,
            'End_Date_Pro': End_date_Pro
        }

        # Append the dictionary to the list
        data.append(project_data)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
with pd.ExcelWriter('output.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
