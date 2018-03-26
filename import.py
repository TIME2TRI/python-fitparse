#!/usr/bin/python

from fitparse import FitFile
import sys
import datetime

now = datetime.datetime.now()

# if(len(sys.argv)){
#     fileName = sys.argv[0];
# } else{
#     fileName = '/Users/soerenkroell/Desktop/19016651587_mo_swim_aber_ohne_session.fit';
# }


if len(sys.argv) >= 2:
     fileName = sys.argv[1]
else:
     fileName = '/Users/soerenkroell/Desktop/19016651587_mo_swim_aber_ohne_session.fit'

print
print "Start " + now.strftime("%H:%M:%S")
print

print "importing file %s"%(fileName)

if len(sys.argv) >= 3:
     fieldName = sys.argv[2]
else:
     fieldName = 'session'

fitfile = FitFile(fileName)

# Get all data messages that are of type record
for record in fitfile.get_messages(fieldName):

    # Go through all the data entries in this record
    for record_data in record:

        # Print the records name and value (and units if it has any)
        if record_data.units:
            print " * %s: %s %s" % (
                record_data.name, record_data.value, record_data.units,
            )
        else:
            print " * %s: %s" % (record_data.name, record_data.value)
    print

now = datetime.datetime.now()

print
print"End " + now.strftime("%H:%M:%S")
print
