# Net-Audit-Parser（OSPF 邻居状态监控与资产自动化盘点 CLI 工具）

基于 Python 开发的轻量级、模块化网络运维自动化巡检工具，专为网络工程师设计，用于快速审计资产变更与解析多厂商 OSPF 状态。

## 核心功能
1、网络资产差异审计：基于 Pandas 进行数据清洗与去重，精准比对新旧表差异，自动输出新增与下线设备列表。
2、多厂商 OSPF 日志解析：结合正则提取（Regex），支持华为 (Huawei VRP) 与思科 (Cisco IOS) 的 OSPF 邻居状态变化解析。
3、交互式 CLI 架构：模块解耦，单点入口交互，具备完整的输入校验与异常捕获逻辑。

## 项目结构
```text
Net-Audit-Parser/
├── main.py              # CLI 交互主控入口
├── asset_processor.py   # Pandas 资产比对引擎
├── ospf_parser.py      # 多厂商 OSPF 正则解析引擎
├── old.csv / new.csv    # 资产审计测试数据集
└── README.md            # 项目说明文档

#克隆项目到本地
git clone https://github.com/LEE07-21/Net-Audit-Parser.git
cd Net-Audit-Parser
#安装依赖
pip install pandas
#运行工具
python main.py
