Android Malware Detection (AMD)
Few years ago, the water, food and clothes were considered essential for survival. But these days, the smartphones are also included in the list    
Android is the most used mobile operating system in the world right now. Android and iOS have created a duopoly in the smartphone market, accounting for more than 95% of the 3.1 billion active smartphone devices in the world. In terms of the sheer volume of devices in use, Android dominates iOS by a large margin with a 75.9% market share in November of 2017 or 2.3 billion smartphones in use. China and India account for almost half of this amount. As flagship Android devices become more powerful, they increasingly challenge Apple’s market share in the West too. Brands like Huawei, Xiaomi, and others are also working to improve their design, innovation, and marketing, challenging iOS' share even more.
Android Users: 2.3 billion
Total smartphones: 3.1 billion
Android’s market share in the US: 62%

Src:  [blog](https://www.quora.com/How-many-people-use-Android-devices-in-the-world)

The android play store (which is a heart of all the android apps) consists of millions of apps. Unfortunately, there are lots of apps on play-store which have malware in it. In this project, we have proposed a AMD which uses supervised machine learning(specifically Decision tree, K-nearest neighbor and Support vector machine) approach in order to detect wheather an app is malware oriented or not. The dataset consists of permission which an app needs from ANDROID_MANIFEST.xml file. This dataset id futher divided into training and test dataset.

The results are as follows: 

|------------------------------------------------------|
| Algorithm | Precision | Recall | F1-score | Accuracy |
|:---------:|----------:|:------:|:--------:|---------:|
|   KNN     |    94%    |   94%  |   94%    |   94%    |
|    DT     |    93%    |   93%  |   93%    |   93%    |
|   SVM     |    93%    |   93%  |   93%    |   93%    |
|------------------------------------------------------|

where KNN: K-Nearest Neighbor,
      DT: Decision Tree,
      SVM: Support Vector Machine.
      
