#
# Burp Suite DAST Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

# Library documentation
# https://github.com/prodigyeducation/python-graphql-client

import bseeptgraphql
import json

def getevents(APIURL,APIKEY,scan_id,event_type=None,doprint=True, output=False):

    query = '''query GetEventLog ($scan_id: ID!, $type: [ScanEventLogType!]) {
        scan_event_log(scan_id: $scan_id, type: $type) {
            entries{
                type
                scanner_message_id
                message
                cause
                remediation
                timestamp
                duplicate_count
            }
        }
    }
    '''

    variables = {"scan_id": scan_id}
    if event_type is not None:
        variables["type"] = event_type

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result
