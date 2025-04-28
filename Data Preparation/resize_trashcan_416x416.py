import os
import cv2



# for file_name in os.listdir(os.path.join("resized_extracted_trash_plastic_images")):
#     image_path = os.path.join("resized_extracted_trash_plastic_images", file_name)    
#     image = cv2.imread(image_path)
#     print(image.shape)

for file_name in os.listdir(os.path.join('extracted_trash_plastic_without_counter_images')):
    
    # path of the image
    file_path = os.path.join('extracted_trash_plastic_without_counter_images', file_name)
    
    # read the image
    image = cv2.imread(file_path)

    # Resize the image to 416x416
    resized_image = cv2.resize(image, (416, 416))

    # save the resized image
    cv2.imwrite(os.path.join('resized_extracted_trash_plastic_without_counter_images', file_name), resized_image)




