import argparse
import json
import sys
import urllib
import urllib.parse

# Create API requests
def create_request(domain, password, hostname, protocol):
	values = {'domain': domain,
				'password': password,
				'command': 'REPLACE ' + hostname + ' 86400 ' + {4: 'A', 6: 'AAAA'}[protocol] + ' DYNAMIC_IP'}
	request = urllib.parse.urlencode(values)
	return request

# Send request
def send_request(request):
	return True

# Get arguments and parse them
def initialise():
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', '--config-file', help='Path to config file.', required=True)
	parser.add_argument('-n', '--dry-run', help='Don\'t actually update DNS records.', required=False, default=False, action='store_true')
	parser.add_argument('-p', '--protocol', help="Only update IPv4 or IPv6 record. Default is both.", choices=['4', '6'])
	args = parser.parse_args()

	with open(args.config_file) as f:
	    config = json.load(f)

	if args.protocol:
		protocols = [int(args.protocol)]
	else:
		protocols = [4, 6]

	return config, args.dry_run, protocols

config, dry_run, protocols = initialise()

for domain in config.keys():
	for protocol in protocols:
		print('Requesting REPLACE for ' + config[domain]['hostname'] + '.' + domain + ' for IPv' + str(protocol))
		request = create_request(domain=domain, password=config[domain]['password'], hostname=config[domain]['hostname'], protocol=protocol)
		result = send_request(request)


