# py-armodel 项目指南

## 项目概述

py-armodel 是一个用于支持 AUTOSAR 模型的 Python 库。AUTOSAR（AUTomotive Open System ARchitecture）是汽车开放系统架构的标准，用于汽车电子控制单元（ECU）软件开发。

该项目提供了一个完整的 ARXML（AUTOSAR XML）文件解析器和写入器，支持多种 AUTOSAR 元素的解析和生成。它实现了 AUTOSAR 标准中定义的各种数据结构、接口、组件和通信模式。

## 主要功能

1. **ARXML 解析**: 支持解析 AUTOSAR XML 文件格式
2. **ARXML 生成**: 支持将 AUTOSAR 模型写入 XML 文件
3. **命令行工具**: 提供多种 CLI 工具用于处理 ARXML 文件
4. **数据模型**: 实现了完整的 AUTOSAR 数据模型（如组件、接口、数据类型等）
5. **连接器处理**: 支持软件连接器的导入导出到 Excel 文件

## 项目架构

```
src/armodel/
├── cli/                    # 命令行工具
├── data_models/            # 数据模型定义
├── lib/                    # 库函数
├── models/                 # AUTOSAR 模型定义
│   └── M2/               # M2 模型层 (MSR 和 AUTOSARTemplates)
├── parser/                 # 解析器实现
├── report/                 # 报告生成
├── transformer/            # 转换器
└── writer/                 # 写入器实现
```

### 核心模块

- **parser.arxml_parser**: 主要的 ARXML 解析器，基于 `AbstractARXMLParser`
- **models.M2.AUTOSARTemplates.AutosarTopLevelStructure**: 
  - `AUTOSAR` 类：单例模式的根对象
  - `AbstractAUTOSAR` 类：提供基础的 AUTOSAR 功能
- **writer.arxml_writer**: ARXML 文件写入器
- **models/**: 包含所有 AUTOSAR 数据模型类

## 主要特性

### 支持的 AUTOSAR 元素

- **组件类型**: 原子组件、组合组件、服务组件等
- **端口接口**: 发送接收接口、客户端服务器接口、模式切换接口
- **数据类型**: 应用数据类型、实现数据类型、记录和数组类型
- **通信**: 端口连接器、通信规范、网络管理
- **行为**: 运行实体、事件、内部行为
- **诊断**: 诊断连接、服务表、事件需求
- **系统**: 系统信号、系统映射、ECU 实例

### 命令行工具

- `arxml-dump`: 输出 ARXML 文件的所有数据
- `arxml-swc`: 列出所有软件组件类型
- `connector2xlsx`: 将连接器导出到 Excel 文件
- `connector-update`: 从 Excel 文件更新连接器
- `armodel-system-signal`: 列出所有系统信号
- `armodel-uuid-checker`: UUID 检查工具

## 构建和测试

### 构建

```bash
# 安装项目
pip install .

# 创建分发包
python setup.py sdist bdist_wheel --universal

# 检查分发包
twine check dist/*
```

### 测试

```bash
# 安装测试依赖
pip install pytest pytest-cov

# 运行测试
pytest --cov=armodel --cov-report term-missing

# 或使用 package.json 中的脚本
npm run pytest
npm run pytest-cov
```

### 文档生成

```bash
pip install sphinx
# 文档生成命令（具体命令在 README 中未详细说明）
```

## 开发约定

- **AUTOSAR 标准**: 项目遵循 AUTOSAR 标准，支持从 4.0.3 到 R24-11 等多个版本
- **代码结构**: 使用分层架构，模型层、解析层、写入层分离
- **单例模式**: `AUTOSAR` 类使用单例模式管理全局文档
- **UUID 管理**: 内置 UUID 管理器，支持重复 UUID 检查
- **类型映射**: 支持应用数据类型和实现数据类型之间的映射

## 版本历史

该项目从 0.1.1 版本发展到 1.8.6 版本，不断增加对 AUTOSAR 标准元素的支持，包括：

- 数据类型和接口的扩展
- 通信和网络管理功能
- 诊断功能
- 安全通信功能
- 系统建模功能
- BSW（基础软件）模块支持

## 依赖项

- **colorama**: 跨平台彩色终端输出
- **openpyxl**: Excel 文件处理
- **lxml**: XML 处理库

## 使用场景

1. **AUTOSAR 开发**: 用于 AUTOSAR 汽车软件开发
2. **模型分析**: 分析和处理 ARXML 文件
3. **数据转换**: 在不同格式间转换 AUTOSAR 模型
4. **工具开发**: 作为其他 AUTOSAR 工具的基础库