rm ~/.ssh/known_hosts
mkdir ~/.azure
touch ~/.azure/credentials
echo -n "[default]\nsubscription_id=$subscription_id\nclient_id=$client_id\nsecret=$secret\ntenant=$tenant">~/.azure/credentials
pip3 install ansible[azure]
curl -sL https://aka.ms/InstallAzureCLIDeb | bash
apt install sshpass
pip3 install azure-servicebus==0.21.0
export ANSIBLE_HOST_KEY_CHECKING=False

echo -n "sudo apt update
sudo apt install python3-pip --assume-yes
mkdir ~/.azure
touch ~/.azure/credentials
echo -n \"[default]
subscription_id=$subscription_id
client_id=$client_id
secret=$secret
tenant=$tenant\">~/.azure/credentials
sudo python3 -m pip install ansible[azure]
sudo apt install sshpass">./scripts/VmStart.sh

echo -n  "sudo python3 -m pip install --user azure-servicebus==0.21.0
sudo python3 -m pip install azure
sudo python3 -m pip install azure-common
touch data.txt
export ANSIBLE_HOST_KEY_CHECKING=False">./scripts/VmStart2.sh