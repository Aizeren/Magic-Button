import os
import sys
from azure.servicebus import ServiceBusService, Message

# Create the QueueClient
sbs = ServiceBusService("magicButtonMB", shared_access_key_name="RootManageSharedAccessKey", shared_access_key_value="SNZewWOTdOkaVShECrp+OCKmSFqW5JCEjEM52slp5TM=")

# Receive the message from the queue
msg = (sbs.receive_queue_message(sys.argv[1], peek_lock=False)).body.decode("utf-8")

#save answer in file
tmpFile = open("./data.txt", "w")
tmpFile.write(msg)
tmpFile.close()