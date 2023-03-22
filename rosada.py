from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# General Stuff about the website
path = '/path/to/directory/chromedriver'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=path)
website = 'http://siops.datasus.gov.br/filtro_rel_ges_covid_municipal.php'
driver.get(website)

# Initial Test: printing the title
print(driver.title)
print()

### Drop Down Menus ###
state_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbUF"]'))
state_options = state_select.options

year_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbAno"]'))
year_options = year_select.options

period_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbPeriodo"]'))
period_options = period_select.options

county_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbMunicipio"]'))
county_options = county_select.options

report_select = Select(driver.find_element(By.XPATH, '//*[@id="gesRelatorio"]'))
report_options = report_select.options

Unique_NUM = 1

# Create CSV file to Store Data
with open("data.csv", "w") as f:
    f.write("UniqueNum,Identifier,State,Municipality,Report,Year,Period,Balance,Expenses\n")

### Loop through all combinations ###
for year in range(1, 3):
    if year == 1:
        current_year = 2021
    else:
        current_year = 2020
    year_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbAno"]'))
    year_select.select_by_index(year)

    for period in range(2, 6):
        current_period = period + 1

        for report in range(0, 4):
            current_report = report + 1

            for index in range(0, len(state_options)):
                state_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbUF"]'))
                state_select.select_by_index(index)
                # Recheck County Options
                county_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbMunicipio"]'))
                county_options = county_select.options

                ### PRIMARY FOR LOOP ###
                for county in range(0, len(county_options)):
                    county_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbMunicipio"]'))
                    county_select.select_by_index(county)
                    current_county = county + 1

                    # Click The Report Button Again
                    report_select = Select(driver.find_element(By.XPATH, '//*[@id="gesRelatorio"]'))
                    report_select.select_by_index(report)

                    # Click Period Button
                    period_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbPeriodo"]'))
                    period_select.select_by_index(period)

                    # Click the Submit Button
                    submit_button = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/form/div[2]/div/input[2]')
                    submit_button.click()

                    # Pulling data from the webpage
                    nameof = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[1]/tbody/tr[2]').text

                    if current_year == 2021:
                        if current_report == 1:
                            total_balance = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[3]/tbody/tr[9]/td[4]').text
                            paid_expenses = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[4]/tbody/tr[11]/td[4]').text
                        elif current_report == 2:
                            total_balance = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[3]/tbody/tr[4]/td[4]').text
                            paid_expenses = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[4]/tbody/tr[11]/td[4]').text
                        elif current_report == 3:
                            total_balance = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[3]/tbody/tr[4]/td[4]').text
                            paid_expenses = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[4]/tbody/tr[11]/td[4]').text
                        elif current_report == 4:
                            total_balance = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[3]/tbody/tr[3]/td[4]').text
                            paid_expenses = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[4]/tbody/tr[11]/td[4]').text
                    elif current_year == 2020:
                        if current_report == 1:
                            total_balance = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[3]/tbody/tr[9]/td[2]').text
                            paid_expenses = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[4]/tbody/tr[11]/td[4]').text
                        elif current_report == 2:
                            total_balance = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[3]/tbody/tr[4]/td[2]').text
                            paid_expenses = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[4]/tbody/tr[11]/td[4]').text
                        elif current_report == 3:
                            total_balance = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[3]/tbody/tr[4]/td[2]').text
                            paid_expenses = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[4]/tbody/tr[11]/td[4]').text
                        elif current_report == 4:
                            total_balance = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[3]/tbody/tr[3]/td[2]').text
                            paid_expenses = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[4]/tbody/tr[11]/td[4]').text

                    report_name = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[2]/tbody/tr/td').text
                    county_name = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[1]/tbody/tr[2]/td').text

                    # Write to CSV file
                    with open("data.csv", "a") as f:
                        f.write(",".join(map(str, [Unique_NUM, nameof[:6], nameof[-2:], county_name[9:-5], report_name[9:], current_year, current_period, total_balance.replace('.','').replace(',','.'), paid_expenses.replace('.','').replace(',','.')])) + "\n")
                    
                    # For Testing
#                     print(f'{Unique_NUM}: Identifier: {nameof[:6]}, State: {nameof[-2:]}, Year: {current_year}, Period: {current_period}, Report: {report_name[9:]}, County: {county_name[9:-5]}, Balance: {total_balance}, Expenses: {paid_expenses}')
                    
                    # Keep track of every thousand pieces of data collected
                    if Unique_NUM % 1000 == 0:
                        print(Unique_NUM)
                    Unique_NUM += 1
                    driver.back()

# Print "finished" statement and quit
print("I'm all done!")
driver.quit()
