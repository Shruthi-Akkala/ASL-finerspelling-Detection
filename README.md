# ASL_Fingerspelling

# Custom Test Dataset:

https://drive.google.com/drive/folders/1E7TX1gVHsRFBa65q_ODwo_zgHHfTHXAa?usp=sharing

# Description

## Custom Model

Custom Test Model folder includes 4 iPython Notebooks:

1) Data extraction - To extract Mediapipe landmarks and save in .txt file
2) ASL_Training - Training the FFNN on the data stored in .txt
3) Livedemo - Live webcam demo
4) CustomEvaluation - Reporting metrics for custom test dataset


There are 10 .txt files that store the data required to pass into FFNNs.

1) Train_X_aug, Train_Y_aug : Extracted data from Augmented YOLO dataset
2) Valid_X_yolo, Valid_X_yolo: Validation from Augmented YOLO dataset
3) Test_X_yolo, Test_Y_yolo: Test Dataset from Augmented YOLO dataset
4) Megalist, Maegalabel: Webcam Dataset landmarks file and corresponding labels
5) custom_test_data_mp, custom_test_labels = Mediapipe landmarks for custom test data and the corresponding labels

There are 3 .h5 files that store the model weights for the FFNN model.

1) bigdataASLNN26 : Weights for Model 3, trained on large but erroneous dataset
2) augdata_2layer : Weights for Model 2, trained on the augmented YOLO dataset
3) wcdata_2layers : Weights for Model 1, trained on the Webcam dataset

Note: The combined Model does not have a separate .h5 file. It post-processes the output of the three models and chooses the output accordingly.
