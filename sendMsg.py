import sys
from azure.servicebus import ServiceBusService, Message

sbs = ServiceBusService("magicButtonMB", shared_access_key_name="RootManageSharedAccessKey", shared_access_key_value="SNZewWOTdOkaVShECrp+OCKmSFqW5JCEjEM52slp5TM=")
msg = Message((sys.argv[2] + " " + sys.argv[3]).encode())
sbs.send_queue_message(sys.argv[1], msg)