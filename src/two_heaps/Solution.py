


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

	# room that held the most meetings
	return count.index(max(count))