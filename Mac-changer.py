import subprocess

new_mac = input("Enter your new mac : ")

def mac_changer(new_mac):
    print("[+] changing you Eth0 mac address to " + new_mac)
    subprocess.run(["ifconfig", "eth0", "down"])
    subprocess.run(["ifconfig", "eth0", "hw", "ether", new_mac])
    subprocess.run(["ifconfig", "eth0", "up"])


mac_changer(new_mac)