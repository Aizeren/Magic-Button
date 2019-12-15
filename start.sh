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
subscription_id=884a98c6-174f-432e-b7db-7fd81c04e0c2
client_id=2b433a65-41b6-474c-83c7-99e5e0ef4fdf
secret=5b4f3320-4d34-44e0-9cb8-4873d049fae4
tenant=08b9d3f9-faf0-44a0-8fe8-28e030ecfb5b\">~/.azure/credentials
sudo python3 -m pip install ansible[azure]
sudo apt install sshpass
sudo python3 -m pip install --user azure-servicebus==0.21.0
sudo python3 -m pip install azure
sudo python3 -m pip install azure-common
touch data.txt
export ANSIBLE_HOST_KEY_CHECKING=False">./scripts/VmStart.sh
