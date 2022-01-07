# AlgoTrade

This repository holds three projects involving my investments and trading. I have been learning these subjects since 2018, and I implemented some code to help me with those. All of the projects are based on the Binance API (https://github.com/binance). I implemented my wrapper for the API instead of using available public ones for security. The idea is to slowly learn about algorithmic trading while increasing my investments and, most importantly, increasing my knowledge while having fun.

This repository is incomplete and public (the real and complete one is private). Most of the code here won't work. Nonetheless, you can look at the main idea of what was implemented.

The three implementations consist of: 
- A Long-Short Term Memory (LSTM) recurrent neural network implementation predicts assets closing price: pricePrediction folder. The predictions are made once a day and are automatically updated to a google sheet available at: https://docs.google.com/spreadsheets/d/1uw284SOUIcdcCHVQ-47AtQavAnArkeiZBmNisIw6Fhk/edit?usp=sharing.  You can check that the bot inserts the predictions one day before the closing. Even though prediction results are not precise, they are promising.

- A trading history analyzer (myaccount.py) shows me all of the trades I performed. It also calculates the average prices on the assets I previously traded, showing me profit/loss on liquidated assets and my potential profit/loss with the assets I still have.

- Initial attempts to implement a trading bot: firstBot.py and spreadFind.py. The first one analyzes the possibility of using Bollinger Bands for systematic trading, and the second one looks for open arbitrage possibilities in a market. These are ard challenges, and I still have a lot to learn to make them work. I have other ideas involving trading setups (such as "power break out"), which are more simple to implement and most certainly can at least guide me to perform a trade myself.

So far, I have almost tripled my (small) investments. I am "learning while doing", always taking calculated risks. All the code was implemented in my free time, aside from my Ph.D. work.
