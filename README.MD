# Data Pipeline for a Histopathology Classifier 


The following project connects a website with a backend pretrained deep learning model. The user can upload a histopathology image which will be classified as either malignant of benign. 

My pretrained convolutional neural network classifies images of prostate pathology. The CNN will use an Inception V3 as a base model. 

According to Jerome Cheng, MD, who pulbished a short summary on computational pathology on July 2020, its is more ideal to use a pre-trained CNN such as VGG-16, VGG-19, ResNet50 or Inception v3. The reason being, that features embedded inside these neural networks can be used to train a classifier for pathology whole slide images. A working example of this model can be found in a study by Iizuka, O., Kanavati, F., Kato, K. et al.(see link below), who used an augmented Inception V3 model to train a deep learning model that recognizes whole slide images of gastric and epithelian tumors. I will therefore use my own customized Inception V3 model to train on a colon cancer dataset. 

- Computationa Pathology by Jerome Cheng, MD: https://www.pathologyoutlines.com/topic/informaticsconvnet.html
- Deep Learning Models for Histopathological Classification of Gastric and Colonic Epithelial Tumours: https://www.nature.com/articles/s41598-020-58467-9