def canCompleteCircuit(gas, cost):
    total_tank = 0
    curr_tank = 0
    start_index = 0

    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        curr_tank += gas[i] - cost[i]
        if curr_tank < 0:
            start_index = i + 1
            curr_tank = 0

    return start_index if total_tank >= 0 else -1

# Example usage
if __name__ == "__main__":
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    print(canCompleteCircuit(gas1, cost1))  # Output: 3

    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    print(canCompleteCircuit(gas2, cost2))  # Output: -1
