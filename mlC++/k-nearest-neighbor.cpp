/* 
*      "k-nearest-neighbor" Alogorithm using c++. 
*
*       
*       For the Implementation, I have taken four arrays that are : 
*       1) numOfRooms      (type:Integar) Contains the number of the Rooms and is of length 23.
*       2) areaOfRooms     (type:Integar) Contains the area   of the Rooms and is of length 23.  
* 		3) typeOfRoom      (type:String)  Contains the type information i.e(House,Flat & Apartment) and is of length 23.
*       4) distanceRecords (type:Integar) Contains the minimum distance of each point from the Mystery point and is of length 23.
*       
*       I am assuming  (numOfRooms,typeOfRoom) as a coordinates of a point.And this way we have 23 points.
*       Then, I am creating a new random Point(Mystry Point) and calculating using the "k-nearest-neighbor" Alogorithm wheather 
*		that point will be of type House,Flat or Apartment.
*/

#include <iostream>
#include <conio.h>
#include <stdlib.h>     
#include <time.h>       
#include <math.h>   
#include <windows.h>

using namespace std;

/*  Functions declaration  */
void gotoxy(short , short); 
int  shortestRoute(int,int,int,int);
int  mysteryObjGeneration(int);
int  sortDistAscendingOrder(int [],string []);
int  generateResult(string []);

int main()
{
	int    numOfRooms[23]  = {1,2,3,4,4,4,5,7,7,7,8,9,8,10,9,1,3,2,1,2,1,2,1};
	int    areaOfRooms[23] = {350,300,300, 250,500,400, 450,850,900, 1200,1500,1300, 1240,1700,1000, 800,900,700, 900,1150,1000,1200,1300};
    string typeOfRoom[23] = {"apartment","apartment","apartment","apartment","apartment","apartment","apartment","house","house","house","house","house","house","house","house","flat","flat","flat","flat","flat","flat","flat","flat"};
	int    distanceRecords[23]; 
	
	srand (time(NULL)); /* initialize random seed: */
    
	// Creating a mystery Point
	int mysNo_of_Rooms  = mysteryObjGeneration(10);   /* contains the Number of Rooms for Mystery point */
	int	mysArea         = mysteryObjGeneration(1700); /* contains the area   of Rooms for Mystery point */


	int numOfRoomsLength  = sizeof(numOfRooms)/sizeof(*numOfRooms);    /* contains the length of `numOfRooms`*/
	int areaOfRoomsLength = sizeof(areaOfRooms)/sizeof(*areaOfRooms);  /* contains the length of `areaOfRooms`*/
	
	int distance = 0; 
	
	for(int j=0; j < numOfRoomsLength; j++ ){	
		distance = shortestRoute(mysNo_of_Rooms,mysArea,numOfRooms[j],areaOfRooms[j]);  /* contains the minimum distance from the Mystery Point*/
	    distanceRecords[j] = distance;
	}
	sortDistAscendingOrder(distanceRecords,typeOfRoom);  /* sort the `distanceRecords` as well as `typeOfRoom`  arrays */
	getch();
	return 0;
}


/**
 * Find the Shortest Route from a Known point to Mystery Point using Euclid's Distance Formula.
 * @param  {Integer} mysRooms.
 * @param  {Integer} mysArea.
 * @param  {Integer} knownRooms.
 * @param  {Integer} knownArea.
 * @return {Integer} Minimum Distance from Mystery Point.
 */
int  shortestRoute(int mysRooms,int mysArea,int knownRooms, int knownArea)
{
	return sqrt( pow((knownRooms - mysRooms),2) + pow((knownArea - mysArea),2));
}


/**
 * Generate the Mystery Point Using Random Number Logic.
 * @param  {Integer} rangeMax.
 * @return {Integer} Random Number for the Mystery Point.
 */
int mysteryObjGeneration(int rangeMax){
	return rand() % rangeMax + 1;
}



/**
 * Sorting the Distance array(contains the minimum  distance from the Known points to the  UnKnown point) in Ascending order. 
 * @param  {Integer Array} distRecord.
 * @param  {String  Array} typeOfRoom.
 */
int sortDistAscendingOrder(int distRecord[],string typeOfRoom[]){
	string temp;
	for (int i = 0; i < 22; i++) {
    	for (int j = 0; j < 22; j++) {
        	if (distRecord[j] > distRecord[j + 1]) {
            	distRecord[j]     = distRecord[j] + distRecord[j + 1];
            	distRecord[j + 1] = distRecord[j] - distRecord[j + 1];
            	distRecord[j]     = distRecord[j] - distRecord[j + 1];
            	
            	
            	temp                 = typeOfRoom[j];
            	typeOfRoom[j]        = typeOfRoom[j + 1];
            	typeOfRoom[j + 1]    = temp;
        	}
       }
   }  
   generateResult(typeOfRoom);  /* Generates the result by taking a  `typeOfRoom` array as a param */
}


/**
 * Generates the Final Result.
 * @param  {String Array} typeOfRoom.
 */
int generateResult(string typeOfRoom[]){
	
	int numOfFlats     = 0;  /* counter for number of `Flats` */
	int numOfApartment = 0;  /* counter for number of `Apartment` */
	int numOfHouse     = 0;  /* counter for number of `House` */
	string  result;  /* will contains the final result */

	for(int j=0;j<3;j++){
			if (typeOfRoom[j] == "flat") numOfFlats++;
			if (typeOfRoom[j] == "apartment") numOfApartment++;
			if (typeOfRoom[j] == "house") numOfHouse++;
	}	

	/* 
	 * If  number of `Flats` is greater than  number of Houses & Apartment,then result will be Flats. 
	 * If  number of `Houses` is greater than  number of Flats & Apartments,then result will be Houses.
	 * If  number of `Apartment` is greater than  number of Flats & Houses,then result will be Apartment.
	*/
	(numOfFlats > numOfApartment && numOfFlats > numOfHouse)? result = "Flat":(numOfApartment > numOfHouse)? result = "Apartment":result = "House";
	
	cout<<"\nThe Mystry Point : "<<result;  /* Contains the final result */
}


/**
 * Moves the Cursor from one point to another.
 * @param  {Short} x.
 * @param  {Short} y.
 */
void gotoxy(short x, short y){
  COORD pos ={x,y};
  SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}













