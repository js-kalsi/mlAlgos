WHAT IS MACHINE LEARNING ?

It is a sub-field of Artifical Inteligence. It is the study of algorithm which learns from examples and experiences instead of relying upon hardcoded rules. I will give you an example which sounds easy but it is imposible to solve it without machine learning.Can you write a code to show the difference between apple and orange? Image I told you to write a program that takes image file as input and does some analysis and outputs the type of fruit. How can you solve this? You have to start by writing lots of manual rules.For example : you can write a code to find how many orange pixels are their in orange image and compare that with the number of green once. The ratio should give you a hint about the type of fruit. That works fine for simple images but as you dive deep into the problem you find the real world is messy and the rules you write has start to break.
How to write code to handle black and white photos or images with no apples and oranges in them at all? In fact any rule you write I can find an image where it cannot work. You need to write tons of rules just to tell the difference between apples and oranges. And if I give you a new problem then you have to start all over again. Clearly we need something better. To solve this we need an algorithm that can figure out the rules for us so that we do not have to write them by hand and for that we are going to use the machine learning techniques.

Source : (http://y2u.be/cKxRvEZd3Mw)


This repository contains the source code for  "k-nearest-neighbor" Alogorithm in javascript as well as in C++. I have learned this algorithm from the blog and also hosted its javascript version (URL : https://mlalgorithm.herokuapp.com/).
Using the same logic I have created my own C++ version of "k-nearest-neighbor" Alogorithm.

For the Implementation C++ version, I have taken four arrays :
1) numOfRooms      (type:Integer) Contains the number of the Rooms and is of length 23.
2) areaOfRooms     (type:Integer) Contains the area   of the Rooms and is of length 23.
3) typeOfRoom      (type:String)  Contains the type information i.e(House,Flat & Apartment) and is of length 23.
4) distanceRecords (type:Integer) Contains the minimum distance of each point from the Mystery point and is of length 23.

I am assuming  (numOfRooms,typeOfRoom) as a coordinates of a point.And this way we have 23 points.
Then, I am creating a new random Point(Mystery Point) and calculating using the "k-nearest-neighbor" Alogorithm wheather
that point will be of type House,Flat or Apartment.
