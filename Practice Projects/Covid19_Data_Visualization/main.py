import pandas as pd
import matplotlib.pyplot as plt

confirmed = pd.read_csv("covid19_confirmed.csv")
deaths = pd.read_csv("covid19_deaths.csv")
recovered = pd.read_csv("covid19_recovered.csv")

confirmed = confirmed.drop(["Province/State", "Lat", "Long"], axis = 1)
deaths = deaths.drop(["Province/State", "Lat", "Long"], axis = 1)
recovered = recovered.drop(["Province/State", "Lat", "Long"], axis = 1)

confirmed = confirmed.groupby(confirmed["Country/Region"]).aggregate("sum")
deaths = deaths.groupby(deaths["Country/Region"]).aggregate("sum")
recovered = recovered.groupby(recovered["Country/Region"]).aggregate("sum")

confirmed = confirmed.T
deaths =  deaths.T
recovered = recovered.T

# Visualization
# Specify which countries to visualize
countries = ["US", "United Kingdom", "China", "Italy", "France", "Spain", "India", "Germany"]

# Calculate the number of new cases each day
def new_cases():
    new_cases = confirmed.copy()
    for each_day in range(1, len(confirmed)):
        new_cases.iloc[each_day] = confirmed.iloc[each_day] - confirmed.iloc[each_day-1]
    
    print(new_cases)
    return new_cases


# Calculates the growth rate each day
def growth_rate():
    growth_rate = confirmed.copy()
    for each_day in range(1, len(confirmed)):
        growth_rate.iloc[each_day] = (new_cases().iloc[each_day] / confirmed.iloc[each_day-1]) * 100
    
    print(growth_rate)
    return growth_rate


# Calculates the number of active cases each day
def active_cases():
    active_cases = confirmed.copy()
    for each_day in range(0, len(confirmed)):
        active_cases.iloc[each_day] = confirmed.iloc[each_day] - deaths.iloc[each_day] - recovered.iloc[each_day]
    
    print(active_cases)
    return active_cases


# Calculates the overall growth rate using the number of active cases
def overall_growth_rate():
    overall_growth_rate = confirmed.copy()
    for each_day in range(1, len(confirmed)):
        overall_growth_rate.iloc[each_day] = ((active_cases().iloc[each_day] - active_cases().iloc[each_day-1]) / active_cases().iloc[each_day-1]) * 100

    print(overall_growth_rate)


# Calculates the death rate of each country
def death_rate():
    death_rate = confirmed.copy()
    for each_day in range(0, len(confirmed)):
        death_rate.iloc[each_day] = (deaths.iloc[each_day] / confirmed.iloc[each_day]) * 100

    print(death_rate)
    return death_rate


# Calculates how many patients need hospitals to recover
def hospitalization_needed():
    hospitalization_rate_estimate = 0.03
    hospitalization_needed = confirmed.copy()
    for each_day in range(0, len(confirmed)):
        hospitalization_needed.iloc[each_day] = active_cases().iloc[each_day] * hospitalization_rate_estimate

    print(hospitalization_needed)


# Formats the Theme of the Line Graph 
# for Confirmed Cases for specified countries
def confirmed_cases_per_country_line():
    ax = plt.subplot()
    ax.set_title("Covid-19: Total Confirmed Cases By Country", color="white")
    ax.set_facecolor("black")
    ax.figure.set_facecolor("#121212")
    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white")

    for country in countries:
        confirmed[country][10:].plot(label=country)

    plt.legend(loc="upper left")
    plt.show()


# Formats the Theme of the Bar Graph 
# for Confirmed Cases Growth Rate for each specified country
def confirmed_cases_growth_rate_per_country_bar():
    for country in countries:
        ax = plt.subplot()
        ax.set_title(f"Covid-19: Total Confirmed Cases Growth Rate {country}", color="white")
        ax.set_facecolor("black")
        ax.figure.set_facecolor("#121212")
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")

        growth_rate()[country][250:].plot.bar()
        plt.show()


# Formats the Theme of the Line Graph 
# for Total Deaths By Country for specified countries
def total_death_per_country_line():
    ax = plt.subplot()
    ax.set_title("Covid-19: Total Deaths By Country", color="white")
    ax.set_facecolor("black")
    ax.figure.set_facecolor("#121212")
    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white")

    for country in countries:
        deaths[country].plot(label=country)

    plt.legend(loc="upper left")
    plt.show()


# Formats the Theme of the Bar Graph 
# for Death Rate for each specified country 
def death_rate_per_country_bar():
    for country in countries:
        ax = plt.subplot()
        ax.set_title(f"Covid-19: Death Rate {country}", color="white")
        ax.set_facecolor("black")
        ax.figure.set_facecolor("#121212")
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")

        death_rate()[country][250:].plot.bar()
        plt.show()


### Activate one of the functions below to print the updated data
#
# new_cases()
# growth_rate()
# active_cases()
# overall_growth_rate()
# death_rate()
# hospitalization_needed()


### Activate one of the functions below to visualize the data
#
# confirmed_cases_per_country_line()
# confirmed_cases_growth_rate_per_country_bar()
# total_death_per_country_line()
# death_rate_per_country_bar()