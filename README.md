### This script is written in Python, uses Selenium and BeautifulSoup.

### Task:

- Speed up the process of sending applications for viewing apartments in the Czech Republic on the website [https://www.bezrealitky.cz](https://www.bezrealitky.cz/).

### Problem:

- Due to the high demand in the real estate market in the Czech Republic, many applicants are not visible to landlords.

### Functional:

1. The program opens a browser with a website
2. Enters personal data, passes authorization
3. Looks for offers on the site according to several characteristics:
    - city
    - price
4. Checks if the user has already visited the real estate profile
5. Visits new profiles and sends a message to the landlord
6. In the console, displays messages for sending a letter or skipping a profile

### Important:

- In some places of the script, you need to change the information to your data

## How to launch:

1. Clone this repository on your computer:

```
git clone https://github.com/chumachenkoo/Generator_QR.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Insert your data:

```
python run.py
```

4. Launch the script:

```
python app.py
```