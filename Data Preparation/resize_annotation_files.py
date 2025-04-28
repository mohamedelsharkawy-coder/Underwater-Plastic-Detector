import os

for file_name in os.listdir("resized_extracted_trash_plastic_annotation"):
    src = os.path.join('resized_extracted_trash_plastic_annotation', file_name)
    dest = os.path.join('resized_extracted_trash_plastic_annotation', f'resized_{file_name}')
    
    os.rename(src, dest)