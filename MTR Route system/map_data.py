station_chinese_map = {
    #东铁线
    "金钟": "ADM",
    "会展": "EXC",
    "红磡": "HUH",
    "旺角东": "MKK",
    "九龙塘": "KOT",
    "大围": "TAW",
    "沙田": "SHT",
    "火炭": "FOT",
    "马场": "RAC",
    "大学": "UNI",
    "大埔墟": "TAP",
    "太和": "TWO",
    "粉岭": "FAN",
    "上水": "SHS",
    "罗湖": "LOW",
    "落马洲": "LMC",
    # 南港岛线
    "海洋公园": "OCP",
    "黄竹坑": "WCH",
    "利东": "LET",
    "海怡半岛": "SOH",
    # 屯马线
    "乌溪沙": "WKS",
    "马鞍山": "MOS",
    "恒安": "HEO",
    "大水坑": "TSH",
    "石门": "SHM",
    "第一城": "CIO",
    "沙田围": "STW",
    "车公庙": "CKT",
    "显径": "HIK",
    "钻石山": "DIH",
    "启德": "KAT",
    "宋皇台": "SUW",
    "土瓜湾": "TKW",
    "何文田": "HOM",
    "尖东": "ETS",
    "柯士甸": "AUS",
    "南昌": "NAC",
    "美孚": "MEF",
    "荃湾西": "TWW",
    "锦上路": "KSR",
    "元朗": "YUL",
    "朗屏": "LOP",
    "天水围": "TIS",
    "兆康": "SIH",
    "屯门":"TUM",
    # 观塘线
    "黄埔": "WHA",
    "油麻地": "YMT",
    "旺角": "MOK",
    "太子": "PRE",
    "石硤尾": "SKM",
    "乐富": "LOF",
    "黄大仙": "WTS",
    "彩虹": "CHH",
    "九龙湾": "KOB",
    "牛头角": "NTK",
    "观塘": "KWT",
    "蓝田": "LAT",
    "油塘": "YAT",
    "调景岭": "TIK",
    # 荃湾线
    "中环": "CEN",
    "尖沙咀": "TST",
    "佐敦": "JOR",
    "深水埗": "SSP",
    "长沙湾": "CSW",
    "荔枝角": "LCK",
    "荔景": "LAK",
    "葵芳": "KWF",
    "葵兴": "KWH",
    "大窝口": "TWH",
    "荃湾": "TSW",
    # 港岛线
    "坚尼地城": "KET",
    "香港大学": "HKU",
    "西营盘": "SYP",
    "上环": "SHW",
    "湾仔": "WAC",
    "铜锣湾": "CAB",
    "天后": "TIH",
    "炮台山": "FOH",
    "北角": "NOP",
    "鲗鱼涌": "QUB",
    "太古": "TAK",
    "西湾河": "SWH",
    "筲箕湾": "SKW",
    "杏花邨": "HFC",
    "柴湾": "CHW",
    # 将军澳线
    "将军澳": "TKO",
    "坑口": "HAH",
    "宝琳": "POA",
    "康城": "LHP",
    # 东涌线
    "香港": "HOK",
    "九龙": "KOW",
    "奥运": "OLY",
    "青衣": "TSY",
    "欣澳": "SUN",
    "东涌": "TUC",
    # 迪士尼线
    "迪士尼": "DIS"
}



reverse_station_chinese_map = {EN :CH for CH, EN in station_chinese_map.items()}


line_chinese_map = {
    "EAL": "东铁线",
    "SIL": "南港岛线",
    "TML": "屯马线",
    "KTL": "观塘线",
    "TWL": "荃湾线",
    "ISL": "港岛线",
    "TKL": "将军澳线",
    "TCL": "东涌线",
    "DRL": "迪士尼线",


}



map = {
    # 港岛线
    "KET": {"HKU": 2},  # 坚尼地城
    "HKU": {"KET": 2, "SYP": 2},  # 香港大学
    "SYP": {"HKU": 2, "SHW": 2},  # 西营盘
    "SHW": {"SYP": 2, "CEN": 2},  # 上环
    "CEN": {"SHW": 2, "ADM": 4, "HOK": 5},  # 中环
    "ADM": {"CEN":2,"WAC": 2, "TST": 4, "EXC": 4, "OCP": 6},  # 金钟（荃湾线、东铁线、南港岛线换乘）
    "WAC": {"ADM": 2, "CAB": 2},  # 湾仔
    "CAB": {"WAC": 2, "TIH": 2},  # 铜锣湾
    "TIH": {"CAB": 2, "FOH": 2},  # 天后
    "FOH": {"TIH": 2, "NOP": 2},  # 炮台山
    "NOP": {"FOH": 2, "QUB": 2},  # 北角（将军澳线换乘）
    "QUB": {"NOP": 2, "TAK": 2, "YAT": 5},  # 鲗鱼涌（将军澳线换乘）
    "TAK": {"QUB": 2, "SWH": 3},  # 太古
    "SWH": {"TAK": 3, "SKW": 2},  # 西湾河
    "SKW": {"SWH": 2, "HFC": 2},  # 筲箕湾
    "HFC": {"SKW": 2, "CHW": 3},  # 杏花邨
    "CHW": {"HFC": 3},  # 柴湾

    # 荃湾线
    "CEN": {"SHW": 2, "ADM": 2, "HOK": 5},  # 中环
    "ADM": {"CEN":2,"WAC": 2, "TST": 4, "EXC": 4, "OCP": 6}, # 金钟
    "TST": {"ADM": 4, "JOR": 2},  # 尖沙咀
    "JOR": {"TST": 2, "YMT": 2},  # 佐敦
    "YMT": {"JOR": 2, "MOK": 2, "HOM": 3},  # 油麻地（观塘线换乘）
    "MOK": {"YMT": 2, "PRE": 1},  # 旺角（观塘线换乘）
    "PRE": {"MOK": 1, "SSP": 2, "SKM": 2},  # 太子
    "SSP": {"PRE": 2, "CSW": 2},  # 深水埗
    "CSW": {"SSP": 2, "LCK": 2},  # 长沙湾
    "LCK": {"CSW": 2, "MEF": 2},  # 荔枝角
    "MEF": {"LCK": 2, "LAK": 3, "TWW": 7, "NAC": 4},  # 美孚（屯马线换乘）
    "LAK": {"MEF": 3, "KWF": 2, "TSY": 2, "NAC": 3},  # 荔景（东涌线换乘）
    "KWF": {"LAK": 2, "KWH": 2},  # 葵芳
    "KWH": {"KWF": 2, "TWH": 2},  # 葵兴
    "TWH": {"KWH": 2, "TSW": 2},  # 大窝口
    "TSW": {"TWH": 2},  # 荃湾

    # 屯马线
    "WKS": {"MOS": 2},  # 乌溪沙
    "MOS": {"WKS": 2, "HEO": 2},  # 马鞍山
    "HEO": {"MOS": 2, "TSH": 2},  # 恒安
    "TSH": {"HEO": 2, "SHM": 4},  # 大水坑
    "SHM": {"TSH": 4, "CIO": 2},  # 石门
    "CIO": {"SHM": 2, "STW": 2},  # 第一城
    "STW": {"CIO": 2, "CKT": 2},  # 沙田围
    "CKT": {"STW": 2, "TAW": 2},  # 车公庙
    "TAW": {"CKT": 2, "HIK": 2, "SHT": 4, "KOT": 6},  # 大围（东铁线换乘）
    "HIK": {"TAW": 2, "DIH": 6},  # 显径
    "DIH": {"HIK": 6, "KAT": 2, "WTS": 2, "CHH": 2},  # 钻石山（观塘线换乘）
    "KAT": {"DIH": 2, "SUW": 2},  # 启德
    "SUW": {"KAT": 2, "TKW": 2},  # 宋皇台
    "TKW": {"SUW": 2, "HOM": 2},  # 土瓜湾
    "HOM": {"TKW": 2, "HUH": 2, "YMT": 3, "WHA": 2},  # 何文田（观塘线换乘）
    "HUH": {"HOM": 2, "ETS": 3, "MKK": 3, "EXC": 5},  # 红磡（东铁线换乘）
    "ETS": {"HUH": 3, "AUS": 3},  # 尖东
    "AUS": {"ETS": 3, "NAC": 4},  # 柯士甸
    "NAC": {"AUS": 4, "MEF": 4, "LAK": 3, "OLY": 1},  # 南昌（东涌线换乘）
    "MEF": {"NAC": 4, "TWW": 7, "LAK": 3, "LCK": 2},  # 美孚
    "TWW": {"MEF": 7, "KSR": 13},  # 荃湾西
    "KSR": {"TWW": 13, "YUL": 5},  # 锦上路
    "YUL": {"KSR": 5, "LOP": 2},  # 元朗
    "LOP": {"YUL": 2, "TIS": 4},  # 朗屏
    "TIS": {"LOP": 4, "SIH": 8},  # 天水围
    "SIH": {"TIS": 8, "TUM": 3},  # 兆康
    "TUM": {"SIH": 3},  # 屯门

    # 东铁线
    "ADM": {"CEN":2,"WAC": 2, "TST": 4, "EXC": 4, "OCP": 6}, # 金钟
    "EXC": {"ADM": 4, "HUH": 5},  # 会展
    "HUH": {"HOM": 2, "ETS": 3, "MKK": 3, "EXC": 5}, #红磡
    "MKK": {"HUH": 3,"KOT": 3},  # 旺角东
    "KOT": {"MKK": 3, "TAW": 6, "SKM": 2, "LOF": 2},  # 九龙塘（观塘线、荃湾线换乘）
    "TAW": {"KOT": 6, "SHT": 4, "CKT": 2, "HIK": 2},  # 大围（屯马线换乘）
    "SHT": {"TAW": 4, "FOT": 3},  # 沙田
    "FOT": {"SHT": 3, "RAC": 20, "UNI": 3,},  # 火炭
    "RAC": {"FOT": 20},  # 马场
    "UNI": {"FOT": 3, "TAP": 7},  # 大学
    "TAP": {"UNI": 7, "TWO": 2},  # 大埔墟
    "TWO": {"TAP": 2, "FAN": 7},  # 太和
    "FAN": {"TWO": 7, "SHS": 3},  # 粉岭
    "SHS": {"FAN": 3, "LOW": 5, "LMC": 8},  # 上水
    "LOW": {"SHS": 5},  # 罗湖
    "LMC": {"SHS": 8},  # 落马洲

    # 观塘线
    "WHA": {"HOM": 2},  # 黄埔
    "HOM": {"WHA": 2, "YMT": 3, "TKW": 2, "HUH": 2},  # 何文田（屯马线换乘）
    "YMT": {"HOM": 3, "MOK": 2, "JOR": 2},  # 油麻地（荃湾线换乘）
    "MOK": {"YMT": 2, "PRE": 1},  # 旺角（荃湾线换乘）
    "PRE": {"MOK": 1, "SKM": 2, "SSP": 2},  # 太子
    "SKM": {"PRE": 2, "KOT": 2},  # 石硤尾
    "KOT": {"SKM": 2, "LOF": 2, "MKK": 3, "TAW": 6},  # 九龙塘（东铁线、荃湾线换乘）
    "LOF": {"KOT": 2, "WTS": 2},  # 乐富
    "WTS": {"LOF": 2, "DIH": 2},  # 黄大仙
    "DIH": {"WTS": 2, "CHH": 2, "HIK": 6, "KAT": 2},  # 钻石山（屯马线换乘）
    "CHH": {"DIH": 2, "KOB": 2},  # 彩虹
    "KOB": {"CHH": 2, "NTK": 2},  # 九龙湾
    "NTK": {"KOB": 2, "KWT": 2},  # 牛头角
    "KWT": {"NTK": 2, "LAT": 2},  # 观塘
    "LAT": {"KWT": 2, "YAT": 2},  # 蓝田
    "YAT": {"LAT": 2, "TIK": 4, "QUB": 5},  # 油塘（将军澳线换乘）
    "TIK": {"YAT": 4, "TKO": 2},  # 调景岭

    # 南港岛线
    "OCP": {"ADM": 6, "WCH": 2},  # 海洋公园
    "WCH": {"OCP": 2, "LET": 2},  # 黄竹坑
    "LET": {"WCH": 2, "SOH": 3},  # 利东
    "SOH": {"LET": 3},  # 海怡半岛

    # 将军澳线
    "NOP": {"QUB": 2, "FOH": 2},  # 北角（港岛线换乘）
    "QUB": {"NOP": 2, "YAT": 5, "TAK": 2},  # 鲗鱼涌（港岛线换乘）
    "YAT": {"QUB": 5, "TIK": 4, "LAT": 2},  # 油塘（观塘线换乘）
    "TIK": {"YAT": 4, "TKO": 2},  # 调景岭
    "TKO": {"TIK": 2, "HAH": 2, "LHP": 6},  # 将军澳
    "HAH": {"TKO": 2, "POA": 2},  # 坑口
    "POA": {"HAH": 2},  # 宝琳
    "LHP": {"TKO": 6},  # 康城

    # 东涌线
    "HOK": {"KOW": 2, "CEN": 5},  # 香港
    "KOW": {"HOK": 2, "OLY": 2},  # 九龙
    "OLY": {"KOW": 2, "NAC": 1},  # 奥运
    "NAC": {"OLY": 1, "LAK": 3, "AUS": 4, "MEF": 4},  # 南昌（屯马线换乘）
    "LAK": {"NAC": 3, "TSY": 2, "MEF": 3, "KWF": 2},  # 荔景（荃湾线换乘）
    "TSY": {"LAK": 2, "SUN": 7},  # 青衣
    "SUN": {"TSY": 7, "TUC": 8, "DIS": 7},  # 欣澳（迪士尼线换乘）
    "TUC": {"SUN": 8},  # 东涌

    # 迪士尼线
    "SUN": {"DIS": 7, "TSY": 7, "TUC": 8},  # 欣澳（东涌线换乘）
    "DIS": {"SUN": 7}  # 迪士尼



}



station_line = {
    # 港岛线
    "KET": ["ISL"],
    "HKU": ["ISL"],
    "SYP": ["ISL"],
    "SHW": ["ISL"],
    "CEN": ["ISL", "TWL"],
    "ADM": ["ISL", "TWL", "EAL", "SIL"],
    "WAC": ["ISL"],
    "CAB": ["ISL"],
    "TIH": ["ISL"],
    "FOH": ["ISL"],
    "NOP": ["ISL", "TKL"],
    "QUB": ["ISL", "TKL"],
    "TAK": ["ISL"],
    "SWH": ["ISL"],
    "SKW": ["ISL"],
    "HFC": ["ISL"],
    "CHW": ["ISL"],

    # 荃湾线
    "TST": ["TWL"],
    "JOR": ["TWL"],
    "YMT": ["TWL", "KTL"],
    "MOK": ["TWL", "KTL"],
    "PRE": ["TWL"],
    "SSP": ["TWL"],
    "CSW": ["TWL"],
    "LCK": ["TWL"],
    "MEF": ["TWL", "TML"],
    "LAK": ["TWL", "TML", "TCL"],
    "KWF": ["TWL"],
    "KWH": ["TWL"],
    "TWH": ["TWL"],
    "TSW": ["TWL"],

    # 屯马线
    "WKS": ["TML"],
    "MOS": ["TML"],
    "HEO": ["TML"],
    "TSH": ["TML"],
    "SHM": ["TML"],
    "CIO": ["TML"],
    "STW": ["TML"],
    "CKT": ["TML"],
    "TAW": ["TML", "EAL"],
    "HIK": ["TML"],
    "DIH": ["TML", "KTL"],
    "KAT": ["TML"],
    "SUW": ["TML"],
    "TKW": ["TML"],
    "HOM": ["TML", "KTL"],
    "HUH": ["TML", "EAL"],
    "ETS": ["TML"],
    "AUS": ["TML"],
    "NAC": ["TML", "TCL"],
    "TWW": ["TML"],
    "KSR": ["TML"],
    "YUL": ["TML"],
    "LOP": ["TML"],
    "TIS": ["TML"],
    "SIH": ["TML"],
    "TUM": ["TML"],

    # 东铁线
    "EXC": ["EAL"],
    "MKK": ["EAL"],
    "KOT": ["EAL", "KTL"],
    "TAW": ["EAL", "TML"],
    "SHT": ["EAL"],
    "FOT": ["EAL"],
    "RAC": ["EAL"],
    "UNI": ["EAL"],
    "TAP": ["EAL"],
    "TWO": ["EAL"],
    "FAN": ["EAL"],
    "SHS": ["EAL"],
    "LOW": ["EAL"],
    "LMC": ["EAL"],

    # 观塘线
    "WHA": ["KTL"],
    "HOM": ["KTL", "TML"],
    "YMT": ["KTL", "TWL"],
    "MOK": ["KTL", "TWL"],
    "PRE": ["KTL", "TWL"],
    "SKM": ["KTL"],
    "KOT": ["KTL", "EAL"],
    "LOF": ["KTL"],
    "WTS": ["KTL"],
    "DIH": ["KTL", "TML"],
    "CHH": ["KTL"],
    "KOB": ["KTL"],
    "NTK": ["KTL"],
    "KWT": ["KTL"],
    "LAT": ["KTL"],
    "YAT": ["KTL", "TKL"],
    "TIK": ["KTL", "TKL"],

    # 南港岛线
    "OCP": ["SIL"],
    "WCH": ["SIL"],
    "LET": ["SIL"],
    "SOH": ["SIL"],

    # 将军澳线
    "NOP": ["TKL"],
    "QUB": ["TKL"],
    "TKO": ["TKL"],
    "HAH": ["TKL"],
    "POA": ["TKL"],
    "LHP": ["TKL"],

    # 东涌线
    "HOK": ["TCL"],
    "KOW": ["TCL"],
    "OLY": ["TCL"],
    "NAC": ["TCL", "TML"],
    "LAK": ["TCL", "TWL"],
    "TSY": ["TCL"],
    "SUN": ["TCL", "DRL"],
    "TUC": ["TCL"],

    # 迪士尼线
    "SUN": ["DRL", "TCL"],
    "DIS": ["DRL"]

}