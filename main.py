import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns


data_eui = pd.read_json('cycles.json')
# print(data_eui)
# data_eui_flatten = pd.json_normalize(data_eui)
data_properties = pd.DataFrame(data_eui['properties'][1])
print(data_properties)


# sns.scatterplot('grossfloorarea', 'siteeui', data=data_properties, hue='propertytype')


color_labels = data_properties['propertytype'].unique()
rgb_values = sns.color_palette("Set2", 23)
color_map = dict(zip(color_labels, rgb_values))
# print(color_map)

fig, ax = plt.subplots()
grouped = data_properties.groupby('propertytype')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='grossfloorarea', y='siteeui', label=key, color=color_map[key])

# plt.scatter(data_properties.loc[:, 'grossfloorarea'], data_properties.loc[:, 'siteeui'],
#             c=data_properties.loc[:, 'propertytype'])
# plt.title('Site EUI vs. floor area')
# plt.xlabel('Gross Floor Area (square metres)')
# plt.ylabel('Site EUI (kWh/m²/yr)')
plt.show()

# data_2021 = pd.read_csv('HourlyTielineData2021.csv')
#
# data_2021['datetime'] = data_2021['Date'] + " " + data_2021['HE'].astype(str) + ":00"
#
# print(type(data_2021['datetime'][23][11:13]))


# def custom_to_datetime(date):
#     # If the hour is single digit, pad 0 in front
#     if date[11:13] in ["1:", "2:", "3:", "4:", "5:", "6:", "7:", "8:", "9:"]:
#         date = date[:11] + "0" + date[12:]
#         return pd.to_datetime(date, format='%m/%d/%Y %H%M')
#     # If the hour is 24, set it to 0 and increment day by 1
#     elif date[11:13] == "24":
#         return pd.to_datetime(date[:-2], format='%m/%d/%Y %H%M') + pd.Timedelta(days=1)
#     else:
#         return pd.to_datetime(date, format='%m/%d/%Y %H%M')


# data_2021['datetime'] = data_2021['datetime'].apply(custom_to_datetime)
# print(data_2021)
# print(data_2021)
# plt.plot(data_2021["datetime"], data_2021["US Tielines"])
# plt.show()

# housing_type = np.array([110.0, 93.2, 79.2, 86.3, 46.7, 41.8, 89.1])
# housing_type_mean = np.mean(housing_type)
# housing_type_normalized = housing_type / housing_type_mean
# print(housing_type_normalized)
#
# housing_income = np.array([63.7, 71.3, 78.7, 86.3, 87.7, 102.0, 122.3])
# housing_income_mean = np.mean(housing_income)
# housing_income_normalized = housing_income/housing_income_mean
# print(housing_income_normalized)
#
# bc_consump = 86.7
#
# columns = ["<20k", "20-40k", "40-60k", "60-80k", "80-100k", "100-150k", "150k+"]
# rows = ["Single-detached", "Double", "Row or terrace", "Duplex",
#         "Low-rise apartment (< 5 stories)", "High-rise apartment (>= 5 stories)", "Mobile home"]
#
# housing_matrix = np.outer(housing_income_normalized, housing_type_normalized) * bc_consump
# print(housing_matrix)
# plt.plot(housing_matrix)
# plt.title('Energy Consumption by Housing')
# plt.xlabel('Income Bracket')
# plt.ylabel('Annual Energy Consumption (Gigajoules)')
# plt.ylim(0, 240)
# plt.xticks(ticks=range(7), labels=columns)
# plt.legend(rows)
# plt.show()
