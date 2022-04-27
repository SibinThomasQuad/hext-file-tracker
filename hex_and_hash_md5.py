import binascii
import os
import hashlib
class Calculate                                     : 
    
    def hex(self,file_name)                         : 
        filename                                    = file_name
        with open(filename, 'rb') as f              : 
            content                                 = f.read()
        return binascii.hexlify(content)
    
    def md5_sum(self,file_name)                     : 
        md5_hash                                    = hashlib.md5(open(file_name,'rb').read()).hexdigest()
        return md5_hash

class Compare                                       : 
    claculate_obj                                   = Calculate()
    
    def file_with_hex(self,file_path,old_hex)       : 
        file_hex                                    = str(self.claculate_obj.hex(file_path))
        if old_hex in file_hex                      : 
            print("[+][HEX] [WARNING] [Target HEX CODE FOUND] ["+file_path+"]")
    
    def file_with_md5(self,file_path,old_hash)      : 
        file_hash                                   = self.claculate_obj.md5_sum(file_path)
        if(file_hash == old_hash):
            print("[+][MD5] [WARNING] [Target MD5 CODE FOUND] ["+file_path+"]")

class Scan                                          : 
    compare_obj                                     = Compare()
    
    def all_files(self,dir_name,target_hex,type)    : 
        root                                        = dir_name
        for path, subdirs, files in os.walk(root)   : 
            for name in files                       : 
                file_path                           = os.path.join(path, name)
                if(type == 'hex'):
                    self.compare_obj.file_with_hex(file_path,target_hex)
                if(type == 'md5'):
                    self.compare_obj.file_with_md5(file_path,target_hex)

def run(directory,hexcode,type)                     : 
    scan_obj                                        = Scan()
    scan_obj.all_files(directory,hexcode,type)

def container()                                     : 
    label                                           = '''
     _   _ _______  __   _____ ____   _  ___  _ 
    | | | |____ \ \/ /  |_   _/ _  | | || \ \| |
    | |_| | |_  |\  /_____| || (_| |_| || |\ ` |
    |  _  |___| |/  |_____| | > _  |_   __|/ . |
    |_| |_|_____/_/\_\    |_|/_/ |_| |_|  /_/|_|
                                            
    '''
    print(label)
    claculate_obj                                   = Calculate()
    print("[1] [Calculate Hex]")
    print("[2] [Calculate MD5]")
    print("[3] [Scan for Rule]")
    print("[0] [Exit]\n")
    task                                            = input("Choose Operation : ")
    if(task == '0'):
        quit()
    if(task == '1'):
        file                                        = input("Enter File Path : ")
        print(claculate_obj.hex(file))
    if(task == '2'):
        file                                        = input("Enter File Path : ")
        print(claculate_obj.md5_sum(file))
    if(task == '3'):
        rule_file                                   = input("Enter rule file name : ")
        print('[+] Scanning Started')
        rule_code                                   = open(rule_file, "r")
        code                                        = rule_code.read()
        exec(code)
        print('[+] Scanning Completed')


try                                                 : 
    container()
except                                              : 
    print("[-] An error occured please check your files is set properly")
