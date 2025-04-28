import cv2

# Function to draw bounding box from YOLO annotations
def draw_yolo_bounding_box(image, annotation, image_width, image_height):
    # Parse YOLO annotation: norm_center_x, norm_center_y, norm_width, norm_height
    norm_center_x, norm_center_y, norm_width, norm_height = annotation
    
    # Convert YOLO format to pixel values
    center_x = int(norm_center_x * image_width)
    center_y = int(norm_center_y * image_height)
    box_width = int(norm_width * image_width)
    box_height = int(norm_height * image_height)
    
    # Calculate top-left and bottom-right corners
    x1 = int(center_x - (box_width / 2))
    y1 = int(center_y - (box_height / 2))
    x2 = int(center_x + (box_width / 2))
    y2 = int(center_y + (box_height / 2))
    
    # Draw rectangle on the image
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green box with thickness of 2
    
    return image

# Load an image
image = cv2.imread("resized_image.jpg")
image_height, image_width, _ = image.shape

# Example YOLO annotation: norm_center_x, norm_center_y, norm_width, norm_height
yolo_annotation = [0.5166666666666667, 0.524074074074074, 0.275, 0.23333333333333334]  # Replace with your actual annotation

# Draw the bounding box
image_with_box = draw_yolo_bounding_box(image, yolo_annotation, image_width, image_height)

# Display the image with the bounding box
cv2.imshow('YOLO Bounding Box', image_with_box)
cv2.waitKey(0)
cv2.destroyAllWindows()
