mkdir ~/.azure
touch ~/.azure/credentials
echo -en "[default]\nsubscription_id=$subscription_id\nclient_id=$client_id\nsecret=$secret\ntenant=$tenant">~/.azure/credentials
echo -en "[default]\nsubscription_id=$subscription_id\nclient_id=$client_id\nsecret=$secret\ntenant=$tenant">~/.azure/credentials

pip3 install ansible[azure]
curl -sL https://aka.ms/InstallAzureCLIDeb | bash
