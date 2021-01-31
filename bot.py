# @Author: Matthew Olivera
# @Date: 29/01/2021

# imports for discord bot and yahoo finance
import discord
import stocks
import os

# discord bot access key (top secret woooooo)
key = 'NjA0ODczOTQ1MDQ0NDg0MTEx.XT0Swg.j3qOdLBM9lIiDeDseaRiNPPzmXc'

# create a dynamic class that inherits from the parent, with infinite upgradeability! i think this looks nicer than the last one with functions floating about
class MyClient(discord.Client):

    # vestigial, but it's nice to have as a landmark to tell where something went wrong
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        # for some reason, i have to warmit up or else the first graph always displays incorrectly
        stocks.stonk('', '', '')
        
    # the big guy. scans all messages 
    async def on_message(self, message):
        # harcoded command (todo change?)
        if message.content[0:4] == '$gme':
            # handy dandy index for all ye curious
            ''' 
            Index
            0: !gme (always)
            1: data (Open, High, Low, Close)
            2: period
            3: intervals (^ dpi, think dots per inch)
            3++: TBD
            '''
            # use list comprehension for n commands
            commands = [x for x in message.content.split(' ')]

            # for debugging
            print(commands)

            # fill every unfilled command with null. i use an arbitrary 10 for expandability
            for i in range(10-len(commands)): commands.append('')

            # run stock code: hint: see stock.py's code! (d, p, i)
            stocks.stonk(commands[1], commands[2], commands[3])

            # system.out.println(picture.jpeg)
            await message.channel.send(file=discord.File('temp.png'))

            # delete it cause why not
            os.remove('temp.png')
        
        # help fucntion = handy 
        elif message.content == '$help':

            # here i use the triple quotes for seemingly no reason
            await message.channel.send('''```
Usage: $gme [Data] [Period] [Interval]
Valid inputs for [Data]: High, Low, Open, Close
Valid inputs for [Period]: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
Valid inputs for [Interval]: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
Don't use intervals for periods larger than a couple years.
Defaults: High, max, auto (yfinance figures it out for me)```''') 

        # for debugging!
        elif message.content.find('test') != -1:
            await message.channel.send('I work!')
            print('I work here too!')
        
        # still... for... debugging...
        print('Message from {0.author}: {0.content}'.format(message))

# create client object 
client = MyClient()

# run the bot! congratz!!
client.run(key)