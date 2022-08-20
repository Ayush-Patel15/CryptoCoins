# CryptoCoins

A website that represents real-time data of top 12 cryptocurrencies by market_cap. 
Data will update after 150 seconds (2.5 minutes) continuosly.

App:- [CryptoCoins](https://cryptocurrency-coins.herokuapp.com/)

Attributes are:- 

- name
- price
- days_high
- days_low
- ath
- atl
- total_supply
- market_cap
- volume
- change of price in last 1hr (percent)
- yeartodate price change percent

It's basically a small website displaying frontend + backend work with the help of Flask framework.


`src` - The folder consist of all the files that are responsible for logic of backend work. It has the scraper function and helpers to scrape the required data from different sources.

`templates` & `static` - The folder consist of all the files that are responsible for frontend structure. It has the .html, .css stylings and images required for structuring the base template.

`app.py` - It's the main server file i.e. consists of all api-endpoints.

#### NOTE: Website is not responsive as of now.

## To Run it Locally

- Make sure you have python(version>=3.0) installed in your system.

- Visit the root-folder i.e. Cryptocoins.

- And install the requirements.txt file.

```python
pip install -r requirements.txt
```

- You are ready to start. To activate flask server locally, run

```python
..\cryptocoins\python app.py
```

- Output will be something like these. Ps- Ignore Warnings!

```bash
* Serving Flask app 'app'
* Debug mode: off
* Running on http://127.0.0.1:5000
```

- Copy the localhost route and paste it in browser. `http://127.0.0.1:5000`


## Feel Free to contribute more..! Either on frontend or backend.

### Create a new branch and contribute..