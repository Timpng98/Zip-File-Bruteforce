#brute force into password protected zip files

from zipfile import ZipFile

#extract the zip file with a given password
def attempt_extract(zf, password):
    try:
        zf.extractall(pwd=password)
        return True
    except:
        return False

def main():
    zipfile = input("Enter the zip file you want to bruteforce: ")
    print("[+] Beginning bruteforce ")
    with ZipFile(zipfile) as zf:
        with open('rockyou.txt', 'rb') as f:
            # loop through password entries in rockyou.txt
            # Attempt to extract the zip file using each password
            for pd in f:
                password = pd.strip()
                # Correct password extract versus incorrect password attempt)
                if attempt_extract(zf, password):
                    print("[+] Password found: ", password)
                else:
                    print("[-] Password not found in list")

if __name__ == "__main__":
    main()