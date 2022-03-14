
# **Arabic Dialect Classification** 
## Table of Content:

 - [Project Overview](#overview)
 -  [Installation](#installation)
 - [File Descriptions](#files)
 - [Get Started](#get_start)
 - [Licensing  and Authors](#L&A)
  
<a name="overview"></a>
## Project Overview 
**This project includes the implementation of the Arabic dialect classification using machine and deep learning models. The implementation included data gathering, text preprocessing, model training, evaluation, and local deployment.**

This project is an

Here is a gif of the DL Model. 

<p align="center">
  <img src= alt="Sublime's custom image"/>
</p>

<a name="installation"></a>
## Installation

This project uses the following software and Python libraries: Please stick to the below versions to avoid any failure. 

 - `Python Version : 3.9.10`
 - `Sklearn Version : 0.24.2.`
 - `NLTK Version : 3.6.2..`
 - `Tensorflow Version : 2.6.1..`
 - `camel_tools Version :  1.2.0'`
 - `Flask Version : 2.0.1`
 
 The other packages are available in python by default.  
 

## File Descriptions <a name="files"></a>
The Repository includes five Folders that contains the project files and some of them has sub folders. The full description is below.

 1. Data Fetching
	   * Data_fetching Notebook	--> data fetching.
	   * dialect_dataset(1).csv	--> ids and labels used to make API post calls.
	   * dataset.csv	--> the acquired dataset.
2.	Deepl learning
	*  Files	--> the output files
	*  Deep_learning	--> the data preprocessing and model training notebook. 
3. Machine learning 
	*  Files	--> the output files
	* machine_learning --> the data preprocessing and model training notebook. 
	* helpyer.py	--> Tokenizer and text_normalize functions
4. DL Deployment
	* templates	--> the index.html file.
	* helper.py	--> input processing and classification.
	* app.py	--> to deploy the model and interact with the webpage. 
5. ML Deployment
	* templates	--> the index.html file.
	* helper.py	--> Tokenizer and text_normalize functions
	* tools.py 	-->  input processing and classification.
	* app.py 		--> to deploy the model and interact with the webpage. 
 ## Get Started
 <a name="get_start"></a>
Use the following command to download the files : 

    git clone https://github.com/sam1o1/Capital_Population_Chatbot

 Go to the directory where you saved this repo using anaconda prompt 
 
    cd [directory path]
 Then, write the following command:
 

    rasa run actions 
The above step is essential in order to run the custom action saved in `actions.py`. So please ***Do NOT FORGET IT*** 
Afterward, Open another anaconda prompt window without the closing the current one and write the following:

       cd [directory path]
       rasa shell 
Finally, you will be able to talk to the bot using the command prompt like the gif above. 
if you want to modify this project and add extra functions, you need to train it again using the below commands:

    rasa train 
and after that repeat the above steps. 
<a name="finding"></a>
<a name="L&A"></a>
## Licensing and Authors

Author : Eslam Abdelghany

Email: eslam322_1@hotmail.com

 
 



