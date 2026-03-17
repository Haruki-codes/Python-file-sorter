import os
import shutil as su


list_folder_type = ['Image','File','Movie','Other']
for x in list_folder_type:
    file_path = os.path.join("path_of_your",x)
    if os.path.isdir(file_path):
        continue
    else:
        os.mkdir(file_path)

image = ('.png','.jpg','.jpeg','Webp','.svg','.avif')
file = ('.pdf','.docx','.txt','.rtf','.zip','.pptx')
movie = ('.mkv',)
system_file = ('.sys', '.dll', '.exe','.ini','.cfg','.so')


for dirpath,dirnames,filenames in os.walk("path_of_your"):
    dirnames[:] = [d for d in dirnames if d not in list_folder_type]
    for f in filenames:
        current_file_path = os.path.join(dirpath, f)      
        if f.lower().endswith(image):
            destination_path = os.path.join("path_you_want_to_Send_file", f) 
            # THE CORRECT CHECK
            if not os.path.exists(destination_path):
                su.move(current_file_path, destination_path)
            else:
                print(f"Skipped {f} - already exists in Image folder")  

        elif f.lower().endswith(file):
                destination_path = os.path.join("path_you_want_to_Send_file",f)
                if not os.path.exists(destination_path):
                    su.move(current_file_path,destination_path)
                else:
                     print(f"Skipped {f} - already exists in File folder")  

        elif f.lower().endswith(movie):
                destination_path = os.path.join("path_you_want_to_Send_file",f)
                if not os.path.exists(destination_path):
                    su.move(current_file_path,destination_path)
                else:
                    print(f"Skipped {f} - already exists in movie folder")  

        else:
                if not f.endswith(system_file):
                    destination_path = os.path.join("path_you_want_to_Send_file",f)
                    if not os.path.exists(destination_path):
                        su.move(current_file_path,destination_path)
                    else:
                        print(f"Skipped {f} - already exists in Other folder")  

print("Done!")
