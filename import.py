#!/usr/bin/python

from fitparse import FitFile

import sys
import datetime
import os
# import json
import simplejson as json

def importFitAndReturnJson(fileName, fieldName):
     fitfile = FitFile(fileName)
     return json.dumps(fitfile.get_messages(fieldName, False, True), iterable_as_array=True)

def importFit(fileName, fieldName):
     now = datetime.datetime.now()

     if fileName:
          print "importing file %s" % (fileName)
          print
          print "Start " + now.strftime("%H:%M:%S")
          print

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
          print "End " + now.strftime("%H:%M:%S")
          print
     else:
          print "Missing filname"


if __name__ == "__main__":
     fileName = False

     if len(sys.argv) >= 2:
          fileName = sys.argv[1]

     if len(sys.argv) >= 3:
          fieldName = sys.argv[2]
     else:
          fieldName = 'session'

     if len(sys.argv) >= 4:
          asJson = sys.argv[3]
     else:
          asJson = False

     if asJson:
          print importFitAndReturnJson(fileName, fieldName)
     else:
          print importFit(fileName, fieldName)
