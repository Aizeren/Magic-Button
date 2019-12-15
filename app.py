import os

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def main():
	return render_template('index.html')


@app.route('/process_data/', methods=['POST'])
def process_data():
	#create vars with values of fields
	a = request.form["a"]
	b = request.form["b"]

	#create virtual machine
	os.system("ansible-playbook createVM.yml")

	#read VM piblic IP 
	tmpFile = open("./results/VMIP.txt", "r")
	nodeIP = tmpFile.read()
	tmpFile.close()

	#config hosts
	os.system("mkdir /etc/ansible")
	os.system("echo \"vm ansible_host="+nodeIP+" ansible_ssh_user=$admin_username ansible_ssh_pass=$admin_password \">/etc/ansible/hosts")
	
	#install requiered packages
	os.system("ansible-playbook installPacksOnVM.yml")

	#send requiered files to remote node
	os.system("ansible-playbook sendFilesToVM.yml")

	#create queues
	fromAppToVmQueueName = "fromAppToVmQueue"
	os.system("python3 createQueue.py "+fromAppToVmQueueName)
	fromVMToAppQueueName = "fromVmToVmQueue"
	os.system("python3 createQueue.py "+fromVMToAppQueueName)

	#send message to service bus
	os.system("python3 sendMsg.py "+fromAppToVmQueueName+" "+a+" "+b)

	#run start.py script on vm
	os.system("ansible-playbook startCalc.yml")

	#wait for answer message from service bus
	tmpFile = open("./results/result.txt", "r")
	while (tmpFile.read() == ""):
		os.system("python3 receiveMsg.py "+fromVMToAppQueueName)
	tmpFile.close()
	
	tmpFile = open("./results/result.txt", "r")
	result = tmpFile.read()
	tmpFile.close()
	#clear file
	open('./results/result.txt', 'w').close()
	
	return render_template('result.html', res = result)


if __name__ == "__main__":
	app.run()