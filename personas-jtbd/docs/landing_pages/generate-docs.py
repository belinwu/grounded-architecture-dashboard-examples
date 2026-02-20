import json
import datetime

# loading config
config = json.load(open('../../config.json'))

personas = json.load(open('../../data/personas.json'))

template = open('templates/landing_page.html').read();

dateString = datetime.date.today().strftime('%Y-%m-%d')

all_personas = []

for group in personas:
    print(group['group'])
    for persona in group['personas']:
        persona['domain'] = group['group']
        all_personas.append(persona)

for group in personas:
    for persona in group['personas']:
        name = persona['name']

        htmlFile = 'docs/' + str(persona['id']) + '.html'
        print(htmlFile)
        with open(htmlFile, 'w') as html_file:
            html_file.write(template
                            .replace('${date}', dateString)
                            .replace('${config}', json.dumps(config))
                            .replace('${all_personas}', json.dumps(all_personas))
                            .replace('${persona_name}', persona['name'])
                            .replace('${persona}', json.dumps(persona)))
