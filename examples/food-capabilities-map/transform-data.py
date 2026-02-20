import json

data = json.load(open('data/__data.json'))

export_data = {
    'metadata': {
        'exportDate': '2025-02-09'
    },
    'data': [{'source': 'Capabilities', 'data': []}]
}

for group in data['groups']:
    domain = group['name']

    for capability in group['capabilities']:
        print(capability['name'])
        for sub_capability in capability['sub_capabilities']:
            print(sub_capability)

            export_capability = {
                'capability': sub_capability['name'],
                'domain': group['name'],
                'id': sub_capability['id'],
                'type': 'full-stack',
                'group': capability['name'],
                'details_sheet_gid': '',
                'discussions_sheet_gid': '',
                'targets_sheet_gid': '',
                'architecture_sheet_gid': '',
                'code': sub_capability['id'],
                'short_description': sub_capability['description'],
                'in_flight': 'true',
                'live': 'false',
                'people': 'Person1 Name, Role 1\nPerson2 Name, Role 2\n',
                'teams': 'Team 1',
                'slack_channels': '#org-slack-channel-1',
                'document_links': 'Grounded Architecture, https://grounded-architecture.io',
                'source_code_repositories': 'apache/activemq, asf/activemq/activemq, ActiveMQ main repo\napache/activemq-artemis, asf/activemq/activemq-artemis, Artemis main repo',
                'source_code_landscape_analysis': 'asf/activemq',
                'aws_accounts': 'account-1\naccount-2'
            }

            export_data['data'][0]['data'].append(export_capability)

with open('data/details.json', 'w') as file:
    file.write(json.dumps(export_data))