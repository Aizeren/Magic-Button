import os
import sys
from azure.servicebus import QueueClient, Message

# Create the QueueClient
queue_client = QueueClient.from_connection_string("Endpoint=sb://magicbuttonmb.$servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=SNZewWOTdOkaVShECrp+OCKmSFqW5JCEjEM52slp5TM=", sys.argv[1])

# Receive the message from the queue
with queue_client.get_receiver() as queue_receiver:
    messages = queue_receiver.fetch_next(timeout=3)
    for message in messages:
        args = message.split(" ")
        res = args[0]+args[1]
        tmpfile = open("./result.txt", "w")
        tmpfile.write(res)
        tmpfile.close()
        os.system("ansible-playbook sendFilesToApp.yml")
        message.complete()
