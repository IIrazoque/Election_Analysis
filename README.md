# Election_Analysis
Using python for Colorado's election analysis
## Project Overview 
Tom and Seth both employees as Colorado's Board of Elections and we were given the task to audit a local congressional election.

1. Using python we calculated the total number of votes casts
2. Created a list of candidates & counties who received votes
3. Calculated the total number of voters per candidate and counts for each county
4. Calculated the percentage of votes for each candidate and calculated the percentage per county
5. Determined the winner of the election based on popular vote and the largest county turnout

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.5, Visual Studio, 1.38.1
- Delivery form: election_analysis.txt

## Candidate Results 
Election data shows -
*There were "368,711" votes casted in the election*

*The candidates were :*

- Charles Casper Stockham
-  Diana DeGette
-   Raymon Anthony Doane

*The candidates results were the following :*

1) Charles Casper Stockham received 23.0% of the vote and 85,213 number of the votes 
2) Diana DeGette received 73.8% of the vote and 272,892 number of the votes
3) Raymon Anthony Doane received 3.1% of the vote and 11,606 number of the votes

### **The winner of the election was Diana DeGette who received 73.8% of the vote and 272,892 number of the votes!**

## County Results
Election data shows -
* A break down of percentage votes per county and total votes per county :*

- Jefferson: 10.5% (38,855 total votes)
- Denver: 82.8% (306,055 total votes)
- Arapahoe: 6.7% (24,801 total votes)

![This is an image](https://github.com/IIrazoque/Election_Analysis/blob/948330858e6ab4be5502c1605afa53b8a8c5d4d1/Resources/terminal_display_screenshot.PNG)


## Election Audit Summary
Our original code with Tom and Seth was solely candidate statistics. We added similar if, for, and print statements to generate county details. 
The first task was to create a list and dictionary to for "county analysis". 

![This is an image](https://github.com/IIrazoque/Election_Analysis/blob/948330858e6ab4be5502c1605afa53b8a8c5d4d1/Resources/creating_list_dicts_variables.PNG)

Our second step was to add "keys" into the list we created above; candidate_options and county_names. In this particular "if" statement we looked for unique "keys" and started the count for each unique key, hence each candidate and county name. We did this by using the “not in” membership operator. 


![This is an image](https://github.com/IIrazoque/Election_Analysis/blob/948330858e6ab4be5502c1605afa53b8a8c5d4d1/Resources/adding%20keys%20to%20list.PNG)

The next step was to create "for" loop to calculate the percentage and total count from the dictionaries we created earlier. Since the county_count is a string variable, we set the county to a string as shown below.

![This is an image](https://github.com/IIrazoque/Election_Analysis/blob/948330858e6ab4be5502c1605afa53b8a8c5d4d1/Resources/for%20loop%20code.png)

followed by the "if" statement to retrieve the winning candidate and largest county turnout. Keeping in mind that the if statement lives inside the for loop.

![This is an image](https://github.com/IIrazoque/Election_Analysis/blob/948330858e6ab4be5502c1605afa53b8a8c5d4d1/Resources/if%20statement%20code.png)
Note: We converetd county into a string since county_turnout variable was called out as a string. This was not applicable to the candidate_name since the winning_candidate variable are already strings themselves. 



