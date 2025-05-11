# Meetings Room III
import heapq

def most_booked(meetings, rooms):
    # Count array to track the number of meetings each room holds
    count = [0] * rooms

    # Create min-heaps for available rooms and used rooms
    available = [i for i in range(rooms)]
    used_rooms = []

    # Sort the meetings by their start time
    meetings.sort()
    for start_time, end_time in meetings:
        # Free up rooms that have finished their meetings by the current start time
        while used_rooms and used_rooms[0][0] <= start_time:
            ending, room = heapq.heappop(used_rooms)
            heapq.heappush(available, room)

        # If no rooms are available, delay the meeting until a room becomes free
        if not available:
            end, room = heapq.heappop(used_rooms)
            end_time = end + (end_time - start_time)
            heapq.heappush(available, room)

        # Allocate the meeting to the available room with the lowest number
        room = heapq.heappop(available)
        heapq.heappush(used_rooms, (end_time, room))
        count[room] += 1
    return count.index(max(count))




def minimum_machines(tasks: list[list[int]]) -> int:
    machines = []
    tasks.sort()

    for start, end in tasks:
        if machines and machines[0] <= start:
            heapq.heappop(machines)

        heapq.heappush(machines, end)

    return len(machines)


def connect_sticks(sticks: list[int]) -> int:
    heapq.heapify(sticks)
    total_cost = 0

    while len(sticks) > 1:
        f = heapq.heappop(sticks)
        s = heapq.heappop(sticks)

        cost = f + s
        total_cost += cost

        heapq.heappush(sticks, cost)
    return total_cost
