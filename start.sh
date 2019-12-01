touch ~/.azure/credentials
echo -en "[default]\nsubscription_id=$subscription_id\nclient_id=$client_id\nsecret=$secret\ntenant=$tenant">~/.azure/credentials
pip3 install -r requirements.txt
curl -sL https://aka.ms/InstallAzureCLIDeb | bash

