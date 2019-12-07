import sys
from azure.servicebus import QueueClient, Message

# Create the QueueClient
queue_client = QueueClient.from_connection_string("Endpoint=sb://magicbuttonmb.$servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=SNZewWOTdOkaVShECrp+OCKmSFqW5JCEjEM52slp5TM=", sys.argv[1])

# Send a test message to the queue
msg = Message((sys.argv[2]+" "+sys.argv[3]).encode())
queue_client.send(msg)