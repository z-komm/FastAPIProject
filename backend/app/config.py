# backend/app/config.py

def get_combined_prompt():
    with open("app/config/system_prompt.txt") as sysf, open("app/config/master_prompt.txt") as mastf:
        return sysf.read() + "\n\n" + mastf.read()