#
# Burp Suite DAST Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json

#
# Get the scan schedules configured in the system
#
def getscheduleitems(APIURL,APIKEY,doprint=True, output=False, sortby="start", sortorder="asc"):
 
    # , sort_order: SortOrder <- DIDNTWORK
    query = '''
        query GetScheduleItems  ($sort_by: SortBy) {
            schedule_items (sort_by: $sort_by) {
                id
                sites{
                    id
                    name
                }
                folders{
                    id
                    name
                }
                schedule {
                    initial_run_time
                    rrule
                }
                has_run_more_than_once
                scheduled_run_time
            }
        }
        '''

    variables = { 
            "sort_by": sortby, 
            "sort_order": sortorder, 
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result

#
# Add a scan schedule
#
def addscanschedule(APIURL,APIKEY,siteids, initialruntime, schedule, scan_configuration_ids,doprint=True, output=False ):
 
    query = '''
    mutation CreateScheduleItems  ($ids: [ID!]!, $initial_run_time: Timestamp, $schedule: String, $scan_configuration_ids: [ID!]) {
        create_schedule_item (
            input: {
                site_ids: $ids
                schedule: {
                    initial_run_time: $initial_run_time
                    rrule: $schedule
                }
                scan_configuration_ids: $scan_configuration_ids
            } 
        ) 

        {
            schedule_item{
                id
                sites {
                    id
                    name
                }
                schedule {
                    initial_run_time
                    rrule
                }
                scan_configurations {
                    id
                    name
                }
            }
        }
    }
    '''

    variables = {
            "ids": siteids,
            "initial_run_time": initialruntime,
            "schedule": schedule,
            "scan_configuration_ids": scan_configuration_ids
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result


#
# Update a scan schedule
#
def updatescanschedule(APIURL,APIKEY,scheduleid, siteids, initialruntime, schedule, scan_configuration_ids,doprint=True, output=False):
 
    query = '''
    mutation UpdateScheduleItems  ($schedule_id: ID!, $site_ids: [ID!], $initial_run_time: Timestamp, $initial_run_time_is_set: Boolean, $schedule: String, $rrule_is_set: Boolean, $scan_configuration_ids: [ID!]) {
        update_schedule_item (
            input: {
                id: $schedule_id
                site_ids: $site_ids
                schedule: {
                    initial_run_time: $initial_run_time
                    initial_run_time_is_set: $initial_run_time_is_set
                    rrule: $schedule
                    rrule_is_set: $rrule_is_set
                }
                scan_configuration_ids: $scan_configuration_ids
            } 
        ) 

        {
            schedule_item{
                id
                sites {
                    id
                    name
                }
                schedule {
                    initial_run_time
                    rrule
                }
                scan_configurations {
                    id
                    name
                }
                has_run_more_than_once
                scheduled_run_time
            }
        }
    }
    '''

    variables = {
            "schedule_id": scheduleid,
            "site_ids": siteids,
            "initial_run_time": initialruntime,
            "initial_run_time_is_set": True,
            "schedule": schedule,
            "rrule_is_set": True,
            "scan_configuration_ids": scan_configuration_ids
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result

#
# Delete a scan schedule
#
def deletescanschedule(APIURL,APIKEY,scanid,doprint=True, output=False):
 
    query = '''
    mutation DeleteScheduleItem  ($id: ID!) {
        delete_schedule_item (
            input: {
               id: $id
            } 
        ) 

        {
            id
        }
    }
    '''

    variables = { 
            "id": scanid
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result



