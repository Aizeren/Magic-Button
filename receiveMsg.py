import os
import sys
from azure.servicebus import ServiceBusService, Message

# Create the QueueClient
sbs = ServiceBusService("magicButtonMB", shared_access_key_name="RootManageSharedAccessKey", shared_access_key_value="SNZewWOTdOkaVShECrp+OCKmSFqW5JCEjEM52slp5TM=")

msg = (sbs.receive_queue_message(sys.argv[1], peek_lock=False)).body.decode("utf-8")
# Receive the message from the queue

        #save answer in file
tmpFile = open("./results/result.txt", "w")
tmpFile.write(msg)
tmpFile.close()