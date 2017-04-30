WHAT IS MACHINE LEARNING ?

It is a sub-field of Artifical Inteligence. It is the study of algorithm which learns from examples and experiences instead of relying upon hardcoded rules. I will give you an example which sounds easy but it is imposible to solve it without machine learning.Can you write a code to show the difference between apple and orange? Image I told you to write a program that takes image file as input and does some analysis and outputs the type of fruit. How can you solve this? You have to start by writing lots of manual rules.For example : you can write a code to find how many orange pixels are their in orange image and compare that with the number of green once. The ratio should give you a hint about the type of fruit. That works fine for simple images but as you dive deep into the problem you find the real world is messy and the rules you write has start to break.
How to write code to handle black and white photos or images with no apples and oranges in them at all? In fact any rule you write I can find an image where it cannot work. You need to write tons of rules just to tell the difference between apples and oranges. And if I give you a new problem then you have to start all over again. Clearly we need something better. To solve this we need an algorithm that can figure out the rules for us so that we do not have to write them by hand and for that we are going to use the machine learning techniques.

[Defination source](https://www.youtube.com/watch?v=cKxRvEZd3Mw&list=PLT6elRN3Aer7ncFlaCz8Zz-4B5cnsrOMt)

This repository contains the source code for  "k-nearest-neighbor" Alogorithm in javascript as well as in C++. I have learned this algorithm from the [blog](http://burakkanber.com/blog/machine-learning-in-js-k-nearest-neighbor-part-1/)  and also hosted its javascript [version](https://mlalgorithm.herokuapp.com/).
Using the same logic I have created my own C++ version of "k-nearest-neighbor" Alogorithm.
Consider a table for understanding about this alogithm :

| Rooms| Area | Type      |
| -----|:----:| ---------:|
| 1    | 350  | apartment |
| 2    | 300  | apartment |
| 3    | 300  | apartment |
| 4    | 250  | apartment |
| 4    | 500  | apartment |
| 4    | 400  | apartment |
| 5    | 450  | apartment |
| 7    | 850  | house     |
| 7    | 900  | house     |
| 7    | 1200 | house     |
| 8    | 1500 | house     |
| 9    | 1300 | house     |
| 8    | 1240 | house     |
| 10   | 1700 | house     |
| 9    | 1000 | house     |
| 1    | 800  | flat      |
| 3    | 900  | flat      |
| 2    | 700  | flat      |
| 1    | 900  | flat      |
| 2    | 1150 | flat      |
| 1    | 1000 | flat      |
| 2    | 1200 | flat      |
| 1    | 1300 | flat      |

We're going to plot the above as points on a graph in two dimensions, using number of rooms as the x-axis and the area as the y-axis.

When we inevitably run into a new, unlabeled data point ("mystery point"), we'll put that on the graph too. Then we'll pick a number (called "k") and just find the "k" closest points on the graph to our mystery point. If the majority of the points close to the new point are "flats", then we'll guess that our mystery point is a flat.

That's what k-nearest-neighbor means. "If the 3 (or 5 or 10, or 'k') nearest neighbors to the mystery point are two apartments and one house, then the mystery point is an apartment."

[source](http://burakkanber.com/blog/machine-learning-in-js-k-nearest-neighbor-part-1/)

For the Implementation of C++ version, I have taken four arrays :
1) numOfRooms      (type:Integer) Contains the number of the Rooms and is of length 23.
2) areaOfRooms     (type:Integer) Contains the area   of the Rooms and is of length 23.
3) typeOfRoom      (type:String)  Contains the type information i.e(House,Flat & Apartment) and is of length 23.
4) distanceRecords (type:Integer) Contains the minimum distance of each point from the Mystery point and is of length 23.

I am assuming  (numOfRooms,typeOfRoom) as a coordinates of a point.And this way we have 23 points.
Then, I am creating a new random Point(Mystery Point) and calculating using the "k-nearest-neighbor" Alogorithm wheather
that point will be of type House,Flat or Apartment.
