import os.path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats as st

user = '970jwillems'
location = 'C:\\Users\\' + user + '\\Sonova\\Sonova Marketing GmbH - General\\05_DA\\03_Tickets\\Janine\\01_DE_Bus-Mkt\\DASD-555 Marketing Channel Saturation\\'
file = 'markchannelsat_data_monthly.xlsx'
filepath = os.path.join(location, file)


def satr(channel, fig):

    global filepath

    # create and clean dataframe
    df = pd.read_excel(filepath)
    x = 'marketing_costs_in_eur'
    y = 'total_net_sales_hea_in_eur'

    channel_flag = df['marketing_channel'] == channel
    df = df[channel_flag].fillna(0)
    df = df[[x, y]]
    #df = df[df[y] > df[x]]
    df = df[(np.abs(st.zscore(df)) < 3).all(axis=1)]

    x = df[x].to_numpy()
    y = df[y].to_numpy()
    perm = x.argsort()
    x = x[perm]
    y = y[perm]

    # execute polyfit and find saturation point
    z = np.polyfit(x, y, 2)
    p = np.poly1d(z)

    xlim = np.amax(x) * 1.5
    xt = np.linspace(0, xlim, 100)
    yt = p(xt)
    xtyt = zip(xt, yt)
    xtn = []
    ytn = []
    
    for i in xtyt:                      # find xt, yt where net sales is higher than marketing spend (roas > 1) 
        if i[1] > i[0]:
            xtn.append(i[0])
            ytn.append(i[1])
     
    max_yt = max(yt)
    max_i = list(yt).index(max_yt)      # get the index of the maximum net sales to find the corresponding marketing spend
    max_ytn = max(ytn)
    max_in = list(ytn).index(max_ytn)   # get the index of the maximum net sales with roas > 1 to find the corresponding marketing spend

    # output
    print('\n')
    print('Equation of saturation line for ' + f'{channel}: ' + f'{p}')
    print('For ' + f'{channel} ' + 'the maximum Net Sales equals ' + f'{round(max_yt)} EUR per month')
    print('This is reached at a Marketing Spend of ' + f'{round(list(xt)[max_i])} EUR per month')
    print('For ' + f'{channel} ' + 'the maximum Net Sales with ROAS > 1 equals ' + f'{round(max_ytn)} EUR per month')
    print('This is reached at a Marketing Spend of ' + f'{round(list(xtn)[max_in])} EUR per month')

    plt.figure(fig)
    plt.scatter(x, y, color='black', s=12)
    plt.plot(xt, p(xt), color='lightblue', linewidth=3)   # trendline with defined datapoints for spend

    for x,y in zip(x,y):
        label = "{:.0f}".format(x) + "; " +"{:.0f}".format(y)
        plt.annotate(label,(x,y), color='grey', fontsize=6, xytext=(0,5), textcoords='offset points', ha='center')
        
    plt.title(f'{channel} ' + 'Marketing Spend against Net Sales w/ Trendline')
    plt.xlabel('Marketing Spend', fontsize=10)
    plt.ylabel('Net Sales', fontsize=10)
    plt.rc('axes', labelsize=12)


#Yes: Google Search, Facebook, Outbrain // No: Bing, Zemanta, Taboola
fig = 0
channels = ['Facebook', 'Google Search', 'Outbrain']

for channel in channels:
    fig = fig +1
    satr(channel, fig)

plt.show()

