import random
import matplotlib.pyplot as plt

# Define UE class
class UE:
    def __init__(self, ue_id):
        self.ue_id = ue_id
        self.cqi = random.randint(1, 15)  # Random CQI (1 to 15)
        self.buffer_status = random.randint(0, 100)  # Buffer data in KB
        self.allocated_prbs = 0  # PRBs allocated by the scheduler

# Proportional Fair Scheduler
def proportional_fair_scheduler(ues, total_prbs):
    # Calculate weights for each UE based on CQI and buffer status
    weights = []
    for ue in ues:
        weight = ue.cqi * ue.buffer_status  # Combine CQI and buffer as the score
        weights.append(weight)

    # Normalize weights to ensure fair distribution
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]

    # Allocate PRBs proportionally to the weights
    for ue, weight in zip(ues, normalized_weights):
        ue.allocated_prbs = int(weight * total_prbs)  # Calculate proportional allocation

    # Handle leftover PRBs (due to rounding)
    leftover_prbs = total_prbs - sum(ue.allocated_prbs for ue in ues)
    if leftover_prbs > 0:
        # Assign leftover PRBs to UEs with the highest weights
        sorted_ues = sorted(ues, key=lambda ue: weights[ue.ue_id - 1], reverse=True)
        for i in range(leftover_prbs):
            sorted_ues[i % len(sorted_ues)].allocated_prbs += 1

# Visualize PRB Allocation
def visualize_allocation(ues):
    ue_ids = [ue.ue_id for ue in ues]
    allocations = [ue.allocated_prbs for ue in ues]

    plt.bar(ue_ids, allocations)
    plt.title("PRB Allocation per UE (Proportional Fair)")
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
    proportional_fair_scheduler(ues, total_prbs)

    # Display results
    print("PRB Allocation Results (Proportional Fair):")
    for ue in ues:
        print(f"UE {ue.ue_id}: CQI={ue.cqi}, Buffer={ue.buffer_status} KB, Allocated PRBs={ue.allocated_prbs}")

    # Visualize allocation
    visualize_allocation(ues)
