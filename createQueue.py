import sys
from azure.servicebus import ServiceBusClient

queueName = sys.argv[1]

sb_client = ServiceBusClient.from_connection_string('Endpoint=sb://magicbuttonmb.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=SNZewWOTdOkaVShECrp+OCKmSFqW5JCEjEM52slp5TM=')
sb_client.create_queue(queueName)