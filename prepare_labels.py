import pandas as pd
import os
import glob
import cv2

from tqdm import tqdm

show_info = True
images_with_required_classes = 0
total_images = 0
labels = {
    'green': 0,
    'red': 1,
    'yellow': 2
}

root_folder_names = ['light', 'dark']
root_folder_name_mapper = {
    'light': 'dayClip',
    'dark': 'nightClip'
}

annotation_root = '../My Drive/color_detection/labels'
image_root = '../My Drive/color_detection/dataset'


def get_coords(tag, x_min, y_min, x_max, y_max, images_with_required_classes):
        
        if tag in labels:
            if tag == 'green':
                label = labels['green']
                color = (0, 255, 0)
            elif tag == 'red':
                label = labels['red']
                color = (255, 255, 0)
            elif tag == 'yellow':
                label = labels['yellow']
                color = (255, 0, 0)

            x_center = ((x_max + x_min) / 2) / 416
            y_center = ((y_max + y_min) / 2) / 416
            w = (x_max - x_min) / 416
            h = (y_max - y_min) / 416
            return label, x_center, y_center, w, h
        else:
            label = ''
            x_center = ''
            y_center = ''
            w = ''
            h = ''
            return label, x_center, y_center, w, h

for root_folder_name in root_folder_names:
    folder_names = os.listdir(f"{annotation_root}/{root_folder_name}")
    num_folders = len(folder_names)
    mapped_clip = root_folder_name_mapper[root_folder_name]

    for i in range(1,  num_folders+1): 
        print('##### NEW CSV AND IMAGES ####')
        # read the annotation CSV file
        df = pd.read_csv(f"{annotation_root}/{root_folder_name}/{mapped_clip}{i}/labels.csv", 
                         delimiter=';')
        # get all image paths
        image_paths = glob.glob(f"{image_root}/{root_folder_name}/{root_folder_name}/{mapped_clip}{i}/frames/*.jpg")
        image_paths.sort()

        total_images += len(image_paths)

        tags = df['Annotation tag'].values
        x_min = df['Upper left corner X'].values
        y_min = df['Upper left corner Y'].values
        x_max = df['Lower right corner X'].values
        y_max = df['Lower right corner Y'].values

        file_counter = 0 # to counter through CSV file
        # iterate through all image paths
        for i, image_path in tqdm(enumerate(image_paths), total=len(image_paths)):
            image_name = image_path.split(os.path.sep)[-1]
            # iterate through all CSV rows
            for j in range(len(df)):
                if file_counter < len(df):
                    file_name = df.loc[file_counter]['Filename'].split('/')[-1]
                    if file_name == image_name:
                        label, x, y, w, h = get_coords(tags[file_counter], 
                                                    x_min[file_counter],
                                                    y_min[file_counter],
                                                    x_max[file_counter],
                                                    y_max[file_counter], 
                                                    images_with_required_classes)
                        with open(f"../My Drive/color_detection/labels/{image_name.split('.')[0]}.txt", 'a+') as f:
                            if type(label) == int:
                                f.writelines(f"{label} {x} {y} {w} {h}\n")
                                f.close()
                            else:
                                f.writelines(f"")
                                f.close()
                            image = cv2.imread(image_path, cv2.IMREAD_COLOR)
                            cv2.imwrite(f"../My Drive/color_detection/images/{image_name}", image)
                            file_counter += 1
                        # continue
                    if file_name != image_name:
                        break

print(f"Total images annotated: {total_images}")
