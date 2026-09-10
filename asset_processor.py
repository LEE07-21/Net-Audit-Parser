#import os
import pandas as pd
import csv
# current_dir = os.path.dirname(os.path.abspath(__file__))
# old_path = os.path.join(current_dir, "old.csv")
# new_path = os.path.join(current_dir, "new.csv")
# df_1 = pd.read_csv(old_path)
# df_2 = pd.read_csv(new_path)
def process_assets(old_csv, new_csv):
    """
    读取新旧资产CSV文件，比对差异并输出增删改状态报告
    """
    print(f"正在读取资产表：{old_csv} 和 {new_csv}...")
    df_1 = pd.read_csv(old_csv)
    df_2 = pd.read_csv(new_csv)

    print("====================old_dev====================")
    print(df_1)
    print("=" * 47)
    clean_df_1 = df_1.drop_duplicates(keep="first")
    if df_1.duplicated().any():
        print("\nold_dev有重复内容！查重后如下表：")
        print("=================clean_old_dev=================")
        print(clean_df_1)
        print("=" * 47)
    else:
        print("old_dev无重复内容！")

    print("\n====================new_dev=====================")
    print(df_2)
    print("=" * 47)
    clean_df_2 = df_2.drop_duplicates(keep="first")
    if df_2.duplicated().any():
        print("\nnew_dev有重复内容！查重后如下表：")
        print("=================clean_new_dev=================")
        print(clean_df_2)
        print("=" * 47)
    else:
        print("\nnew_dev无重复内容！")
    print("\n")
    old_dev_name = set(clean_df_1["device_name"])
    new_dev_name = set(clean_df_2["device_name"])
    print(f"旧设备：{old_dev_name}")
    print(f"新设备：{new_dev_name}")
    print("\n")
    added_dev = new_dev_name - old_dev_name
    removed_dev = old_dev_name - new_dev_name
    print(f"增加设备：{added_dev}")
    print(f"减少设备：{removed_dev}")
    print("\n")

if __name__ == "__main__":
    try:
        process_assets("old.csv", "new.csv")
    except Exception as e:
        print(f"测试运行失败，请检查CSV文件是否存在：{e}")

