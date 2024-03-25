import json
from urllib.request import urlopen

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import requests
from bs4 import BeautifulSoup, SoupStrainer

season = 2023
target_url = ('https://www.fangraphs.com/leaders/major-league?pos=all&stats=bat'
              f'&lg=all&type=0&season={season}&month=0&season1={season}&ind=0&'
              'qual=0&pagenum=1&pageitems=2000000000')

html = requests.get(target_url)
soup = BeautifulSoup(html.content, 'html.parser', from_encoding='utf_8')
json_object = json.loads(soup.find('script', type='application/json').text)
data = json_object['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['data']

df = pd.DataFrame(data).replace('- - -', np.nan).drop(columns=['Name', 'PlayerNameRoute', 'Team', 'TeamName', 'TeamNameAbb', 'teamid', 'AgeR', 'SeasonMin', 'SeasonMax']).rename(columns={'xMLBAMID': 'MLBAMID'})



"""
<script id="__NEXT_DATA__" type="application/json">
"pageprops": {
    "dehydratedState": {
        "mutations":[],
        "queries": [{"state": {"data": {"data": [{}, {}, ..., {}]}}}]
    }
}
"""
