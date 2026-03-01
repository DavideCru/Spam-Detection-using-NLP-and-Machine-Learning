import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('mail_data.csv')

print(df)

data = df.where((pd.notnull(df)), '')

data.head()

data.info()

data.shape

data.loc[data['Category'] == 'spam', 'Category',] = 0
data.loc[data['Category'] == 'ham', 'Category',] = 1

data['Category'].value_counts().plot(kind='bar', color=['orange', 'skyblue'])
plt.title("Distribution of Spam vs Ham Emails")
plt.xlabel("Category (Spam = 0 , Ham = 1)")
plt.ylabel("Count")
plt.show()

fig, axes = plt.subplots(1,2, figsize=(10,4))

axes[0].hist(data[data['Category'] == 0]['Length'], bins=50, color='skyblue')
axes[0].set_title("Spam Length")

axes[1].hist(data[data['Category'] == 1]['Length'], bins=50, color='orange')
axes[1].set_title("Ham Length")

plt.show()

print("Average length Spam:", data[data['Category']==0]['Length'].mean())
print("Average length Ham:", data[data['Category']==1]['Length'].mean())

print(X)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 3)

print(X.shape)
print(X_train.shape)
print(X_test.shape)

print(Y.shape)
print(Y_train.shape)
print(Y_test.shape)

feature_extraction = TfidfVectorizer(min_df = 1, stop_words = 'english', lowercase = True)

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')


print(X_train)

print(X_train_features)

print(X_train)

print(X_train_features)

model = LogisticRegression()

model.fit(X_train_features, Y_train)

feature_names = feature_extraction.get_feature_names_out()
coefficients = model.coef_[0]

top_spam = coefficients.argsort()[:10]
top_ham = coefficients.argsort()[-10:]

print("Top words for Spam:")
print([feature_names[i] for i in top_spam])

print("\nTop words for Ham:")
print([feature_names[i] for i in top_ham])

spam_words = [feature_names[i] for i in top_spam]
ham_words = [feature_names[i] for i in top_ham]

spam_values = coefficients[top_spam]
ham_values = coefficients[top_ham]

words = spam_words + ham_words
values = list(spam_values) + list(ham_values)

colors = ['orange'] * len(spam_words) + ['skyblue'] * len(ham_words)

plt.figure(figsize=(10,6))
plt.barh(words, values, color=colors)
plt.axvline(0)  # linea centrale
plt.title("Top Influential Words (Spam vs Ham)")
plt.xlabel("Coefficient Value")
plt.show()

prediction_on_training_data = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)

print('Acc on trainig data : ', accuracy_on_training_data)

prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)

cm = confusion_matrix(Y_test, prediction_on_test_data)
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()
plt.xticks([0,1], ["Spam (0)", "Ham (1)"])
plt.yticks([0,1], ["Spam (0)", "Ham (1)"])
for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", va="center")
plt.show()

print('Acc on test data : ', accuracy_on_training_data)

input_your_mail = ["You are guaranteed the latest Nokia Phone, a 40GB iPod MP3 player or a Â£500 prize! Txt word: COLLECT to No: 83355! IBHltd LdnW15H 150p/Mtmsgrcvd18+"]

input_data_features = feature_extraction.transform(input_your_mail)

prediction = model.predict(input_data_features)

print(prediction)

if(prediction[0] == 1):
    print('Ham mail')
else:
    print('Spam mail')

