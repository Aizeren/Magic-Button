import sys
import os
from azure.servicebus import ServiceBusService

queueName = sys.argv[1]
sbs = ServiceBusService("magicButtonMB", shared_access_key_name="RootManageSharedAccessKey", shared_access_key_value="SNZewWOTdOkaVShECrp+OCKmSFqW5JCEjEM52slp5TM=")

sbs.create_queue(queueName)