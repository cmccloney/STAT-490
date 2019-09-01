import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("""
Assignment 1
Conner McCloney

# 1
a)

A research question that could be addressed with regression. Create a plot similar to Figure 1.1 in ISL to display the data relevant to your research question.

Can we predict the average rating of a book from Goodreads?

Source: [https://www.kaggle.com/jealousleopard/goodreadsbooks]

(See Figure 1)

""")

#There's bad rows in the dataset, doing it this way will ignore the extra columns
#present in some rows
cols = pd.read_csv('books.csv', nrows=2).columns
books_data = pd.read_csv('books.csv', usecols=cols)
#
books_data['average_rating'] = pd.to_numeric(books_data['average_rating'], errors='coerce')
books_data['ratings_count'] = pd.to_numeric(books_data['ratings_count'], errors='coerce')
books_data['text_reviews_count'] = pd.to_numeric(books_data['text_reviews_count'], errors='coerce')
books_data['# num_pages'] = pd.to_numeric(books_data['# num_pages'], errors='coerce')

f1 = plt.figure(figsize=(15,10))
ax1 = f1.add_subplot(3,1,1)
ax1.scatter(books_data['ratings_count'],books_data['average_rating'])
plt.xlabel('Number of Ratings')
plt.ylabel('Average Rating')
plt.show(block=False)
ax2 = f1.add_subplot(3,1,2)
ax2.scatter(books_data['text_reviews_count'],books_data['average_rating'])
plt.xlabel('Number of Text Reviews')
plt.ylabel('Average Rating')
plt.show(block=False)
ax3 = f1.add_subplot(3,1,3)
ax3.scatter(books_data['# num_pages'],books_data['average_rating'])
plt.xlabel('Number of Pages')
plt.ylabel('Average Rating')
plt.xticks(np.arange(0, 7000, 200))
plt.tight_layout()
plt.show(block=False)
'''
ax4 = f1.add_subplot(4,1,4)
ax4 = sns.boxplot(x=books_data['language_code'],y=books_data['average_rating'])
plt.xlabel('Language Code')
plt.ylabel('Average Rating')
plt.tight_layout()
plt.show(block=False)
'''
print("""
b)

A research question that could be addressed with classification. Create a plot similar to Figure 1.2 in ISL to display the data relevant to your research question.

Is there a relationship between the dispersion measure signal-to-noise ratio (DM-SNR) curve and the classification of an observed measurement as a pulsar or a false positive?

Source: [https://www.kaggle.com/pavanraj159/predicting-a-pulsar-star]

(See Figure 2)

""")

pulsar_data = pd.read_csv('pulsar_stars.csv', delimiter=',')

def change_value(df):
    if df['target_class'] == 0:
        return "False Positive"
    elif df['target_class'] == 1:
        return "Pulsar"

pulsar_data['target_class']=pulsar_data.apply(change_value,axis=1)

f2 = plt.figure(figsize=(15,10))
ax5 = f2.add_subplot(1,4,1)
ax5 = sns.boxplot(y=' Mean of the integrated profile',x='target_class',data=pulsar_data)
plt.ylabel('Mean of DM-SNR curve')
plt.xlabel('Target Reading')
plt.show(block=False)
ax6 = f2.add_subplot(1,4,2)
ax6 = sns.boxplot(y=' Standard deviation of the integrated profile',x='target_class',data=pulsar_data)
plt.ylabel('Standard deviation of DM-SNR curve')
plt.xlabel('Target Reading')
plt.show(block=False)
ax7 = f2.add_subplot(1,4,3)
ax7 = sns.boxplot(y=' Excess kurtosis of the integrated profile',x='target_class',data=pulsar_data)
plt.ylabel('Excess kurtosis of DM-SNR curve')
plt.xlabel('Target Reading')
plt.show(block=False)
ax8 = f2.add_subplot(1,4,4)
ax8 = sns.boxplot(y=' Skewness of the integrated profile',x='target_class',data=pulsar_data)
plt.ylabel('Skewness of DM-SNR curve')
plt.xlabel('Target Reading')
plt.tight_layout()
plt.show(block=False)

print("""
# 2

The book distinguishes between prediction and inference, but I would argue that both are forms of inference - one is predictive and one is explanatory. 
Explain, in your own words the difference between these two inferential objectives.

The difference between predictive inference and explanatory inference, is that in predictive inference our main or primary objective or goal is to 
create a model that can predict a response y given the values for our predictor variables x as accurately as possible. Whereas for explanatory inference, 
our primary objective is in determining and understanding the relationship between the predictor variables and the response. 
For predictive inference, we are less interested in understanding this relationship and more interested in being able to accurately predict the response value for future observations, 
whereas for explanatory inference, our goal is the reverse. Due to this, explanatory inferential models tend to be less complex than predictive inferential models, 
because they are easier to understand and use to explain the relationship, if it is present.

# 3

Discuss differences and similarities between parametric and non-parametric approaches to estimating f.

Parametric approaches start with an assumption of the shape or form of f, so that the problem of estimating f can be reduced to estimating a set of 
parameters that f is now comprised of, based on the shape or form assumed. For non-parametric approaches however, no explicit assumption is made, 
and the goal is to estimate f as accurately as possible, subject to the fit being smooth. This approach can be more accurate, but needs more observations than a parametric approach, 
and tends to generate a more complex model. Due to this, parametric apporaches are better suited for explanatory inference, because the assumption of 
the shape of f tends to reduce the complexity of the model, making the relationship easier to understand and describe. 

# 4

In your own words, explain the difference between supervised and unsupervised learning.

Supervised learning is using statistical learning methods to build a model that attempts to predict the response or output variable based on one or more input or predictor variables.
Unsupervised learning has one or more input variables, but lacks any supervisory output variable, and instead seeks to describe and understand the relationship between these input variables, 
using grouping or some other method. There can also be a situation, where some observations contain a response value, while other observations don't, which is a semi-supervised learning problem.


""")
