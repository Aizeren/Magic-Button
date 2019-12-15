mkdir ~/.azure
touch ~/.azure/credentials
echo -n "[default]\nsubscription_id=$subscription_id\nclient_id=$client_id\nsecret=$secret\ntenant=$tenant">~/.azure/credentials
pip3 install ansible[azure]
curl -sL https://aka.ms/InstallAzureCLIDeb | bash
apt install sshpass
export ANSIBLE_HOST_KEY_CHECKING=False
pip3 install azure-servicebus==0.21.0
export KEY_NAME=RootManageSharedAccessKey
export NAMESPACE=magicButtonMB
export KEY_VALUE=SNZewWOTdOkaVShECrp+OCKmSFqW5JCEjEM52slp5TM=