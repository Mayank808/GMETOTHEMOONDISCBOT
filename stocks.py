# @Author: Matthew Olivera
# @Date:  30/01/2021

# imports, ticker monitor and a graphing calcualtor
import yfinance as yf
from matplotlib import pyplot as plt

# make function so i can dynamically pass inputs etc
def stonk(d, p, i):

    # defaults. if someone knows a better way to do this, dm me!
    if d == '': d = 'High'
    if p == '': p = 'max'
    
    # intervals don't work great for long periods, so i made it optional
    if i == '':
        # downlod the ticker. its a pandas dataframe! so i can immediately plot it in plt
        gme = yf.download('GME', period=p)
    else:
        gme = yf.download('GME', period=p, interval = i)

    # plot graph at selected or default key
    gme[d].plot()

    # TODO: Dynamic labels???
    plt.xlabel('Date')
    plt.ylabel('Money')

    # this was important to add, and im glad i could.
    plt.title('GME to the Moon')

    # in 2077, companies are legally forced to have dark mode enabled by default. 
    plt.style.use('dark_background')

    # save the image to working directory as temp. anyone got a better name?
    plt.savefig('temp.png')

    # clear fig from ram or else it just displays the largest graph with different colours. 
    plt.clf()