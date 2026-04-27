# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "kagglehub==1.0.0",
#     "marimo>=0.20.4",
#     "pyyaml==6.0.3",
#     "ultralytics",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo

    return


@app.cell
def _():
    # import kagglehub
    # kaushigihanml_kids_and_adults_detection_path = kagglehub.dataset_download('kaushigihanml/kids-and-adults-detection')

    # print('Data source import complete.')
    return


@app.cell
def _():
    # packages added via marimo's package management: ultralytics !pip install ultralytics -q
    # packages added via marimo's package management: pyyaml !pip install pyyaml -q
    return


@app.cell
def _():
    import os
    import random
    import cv2
    import matplotlib.pyplot as plt
    import yaml

    class data_visualization:

        def __init__(self, main_data_path, dataset_path, data1_yaml):
            self.dataset_path = dataset_path
            self.data1_yaml = data1_yaml
            self.main_data_path = main_data_path
            self.train_labels = None
            self.test_labels = None
            self.unique_labels = None
            self.unique_name = None
            self.get_labels_count()
            self.data_distribution()

        def get_labels_count(self):
            self.train_labels = []
            self.test_labels = []
            for folder_name in os.listdir(self.dataset_path):
                if folder_name.endswith('.cache'):
                    pass
                else:
                    folder_path = os.path.join(dataset_path, folder_name)
                    for file_name in os.listdir(folder_path):
                        if file_name.endswith('.txt'):
                            file_path = os.path.join(folder_path, file_name)
                            with open(file_path, 'r') as file:
                                for line in file:
                                    class_label = line.split()[0]  # Loop through all .txt files in the dataset folder
                                    if folder_name == 'train':
                                        self.train_labels.append(class_label)
                                    else:
                                        self.test_labels.append(class_label)
            self.unique_labels = list(set(self.train_labels))
            return (self.train_labels, self.test_labels)  # Extract the class label (first number in the line)

        def pie_chart(self, label_counts, class_labels, cate):
            colors = ['#ff9999', '#66b3ff', '#99ff99']
            total = sum(label_counts)
            percentages = [count / total * 100 for count in label_counts]
            plt.figure(figsize=(5, 5))
            plt.pie(label_counts, labels=[f'{label} ({count}, {percentage:.1f}%)' for label, count, percentage in zip(class_labels, label_counts, percentages)], colors=colors, autopct='%1.1f%%', startangle=90)
            plt.title(f'{cate} Data Distribution by Class')
            plt.show()
            print('\n')

        def data_distribution(self):
            with open(self.data1_yaml, 'r') as file:  # Adjust colors as needed
                data = yaml.safe_load(file)
            classes = data['names']  # Calculate percentages for the labels
            self.unique_name = list(classes.values())
            class_labels = []
            train_label_counts = []
            test_label_counts = []  # Create a pie chart
            for class_label_key in classes.keys():
                class_labels.append(classes[class_label_key])
                if self.train_labels is not None:
                    train_label_counts.append(self.train_labels.count(str(class_label_key)))
                if self.test_labels is not None:
                    test_label_counts.append(self.test_labels.count(str(class_label_key)))
            if train_label_counts is not None:
                self.pie_chart(train_label_counts, class_labels, 'Train')
            if test_label_counts is not None:
                self.pie_chart(test_label_counts, class_labels, 'Test')

        def plot_random_samples(self, split, num_samples=6):
            class_names = self.unique_name
            images_dir = os.path.join(self.main_data_path, 'images', split)
            image_paths = [os.path.join(images_dir, file_name) for file_name in os.listdir(images_dir) if file_name.endswith('.jpg') or file_name.endswith('.png')]
            random_samples = random.sample(image_paths, num_samples)
            fig, axes = plt.subplots(2, 3, figsize=(12, 8))
            axes = axes.ravel()
            for idx, img_path in enumerate(random_samples):
                image = cv2.imread(img_path)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                annotation_path = img_path.replace('images', 'labels').replace('.jpg', '.txt').replace('.png', '.txt')
                if os.path.exists(annotation_path):
                    with open(annotation_path, 'r') as file:
                        annotations = file.readlines()
                    h, w, _ = image.shape  # Example dataset
                    for annotation in annotations:  # Replace with your actual labels
                        class_id, x_center, y_center, width, height = map(float, annotation.split())  # Replace with counts of each label in your dataset
                        x_center, y_center, width, height = (x_center * w, y_center * h, width * w, height * h)
                        x1, y1 = (int(x_center - width / 2), int(y_center - height / 2))
                        x2, y2 = (int(x_center + width / 2), int(y_center + height / 2))
                        color = (255, 0, 0)
                        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
                        class_name = class_names[int(class_id)] if int(class_id) < len(class_names) else f'Class {int(class_id)}'
                        cv2.putText(image, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 4)
                axes[idx].imshow(image)
                axes[idx].axis('off')
                axes[idx].set_title(f'{split.capitalize()} Sample {idx + 1}')
            for i in range(len(random_samples), len(axes)):
                axes[i].axis('off')
            plt.tight_layout()
            plt.show()

        
    dataset_path = './kagglehub/datasets/kaushigihanml/kids-and-adults-detection/versions/2/children_and_adults/labels'
    data1_yaml = './kagglehub/datasets/kaushigihanml/kids-and-adults-detection/versions/2/children_and_adults/data1.yaml'
    main_data_path = './kagglehub/datasets/kaushigihanml/kids-and-adults-detection/versions/2/children_and_adults'
    obj = data_visualization(main_data_path, dataset_path, data1_yaml)  # Get image paths for the specified split  # Randomly sample images  # Create a 3x2 grid to display the images  # Flatten axes for easy iteration  # Load the image  # Convert BGR to RGB  # Get corresponding annotation file path in the labels folder  # Draw bounding boxes from YOLO annotations  # Draw the bounding box  # Red color for bounding box  # Add class name  # Plot the image in the grid  # Turn off axis  # Hide any unused subplots
    return data1_yaml, obj, yaml


@app.cell
def _(obj):
    obj.plot_random_samples(split="train",num_samples=6)
    return


@app.cell
def _(obj):
    obj.plot_random_samples(split="val",num_samples=6)
    return


@app.cell
def _(data1_yaml, yaml):
    file_path = data1_yaml
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    print(data)
    classes = data['names']
    print('classes Name :', classes)
    return


@app.cell
def _():
    # magic command not supported in marimo; please file an issue to add support
    # %%writefile /kaggle/working/kidsandAdults_yolo_config.yaml
    # 
    # path: '/kaggle/input/kids-and-adults-detection/children_and_adults' # dataset root dir
    # train: images/train  # train images (relative to 'path')
    # val: images/val  # val images (relative to 'path')
    # 
    # names:
    #   0: "Kid"
    #   1: "Adult"
    return


@app.cell
def _():
    ### 4. Train model ###
    from ultralytics import YOLO
    model = YOLO('yolo11s.pt')
    # Load a model
    # Use the model
    results = model.train(data='./kagglehub/datasets/kaushigihanml/kids-and-adults-detection/versions/2/kidsAdults_yolo_config.yaml', epochs=25, imgsz=640, device='cpu')  # load pre trained mode
    return (model,)


@app.cell
def _(model):
    urls = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ09q9-SnHjARL2_h4WNFz9m_pFT346kN395w&s', 'https://www.ctbehavioralhealth.com/wp-content/uploads/2017/10/child-adult-evaluation.jpg', 'https://img.freepik.com/free-photo/front-view-mother-holding-newborn-baby_23-2150227213.jpg', 'https://wp.en.aleteia.org/wp-content/uploads/sites/2/2018/06/web3-child-swing-mother-fun-smile-laugh-shutterstock.jpg?resize=620,350&q=75']
    for i, url in enumerate(urls):
        print(f'Prediction {i + 1} results ')
        results_1 = model([url])
        for result in results_1:
            predict_out = result.boxes.data.tolist()
            print(predict_out)
            result.show()
            result.save(filename='result.jpg')
            print('\n')  # Predict results  # return a generator of Results objects  # Process results generator  # Boxes object for bounding box outputs  # display to screen
    return


if __name__ == "__main__":
    app.run()
