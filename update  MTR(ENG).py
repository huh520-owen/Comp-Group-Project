import heapq
from map_data import *  # Assumes you have the necessary station and line mappings


class RoutePlanner:
    def __init__(self, map):
        self.map = map

    def dijkstra(self, start, end):
        heap = [(0, start, [])]
        visited = {}

        while heap:
            cost_time, station, path = heapq.heappop(heap)

            if station in visited and visited[station] <= cost_time:
                continue
            visited[station] = cost_time
            new_path = path + [station]

            if station == end:
                return new_path, cost_time

            for other_station, other_time in self.map.get(station, {}).items():
                new_cost_time = cost_time + other_time
                if other_station not in visited or visited[other_station] > new_cost_time:
                    heapq.heappush(heap, (new_cost_time, other_station, new_path))

        return None, None


class TransferDetector:
    def __init__(self, station_line):
        self.station_line = station_line

    def transfer(self, path):
        transfer_station = []
        now_line = []

        for i in range(len(path) - 1):
            now = path[i]
            next = path[i + 1]
            same_line = set(self.station_line.get(now, [])).intersection(self.station_line.get(next, []))
            if not same_line:
                continue
            if not now_line:
                now_line = list(same_line)
            else:
                new_same = list(same_line)
                if not set(new_same).intersection(now_line):
                    transfer_information = {
                        "station": now,
                        "line_from": now_line[0],
                        "line_to": new_same[0],
                    }
                    transfer_station.append(transfer_information)
                    now_line = new_same

        return transfer_station


def transfer_output(transfer_station):
    if not transfer_station:
        return "No transfers needed"

    message = []
    for t in transfer_station:
        mess_EN = f"Transfer at {reverse_station_english_map[t['station']]} from {line_english_map[t['line_from']]} to {line_english_map[t['line_to']]} \n"
        message.append(mess_EN)
    return "".join(message)


def route_MTR():
    print("Hong Kong MTR Route Planning System")
    print("=" * 50)

    valid_english = list(station_english_map.keys())

    while True:  # Loop to continuously ask for input until valid
        start = input("Please enter the starting station name: ").strip()
        end = input("Please enter the destination station name: ").strip()

        start_code = station_english_map.get(start)
        end_code = station_english_map.get(end)

        if not start_code or not end_code:
            print("Error: The station name entered is invalid. Please check the following valid names:")
            print(",".join(valid_english))
            continue  # Continue the loop to ask for input again

        planner = RoutePlanner(map)
        path, total_time = planner.dijkstra(start_code, end_code)

        if not path:
            print("Cannot find a valid route.")
            print("Please enter the correct names.")
            continue  # Continue the loop if no valid route is found

        detector = TransferDetector(station_line)
        transfers = detector.transfer(path)
        english_path = [reverse_station_english_map[i] for i in path]

        print("\n==== Route Planning Result ====")
        print(f"Route: {'->'.join(english_path)}")
        print(f"Total time: {total_time} minutes")
        print("\n==== Transfer Information ====")
        print(transfer_output(transfers))

        break  # Exit the loop after successful execution


if __name__ == "__main__":
    route_MTR()
    
