# MAC_Scheduler_Project
LTE MAC Scheduler Simulation
Objective: Implement a MAC layer scheduler that allocates PRBs to UEs based on algorithms like Round Robin, Proportional Fair, or Maximum Throughput.
Features: 
•	Input: CQI reports, QoS parameters, buffer status.
•	Output: PRB allocation for UEs.
•	Visualization: Resource usage, fairness, and throughput graphs.
What is MAC Scheduler?
MAC Scheduler is a component of LTE network’s radio resource management. It allocates radio resources like time and frequency slots, to various UEs or services in efficient manner.
Function of MAC Scheduler:
•	Resource Allocation: Dynamically assigns radio resources to UEs per Transmission Interval (TI), prioritizing QoS, channel conditions, and congestion.
•	Scheduling Algorithms: Implements algorithms like Proportional Fair, Round Robin, or Maximum C/I to determine UE resource allocation.
•	QoS Management: Allocates resources based on QoS needs, ensuring strict requirements for real-time services like voice and video.
•	HARQ Management: Manages Hybrid Automatic Repeat Request processes to enhance transmission reliability through error correction.
•	Fairness and Load Balancing: Ensures fairness among UEs, prevents resource monopolization, and balances network load across cells.
•	Buffer Management: Prioritizes UEs with larger data buffers to avoid overflow and ensure smooth data transmission.
•	Interference Management: Mitigates interference, particularly for cell-edge users, by adjusting resource allocation.
•	Dynamic Adaptation: Continuously adapts to changing conditions like channel quality, user mobility, and traffic load.
•	Spectral Efficiency: Optimizes the use of radio resources for improved network and spectral efficiency.
•	Layer Coordination: Collaborates with RLC and physical layers to enable seamless data flow.
•	Power Control: Regulates UE transmission power for desired SINR, reduced interference, and extended battery life.
Project Goal:
Simulate a MAC layer scheduler that dynamically allocates Physical Resource Blocks (PRBs) to UEs based on scheduling algorithms like Round Robin or Proportional Fair.
Steps for creating the scheduler:

Step 1: Understand the Scheduler:
The MAC scheduler decides:
1.	Which UE gets the resources (based on priority, QoS, or fairness).
2.	How much resource is allocated (PRBs assigned per UE).
Key inputs for the scheduler:
•	CQI (Channel Quality Indicator): Reflects channel conditions for each UE.
•	Buffer Status: Indicates the amount of data waiting to be sent for each UE.
•	QoS Requirements: Determines priority among UEs.

Step 2: Define the Problem
1.	Simulate n UEs with random CQI values and buffer statuses.
2.	Implement a Round Robin Scheduler/ Proportional Fair Scheduler as per requirement.
3.	Allocate total PRBs across the UEs.
4.	Visualize the PRB allocation.
   
Step 3: Set Up the code
Here’s how we’ll structure the program:
1.	UE Class: Represents each user equipment with its CQI and buffer status.
2.	Scheduler Function: Allocates PRBs based on a scheduling algorithm.
3.	Visualization: Plots PRB allocation using a bar chart.
   
Step 4: Code Implementation using Python

Step 5: Output 
For Round Robin Scheduler
PRB Allocation Results:
UE 1: CQI=12, Buffer=73 KB, Allocated PRBs=4
UE 2: CQI=9, Buffer=48 KB, Allocated PRBs=4
UE 3: CQI=15, Buffer=21 KB, Allocated PRBs=4
UE 4: CQI=7, Buffer=56 KB, Allocated PRBs=4
UE 5: CQI=11, Buffer=67 KB, Allocated PRBs=4
CQI: Randomly generated (from 1 to 15).
Buffer: Random value (from 0 to 100 KB).
Allocated PRBs: All UEs will get 4 PRBs each since there are 20 PRBs in total.
Note: The exact numbers for CQI and buffer status will change every time you run the program because they are randomly generated.
Visualization in Bar graph:
The bar chart will display PRB allocation for each UE. Since it's a Round Robin Scheduler, the bars will be nearly equal for each UE, but if the number of UEs is less than the total PRBs, there will be an even distribution of PRBs (any leftover PRBs will be distributed evenly among the UEs).
This allocation is for even number of PRB’s = 20
 
This allocation is for odd number of PRB’s = 22
PRB Allocation Results:
UE 1: CQI=12, Buffer=98 KB, Allocated PRBs=5
UE 2: CQI=2, Buffer=28 KB, Allocated PRBs=5
UE 3: CQI=15, Buffer=24 KB, Allocated PRBs=4
UE 4: CQI=7, Buffer=44 KB, Allocated PRBs=4
UE 5: CQI=7, Buffer=16 KB, Allocated PRBs=4
 

For Prportional Fair Scheduler
PRB Allocation Results (Proportional Fair):
UE 1: CQI=5, Buffer=42 KB, Allocated PRBs=1
UE 2: CQI=14, Buffer=59 KB, Allocated PRBs=7
UE 3: CQI=12, Buffer=43 KB, Allocated PRBs=5
UE 4: CQI=7, Buffer=50 KB, Allocated PRBs=3
UE 5: CQI=10, Buffer=47 KB, Allocated PRBs=4
This allocation is for even number of PRB’s = 20
Inputs:
•	Total PRBs: 20
•	Number of UEs: 5
•	Randomly Generated CQI and Buffer Status: 
•	UE 1: CQI=5, Buffer=42 KB
•	UE 2: CQI=14, Buffer=59 KB
•	UE 3: CQI=12, Buffer=43 KB
•	UE 4: CQI=7, Buffer=50 KB
•	UE 5: CQI=10, Buffer=47 KB
Step 1: Calculate Weights
Weights are calculated as:
Weight = CQI * Buffer
For each UE:
UE 1: Weight = 5 * 42 = 210
UE 2: Weight = 14 * 59 = 826
UE 3: Weight = 12 * 43 = 516
UE 4: Weight = 7 * 50 = 350
UE 5: Weight = 10 * 47 = 470
Step 2: Normalize Weights
Sum of all weights:
Total Weight = 210 + 826 + 516 + 350 + 470 = 2372
Normalized weights (proportions):
UE 1: 210 / 2372≈ 0.089
UE 2: 826 / 2372 ≈ 0.348
UE 3: 516 / 2372 ≈ 0.218
UE 4: 350 / 2372 ≈ 0.148
UE 5: 470 / 2372 ≈ 0.198
Step 3: Calculated PRBs
PRBs are calculated as:
Calculated PRBs = Normalized Weight * Total PRBs
For each UE:
UE 1: 0.089 * 20 ≈ 1 PRBs
UE 2: 0.348 * 20 ≈ 7 PRBs
UE 3: 0.218 * 20 ≈ 5 PRBs
UE 4: 0.148 * 20 ≈ 3 PRBs
UE 5: 0.198 * 20 ≈ 4 PRB
Allocation of PRB will be done with keeping Buffer status and Calculated PRB.
Step 4: Handle Leftover PRBs
•	Total calculated PRBs = 1 + 7 + 5 + 3 + 4 = 20
•	No leftover PRBs in this case.
For leftover case like PRB = 22 (Difference=22-20=2)
Distribute leftover PRBs to UEs with the highest weights:
UE (highest weight) gets 1 additional PRB → x + 1 = x+1 PRBs.
UE (second highest weight) gets 1 additional PRB → y + 1 = y+1 PRBs.
And so on with 3rd highest
Bar Chart: A bar chart will show:
•	UE 2 (highest weight) receiving the most PRBs.
•	UE 1 (lowest weight) receiving the least PRBs.
•	A gradual distribution based on weights.
 
This allocation is for odd number of PRB’s = 22
PRB Allocation Results (Proportional Fair):
UE 1: CQI=1, Buffer=18 KB, Allocated PRBs=0
UE 2: CQI=3, Buffer=31 KB, Allocated PRBs=1
UE 3: CQI=5, Buffer=61 KB, Allocated PRBs=6
UE 4: CQI=8, Buffer=70 KB, Allocated PRBs=11
UE 5: CQI=9, Buffer=19 KB, Allocated PRBs=4
 
