# Bitcoin Lottery

### Simple Python script for generating Bitcoin addresses and checking them for balance on the blockchain.

As of 2021, there are over 10m bitcoins ($85b) accumulated in dormant bitcoin addresses with no outgoing transactions at all since the Satoshi era, so these scripts are more or less like playing the lottery with an infinite amount of attempts.

Needless to say, you're more likely to throw random mechanical parts off a cliff and come down to a fully working car rather than finding a collision, but you're still free to try! 👀

# Scripts 

There are two main scripts, `BTC_Lottery_Create.py` will generate a random private key with matching public compressed and uncompressed key (They're two different wallet addresses) and test it against a public blockchain for any balance. (Slower script).

The second script `BTC_Lottery_From_List.py` will take in a list of dynamically generated private and public keys (In this case [cryptoguru](https://lbc.cryptoguru.org/dio/) and test every single wallet in that page for balance. HTTP requests are asynchronous, so consider adding a timeout to not get flagged as spam by the blockchain API. (Faster script)

# First time run
 - Make sure you have Python 3 or higher installed and setup as OS PATH.
 - Run 'pip install -r -requirements.txt' on the same folder.
 - Run the script.
 - If any collision is found, a 'loot.txt' file will be created, containing the private key to access the wallet.
 - (OPTIONAL) Add your Telegram bot details in the commented section to get notified via message if a collision is found!


# Screenshots
`BTC_Lottery_Create.py`

![EuxImxg](https://user-images.githubusercontent.com/85108160/129419646-8f7527e8-6a35-44c9-a271-2266f22ead64.png)

`BTC_Lottery_From_List.py`

![2UI5LrW](https://user-images.githubusercontent.com/85108160/129419795-23519077-49cb-48fe-b2fc-5c0b627e7d91.png)

# Contribution
This is just a small project I had in mind so I'm sure it can be improved in many ways, I'm open to any suggestion!
