def crop_images_in_folder(input_folder, output_folder, crop_size_mm):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get the list of image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.tif'))]

    for image_file in image_files:
        # Load the image using OpenCV
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        # Convert image from BGR to RGB for matplotlib display
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Calculate the cropping dimensions
        height, width, _ = image.shape
        crop_size = int(crop_size_mm * 2.83465)  # Convert mm to pixels assuming 72 dpi (2.83465 pixels/mm)
        crop_height = height - 2 * crop_size
        crop_width = width - 2 * crop_size

        # Perform the cropping
        cropped_image = image[crop_size:crop_size + crop_height, crop_size:crop_size + crop_width]

        # Save the cropped image to the output folder
        output_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_path, cropped_image)

        print(f"Cropped image saved: {output_path}")
