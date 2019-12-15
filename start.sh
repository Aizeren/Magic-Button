mkdir ~/.azure
touch ~/.azure/credentials
echo -n "[default]\nsubscription_id=$subscription_id\nclient_id=$client_id\nsecret=$secret\ntenant=$tenant">~/.azure/credentials
pip3 install ansible[azure]
curl -sL https://aka.ms/InstallAzureCLIDeb | bash
apt install sshpass
pip3 install azure-servicebus==0.21.0
export ANSIBLE_HOST_KEY_CHECKING=False

echo -n "mkdir ~/.azure\ntouch ~/.azure/credentials\necho -n \"[default]\nsubscription_id=$subscription_id\\nclient_id=$client_id\\nsecret=$secret\\ntenant=$tenant\">~/.azure/credentials">VmStart.sh
echo -n "\npip3 install ansible[azure]\ncurl -sL https://aka.ms/InstallAzureCLIDeb | bash\napt install sshpass\npip3 install azure-servicebus==0.21.0\npip3 install azure\npip3 install azure-common\nexport ANSIBLE_HOST_KEY_CHECKING=False">>VmStart.sh
