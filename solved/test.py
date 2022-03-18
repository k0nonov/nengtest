import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
                hostname="192.168.88.202",
                username="super",
                password="super",
                look_for_keys=False,
                allow_agent=False,
                )
ssh = client.invoke_shell()
ssh.send("conf\n")

for i in range(5,11):
    command = "interface Ethernet1/0/"+str(i)+'\n'
    ssh.send(command)
    ssh.send("switchport access vlan 10\n")

ssh.send("sh run | inc switch")
print(ssh.recv(3000).decode("UTF-8"))
ssh.send("exit\n")
ssh.send("exit\n")
ssh.close()
