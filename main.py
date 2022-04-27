import binascii
import os
class Calculate:
    def hex(self,file_name):
        filename = file_name
        with open(filename, 'rb') as f:
            content = f.read()
        return binascii.hexlify(content)
class Compare:
    def file_with_hex(self,file_path,old_hex):
        claculate_obj = Calculate()
        file_hex = str(claculate_obj.hex(file_path))
        if old_hex in file_hex:
            print("[+] ['WARNING'] [Target HEX CODE FOUND] ["+file_path+"]")
class Scan:
    compare_obj = Compare()
    def all_files(self,dir_name,target_hex):
        root = dir_name
        for path, subdirs, files in os.walk(root):
            for name in files:
                file_path = os.path.join(path, name)
                self.compare_obj.file_with_hex(file_path,target_hex)
def run(directory,hexcode):       
    scan_obj = Scan()
    scan_obj.all_files(directory,hexcode)
def container():
    label = '''
     _   _ _______  __   _____ ____   _  ___  _ 
    | | | |____ \ \/ /  |_   _/ _  | | || \ \| |
    | |_| | |_  |\  /_____| || (_| |_| || |\ ` |
    |  _  |___| |/  |_____| | > _  |_   __|/ . |
    |_| |_|_____/_/\_\    |_|/_/ |_| |_|  /_/|_|
                                            
    '''
    print(label)
    print("[1] [Calculate Hex]\n")
    print("[2] [Scan for Hex]\n")
    task = input("Choose Operation : ")
    if(task == '1'):
        file = input("Enter File Path : ")
        claculate_obj = Calculate()
        print(claculate_obj.hex(file))
    if(task == '2'):
        rule_file = input("Enter rule file name : ")
        rule_code = open(rule_file, "r")
        code = rule_code.read()
        exec(code)
container()
