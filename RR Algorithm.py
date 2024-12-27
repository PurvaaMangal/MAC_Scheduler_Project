import random
import matplotlib.pyplot as plt

# Define UE class
class UE:
    def __init__(self, ue_id):
        self.ue_id = ue_id
        self.cqi = random.randint(1, 15)  # Random CQI (1 to 15)
        self.buffer_status = random.randint(0, 100)  # Buffer data in KB
        self.allocated_prbs = 0  # PRBs allocated by the scheduler

# Round Robin Scheduler
def round_robin_scheduler(ues, total_prbs):
    num_ues = len(ues)
    prbs_per_ue = total_prbs // num_ues  # Divide PRBs equally
    leftover_prbs = total_prbs % num_ues  # Any leftover PRBs

    # Allocate PRBs to each UE
    for ue in ues:
        ue.allocated_prbs = prbs_per_ue

    # Distribute leftover PRBs
    for i in range(leftover_prbs):
        ues[i % num_ues].allocated_prbs += 1

# Visualize PRB Allocation
def visualize_allocation(ues):
    ue_ids = [ue.ue_id for ue in ues]
    allocations = [ue.allocated_prbs for ue in ues]

    plt.bar(ue_ids, allocations)
    plt.title("PRB Allocation per UE")
    plt.xlabel("UE ID")
    plt.ylabel("Allocated PRBs")
    plt.show()

# Main function
if __name__ == "__main__":
    total_prbs = 22  # Total PRBs available
    num_ues = 5  # Number of UEs

    # Create UEs
    ues = [UE(ue_id=i) for i in range(1, num_ues + 1)]

    # Run the scheduler
    round_robin_scheduler(ues, total_prbs)

    # Display results
    print("PRB Allocation Results:")
    for ue in ues:
        print(f"UE {ue.ue_id}: CQI={ue.cqi}, Buffer={ue.buffer_status} KB, Allocated PRBs={ue.allocated_prbs}")

    # Visualize allocation
    visualize_allocation(ues)
