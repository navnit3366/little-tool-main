import code
import urllib.request
import pyfiglet
import cryptocode
import socket
import threading

#banner
banner = pyfiglet.figlet_format("MEAW  TOOLS")
print(banner)
print("-" * 70)
print("1. port scanning")
print("2. message encryption")
print("3. message decryption (decryption from 2.)")
print("4. get website source code")
print("0. exit")

def main():
    #tool input
    tool = input("-" * 70 + "\n[input number] >> ")

    if tool == "0":
        pass

    if tool == "1":
        target = input("\n[PORT SCANNING] Input target: ")
        def port_scanner(port):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                print(f"Port {port} is open")
            except:
                pass

        for port in range(1, 5050):
            thread = threading.Thread(target=port_scanner, args=[port])
            thread.start()
        main()

    if tool == "2":
        msg = input("\n[MESSAGE ENCRYPTION] Input text: ")
        key = "1-2-3-4-lmao-1-2-3-4"
        encoded = cryptocode.encrypt(msg, key)
        print(f"encrypted msg: {encoded}")
        main()

    if tool == "3":
        msg = input("\n[MESSAGE DECRYPTION] Input eccrypted text: ")
        key = "ela-is-yachis-little-girl-177013-UwU"
        decoded = cryptocode.decrypt(msg, key)
        print(f"decrypted message: {decoded}")
        main()

    if tool == "4":
        url = input("[WEBSCRAPER] Input url: ")
        try:
            page = urllib.request.urlopen(url)
            code = page.read()
            print(str(code))
        except:
            page = urllib.request.urlopen(f"https://{url}")
            code = page.read()
            print(str(code))
        main()
    
main()
