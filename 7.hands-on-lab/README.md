# Hands-on Lab: Hit the RHODS

In this exercise, you will complete the data science project for detecting fraudulent credit card transactions. In the previous exercise, you have seen how to run pipelines for detecting fraudulent transactions using a pre-trained model. Let's now create a new version of this model and deploy it!

The lab materials include notebooks that implement parts of the project workflow.
Your task is to complete the missing parts of those notebooks and create a data science pipeline and serve the model to meet the lab specifications.

## Prerequisites

The lab scenario assumes that the dataset is available in the S3 bucket that you have created in the [RHODS administration quick course](https://redhatquickcourses.github.io/rhods-admin/rhods-admin/1.33/index.html).

You will also use the same bucket to store the trained model and pipeline output reports.

The dataset is a CSV file called `credictcard.csv`.


> **NOTE**
>
> If you have not initialized your S3 store in the administration course, then you can follow these steps:
>
> * Create the S3 object store.
> You can create an s3 object store with Minio, by using this guide:  https://ai-on-openshift.io/tools-and-applications/minio/minio/.
>
> * Download the dataset file from https://drive.google.com/file/d/1Gd-ENv1SdqcXYFf81KKIWAsSFwe0Z6ch/view?usp=sharing.
Alternatively, you can download the dataset from Kaggle (https://www.kaggle.com/code/janiobachmann/credit-fraud-dealing-with-imbalanced-datasets/input).
>
> * Upload the dataset into the root of your S3 bucket.


## Specifications

* Perform your exercise in a TensorFlow workbench.
Make sure that the workbench is associated to a data connection that includes your S3 connection settings.
Make sure that the workbench size is at least `Medium`.

* Clone the https://github.com/RedHatQuickCourses/rhods-qc-apps repository into your workbench.
The materials for this lab are located in the `7.hands-on-lab/` directory.

* Collect the data.
Use the `1.collect` notebook to download the `creditcard.csv` file into `data/creditcard.csv`.

* Explore and preprocess data.
Use the `2.exploration` and `3.preprocessing` notebooks.
You do not need to make changes to these notebooks.

* Train the model.
Use the `4.model_training` notebook.
After training, add the code to convert the model to ONNX format.


* Upload the model to S3.
Use the `4.model_upload` notebook.

* Create a data science pipeline.
 Note that, in the [pipelines quick course](https://redhatquickcourses.github.io/rhods-pipelines/rhods-pipelines/1.33/index.html) you already created a pipeline for offline scoring, that is, for classification of unlabeled transactions given a pretrained model file.

  In this case, you must build a pipeline to train a model.
 This pipeline must collect training data, preprocess the data, train the model, and upload the trained model.

* Create a model server and serve the model that you uploaded to S3.
Expose the model via an external route.
The model framework must be `onnx` version 1.

* Test that you can consume the deployed model by using the `6.test` notebook.


You can find the solutions in the `solutions` directory.
