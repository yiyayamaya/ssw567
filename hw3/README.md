# ssw567 hw3


Q1

| input                  | values      | 1  | 2   | 3   | 4   | 5   | 6   |
|------------------------|-------------|----|-----|-----|-----|-----|-----|
| \>=63 years            | Y,N | Y  | Y   | Y   | Y   | N   | N   |
| \>=80 years            | Y,N  | Y  | Y   | N   | N   | N   | N   |
| salary < 90000         | Y,N | Y  | N   | Y   | N   | Y   | N   |
| result                 |      |    |     |     |     |     |     |
| 1.5%                   |    |    | x   |     | x   |     |     |
| 1.55%                  |     | x  |     |     |     |     |     |
| 1.6%                   |      |    |     | x   |     |     |     |
| not eligible to retire |      |    |     |     |     | x   | x   |

combine 2and4 5and6

| input                  | values      | 1  | 2   | 3   | 4   |
|------------------------|-------------|----|-----|-----|-----|
| \>=63 years            | Y,N | Y  | Y   | Y   | N   |
| \>=80 years            | Y,N  | Y  | -   | N   | N   |
| salary < 90000         | Y,N | Y  | N   | Y   | -   |
| result                 |      |    |     |     |     |
| 1.5%                   |    |    | x   |     |     |
| 1.55%                  |     | x  |     |     |     |
| 1.6%                   |      |    |     | x   |     |
| not eligible to retire |      |    |     |     | x   |

Q2

| States\Inputs | Full power | Half power | Timer    | Number   | Door Open | Door closed | start     | cancel  | time out |
|---------------|------------|------------|----------|----------|-----------|-------------|-----------|---------|----------|
| waiting       | Full power | Half power |          |          |           |             |           |         |          |
| Full power    |            | Half power | Set time |          |           |             |           |         |          |
| Set time      |            |            |          | Set time | Disabled  | Enabled     |           |         |          |
| Half power    | Full power |            | Set time |          |           |             |           |         |          |
| Disabled      |            |            |          |          |           | Enabled     |           |         |          |
| Enalbled      |            |            |          |          |           |             | Operation |         |          |
| Operation     |            |            |          |          | Disabled  |             |           | Waiting | Waiting  |

| Test case ID | Current State | Command     | action                      | Next State |
|--------------|---------------|-------------|-----------------------------|------------|
| T-200        | waiting       | Full power  | do:set power=600            | Full power |
| T-201        | waiting       | Half power  | do:set power=300            | Half power |
| T-202        | Full power    | Half power  | do:set power=300            | Half power |
| T-203        | Full power    | Timer       | do:get number exit:set time | Set time   |
| T-204        | Set time      | Number	     | do:get number exit:set time | Set time	  |
| T-205        | Set time      | Door Open   | do:display 'Waiting'        | Disabled   |
| T-206        | Set time      | Door closed | do:display 'Ready'          | Enabled    |
| T-207        | Half power    | Full power  | do:set power=600            | Full power |
| T-208        | Half power    | Timer       | do:get number exit:set time | Set time   |
| T-209        | Disabled      | Door closed | do:display 'Ready'          | Enabled    |
| T-210        | Enabled       | start       | do:operate oven             | Operation  |
| T-211        | Operation     | Door Open   | do:display 'Waiting'        | Disabled   |
| T-212        | Operation     | cancel      | do:display time             | Waiting    |
| T-213        | Operation     | time out    | do:display time             | Waiting    |



1. Assignment Description: HW 03 - Decision Table and State Diagram

2. Author: Xingjian Wu

3. Summary:  as the tables above

5. Detailed results, if any

6. Honor pledge I affirm that I will not give or receive any unauthorized help on this assignment, and that all work will be my own.

