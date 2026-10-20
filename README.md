Name:Eileen Njoki Mwangi
Project Title: python-machine-learning-assignment

#Supervised Learning project Description:
This project predicts examination scores based on hours studied. It uses linear regression algorithm (supervised learning) to learn the relationship between hours studies and examination scores. The trained model then predicts expected examination score for a student based on their hours studied.Matplotlib has been used to visualize the relationship between study hours and examination score.

#Unsupervised Learning project Description:
This project groups customers based on their monthly spending and monthly visits to a supermarket. It uses K-Means algorithm (unsupervised learning) to identify patterns and assing customers to groups.Matplotlib has also been used to visualize the customer groups with different colors representing different groups.

#Instructions for installing dependencies and running code.
    #Your machine should have the following installed:
Python or Python3
Git
And internet connectivity to install dependencies

    #These projects use the following libraries:
scikit-learn
matplotlib
numpy

    #Instructions for installing and running code
1.Clone the repository:
    git clone https://github.com/mwangieileen/python-machine-learning-assignment.git
2.Install dependencies:
    pip install -r requirements.txt
3.Run projects
    python supervised_ml.py
    python unsupervised_ml.py
    Note: For python3 replace 'python' with 'python3'
    Also note: Project unsupervised_ml has 2 output formats, one is as per the example given and the 2nd one is human readable output.


#Answers to the theory Questions 
1.Supervised ML(machine learning) is a type of ML where the algorithm is trained using labeled data,that is, inputs(features) and outputs(labels).

2.Unsupervised ML is a type of machine learning where the algoriths is trained using unlabelled data but it uses the grouping of related data by studying relationships/patterns. Its output is groups which contain related data

3.Supervised learning predicts data from studying already existing outputs and used labelled data while unsupervised learning groups data into groups based off of relationship and patters while using unlabelled data.

4.Linear Regression algorithm trains from data which is labelled. The data used has inputs and outputs hence being considered supervised learning.

5.K-Means uses grouping as its principle and does not use labelled data which makes it unsupervised learning.It only checks for similarities in data and places them in groups depending on that.

6.fit() is the method used to train models, it 'assigns' the provided data into the model which the model then uses to learn patterns and relationships before prediction.predict() on the other hand is the method used to make predictions based on what the model has learnt from the data during training.

7.Supervised learning-Email spam filtering and credit card fraud detection
Unsupervised learning-customer segmentation and social media recommendations
