# py-armodel 项目指南

## 项目概述

py-armodel 是一个用于支持 AUTOSAR 模型的 Python 库。AUTOSAR（AUTomotive Open System ARchitecture）是汽车开放系统架构的标准，用于汽车电子控制单元（ECU）软件开发。

该项目提供了一个完整的 ARXML（AUTOSAR XML）文件解析器和写入器，支持多种 AUTOSAR 元素的解析和生成。它实现了 AUTOSAR 标准中定义的各种数据结构、接口、组件和通信模式。

**当前版本**: 1.9.0  
**Python 要求**: >= 3.5  
**许可证**: MIT  
**仓库**: http://github.com/melodypapa/py-armodel

## 主要功能

1. **ARXML 解析**: 支持解析 AUTOSAR XML 文件格式
2. **ARXML 生成**: 支持将 AUTOSAR 模型写入 XML 文件
3. **命令行工具**: 提供多种 CLI 工具用于处理 ARXML 文件
4. **数据模型**: 实现了完整的 AUTOSAR 数据模型（如组件、接口、数据类型等）
5. **连接器处理**: 支持软件连接器的导入导出到 Excel 文件
6. **系统建模**: 支持系统信号、系统映射、ECU 实例
7. **诊断功能**: 支持诊断连接、服务表、事件需求
8. **通信协议**: 支持 CAN、LIN、FlexRay、Ethernet 等通信协议
9. **BSW 支持**: 完整的基础软件模块描述支持

## 项目架构

```
src/armodel/
├── cli/                    # 命令行工具
│   ├── arxml_dump_cli.py      # ARXML 数据转储
│   ├── arxml_format_cli.py    # ARXML 格式化
│   ├── connector2xlsx_cli.py  # 连接器导出到 Excel
│   ├── connector_update_cli.py # 从 Excel 更新连接器
│   ├── swc_list_cli.py        # 软件组件列表
│   ├── system_signal_cli.py   # 系统信号列表
│   ├── memory_section_cli.py  # 内存段管理
│   ├── file_list_cli.py       # 文件列表
│   ├── uuid_checker_cli.py    # UUID 检查器
│   └── format_xml_cli.py      # XML 格式化
├── data_models/            # 数据模型定义
│   └── sw_connector.py        # 软件连接器模型
├── lib/                    # 库函数
│   ├── cli_args_parser.py     # CLI 参数解析
│   ├── sw_component.py        # 软件组件工具
│   └── system_signal.py       # 系统信号工具
├── models/                 # AUTOSAR 模型定义
│   ├── M2/                    # M2 模型层
│   │   ├── AUTOSARTemplates/  # AUTOSAR 模板
│   │   │   ├── AutosarTopLevelStructure.py
│   │   │   ├── ECUCDescriptionTemplate.py
│   │   │   ├── ECUCParameterDefTemplate.py
│   │   │   ├── CommonStructure/    # 通用结构
│   │   │   ├── BswModuleTemplate/  # BSW 模块模板
│   │   │   ├── SWComponentTemplate/ # 软件组件模板
│   │   │   ├── SystemTemplate/     # 系统模板
│   │   │   ├── EcuResourceTemplate/ # ECU 资源模板
│   │   │   ├── GenericStructure/   # 通用结构
│   │   │   └── DiagnosticExtract/  # 诊断提取
│   │   └── MSR/                # MSR 元数据
│   └── utils/                 # 工具类
│       └── uuid_mgr.py         # UUID 管理器
├── parser/                 # 解析器实现
│   ├── arxml_parser.py          # ARXML 解析器
│   ├── abstract_arxml_parser.py # 抽象解析器基类
│   ├── connector_xlsx_parser.py # 连接器 Excel 解析器
│   ├── excel_parser.py          # Excel 解析器
│   └── file_parser.py           # 文件解析器
├── report/                 # 报告生成
│   ├── connector_xls_report.py  # 连接器 Excel 报告
│   └── excel_report.py          # Excel 报告
├── transformer/            # 转换器
│   ├── abstract.py              # 抽象转换器
│   └── admin_data.py            # 管理数据转换
└── writer/                 # 写入器实现
    ├── arxml_writer.py          # ARXML 写入器
    └── abstract_arxml_writer.py # 抽象写入器基类
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

#### 组件类型
- **原子组件**: ApplicationSwComponentType, SensorActuatorSwComponentType
- **组合组件**: CompositionSwComponentType
- **服务组件**: ServiceSwComponentType

#### 端口接口
- **发送接收接口**: SenderReceiverInterface
- **客户端服务器接口**: ClientServerInterface
- **模式切换接口**: ModeSwitchInterface
- **参数接口**: ParameterInterface
- **NV 数据接口**: NvDataInterface

#### 数据类型
- **应用数据类型**: ApplicationDataType, ApplicationArrayDataType
- **实现数据类型**: ImplementationDataType
- **基础类型**: BaseTypes
- **记录和数组类型**: ApplicationRecordElement, ApplicationArrayElement
- **计算方法**: CompuMethod
- **数据约束**: DataConstr
- **单位**: Unit

#### 通信
- **端口连接器**: AssemblySwConnector, DelegationSwConnector
- **通信规范**: ServerComSpec, ModeSwitchReceiverComSpec, NvProvideComSpec, NvRequireComSpec
- **网络管理**: NM-CONFIG, NM-NODE, NM-CLUSTER, CAN-NM-MODE, UDP-NM-CLUSTER
- **CAN 通信**: CAN-FRAME, CAN-COMMUNICATION-CONNECTOR, CAN-CONTROLLER
- **LIN 通信**: LIN-CLUSTER, LIN-UNCONDITIONAL-FRAME, LIN-MASTER, LIN-TP-CONFIG
- **FlexRay 通信**: FLEXRAY-CLUSTER, FLEXRAY-COMMUNICATION-CONNECTOR, FLEXRAY-FRAME
- **Ethernet 通信**: ETHERNET-COMMUNICATION-CONNECTOR, ETHERNET-PHYSICAL-CHANNEL, SO-AD-CONFIG
- **端到端保护**: EndToEndProtectionSet, EndToEndProtection

#### 行为
- **运行实体**: RunnableEntity
- **事件**: InitEvent, DataReceiveEvent, SwcModeSwitchEvent, BswBackgroundEvent, BswDataReceivedEvent
- **内部行为**: InternalBehavior, SwcInternalBehavior, BswInternalBehavior
- **实现**: SwcImplementation, BswImplementation

#### 诊断
- **诊断连接**: DiagnosticConnection
- **服务表**: DiagnosticServiceTable
- **事件需求**: DiagnosticEventNeeds, DiagnosticEventInfoNeeds
- **DCM 需求**: DiagnosticCommunicationManagerNeeds, DiagnosticRoutineNeeds, DiagnosticValueNeeds

#### 系统
- **系统信号**: SystemSignal, SystemSignalGroup
- **系统映射**: SWC-TO-ECU-MAPPING, SW-MAPPINGS
- **ECU 实例**: ECU-INSTANCE
- **根软件组合**: ROOT-SOFTWARE-COMPOSITIONS

#### BSW 模块
- **BSW 模块描述**: BswModuleDescription
- **BSW 行为**: BswBehavior
- **BSW 调度实体**: BswSchedulableEntity
- **BSW 调用实体**: BswCalledEntity

#### ECUC 配置
- **ECUC 集合**: EcucValueCollection
- **ECUC 模块配置**: EcucModuleConfigurationValues
- **ECUC 容器值**: EcucContainerValue
- **ECUC 参数值**: EcucParameterValue
- **ECUC 模块定义**: EcucModuleDef
- **ECUC 参数定义**: EcucParamDef (Boolean, String, Integer, Float, Enumeration)

### 命令行工具

#### arxml-dump
输出 ARXML 文件的所有数据到屏幕
```bash
arxml-dump --arxml <file1.arxml> --arxml <file2.arxml>
```

#### arxml-format
格式化 ARXML 文件
```bash
arxml-format <input.arxml> <output.arxml>
```

#### armodel-component
列出所有软件组件类型
```bash
armodel-component <arxml_folder>
armodel-component --format long --filter CompositionSwComponent <arxml_folder>
```

#### connector2xlsx
将连接器导出到 Excel 文件
```bash
connector2xlsx <input.arxml> <output.xlsx>
```

#### connector-update
从 Excel 文件更新连接器
```bash
connector-update <input.arxml> <excel_file.xlsx> <output.arxml>
```

#### armodel-system-signal
列出所有系统信号
```bash
armodel-system-signal <arxml_folder>
```

#### armodel-memory-section
管理内存段
```bash
armodel-memory-section <arxml_folder>
```

#### armodel-file-list
列出文件信息
```bash
armodel-file-list <arxml_folder>
```

#### armodel-uuid-checker
UUID 检查工具
```bash
armodel-uuid-checker <arxml_folder>
```

#### format-xml
格式化 XML 文件
```bash
format-xml <input.xml> <output.xml>
```

## 构建和测试

### 安装

```bash
# 从源码安装
pip install .

# 从 PyPI 安装
pip install armodel
```

### 构建

```bash
# 创建分发包
python setup.py sdist bdist_wheel --universal

# 检查分发包
twine check dist/*

# 上传到 PyPI
twine upload dist/*
```

### 测试

#### 测试结构

项目采用 pytest 进行单元测试，测试文件组织如下：

```
tests/
├── test_armodel/
│   ├── __init__.py
│   ├── cli/                    # CLI 工具测试
│   ├── models/                 # 模型类测试
│   │   ├── test_ar_object.py
│   │   ├── test_ar_package.py
│   │   ├── test_ar_ref.py
│   │   ├── test_bsw_module_template.py
│   │   ├── test_common_structure.py
│   │   ├── test_data_dictionary.py
│   │   ├── test_data_prototype.py
│   │   ├── test_datatype.py
│   │   ├── test_ECUCParameterDefTemplate.py
│   │   ├── test_general_structure.py
│   │   ├── test_Identifiable.py
│   │   ├── test_implementation.py
│   │   ├── test_m2_msr.py
│   │   ├── test_port_interface.py
│   │   └── test_port_prototype.py
│   └── parser/                 # 解析器测试
│       ├── test_arxml_parser.py
│       ├── test_bsw_module_descriiption.py
│       ├── test_implementation_data_type.py
│       ├── test_rte_event.py
│       ├── test_runnable_entity.py
│       ├── test_sw_components.py
│       └── test_system.py
├── requirements.txt            # 测试依赖
└── setup.cfg                  # pytest 配置
```

#### 运行测试

```bash
# 安装测试依赖
pip install pytest pytest-cov

# 运行所有测试
pytest

# 运行测试并生成覆盖率报告
pytest --cov=armodel --cov-report term-missing

# 运行特定测试文件
pytest tests/test_armodel/parser/test_arxml_parser.py

# 运行特定测试函数
pytest tests/test_armodel/parser/test_arxml_parser.py::test_parse

# 运行测试并显示详细输出
pytest -v

# 运行测试并显示 print 输出
pytest -s
```

#### 使用 package.json 脚本

```bash
# 运行测试
npm run pytest

# 运行测试并生成覆盖率报告
npm run pytest-cov

# 运行 flake8 代码检查
npm run flake8
```

#### 测试覆盖

测试覆盖以下主要功能：

- **ARXML 解析**: 各种 AUTOSAR 元素的解析
- **ARXML 写入**: 模型序列化为 ARXML
- **数据模型**: 所有 AUTOSAR 模型类
- **引用解析**: ARRef 引用解析和验证
- **类型系统**: 数据类型和类型映射
- **组件系统**: 软件组件类型和端口
- **行为系统**: 运行实体和事件
- **通信系统**: 连接器和通信规范
- **BSW 模块**: 基础软件模块描述
- **ECUC 配置**: ECUC 参数和容器

#### 编写测试

添加新测试时，请遵循以下规范：

1. 测试文件命名：`test_<module_name>.py`
2. 测试函数命名：`test_<functionality>`
3. 使用 pytest fixtures 进行测试设置
4. 包含正常情况和边界情况测试
5. 测试文件应放在对应的 `tests/test_armodel/` 子目录中

示例：

```python
import pytest
from armodel.parser.arxml_parser import ARXMLParser

def test_parse_simple_arxml():
    """测试简单的 ARXML 文件解析"""
    parser = ARXMLParser()
    model = parser.parse_from_file('test_files/simple.arxml')
    
    assert model is not None
    assert len(model.getARPackages()) > 0
```

#### 测试数据

测试使用 `test_files/` 目录中的 ARXML 文件作为测试数据：

```
test_files/
├── AUTOSAR_Datatypes.arxml
├── AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml
├── AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml
├── AUTOSAR_MOD_AISpecification_CompuMethod_Blueprint.arxml
├── AUTOSAR_MOD_AISpecification_DataConstr_Blueprint.arxml
├── AUTOSAR_MOD_AISpecification_PortInterface_Blueprint.arxml
├── AUTOSAR_MOD_AISpecification_SwComponentTypes_Blueprint.arxml
├── BswM_Bswmd.arxml
├── BswMMode.arxml
├── CanSystem.arxml
├── SoftwareComponents.arxml
└── SwRecordDemo.arxml
```

### 文档生成

项目支持两种文档生成方式：

#### Sphinx 文档

```bash
# 安装文档依赖
pip install -r docs/requirements.txt

# 生成 HTML 文档
cd docs
make html

# 清理文档
make clean

# 实时预览文档（需要安装 sphinx-autobuild）
pip install sphinx-autobuild
sphinx-autobuild . _build/html
```

#### MkDocs 文档

```bash
# 安装 MkDocs
pip install mkdocs

# 生成文档
mkdocs build

# 启动本地服务器预览
mkdocs serve
```

## 开发约定

- **AUTOSAR 标准**: 项目遵循 AUTOSAR 标准，支持从 4.0.3 到 R24-11 等多个版本
- **代码结构**: 使用分层架构，模型层、解析层、写入层分离
- **单例模式**: `AUTOSAR` 类使用单例模式管理全局文档
- **UUID 管理**: 内置 UUID 管理器，支持重复 UUID 检查
- **类型映射**: 支持应用数据类型和实现数据类型之间的映射
- **命名约定**: 遵循 Python PEP 8 编码规范
- **测试覆盖**: 使用 pytest 进行单元测试，要求高代码覆盖率
- **代码检查**: 使用 flake8 进行代码质量检查

## 依赖项

### 运行时依赖
- **colorama**: 跨平台彩色终端输出
- **openpyxl**: Excel 文件处理
- **lxml**: XML 处理库

### 开发依赖
- **pytest**: 单元测试框架
- **pytest-cov**: 代码覆盖率工具
- **flake8**: 代码风格检查工具
- **sphinx**: 文档生成工具
- **sphinx-rtd-theme**: Read the Docs 文档主题

## 持续集成

项目使用 GitHub Actions 进行持续集成，支持 Python 3.8、3.9、3.10、3.11 和 3.12 版本。

CI 流程包括：
1. 安装依赖
2. Lint 检查（flake8）
3. 运行测试（pytest）

配置文件位于 `.github/workflows/python-package.yml`。

## 使用场景

1. **AUTOSAR 开发**: 用于 AUTOSAR 汽车软件开发
2. **模型分析**: 分析和处理 ARXML 文件
3. **数据转换**: 在不同格式间转换 AUTOSAR 模型
4. **工具开发**: 作为其他 AUTOSAR 工具的基础库
5. **系统集成**: 支持系统级建模和配置
6. **诊断开发**: 支持诊断功能的开发和验证
7. **通信配置**: 支持多种通信协议的配置和管理

## 版本历史

### Version 1.9.0
- 当前稳定版本

### Version 1.8.7
- 修正 BswEvent 的基类
- 导出 RunnableEntity 类
- 为 getDestType 添加更多类支持

### Version 1.8.6
- 支持 NvProvideComSpec 和 NvRequireComSpec
- 改进 ParameterAccess

### Version 1.8.5
- 重新组织 SwConnector 类
- 如果 rootSwCompositionPrototype 的短名称无效则抛出错误
- 支持 NvProvideComSpec
- 修复 ARPackage 和其他 ARElements 的重复短名称问题

### Version 1.8.4
- 支持 BSW-SYNCHRONOUS-SERVER-CALL-POINT 和 RETURN-TYPE
- 添加 armodel-uuid-checker CLI 工具
- 移除布尔类型中的空格

### Version 1.8.3
- 支持 VALUE 的 SHORT-LABEL
- 支持 MAX-DELTA-COUNTER-INIT, MAX-NO-NEW-OR-REPEATED-DATA, USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS, MASK

### Version 1.8.2
- 修复 AUTOSAR XML schema 问题

### Version 1.8.1
- 支持 MODE-DECLARATION-MAPPING-SET, MODE-INTERFACE-MAPPING
- 支持 ECUC 模块定义和参数定义
- 支持相同短名称但不同类型的元素添加和定位

### Version 1.8.0
- 支持 DLT-USER-NEEDS
- 改进 UUID 检查
- 改进 AbstractAUTOSAR 的 find 方法以支持 dest 验证
- 添加 findXXX 方法（findAtomicSwComponentType, findSystemSignal 等）

### Version 1.7.9
- 改进 BSW-MODULE-DESCRIPTION, BSW-INTERNAL-BEHAVIOR, LIFE-CYCLE-INFO-SET, PHYSICAL-DIMENSION
- 支持 ACTIVATION-POINTS, CALL-POINTS, LIFE-CYCLE-INFO, COLLECTION, KEYWORD-SET, FIGURE
- 添加 API 设置 AUTOSAR 发布版本

### Version 1.7.8
- 支持静态内存、接收策略、FlexRay 通信等
- 改进多个 AR 元素
- 启用 Flake8 代码检查
- 添加 CompositionSwComponentType 支持
- 添加重复 UUID 检查

### Version 1.7.0 - 1.7.7
- 持续添加对系统建模、通信协议、诊断功能的支持
- 支持 CAN、LIN、Ethernet、FlexRay 等通信协议
- 支持诊断连接、服务表、事件需求
- 支持端到端保护
- 支持安全通信

### Version 1.4.0 - 1.6.0
- 添加 ARXML 写入功能
- 支持更多 AUTOSAR 元素
- 添加系统信号列表 CLI 工具
- 支持 ECUC 配置

### Version 1.0.0 - 1.3.0
- 添加日志支持
- 添加 BswMD 支持
- 添加事件支持（InitEvent, DataReceiveEvent, SwcModeSwitchEvent）
- 添加 SwcImplementation 支持
- 支持 DelegationSwConnector

### Version 0.1.1 - 0.1.3
- 初始版本
- 支持 ARRAY 类型的 ImplementationDataType
- 支持 AsynchronousServerCallPoint
- 修复 Limit 的 intervalType 属性问题

## 参考

- [AUTOSAR 官方网站](https://www.autosar.org/)
- [项目 GitHub 仓库](http://github.com/melodypapa/py-armodel)
- [PyPI 包页面](https://pypi.org/project/armodel/)
- [在线文档](https://py-armodel.readthedocs.io/)
- [GitHub Actions](https://github.com/melodypapa/py-armodel/actions)
- [覆盖率报告](https://coveralls.io/github/melodypapa/py-armodel)

## Prompts

help me create one python script to extract the attributes of classes in
   @autosar/AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate/AUTOSAR_CP_TPS_BSWModuleDescriptionT
   emplate_part_05.pdf  and update the file @docs/autosar/bsw_module_description_template.md 

convert the type comments to variable declarations of all the class in @ and add the comments for each class

add the comments for the class in @.

valdate the changes with flake8 and pytest.

increase the test coverage for the @ to 100% and add the comments for each tests file.

change the @tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate folder structure same as @src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate folder structure. 