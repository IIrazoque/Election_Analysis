# Election_Analysis
Using python for Colorado's election analysis
## Project Overview 
Tom and Seth both employees as Colorados Board of Elections and we were given the task to audit a local congressional election.

1. Using python we calculated the total number of votes casts
2. Created a list of candidates & counties who recieved votes
3. Calculated the total number of voters per candidate and counts for each county
4. Calculated the percentage of votes for each candidate and calculated the percenatge per county
5. Determined the winner of the election based on popular vote and the largest county turnout

## Resources
-Data Source: election_results.csv
-Software: Python 3.8.5, Visual Studio, 1.38.1
-Delivery form: election_analysis.txt

## Candidate Results 
Election data shows -
*There were "368,711" votes casted in the election
*The candidates were :
1) Charles Casper Stockham
2) Diana DeGette 
3) Raymon Anthony Doane
*The candidates results were the following :
1) Charles Casper Stockham recieved 23.0% of the vote and 85,213 number of the votes 
2) Diana DeGette recieved 73.8% of the vote and 272,892 number of the votes
3) Raymon Anthony Doane recieved 3.1% of the vote and 11,606 number of the votes

*The winner of the election was Diana DeGette who recieved 73.8% of the vote and 272,892 number of the votes!

## County Results
Election data shows -
* A break down of percentage votes per county and total votes per county
- Jefferson: 10.5% (38,855 total votes)
- Denver: 82.8% (306,055 total votes)
- Arapahoe: 6.7% (24,801 total votes)

!{This is an Image] TERMINAL DISPLAY 


## Election Audit Summary
Our original code with Tom and Seth was soley candidate statistics. We added similar if, for, and print statements to generate county details. 
The first task was to create a list and dictionary to for "county analysis". Our second step was to create variables for the "if" statement and "for" loops. We used “not in” membership operators to look though the county names & candidate options list and add the unique value members to the list itself. 

![This is an image] ADDING KEYS TO  LIST 

The next step was to create "for" loop to calculate the percentage and total count from the dictionaries we created earlier. 

![This isan image] FORLOOPS

followed by the "if" statement to retrieve the winning candidate and largest county turnout

![This is an image] IF STATEMENT 
Note: We converetd county into a string since county_turnout variable was called out as a string. This was not applicable to the candidate_name since the winning_candidate variable are already strings themselves. 



