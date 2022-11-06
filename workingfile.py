import argparse
import json

import requests

parser= argparse.ArgumentParser(description='finds the stadiums')
parser.add_argument('player',metavar='player', type=str, help='enter your player')
args = parser.parse_args()

player = args.player


url='https://www.thesportsdb.com/api/v1/json/2/searchplayers.php?p=' + player
r = requests.get(url)
data=json.loads(r.text)
print(data['player'][0]["strDescriptionEN"])
