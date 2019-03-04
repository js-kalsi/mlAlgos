WHAT IS MACHINE LEARNING ?

It is a sub-field of Artifical Inteligence. It is the study of algorithm which learns from examples and experiences instead of relying upon hardcoded rules. I will give you an example which sounds easy but it is imposible to solve it without machine learning.Can you write a code to show the difference between apple and orange? Image I told you to write a program that takes image file as input and does some analysis and outputs the type of fruit. How can you solve this? You have to start by writing lots of manual rules.For example : you can write a code to find how many orange pixels are their in orange image and compare that with the number of green once. The ratio should give you a hint about the type of fruit. That works fine for simple images but as you dive deep into the problem you find the real world is messy and the rules you write has start to break.
How to write code to handle black and white photos or images with no apples and oranges in them at all? In fact any rule you write I can find an image where it cannot work. You need to write tons of rules just to tell the difference between apples and oranges. And if I give you a new problem then you have to start all over again. Clearly we need something better. To solve this we need an algorithm that can figure out the rules for us so that we do not have to write them by hand and for that we are going to use the machine learning techniques.

[Defination source](https://www.youtube.com/watch?v=cKxRvEZd3Mw&list=PLT6elRN3Aer7ncFlaCz8Zz-4B5cnsrOMt)


This repository contains the source code of following projects:

| S. No. | Project | Language used | Folder         |
|:------:|:-------:| :------------:|| :------------:|
| a      | Implementation of K-nearest-neighbor Algorithm     |  Javascript, C++ | `k_means_clustering`|
| b      | Iris Dataset Clustering(iris_dataset_clustering) using Inverted Dirichlet and Generalized Inverted Dirichlet.    |  Python | `iris_dataset_clustering` |
| c      | Android Malware Detection Detection     | Python | `virus_detector` |


a) Implementation of K-nearest-neighbor Algorithm in javascript as well as in C++.
b) Iris Dataset Clustering(iris_dataset_clustering) using Inverted Dirichlet(ID) and Generalized Inverted Dirichlet(GID) Finite Mixture Models(FMM).
The `iris_dataset_clustering` folder contains the source code for ID and GID FMM. Both ID and GID  are very flexible mixture model(MM) as compare to Gaussian Mixture Model (GMM). In this, we have used IDMM and GIDMM for the clustering of Iris dataset.

c) Android Malware Detection (AMD)
The `virus_detector` folder contains the source code of AMD. 
