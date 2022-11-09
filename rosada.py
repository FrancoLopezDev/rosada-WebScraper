from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# General Stuff about the website
path = '/Users/admin/desktop/projects/scraper/chromedriver'
options = Options()
options.headless = True
# options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=path)
website = 'http://siops.datasus.gov.br/filtro_rel_ges_covid_municipal.php'
driver.get(website)

# Initial Test: printing the title
print(driver.title)
print()

# List to Store stuff in
totals = []

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

### Loop through all combinations ###
for year in range(1, 3):
    year_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbAno"]'))
    year_select.select_by_index(year)
    if year == 1:
        current_year = 2021
    else:
        current_year = 2020

    for period in range(0, len(period_options)):
        period_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbPeriodo"]'))
        period_select.select_by_index(period)
        current_period = period + 1

        for report in range(0, len(report_options)):
            report_select = Select(driver.find_element(By.XPATH, '//*[@id="gesRelatorio"]'))
            report_select.select_by_index(report)
            current_report = report + 1

            for county in range(0, len(county_options)):
                county_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbMunicipio"]'))
                county_select.select_by_index(county)
                current_county = county + 1

                for index in range(0, len(state_options)):
                    state_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbUF"]'))
                    state_select.select_by_index(index)

                    period_select = Select(driver.find_element(By.XPATH, '//*[@id="cmbPeriodo"]'))
                    period_select.select_by_index(period)

                    # Click the Submit Button
                    submit_button = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/form/div[2]/div/input[2]')
                    submit_button.click()

                    # Pulling data from the webpage
                    nameof = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[1]/tbody/tr[2]').text
                    total_balance = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[3]/tbody/tr[9]/td[4]').text
                    paid_expenses = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[4]/tbody/tr[11]/td[4]').text

                    report_name = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[2]/tbody/tr/td').text
                    county_name = driver.find_element(By.XPATH, '//*[@id="arearelatorio"]/div[1]/div/table[1]/tbody/tr[2]/td').text

                    # Update list with the new info
                    # totals.update({Unique_NUM: [nameof[8:], nameof[:6], current_year, total_balance, paid_expenses]})
                    totals.append([Unique_NUM, nameof[:6], nameof[-2:], county_name[9:-5], report_name[9:], current_year, current_period, total_balance, paid_expenses])

                    print(f'{Unique_NUM}: Identifier: {nameof[:6]}, State: {nameof[-2:]}, Year: {current_year}, Period: {current_period}, Report: {report_name[9:]}, Municipality: {county_name[9:-5]}, Balance: {total_balance}, Expenses: {paid_expenses}')
                    # print(totals)
                    Unique_NUM += 1
                    driver.back()

# Print the final List and quit
print(len(totals))
print(totals)
driver.quit()