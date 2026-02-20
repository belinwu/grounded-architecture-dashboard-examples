import json
import datetime

# loading config
config = json.load(open('config.json'))

data = json.load(open('data/personas.json'))
dateString = datetime.date.today().strftime('%Y-%m-%d')

with open('docs/index.html', 'w') as html_file:
    template = open('templates/documents.html').read()
    html_file.write(template
                    .replace('${date}', dateString)
                    .replace('${personas}', json.dumps(data)))

