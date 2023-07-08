import requests


url = 'https://akabab.github.io/superhero-api/api/all.json'
respons = requests.get(url)

if 200 <= respons.status_code < 300:
  data = respons.json()
  all_hero = {}

  for hero in data:
    all_hero[hero['name']] = hero['powerstats']['intelligence']

  m_hero = {}

  for name in all_hero:
    if name == 'Hulk' or name == 'Captain America' or name == 'Thanos':
      m_hero[name] = all_hero[name]
      
  print(max(m_hero, key=m_hero.get))
