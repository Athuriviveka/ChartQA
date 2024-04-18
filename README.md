**Facial Expression Recognition using Temporal Ensembling for Semi-Supervised Learning**

This repository contains code for implementing and evaluating the Temporal Ensembling algorithm for semi-supervised learning on the FER2013 dataset.

Reference:(https://github.com/ShuvenduRoy/SSL_FER/tree/main)

Reference Paper Link: [FER](https://arxiv.org/pdf/2208.00544v1.pdf)

**Summary**

The existing research conducted a comprehensive study on semi-supervised learning methods for Facial Expression Recognition (FER). They explored eight semi-supervised learning methods, including Pi-Model, Pseudolabel, Mean-Teacher, VAT, MixMatch, ReMixMatch, UDA, and FixMatch. The study evaluated these methods on three FER datasets: FER13, RAF-DB, and AffectNet. Their analysis focused on comparing the performance of these methods against fully-supervised training, highlighting the potential of semi-supervised approaches to achieve comparable results with smaller labeled datasets. **The research aimed to reduce the reliance on large annotated datasets for training deep neural networks in FER tasks.**

In our study, we focuses on enhancing the performance of facial expression recognition systems through the implementation of **temporal ensembling within a semi-supervised learning framework.** By leveraging temporal dynamics in the learning process, we aim to reduce the reliance on annotated data, thereby addressing a key challenge in the field. We conducted experiments on the [FER2013 dataset] https://www.kaggle.com/datasets/msambare/fer2013, exploring four distinct scenarios with varying numbers of labeled datasets per class. Through our empirical investigation, we aim to elucidate the effectiveness of temporal ensembling in semi-supervised facial expression recognition, paving the way for more accurate and reliable systems in affective computing and human-machine interaction domains.

**Our Contribution**

Applied Temporal Ensembling, a semi-supervised learning method, to FER2013 dataset.
Evaluated its performance with varying numbers of labeled samples per class (10, 25, 100, and 250).
Aims to improve facial expression recognition using limited labeled data.
Extends prior research by exploring the effectiveness of Temporal Ensembling in FER.

**About the dataset**

The data consists of 48x48 pixel grayscale images of faces. The faces have been automatically registered so that the face is more or less centred and occupies about the same amount of space in each image.

The task is to categorize each face based on the emotion shown in the facial expression into one of seven categories (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral). The training set consists of 28,709 examples and the public test set consists of 3,589 examples.

**Folders/Files**

Dataset : Folder containing project datasets.

- Dataset
    - test                        # Folder containing test images (original dataset)
        - Angry                  # Folder containing test images for Angry emotion
        - Disgust                # Folder containing test images for Disgust emotion
        - Fear                   # Folder containing test images for Fear emotion
        - Happy                  # Folder containing test images for Happy emotion
        - Sad                    # Folder containing test images for Sad emotion
        - Surprise               # Folder containing test images for Surprise emotion
        - Neutral                # Folder containing test images for Neutral emotion
    - train                       # Folder containing original training data(original dataset)
        - Angry                  
        - Disgust                
        - Fear                   
        - Happy                  
        - Sad                    
        - Surprise               
        - Neutral                
    - labeled_scenarios           # Folder containing labeled scenarios(Preprocessed datset)
        - 10_labeled              # Folder for scenario with 10 labeled images per class
            - Angry              
            - Disgust      
            - Fear            
            - Happy             
            - Sad               
            - Surprise           
            - Neutral            
        - 25_labeled              # Folder for scenario with 25 labeled images per class
            ...
        - 100_labeled             # Folder for scenario with 100 labeled images per class
            ...
        - 250_labeled             # Folder for scenario with 250 labeled images per class
            ...
    - unlabeled                   # Folder containing unlabeled data(Preprocessed dataset)
        - Angry                  
        - Disgust                
        - Fear                   
        - Happy                  
        - Sad                    
        - Surprise               
        - Neutral                


saved_models : Folder for storing trained models
fer_dataset_preprocessor.py : This Python script is responsible for preprocessing the original FER2013 dataset. It splits the dataset into labeled and unlabeled data and further categorizes the labeled data into four different categories based on the number of samples per class (10, 25, 100, and 250). This preprocessing step is crucial for preparing the data for training and evaluation in a semi-supervised learning setup.
Temporal_ensembling.ipynb: 
This Jupyter Notebook contains the implementation of the Temporal Ensembling algorithm for semi-supervised learning applied to the FER2013 dataset. The notebook includes:

CNN modeling: Definition of the convolutional neural network architecture for facial expression recognition.
Parameter definition: Specification of hyperparameters and model configurations.
Data augmentation: Integration of data augmentation techniques to increase the diversity of the training data and improve model generalization.
Temporal ensembling: Implementation of the temporal ensembling algorithm, including optimizer setup, consistency loss computation, and labeled loss calculation.
Model evaluation: Code for training the model using labeled and unlabeled data, as well as evaluation metrics calculation such as accuracy, loss, confusion matrix, and classification report.
Visualization: Visualization of sample predictions and other relevant metrics to assess model performance.

Evaluation.ipynb: This notebook loads and evaluates models trained in Temporal_ensembling.ipynb, generating classification reports for comparison.

**Results**
The results obtained from our implementation of temporal ensembling for semi-supervised FER on the FER2013 dataset are presented below.

| Scenario          | Precision | Recall | F1-Score | Accuracy | Support |
|-------------------|-----------|--------|----------|----------|---------|
| 10 Labeled        | 0.12      | 0.10   | 0.11     | 0.14     | 958     |
| 25 Labeled        | 0.12      | 0.13   | 0.13     | 0.16     | 958     |
| 100 Labeled       | 0.15      | 0.13   | 0.13     | 0.14     | 958     |
| 250 Labeled       | 0.15      | 0.16   | 0.15     | 0.16     | 958     |


**How to run**

### Files Description:

1. **fer_dataset_preprocessor.py**:
   - Purpose: Preprocesses the FER2013 dataset.
   - How to run: Execute the script in a Python environment.
   - Command: `python fer_dataset_preprocessor.py`

2. **Temporal_ensembling.ipynb**:
   - Purpose: Implements the Temporal Ensembling algorithm.
   - How to run: Open the Jupyter notebook in a Python environment.
   - Command: `jupyter notebook Temporal_ensembling.ipynb`
   
3. **Evaluation.ipynb**:
   - Purpose: Evaluates the trained models.
   - How to run: Open the Jupyter notebook in a Python environment.
   - Command: `jupyter notebook Evaluation.ipynb`
