import os

from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)
a = 0
b = 0
result = 0

@app.route("/")
def main():
	return render_template('index.html')


@app.route('/createvm/', methods=['POST'])
def createvm():
	#create vars with values of fields
	global a
	global b
	a = request.form["a"]
	b = request.form["b"]

	os.system("rm ~/.ssh/known_hosts")

	#create virtual machine
	os.system("ansible-playbook ./scripts/createVM.yml")

	#read VM piblic IP 
	tmpFile = open("./results/VMIP.txt", "r")
	nodeIP = tmpFile.read()
	tmpFile.close()

	#config hosts
	os.system("mkdir /etc/ansible")
	os.system("echo \"vm ansible_host="+nodeIP+" ansible_ssh_user=$admin_username ansible_ssh_pass=$admin_password \">/etc/ansible/hosts")
	#os.system("echo \"vm ansible_host="+nodeIP+" ansible_ssh_user=panda ansible_ssh_pass=superior0@mail.ru \">/etc/ansible/hosts")

	return redirect(url_for("installpacks"))


@app.route('/installpacks/')
def installpacks():
	#install requiered packages
	os.system("ansible-playbook ./scripts/installPacksOnVM.yml")

	return redirect(url_for("installpacks2"))


@app.route('/installpacks2/')
def installpacks2():
	#install requiered packages
	os.system("ansible-playbook ./scripts/installPacksOnVM2.yml")

	return redirect(url_for("runcalc"))


@app.route('/runcalc/')
def runcalc():
	global result
	#send requiered files to remote node
	os.system("ansible-playbook ./scripts/sendFilesToVM.yml")

	#create queues
	fromAppToVmQueueName = "fromAppToVmQueue"
	os.system("python3 ./scripts/createQueue.py "+fromAppToVmQueueName)
	fromVMToAppQueueName = "fromVmToAppQueue"
	os.system("python3 ./scripts/createQueue.py "+fromVMToAppQueueName)

	#send message to service bus
	os.system("python3 ./scripts/sendMsg.py "+fromAppToVmQueueName+" "+a+" "+b)

	#run start.py script on vm
	os.system("ansible-playbook ./scripts/startCalc.yml")

	#wait for answer message from service bus
	tmpFile = open("./results/result.txt", "r")
	while (tmpFile.read() == ""):
		os.system("python3 ./scripts/receiveMsg.py "+fromVMToAppQueueName)
	tmpFile.close()
	
	tmpFile = open("./results/result.txt", "r")
	result = tmpFile.read()
	tmpFile.close()
	#clear file
	open('./results/result.txt', 'w').close()

	tmpFile = open("./results/test.txt", "w")
	tmpFile.write(result)
	tmpFile.close()

	return redirect(url_for("removevm"))

@app.route('/removevm/')
def removevm():
	os.system("ansible-playbook ./scripts/removeVm.yml")
	
	return render_template('result.html', res = result)


if __name__ == "__main__":
	app.run()