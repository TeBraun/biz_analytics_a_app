import streamlit as st

st.title("Vorhersage der Lebenserwartung neugeborener Frauen in Deutschland")

"Autor: Teresa Braunstein (http://github.com/TeBraun)"

"Bei Eingabe des Geburtsjahres werden die durchschnittlich zu erwartenden Lebensjahre neugeborener Frauen in Deutschland ausgegeben."

# Model mit Scipy
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
Life_expectancy = [82.662, 82.77, 82.87, 82.98, 83.105, 83.227, 83.353, 83.48, 83.60, 83.728, 83.84]

from scipy.stats import linregress

regression_result = linregress(years, Life_expectancy)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept


def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result

desired_year = st.number_input('Jahr', value=2022)

prediction = scipy_model(desired_year)
prediction_rounded = round(prediction, 2)

'Die Vorhersage der Lebenserwartung für das ausgewählte Geburtsjahr ist:'

st.write(prediction_rounded)

'Jahre'

st.subheader('Über das Modell und die Daten')

"Das Modell ist ein lineares Regressionsmodell auf Grundlage von Daten von 2010 bis 2020. "
"Es steht ein Datenpunkt pro Jahr zur Verfügung."

"Die Daten stammen aus folgender Quelle:"

"https://ourworldindata.org/grapher/womens-life-expectancy-at-birth?tab=chart&country=~OWID_WRL"
#%%
