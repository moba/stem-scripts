#!/usr/bin/python

##
## fetches latest descriptors and returns some numbers
## on the top 80% relays that allow exiting to port 80
##
##

CHECK_PORT = 80  # exit == allows port 80
TOP_PERCENT = 80 # limit analysis to 80% of total observed bw

from stem.descriptor.remote import DescriptorDownloader # to fetch descriptors
from stem.descriptor import parse_file # alternatively, for local parsing
import os
import collections
from difflib import SequenceMatcher

if os.path.exists('cached-consensus'):
    print "Using cached-consensus present in current directory:"
    descriptors = parse_file('cached-consensus')
else:
    print "Fetching latest descriptors, can take a while..."
    downloader = DescriptorDownloader()
    query = downloader.get_server_descriptors()
    descriptors = query.run()

print ""

#exits_only = filter(lambda descriptor:descriptor.exit_policy.is_exiting_allowed(), descriptors)
exits_only = filter(lambda descriptor:descriptor.exit_policy.can_exit_to(port=CHECK_PORT), descriptors)
exits_sorted =  sorted(exits_only, key=lambda descriptor:descriptor.observed_bandwidth,reverse=True)

print "%s relays (%s exits)" % (len(descriptors), len(exits_sorted))

total_bw = 0
total_exit_bw = 0

for desc in descriptors:
    total_bw += desc.observed_bandwidth
for desc in exits_sorted:
    total_exit_bw += desc.observed_bandwidth

print "total bandwidth non-exit relays: {} MB/s".format( (total_bw-total_exit_bw) / 1024 / 1024)
print "total bandwidth exit relays: {} MB/s".format(total_exit_bw / 1024 / 1024)
print ""

accumulated_bw = 0
top_relays=[]
top_contacts={}

for desc in exits_sorted:
    accumulated_bw += desc.observed_bandwidth
    top_relays.append(desc)
    if desc.contact in top_contacts:
        contact_bw, contact_count = top_contacts[desc.contact]
        contact_bw += desc.observed_bandwidth
        contact_count += 1
        top_contacts[desc.contact]=(contact_bw,contact_count)
    else:
        top_contacts[desc.contact]=(desc.observed_bandwidth,1)
    if (accumulated_bw > total_exit_bw * TOP_PERCENT/100): break

print "{}% ({} MB/s): {} exit relays".format(TOP_PERCENT,total_exit_bw * TOP_PERCENT/100 / 1024 / 1024, len(top_relays))

print "Fastest: {} ({} MB/s): {}".format(top_relays[0].nickname, top_relays[0].observed_bandwidth / 1024 / 1024, top_relays[0].contact)
print "Slowest: {} ({} MB/s): {}".format(top_relays[-1].nickname, top_relays[-1].observed_bandwidth / 1024/1024, top_relays[-1].contact)
print ""
print "Total contacts: {}".format(len(top_contacts))
print ""

fuzzy_contacts = {}
added = False

for contact, (bandwidth,count) in top_contacts.iteritems():
    if (contact is None): contact='<none>'
    for fuzzy_contact,(fuzzy_bandwidth,fuzzy_count) in fuzzy_contacts.iteritems():
        if (SequenceMatcher(None, contact, fuzzy_contact).ratio()>0.9):
            fuzzy_contacts[fuzzy_contact] = ( (fuzzy_bandwidth + bandwidth), (fuzzy_count + count) )
            added = True
    if not added:
            fuzzy_contacts[contact]=(bandwidth, count)
            added = False

print "Fuzzy total: {}".format(len(fuzzy_contacts.keys()))
print ""

print "MBit/s  | #Relays | Contact"
for contact, (bandwidth, count) in collections.Counter(fuzzy_contacts).most_common(30):
    print "{:<7} | {:<7} | {}".format(bandwidth / 1024 / 1024 * 8, count, contact)
