import heapq
from map_data import *



def dijkstra(map, start, end):
    heap = [(0, start, [])]
    visited = {}

    while heap:
        cost_time ,station ,path = heapq.heappop(heap)
        
        if station in visited and visited[station]<= cost_time:
            continue
        visited[station] = cost_time
        new_path = path + [station]
        
        if station == end:
            return new_path , cost_time
        
        for other_station, other_time in map.get(station,{}).items():
            new_cost_time = cost_time + other_time
            if other_station not in visited or visited[other_station] > new_cost_time:
                heapq.heappush(heap,(new_cost_time, other_station, new_path))
    
    return None , None


def transfer(path):
    transfer_station = []
    now_line = []

    for i in range(len(path) - 1):
        now = path[i]
        next = path[i + 1]

        same_line = set(station_line.get(now, [])).intersection(station_line.get(next, []))
        if not same_line :
            continue
        if not now_line :
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



def  transfer_output(transfer_station):
    if not transfer_station :
        return "全程无需换乘/No transfer"

    message = []
    for t in transfer_station:
        mess_CH =f"在 {reverse_station_chinese_map[t['station']]} 换乘从 {line_chinese_map[t['line_from']]} 到 {line_chinese_map[t['line_to']]} \n"
        message.append(mess_CH)
        final ="\n".join(message)
    return final


def route_MTR():
    print("香港地铁2025路线规划系统")
    print("HONG KONG MTR ROUTE PLANNING SYSTEM")
    print("="*50)

    valid_chinese = list(station_chinese_map.keys())

    start = input("请输入起点车站名称：").strip()
    end = input("请输入终点车站名称：").strip()

    start_code = station_chinese_map.get(start)
    end_code = station_chinese_map.get(end)


    if not start_code or not end_code:
        print("错误：输入的车站名称无效，请检查以下有效名称：")
        print(",".join(valid_chinese))
        return
    
    path, total_time = dijkstra(map,start_code,end_code)

    if not path:
        print("无法找到有效路线")
        print("请输入正确名称")
        return
    
    transfers = transfer(path)
    chinese_path = [reverse_station_chinese_map[i] for i in path]

    print("\n====路线规划结果====")
    print(f"路线：{'->'.join(chinese_path)}")
    print(f"总时间：{total_time}分钟")
    print("\n ====换乘信息====")
    print(transfer_output(transfers))


if __name__ == "__main__":
    route_MTR()
