# Mobile Price Prediction
____________________________________________________
## Context
The mobile shop company has decided to introduce a new feature to help customers determine the price category of a mobile phone based on its specifications. This feature will allow customers to input the specific features they are looking for in a mobile phone, such as RAM, internal memory, camera quality, and screen size, and receive an estimated price range for the phone.

To develop this feature, the mobile shop company plans to build a predictive model that can estimate the price range of a mobile phone based on its features. The company has collected sales data from various companies in the mobile phone industry to train the predictive model.

Once the predictive model is developed, the mobile shop company plans to integrate it into their website and mobile app, allowing customers to use the feature to get an estimated price range for the mobile phone they are looking for. The company hopes that this feature will help customers make more informed purchasing decisions and enable them to find mobile phones that fit their budget and meet their specific needs.

________________________________________________________
## Algorthims 
I used train four different machine learning algorithms: 
- **Logistic Regression**
- K-nearest neighbors (KNN)
- support vector machine (SVM)
- Random Forest.

After evaluating the performance of each algorithm, it was found that the SVM algorithm had the highest accuracy, with a score of 96.75%. Additionally, the SVM algorithm had a high F1-score of 97%, indicating that it was able to accurately predict both positive and negative instances of the price range category.

Based on these results,Mobile Shop company decided to use the SVM algorithm in their new feature to predict the price range of mobile phones based on their features. By using this algorithm, they hope to provide customers with accurate and reliable estimates of the price range of the mobile phone they are interested in purchasing.
