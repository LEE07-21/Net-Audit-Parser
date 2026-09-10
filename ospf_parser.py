import re
def parse_ospf_log(log_text):
    """解析OSPF多厂商日志函数"""
    ospf_results = []
    pattern_hw = r"Router ID:\s*([\d\.]+).*?State:\s*([\w\-]+)"
    pattern_cis = r"^([\d\.]+)\s+\d+\s+([0-9A-Z/]+(?:\s+-)?)"



    for  line in log_text.splitlines():
        try:
            line_str = line.strip()
            if not line_str:
                continue
            match_hw = re.search(pattern_hw, line)
            if match_hw:
                ospf_results.append({
                    "vendor": "Huawei",
                    "router_id": match_hw.group(1),
                    "state": match_hw.group(2)
                })
            match_cis = re.search(pattern_cis, line)
            if match_cis:
                ospf_results.append({
                    "vendor": "Cisco",
                    "router_id": match_cis.group(1),
                    "state": match_cis.group(2)
                })
                continue
        except Exception as e:
            print(f"解析此行时发生错误：{line_str},错误信息：{e}")
    return ospf_results
if __name__ == "__main__":
    ospf_log = """
========================= [Device 1: Beijing-Core-H3C/Huawei VRP] ===================================

 VRP (R) Software, Version 8.130 (CE6800 V100R006C00)
 Copyright (C) 2012-2021 HUAWEI TECH CO., LTD.

                        OSPF Process 1 with Router ID 192.168.10.1
                               Neighbor Table

 Area 0.0.0.0 interface 10.1.1.1(Vlanif10)'s neighbors
 Router ID: 192.168.20.2      Address: 10.1.1.2        State: Full        Mode: Nbr is Master  Pri: 1
 Router ID: 192.168.30.3      Address: 10.1.1.3        State: 2-Way       Mode: Nbr is Slave   Pri: 1
 Router ID: 192.168.40.4      Address: 10.1.1.4        State: ExStart     Mode: -              Pri: 1

==================== [Device 2: Shanghai-Edge-Cisco IOS] =========================
Cisco IOS XE Software, Version 16.09.03
Neighbor ID     Pri   State           Dead Time   Address         Interface
10.20.20.2      1   FULL/BDR        00:00:32    172.16.1.2      GigabitEthernet0/0
10.30.30.3      1   2WAY/DROTHER    00:00:36    172.16.1.3      GigabitEthernet0/0
10.40.40.4      1   INIT/ -         00:00:38    172.16.1.4      GigabitEthernet0/0
"""
    parsed_data = parse_ospf_log(ospf_log)
    print("======= OSPF 邻居解析结果 =======")
    for item in parsed_data:
        print(f"厂商：{item['vendor']} | 邻居ID：{item['router_id']} | 状态：{item['state']}")