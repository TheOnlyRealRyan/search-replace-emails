# TODO: Create .env to store global variable(list of emails) 
'''
This script is used to navigate through a folder and change emails found in the files to a new email.
It can also cleanup formatting of emails for standardisation.
'''

import os, fnmatch, random, re

# Global Variables and lists 
new_emails=(
    "myNewEmail@email.com",
    "yourNeweMail@email.com",
    "aNewPersonEmail@email.com",
)

replace_emails={
    "myemail@email.com":"myNewEmail@email.com",
    "Youremail@email.com":"yourNeweMail@email.com"
}

def cleanup(directory: str, filePattern: str) -> None:
    print("-->Starting cleanup()")
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                output_file = f.read()

            # --- Logic Here --- 
            new_email = ""
            
            # Find email
            variation_1 = re.findall("email:", output_file)
            variation_2 = re.findall("mail:", output_file)
            
            if variation_1 or variation_2:
                pass
            else:
                new_email = random.choice(new_emails)  
            
            # Standaridse email formats (has to be known)
            #TODO: OPTIONAL: create a looping script <--"email"--> and removes excess fluff
            
            output_file = re.sub("email2:", "email:", output_file)
            output_file = re.sub("email address:", "email:", output_file)
            output_file = re.sub("mail:", "email:", output_file)
            
            
            
            # --- Write Here ---
            with open(filepath, "w") as f:
                try:
                    if len(new_email) > 0:
                        print(f"-->Email Does not exist. Creating new email - {filepath}")
                        output_file = re.sub("email:", f"email: {new_email}", output_file)

                    f.write(output_file)
                    print("-->Write Successful")
                    
                except Exception as e:
                    print(e)
                    print(f"!!-->Critical Failure when writing at cleanup() - {filepath}")
                
                
def replace_single(directory: str, filePattern: str, search_email: str, replace_email: str) -> None:
    print("-->Starting replace_single()")
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                output_file = f.read()
            
            # --- Logic Here ---
            email = re.findall(f"email: {search_email}", output_file)
            
            # Replace here:
            try:
                if len(email) > 0:
                    print(f"-->Replacing Email: {email} - filepath: {filepath}")
                    output_file = re.sub(f"email: {search_email}", f"email: {replace_email}", output_file)
                else:
                    pass
            except Exception as e:
                print(e)
                print("!!-->Critical Failure at replace_single() - {filepath}")
            
            
            # --- Write Here ---
            with open(filepath, "w") as f:
                try:
                    f.write(output_file)
                    print("-->Write Successful")

                except Exception as e:
                    print(e)
                    print("-->Critical Failure! - " + filepath)


def replace_all(directory: str, filePattern: str) -> None:
    print("-->Starting replace_all()")
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                output_file = f.read()
                
            email = re.findall("email: ([A-Za-z0-9.@-]*)", output_file)
            
            if isinstance(email, list) and len(email) > 0:
                email = email[0].lower()
                
            # replace old email with new email
            try:
                if len(email) > 0:
                    if (any(email in i for i in replace_emails.keys())):
                        print(f"-->Replacing email with specific email - {filepath}")
                        new_email = replace_emails[email]
                        output_file = re.sub("email: ([A-Za-z0-9.@-]*)", f"email: {new_email}", output_file)
                    elif not(any(email in i for i in new_emails)):
                        new_email = random.choice(new_emails)
                        output_file = re.sub("email: ([A-Za-z0-9.@-]*)", f"email: {new_email}", output_file)
                else:
                    print(f"!-->email replacement issue in replace_all() - {filepath}")
                    
            except Exception as e:
                print(e)
                print(f"!!-->Critical Failure at replace_all() - {filepath}")    
                    # --- Write Here ---
            with open(filepath, "w") as f:
                try:
                    f.write(output_file)
                    print("-->Write Successful")

                except Exception as e:
                    print(e)
                    print("-->Critical Failure! - " + filepath)
                    
def main() -> None:
    path = "./search_here"
    file_type = "*.txt"
    
    search_email = "myNewEmail@email.com"
    replace_email = "yournewemail@gmail.com"
    
    cleanup(path, file_type)
    replace_single(path, file_type, search_email, replace_email)
    # replace_all(path, file_type)
    
if __name__ == "__main__":
    main()