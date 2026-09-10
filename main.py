from asset_processor import process_assets
from ospf_parser import parse_ospf_log

def show_menu():
    """打印CLI主菜单"""
    print("\n" + "=" * 40)
    print("  OSPF邻居状态监控与资产自动化盘点CLI 工具  ")
    print("\n" + "=" * 40)
    print("1. 运行网络资产差异审计 (CSV 比对)")
    print("2. 运行多厂商 OSPF 邻居状态巡检")
    print("0. 退出系统")
    print("=" * 40)

def main():
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
    while True:
        show_menu()
        choice = input("请选择要执行的操作 (0-2): ").strip()

        if choice == "1":
            print("\n正在调取资产处理模块...")
            # 用 try/except 防御文件读取异常（第 6 课）
            try:
                # 调用 asset_processor.py 中的函数
                process_assets("old.csv", "new.csv")
            except Exception as e:
                print(f"资产处理失败，原因: {e}")

        elif choice == "2":
            print("\n正在启动多厂商 OSPF 巡检解析引擎...")
            results = parse_ospf_log(ospf_log)

            print("\n--- OSPF 巡检结果汇总 ---")
            for item in results:
                print(f"厂商: {item['vendor']:<8} | 邻居 IP: {item['router_id']:<15} | 状态: {item['state']}")

        elif choice == "0":
            print("\n感谢使用，系统已安全退出！")
            break  # 跳出循环，结束程序

        else:
            print("\n输入有误，请输入有效的选项 (0, 1, 2)！")


if __name__ == "__main__":
    main()