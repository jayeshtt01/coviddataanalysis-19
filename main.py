import pandas as pd

covid_data = None

def load_covid_data(worldometer_data):
    global covid_data
    try:
        covid_data = pd.read_csv(worldometer_data)
        covid_data.columns = covid_data.columns.str.strip()
    except FileNotFoundError:
        print(f"Error: File '{worldometer_data}' not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: File '{worldometer_data}' is empty.")
    except pd.errors.ParserError:
        print(f"Error: Parsing issue with file '{worldometer_data}'. Please check the file format.")
    except Exception as e:
        print(f"Error: Unexpected error occurred while loading data: {str(e)}")

# Function to get new cases for a specific country
def get_new_cases(data, country_name):
    if data is None:
        print("Error: COVID data not loaded.")
        return None
    
    country_data = data[data['Country'].str.contains(country_name, case=False)]
    if not country_data.empty:
        new_cases = country_data.iloc[0]['NewCases']
        return new_cases
    else:
        return None

# Function to get total deaths for a specific country
def get_total_deaths(data, country_name):
    if data is None:
        print("Error: COVID data not loaded.")
        return None
    
    country_data = data[data['Country'].str.contains(country_name, case=False)]
    if not country_data.empty:
        total_deaths = country_data.iloc[0]['TotalDeaths']
        return total_deaths
    else:
        return None

# Function to get total recovered for a specific country
def get_total_recovered(data, country_name):
    if data is None:
        print("Error: COVID data not loaded.")
        return None
    
    country_data = data[data['Country'].str.contains(country_name, case=False)]
    if not country_data.empty:
        total_recovered = country_data.iloc[0]['TotalRecovered']
        return total_recovered
    else:
        return None

# Function to get active cases for a specific country
def get_active_cases(data, country_name):
    if data is None:
        print("Error: COVID data not loaded.")
        return None
    
    country_data = data[data['Country'].str.contains(country_name, case=False)]
    if not country_data.empty:
        active_cases = country_data.iloc[0]['ActiveCases']
        return active_cases
    else:
        return None

# Function to get serious or critical cases for a specific country
def get_serious_critical(data, country_name):
    if data is None:
        print("Error: COVID data not loaded.")
        return None
    
    country_data = data[data['Country'].str.contains(country_name, case=False)]
    if not country_data.empty:
        serious_critical = country_data.iloc[0]['Serious,Critical']
        return serious_critical
    else:
        return None

# Function to get total cases per 1M population for a specific country
def get_tot_cases_per_1m_pop(data, country_name):
    if data is None:
        print("Error: COVID data not loaded.")
        return None
    
    country_data = data[data['Country'].str.contains(country_name, case=False)]
    if not country_data.empty:
        tot_cases_per_1m_pop = country_data.iloc[0]['Tot Cases/1M pop']
        return tot_cases_per_1m_pop
    else:
        return None

# Function to get deaths per 1M population for a specific country
def get_deaths_per_1m_pop(data, country_name):
    if data is None:
        print("Error: COVID data not loaded.")
        return None
    
    country_data = data[data['Country'].str.contains(country_name, case=False)]
    if not country_data.empty:
        deaths_per_1m_pop = country_data.iloc[0]['Deaths/1M pop']
        return deaths_per_1m_pop
    else:
        return None
        

# Menu function to display options and fetch data based on user input
def menu(data):
    while True:
        print("|-----------------------------------------|")
        print("|                                         |")
        print("| WELCOME TO COVID-19 ANALYSIS BY JAYESH TT|")
        print("|                                         |")
        print("|-----------------------------------------|")
        print("\nMenu:")
        print("1. New Cases")
        print("2. Total Deaths")
        print("3. Total Recovered")
        print("4. Active Cases")
        print("5. Serious or Critical Cases")
        print("6. Total Cases per 1M Population")
        print("7. Deaths per 1M Population")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            print("Exiting...")
            return
        elif choice == '1':
            country_name = input("Enter the country name: ")
            result = get_new_cases(data, country_name)
            if result is not None:
                print(f"New cases in {country_name}: {result}")
            else:
                print(f"No data found for {country_name}.")
        elif choice == '2':
            country_name = input("Enter the country name: ")
            result = get_total_deaths(data, country_name)
            if result is not None:
                print(f"Total deaths in {country_name}: {result}")
            else:
                print(f"No data found for {country_name}.")
        elif choice == '3':
            country_name = input("Enter the country name: ")
            result = get_total_recovered(data, country_name)
            if result is not None:
                print(f"Total recovered in {country_name}: {result}")
            else:
                print(f"No data found for {country_name}.")
        elif choice == '4':
            country_name = input("Enter the country name: ")
            result = get_active_cases(data, country_name)
            if result is not None:
                print(f"Active cases in {country_name}: {result}")
            else:
                print(f"No data found for {country_name}.")
        elif choice == '5':
            country_name = input("Enter the country name: ")
            result = get_serious_critical(data, country_name)
            if result is not None:
                print(f"Serious or critical cases in {country_name}: {result}")
            else:
                print(f"No data found for {country_name}.")
        elif choice == '6':
            country_name = input("Enter the country name: ")
            result = get_tot_cases_per_1m_pop(data, country_name)
            if result is not None:
                print(f"Total cases per 1M population in {country_name}: {result}")
            else:
                print(f"No data found for {country_name}.")
        elif choice == '7':
            country_name = input("Enter the country name: ")
            result = get_deaths_per_1m_pop(data, country_name)
            if result is not None:
                print(f"Deaths per 1M population in {country_name}: {result}")
            else:
                print(f"No data found for {country_name}.")
        else:
            print("Invalid choice. Please enter a number from the menu.")

def main():
    csv_file = r'C:\Users\Dell\OneDrive\Desktop\python project\worldometer_data.csv'
    load_covid_data(csv_file)
    if covid_data is not None:
        menu(covid_data)

if __name__ == "__main__":
    main()
