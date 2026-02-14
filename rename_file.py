import os 
from datetime import datetime 

folder_path = "/Users/venkatasaikumargundu/Desktop/Resume and Cover Letter"

today = datetime.now().strftime("%Y-%m-%d")

for file in os.listdir(folder_path):

    if file.startswith("."):
        continue

    if "saikumar_" in file.lower():
        continue

    old_file = os.path.join(folder_path, file)

    if os.path.isfile(old_file):

        name, ext = os.path.splitext(file)

        lower_name = name.lower()

        if "resume" in lower_name: 
            base = "saikumar_resume"
        elif "cover" in lower_name:
            base = "saikumar_coverletter"
        else: 
            base = "saikumar_document"
        
        new_name = f"{base}_{today}{ext}"

        new_file =os.path.join(folder_path, new_name)

        os.rename(old_file, new_file)

        message =  f"Renamed {file} -> {new_name}"
        print(message)

        with open(log_file, "a") as log: 
            log.write(message +"\n")
