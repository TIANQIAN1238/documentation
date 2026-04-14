---
id: glossary
title: Glossary
description: The following terms have specific definitions within the context of the Temporal Platform.
sidebar_label: Glossary
sidebar_position: 13
toc_max_heading_level: 4
tags:
  - Reference
---

The following terms are used in [Temporal Platform](/Temporal) documentation.

#### [Action](/cloud/pricing#action)

An Action is the fundamental pricing unit in Temporal Cloud. Temporal Actions are the building blocks for Workflow
Executions. When you execute a Temporal Workflow, its Actions create the ongoing state and progress of your Temporal
Application.

<!-- _Tags: [term](/tags/term), [pricing](/tags/pricing), [Temporal-cloud](/tags/Temporal-cloud), [explanation](/tags/explanation)_ -->

#### [Actions Per Second (APS)](/cloud/limits#actions-per-second)

APS, or Actions per second, is specific to Temporal Cloud. Each Temporal Cloud Namespace enforces a rate limit, which is
measured in Actions per second (APS). This is the number of Actions, such as starting or Signaling a Workflow, that can
be performed per second within a specific Namespace.

<!-- _Tags: [term](/tags/term), [pricing](/tags/pricing), [Temporal-cloud](/tags/Temporal-cloud), [explanation](/tags/explanation)_ -->

#### [Activity](/activities)

In day-to-day conversation, the term "Activity" denotes an Activity Type, Activity Definition, or Activity Execution.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Activity Definition](/Activity-definition)

An Activity Definition is the code that defines the constraints of an Activity Task Execution.

<!-- _Tags: [term](/tags/term), [explanation](/tags/explanation)_ -->

#### [Activity 执行](/Activity-执行)

Activity 执行是 Activity 任务执行的完整链。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Activity 心跳](/百科/检测-Activity-故障#Activity-心跳)

Activity 心跳是从执行 Activity 的 Worker 到 Temporal 服务的 ping。

每次 ping 都会通知 Temporal 服务 Activity 执行正在进行，并且 Worker 尚未崩溃。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Activity ID](/Activity-执行#Activity-id)

Activity 执行的唯一标识符。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Activity 任务](/tasks#Activity-任务)

Activity 任务包含执行 Activity 任务所需的上下文。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Activity 任务执行](/tasks#Activity-任务-执行)

当 Worker 使用 Activity 任务提供的上下文并执行
Activity Definition。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Activity 类型](/Activity-定义#Activity-类型)

Activity 类型是名称到 Activity Definition 的映射。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [存档](/Temporal-服务/存档)

存档是一项特定于自托管 Temporal 服务的功能，可自动备份以下位置的事件历史记录：
达到关闭的 Workflow Execution 保留期后，Temporal 服务将持久保留到自定义 Blob 存储。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [异步 Activity 完成](/Activity-执行#异步-Activity-完成)

当外部系统提供计算的最终结果时，就会发生异步 Activity 完成，该计算由
Activity 到 Temporal 系统。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [审核日志记录](/cloud/audit-logs)

审核日志记录是一项为帐户、用户和 Namespace 提供取证访问信息的功能。

<!-- _标签：[术语](/tags/term)、[解释](/tags/explanation)、[Temporal-cloud](/tags/Temporal-cloud)、[操作](/tags/operations)_ -->

#### [授权者插件](/self-hosted-guide/security#authorizer-plugin)

“Authorizer”插件包含一个“Authorize”方法，每个传入的 API 调用都会调用该方法。 `授权`
接收有关 API 调用的信息，以及调用者的角色和权限声明。

<!-- _标签: [术语](/标签/术语)_ -->

#### [可用区](/cloud/high-availability)

可用区是 Temporal 系统的一部分，在其中处理和执行任务或操作。这个设计
帮助管理工作负载并确保任务完成。 Temporal Cloud Namespace 自动分布在
三个可用区，提供我们的云 [SLA](/cloud/sla) 中概述的 99.9% 正常运行时间。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Child Workflow](/child-Workflows)

子 Workflow Execution 是从另一个 Workflow 中生成的 Workflow Execution。

<!-- _标签：[术语](/tags/term)、[解释](/tags/explanation)、[child-Workflow](/tags/child-Workflow)_ -->

#### [声明映射器](/self-hosted-guide/security#claim-mapper)

Claim Mapper 组件是一个可插入组件，用于从 JSON Web 令牌 (JWT) 中提取声明。

<!-- _标签: [术语](/标签/术语)_ -->

#### [Codec Server](/编解码器服务器)

Codec Server 是一个 HTTP 服务器，它使用您的自定义有效负载编解码器通过以下方式远程编码和解码您的数据：
端点。

<!-- _标签: [术语](/标签/术语)_ -->

#### [命令](/Workflow-执行#命令)

命令是 Workflow Task 执行完成后由 Worker 向 Temporal 服务发出的请求操作。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Continue-As-New](/Workflow-执行/Continue-As-New)

Continue-As-New 是一种机制，通过该机制，所有相关状态都会通过新事件传递到新的 Workflow Execution
历史。

<!-- _Tags: [术语](/tags/term), [解释](/tags/explanation), [Continue-As-New](/tags/Continue-As-New)_ -->

#### [核心 SDK](https://Temporal.io/blog/why-rust-powers-core-sdk)

Core SDK 是多个 Temporal SDK 使用的共享通用核心库。 Core SDK 用 Rust 编写，提供
复杂的并发管理和状态机逻辑是其突出的功能之一。集中开发使
核心 SDK 支持将新功能快速可靠地部署到现有 SDK，并更轻松地添加新 SDK
Temporal 生态系统的语言。

<!-- _Tags: [术语](/tags/term), [解释](/tags/explanation), [Continue-As-New](/tags/Continue-As-New)_ -->

#### [自定义 Data Converter](/default-custom-data-converters#custom-data-converter)

自定义 Data Converter 通过用于有效负载转换或有效负载的自定义逻辑扩展了默认 Data Converter
加密。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Data Converter](/数据转换)

Data Converter 是 Temporal SDK 组件，可对进入和退出 Temporal 服务的数据进行序列化和编码。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [默认 Data Converter](/default-custom-data-converters#default-data-converter)

Temporal SDK默认使用Data Converter，使用一系列Payload将对象转换为字节
转换器。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [延迟 Workflow Execution](/Workflow-执行/Timers-延迟)

启动延迟决定启动 Workflow Execution 之前等待的时间量。如果 Workflow 收到
Signal-With-Start 或 Update-With-Start 延迟期间，调度 Workflow Task，剩余延迟为
绕过了。

<!-- _标签: [术语](/tags/term), [解释](/tags/explanation), [delay-Workflow](/tags/delay-Workflow)_ -->

#### [双 Visibility](/双-Visibility)

双 Visibility 是一项特定于自托管 Temporal 服务的功能，可让您设置辅助 Visibility 存储
在您的 Temporal 服务中，以方便将您的 Visibility 数据从一个数据库迁移到另一个数据库。

<!-- _Tags: [术语](/tags/term)、[解释](/tags/explanation)、[过滤列表](/tags/filtered-lists)、[Visibility](/tags/Visibility)_ -->

#### [持久执行](/Temporal#durable-execution)

Temporal 上下文中的持久执行是指 Workflow Execution 维持其状态和
即使面对故障、崩溃或服务器中断也能取得进展。

<!-- _Tags: [Temporal](/tags/Temporal), [持久执行](/tags/durable-execution), [term](/tags/term)_ -->

#### [动态处理程序](/动态处理程序)

动态处理程序是未命名的 Workflow、活动、Signal 或查询，在没有其他命名处理程序时调用
匹配运行时来自服务器的调用。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [事件](/Workflow-执行/事件#事件)

事件由 Temporal 服务创建，以响应外部事件和 Workflow 生成的命令
执行。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Event History](/Workflow-执行/事件#事件历史记录)

如果您的 XPROT019X 需要身份验证，XPROT017X 还将接受 `--codec-auth` 参数来提供
授权标头：

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [故障回复](/cloud/high-availability)

Temporal Cloud 解决了涉及故障转移的中断或事件后，故障回复过程将转移到 Workflow
执行处理返回到事件发生前处于活动状态的原始区域。

#### [故障转移](/cloud/high-availability)

故障转移将 Workflow Execution 处理从活动 Temporal Namespace 区域转移到备用 Temporal Namespace
停电或其他事件期间的区域。备用Namespace区域使用复制来复制数据并防止数据丢失
故障转移期间的损失。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [失败](/Temporal#failure)

Temporal 故障代表系统中发生的各种类型的错误。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [故障转换器](/failure-converter)

此错误表示 [XPROT013X](/tasks#XPROT027X-task) 由于未设置 [CompleteXPROT027XExecution](/references/commands#completeXPROT027Xexecution) 上的属性而失败。

重置任何缺失的属性。
如果负载超过大小限制，请调整负载的大小。

#### [失败](/参考/失败)

故障是 Temporal 系统中发生的各种类型错误的表示。

<!-- _Tags: [失败](/tags/failure), [解释](/tags/explanation), [term](/tags/term)_ -->

#### [前端服务](/Temporal-service/Temporal-server#frontend-service)

前端服务是一种无状态网关服务，它公开强类型的 Proto API。前端服务是
负责速率限制、授权、验证和路由所有入站呼叫。

<!-- _标签: [术语](/标签/术语)_ -->

#### [一般可用性](/evaluate/development-product-features/release-stages#general-availability)

了解有关正式发布阶段的更多信息

<!-- _Tags: [产品发布阶段](/tags/产品发布阶段), [术语](/标签/术语)_ -->

#### [全局 Namespace](/global-Namespace)

全局 Namespace 是将数据从活动 [Temporal 服务](#Temporal-cluster) 复制到备用服务器的 Namespace
使用复制来保持两个 Namespace 同步的服务。 Global Namespace 旨在响应服务
网络拥塞等问题。当主集群的服务受到损害时，[故障转移]（#failover）将转移
控制从主集群到备用集群。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [心跳超时](/百科全书/检测-Activity-failures#heartbeat-timeout)

心跳超时是 Activity 心跳之间的最长时间。

<!-- _Tags: [术语](/tags/term), [解释](/tags/explanation), [超时](/tags/timeouts)_ -->

#### [高可用性](/cloud/high-availability/)

高可用性可确保系统保持正常运行并最大限度地减少停机时间。它通过冗余和
处理故障的故障转移机制，因此最终用户不会意识到发生的事件。 Temporal Cloud 保证了这一高
其服务级别协议 ([SLA](/cloud/sla)) 的可用性

<!-- _Tags: [术语](/tags/term), [解释](/tags/explanation), [超时](/tags/timeouts)_ -->

#### [高可用性功能](/cloud/high-availability#high-availability-features)

高可用性功能会自动同步主 Namespace 及其副本之间的数据，从而保留它们
同步。如果发生事故或中断，Temporal 会自动将您的 Namespace 从主故障转移到
复制品。这支持高水平的业务连续性，允许 Workflow Execution 以最小的成本继续运行
中断或数据丢失。

<!-- _Tags: [术语](/tags/term), [解释](/tags/explanation), [超时](/tags/timeouts)_ -->

#### [历史服务](/Temporal-service/Temporal-server#history-service)

历史服务负责保存 Workflow Execution 状态并确定下一步要做什么
Workflow Execution 通过历史碎片。

<!-- _标签: [术语](/标签/术语)_ -->

#### [历史碎片](/Temporal-service/Temporal-server#history-shard)

历史分片是 Temporal 服务中的一个重要单元，通过它可以控制并发 Workflow Execution 的规模
可以测量吞吐量。

<!-- _标签: [术语](/标签/术语)_ -->

#### [幂等性](/Activity-definition#幂等性)

“幂等”方法可避免流程重复，避免重复提款或错误运送额外订单。
幂等性可防止操作产生额外影响，从而保护您的流程免受意外或重复的影响
行动，以实现更可靠的执行。将您的活动设计为一次且仅一次成功。运行一次操作保持
数据完整性并防止代价高昂的错误。

<!-- _标签: [术语](/标签/术语)_ -->

#### [隔离域](/cloud/high-availability)

隔离域是 Temporal Cloud 基础设施内的定义区域。它有助于遏制故障并防止
它们防止扩散到系统的其他部分，从而提供冗余和容错。

<!-- _标签: [术语](/标签/术语)_ -->

#### [列表过滤器](/list-filter)

列表过滤器是类似 SQL 的字符串，作为高级 Visibility 列表 API 的参数提供。

<!-- _Tags: [术语](/tags/term)、[解释](/tags/explanation)、[过滤列表](/tags/filtered-lists)、[Visibility](/tags/Visibility)_ -->

#### [本地 Activity](/local-Activity)

本地 Activity 是 Activity 执行，与生成它的 Workflow Execution 在同一进程中执行。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [匹配服务](/Temporal-service/Temporal-server#matching-service)

匹配服务负责托管外部 Task Queue 以进行任务调度。

<!-- _标签: [术语](/标签/术语)_ -->

#### [备忘录](/Workflow-执行#memo)

备忘录是一组非索引的用户提供的 Workflow Execution 元数据，当您描述或列出时返回
Workflow Executions。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [多集群复制](/self-hosted-guide/multi-cluster-replication)

多集群复制是一种将 Workflow Execution 从活动集群异步复制到其他集群的功能
被动集群，用于备份和状态重建。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [多云复制](/cloud/high-availability/enable)

多云复制将 Workflow 和元数据复制到不同的云提供商（AWS 或 GCP）。这是
对于出于合规目的而需要跨区域高度可用的组织尤其有利。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [多区域复制](/cloud/high-availability/enable)

多区域复制将 Workflow 和元数据复制到与主区域不在同一位置的不同区域
Namespace。这对于具有多区域架构或需要进行多区域架构的组织特别有利
出于合规目的，跨区域高度可用。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Namespace](/Namespaces)

Namespace 是 Temporal Platform 内的一个隔离单元。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### Nexus 异步完成回调

Nexus 异步完成回调是异步 Nexus Operation 的完成回调。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### Nexus 端点

Nexus 端点是一种反向代理，可以为一个或多个 Nexus Service 提供服务。它将 Nexus 请求路由到目标
Namespace 和 Task Queue，Nexus Worker 正在轮询。这使得服务提供商能够提供干净的服务
收缩并隐藏底层实现，该实现可能由许多内部 Workflow 组成。多个 Nexus 端点
可以针对相同的 Namespace。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### Nexus 机械

Temporal 内置 Nexus 机制，以保证基于状态机的 Nexus Operation 至少执行一次
调用和完成回调。 Nexus 机械使用 [Nexus RPC](/glossary#Nexus-rpc)，这是一种设计为
牢记持久执行，跨 Namespace 边界进行通信。调用者 Workflow 和 Nexus 处理程序不必
直接使用 Nexus RPC，因为 Temporal SDK 提供了简化的开发人员构建、运行和使用 Nexus 的体验
服务。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### Nexus Operation

任意持续时间的操作，可以是同步或异步、短期或长期的，用于连接
Namespace、集群、区域和云内部和之间的持久执行。与传统的 RPC 不同，
异步 Nexus Operation 有一个操作令牌，可用于重新连接到长期存在的 Nexus Operation，例如
例如，由 Temporal Workflow 支持的一个。 Nexus Operations 支持统一的接口来获取设备的状态
操作或其结果、接收完成回调或取消操作 - 所有这些都完全集成到
Temporal Platform。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

## XPROT027X取消禁用

Nexus Operations 事件是调用者 Workflow 中出现的历史事件，用于指示操作的状态
包括“Nexus Operation Scheduled”、“Nexus Operation 已开始”、“Nexus Operation 已完成”。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### Nexus Operation 处理程序

Temporal Worker 中的 Nexus 处理程序代码通常使用 Temporal SDK 构建器函数创建，可以轻松
抽象 Temporal 原语并公开一个干净的服务契约供其他人使用。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### Nexus 注册表

Nexus 注册表管理 Nexus 端点并提供查找服务以在运行时解析 Nexus 请求。在
Temporal 的开源版本中，注册表的范围仅限于集群，而在 Temporal Cloud 中，注册表的范围仅限于
帐户。端点名称在注册表中必须是唯一的。当 Temporal 服务调度 Nexus 请求时，它
通过注册表将请求的端点解析为 Namespace 和 Task Queue。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Nexus RPC](https://github.com/Nexus-rpc/api/blob/main/SPEC.md)

Nexus RPC 是一种以持久执行为设计理念的协议。它支持任意持续时间的操作，可扩展
超越传统的 RPC — 连接 Namespace、集群内部和跨 Namespace 的持久执行的关键基础
区域和云边界。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### Nexus Service

Nexus Service 是任意持续时间的 Nexus Operation 的命名集合，提供微服务合约
适合跨团队和应用程序边界共享。 Nexus Service 已注册到 Temporal Worker，
正在轮询 Nexus 端点的目标 Namespace 和 Task Queue。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### Nexus Service 合约

调用者可用来获取服务和操作名称的通用代码包、架构或文档
服务将为给定操作接受的关联输入/输出类型。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [父关闭策略](/parent-close-policy)

如果 Workflow Execution 是子 Workflow Execution，则父关闭策略决定 Workflow 会发生什么情况
如果其父 Workflow Execution 更改为关闭状态（已完成、失败、超时），则执行。

<!-- _标签：[术语](/tags/term)、[解释](/tags/explanation)、[child-Workflow-executions](/tags/child-Workflow-executions)_ -->

#### [有效负载](/dataconversion#有效负载)

有效负载表示二进制数据，例如活动和 Workflow 的输入和输出。

<!-- _Tags: [term](/tags/term), [payloads](/tags/payloads), [explanation](/tags/explanation)_ -->

#### [有效负载编解码器](/有效负载编解码器)

有效负载编解码器将一组有效负载转换为另一个有效负载数组。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [有效负载转换器](/有效负载转换器)

有效负载转换器序列化数据，将对象或值转换为字节并返回。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [预发布](/评估/开发-生产-功能/发布-阶段#预发布)

了解有关预发布阶段的更多信息

<!-- _Tags: [产品发布阶段](/tags/产品发布阶段), [术语](/标签/术语)_ -->

#### [公开预览](/evaluate/development-product-features/release-stages#public-preview)

了解有关公共预览版发布阶段的更多信息

<!-- _Tags: [产品发布阶段](/tags/产品发布阶段), [术语](/标签/术语)_ -->

#### [Query](/发送消息#发送查询)

Query 是一种同步操作，用于报告 Workflow Execution 的状态。

<!-- _Tags: [术语](/tags/term), [查询](/tags/queries), [解释](/tags/explanation)_ -->

#### [远程数据编码](/remote-data-encoding)

远程数据编码是使用您的自定义 Data Converter 通过以下方式远程解码（和编码）您的有效负载
端点。

<!-- _Tags: [术语](/tags/term), [查询](/tags/queries), [解释](/tags/explanation)_ -->

#### [复制延迟](/cloud/metrics/openmetrics/metrics-reference#Temporal_cloud_v1_replication_lag_p99)

Workflow Update 和历史事件从主用区域到备用区域的传输延迟。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [每秒请求数 (RPS)](/references/dynamic-configuration#service-level-rps-limits)

RPS（即每秒请求数）用于 Temporal 服务（在自托管 Temporal 和 Temporal Cloud 中）。这是
控制服务级别请求速率的措施，例如前端、历史记录或匹配服务。

<!-- _Tags: [术语](/tags/term), [解释](/tags/explanation), [Temporal](/tags/Temporal)_ -->

#### [重置](/Workflow-执行/事件#重置)

重置会终止 Workflow Execution，删除 Event History 中直至重置点的进度，然后
使用相同的 Workflow Type 和 ID 创建一个新的 Workflow Execution 以继续。

<!-- _Tags: [术语](/tags/term), [重置](/tags/resets), [解释](/tags/explanation)_ -->

#### [保留期](/Temporal-service/Temporal-server#retention-period)

保留期是 Workflow Execution Event History 在 Temporal 服务中保留的时间量
持久性存储。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Retry Policy](/百科全书/重试策略)

Retry Policy 是指示 Temporal Server 如何重试 Workflow 故障的属性集合
执行或 Activity 任务执行。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [运行 ID](/Workflow-执行/Workflowid-runid#run-id)

运行 ID 是 Workflow Execution 的全球唯一平台级标识符。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [同域复制](/cloud/high-availability/enable)

同一区域复制将 Workflow 和元数据复制到与主服务器位于同一区域内的隔离域
Namespace。它提供了可靠的故障转移机制，同时保持部署简单性。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Schedule](/Schedule)

Schedule 可以对 Workflow Execution 进行调度。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Schedule-关闭超时](/百科全书/检测-Activity-failures#Schedule-关闭超时)

Schedule 关闭超时是整个 Activity 执行所允许的最长时间，从
第一个 Activity 任务是 Scheduled 到最后一个 Activity 任务，在组成 Activity 任务的链中
Activity 执行，达到关闭状态。

<!-- _Tags: [术语](/tags/term), [解释](/tags/explanation), [超时](/tags/timeouts)_ -->

#### [Schedule-启动超时](/百科全书/检测-Activity-失败#Schedule-启动超时)

Schedule 启动超时是从 Activity 任务被放置到任务中开始允许的最大时间量
排队等待 Worker 从 Task Queue 拾取它。

<!-- _Tags: [术语](/tags/term), [解释](/tags/explanation), [超时](/tags/timeouts)_ -->

#### [Search Attribute](/搜索属性)

Search Attribute 是列表过滤器中使用的索引名称，用于过滤具有搜索的 Workflow Execution 列表
元数据中的属性。

<!-- _Tags: [术语](/tags/term)、[解释](/tags/explanation)、[过滤列表](/tags/filtered-lists)、[Visibility](/tags/Visibility)_ -->

#### [Side Effect](/Workflow-执行/事件#副作用)

Side Effect 是一种执行简短的、非确定性代码片段的方法，例如生成 UUID，该代码片段执行
提供一次函数并将其结果记录到 Workflow Execution Event History 中。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Signal](/发送消息#sending-Signals)

Signal 是对 Workflow Execution 的异步请求。

<!-- _Tags: [术语](/tags/term), [Signals](/tags/Signals), [解释](/tags/explanation)_ -->

#### [Signal-With-Start](/发送消息#Signal-with-start)

Signal-With-Start 启动，Signal 会成为 Workflow Execution，或者如果 Signal 已存在，则仅 Signal 会成为 Workflow Execution。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [启动到关闭超时](/encyclopedia/Detecting-Activity-failures#start-to-close-timeout)

开始到关闭超时是单个 Activity 任务执行所允许的最长时间。

<!-- _Tags: [术语](/tags/term), [解释](/tags/explanation), [超时](/tags/timeouts)_ -->

#### [状态转换](/Workflow-execution#state-transition)

状态转换是 Workflow Execution 的进度单位。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [粘性执行](/粘性执行)

粘性执行是指当 Worker 实体缓存 Workflow Execution Event History 并创建专用任务时
排队收听。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [任务](/任务#任务)

任务是特定 Workflow Execution 或 Activity 执行取得进展所需的上下文。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Task Queue](/任务队列)

Task Queue 是 Worker 进程轮询任务的先进先出队列。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [任务路由](/任务路由)

任务路由是指 Task Queue 与一个或多个 Worker 进程配对，主要用于 Activity 任务执行。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [任务令牌](/Activity-execution#task-token)

任务令牌是 Activity 任务执行的唯一标识符。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal](/Temporal)

Temporal 是可重入进程的可扩展且可靠的运行时，称为 Temporal Workflow Execution。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal 应用程序](/Temporal#Temporal-应用程序)

Temporal 应用程序是一组 Workflow Execution。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal CLI](/cli) {#cli}

Temporal CLI 是 Temporal 命令行工具的最新版本。

<!-- _标签: [term](/tags/term), [cli](/tags/cli)_ -->

#### [Temporal CLIent](/百科全书/Temporal-sdks#Temporal-client)

Temporal CLIent 由 Temporal SDK 提供，提供一组 API 来与 Temporal 服务进行通信。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal Cloud](/云/概述)

Temporal Cloud 是托管的 Temporal 环境，为 Temporal 应用程序提供平台。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal Cloud 帐户 ID](/cloud/Namespaces#Temporal-cloud-account-id)

Temporal Cloud 帐户 ID 是客户的唯一标识符。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal Cloud Namespace ID](/cloud/Namespaces#Temporal-cloud-Namespace-id)

Cloud Namespace Id 是 Temporal Cloud 中 Namespace 的全局唯一标识符。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal Cloud Namespace 名称](/cloud/Namespaces#Temporal-cloud-Namespace-名称)

云 Namespace 名称是客户为 Temporal Cloud 中的 Namespace 提供的名称。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal Cloud gRPC 端点](/cloud/Namespaces#Temporal-cloud-gRPC-端点)

云 gRPC 端点是 Namespace 特定的地址，用于从代码访问 Temporal Cloud。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal 集群](/Temporal-服务)

术语“Temporal Cluster”正在逐步淘汰。相反，术语 [Temporal 服务](#Temporal-service) 现在被
使用过。

#### [Temporal 服务](/Temporal-服务)

Temporal 服务是与持久性和 Visibility 存储配对的 Temporal Server。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal 服务配置](/Temporal-service/configuration)

Temporal 服务配置是 Temporal 服务的设置和配置详细信息，使用 YAML 定义。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal 计划任务](/cron-job)

Temporal Cron 作业是在调用中提供 Cron Schedule 时发生的一系列 Workflow Execution
生成 Workflow Execution。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal Platform](/Temporal#Temporal-平台)

Temporal Platform 由 Temporal 服务和 Worker 进程组成。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal SDK](/百科/Temporal-sdks)

Temporal SDK 是一个特定于语言的库，提供 API 来构建和使用 Temporal CLIent 进行通信
使用 Temporal 服务、开发 Workflow Definition 并开发 Worker 程序。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal Server](/Temporal-服务/Temporal-服务器)

Temporal Server 是四个水平可扩展服务的组合。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Temporal Web UI](/web-ui)

Temporal Web UI 为用户提供 Workflow Execution 状态和元数据以用于调试目的。

<!-- _标签: [term](/tags/term), [web-ui](/tags/web-ui)_ -->

#### [Timer](/Workflow-执行/Timers-延迟)

Temporal SDK 提供 Timer API，以便 Workflow Execution 在处理时间值时具有确定性。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Update](/发送消息#sending-Updates)

Update 是对 Workflow Execution 的请求和来自 Workflow Execution 的响应。

<!-- _Tags: [术语](/tags/term), [Updates](/tags/Updates), [解释](/tags/explanation)_ -->

#### [Visibility](/Temporal-服务/Visibility)

Temporal Platform 中的术语 Visibility 是指使操作员能够查看
当前存在于 Temporal 服务中的 Workflow Execution。

<!-- _标签: [术语](/标签/术语)_ -->

#### [Worker](/Workers#Worker)

在日常对话中，术语 Worker 用于表示 Worker 程序和 Worker 进程。 Temporal
文档的目的是明确并区分它们。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Worker 实体](/Workers#Worker-实体)

Worker 实体是 Worker 进程中侦听特定 Task Queue 的单个 Worker。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Worker 进程](/Workers#Worker-进程)

Worker 进程负责轮询 Task Queue、使任务出列、执行代码以响应任务，
并将结果响应 Temporal Server。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Worker 程序](/Workers#Worker-程序)

Worker 程序是定义 Worker 进程约束的静态代码，使用 API 开发
Temporal SDK。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Worker 服务](/Temporal-服务/Temporal-服务器#Worker-服务)

Worker 服务对复制队列、系统 Workflow 和（早于
1.5.0) Kafka Visibility 处理器。

<!-- _标签: [术语](/标签/术语)_ -->

#### [Worker 会话](/任务路由#Worker-会话)

Worker 会话是某些 SDK 提供的一项功能，它提供了一种简单的方法来确保 Activity 任务
使用相同的 Worker 执行，无需您手动指定 Task Queue 名称。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Workflow](/Workflows)

在日常对话中，术语“Workflow”经常表示 Workflow Type、Workflow Definition 或 Workflow Definition。
Workflow Execution。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Workflow Definition](/Workflow-定义)

Workflow Definition 是定义 Workflow Execution 约束的代码。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Workflow Execution](/Workflow-执行)

Temporal Workflow Execution 是一款耐用、可扩展、可靠且反应式的功能执行器。它的主要单位是
Temporal 应用程序的执行。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Workflow Execution 超时](/百科全书/检测-Workflow-失败#Workflow-执行超时)

Workflow Execution 超时是 Workflow Execution 可以执行的最长时间（具有打开状态）
包括重试和任何“继续作为新”的使用。

<!-- _Tags: [术语](/tags/term), [解释](/tags/explanation), [超时](/tags/timeouts)_ -->

#### [Workflow 历史导出](/cloud/export)

Workflow 历史记录导出允许用户将关闭的 Workflow 历史记录导出到用户的云存储接收器。

<!-- _标签：[术语](/tags/term)、[解释](/tags/explanation)、[Temporal-cloud](/tags/Temporal-cloud)、[操作](/tags/operations)_ -->

#### [Workflow Id](/Workflow-执行/Workflowid-runid#Workflow-id)

Workflow Id 是 Workflow Execution 的可定制应用程序级标识符，对于 Open
Namespace 内的 Workflow Execution。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Workflow Id 冲突策略](/Workflow-execution/Workflowid-runid#Workflow-id-conflict-policy)

Workflow Id 冲突策略确定在生成新的 Workflow Execution 时如何解决冲突
Open Workflow Execution 已使用特定的 Workflow Id。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Workflow Id 重用策略](/Workflow-execution/Workflowid-runid#Workflow-id-reuse-policy)

Workflow Id 重用策略确定是否允许 Workflow Execution 与特定 Workflow Id 一起生成，如果
Workflow Id 已与之前的、现已关闭的 Workflow Execution 一起使用。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Workflow 运行超时](/百科全书/检测-Workflow-failures#Workflow-run-timeout)

这是单次 Workflow 运行的最大时间限制。

<!-- _Tags: [术语](/tags/term), [解释](/tags/explanation), [超时](/tags/timeouts)_ -->

#### [Workflow Task](/任务#Workflow-任务)

Workflow Task 是一个任务，其中包含使用 Workflow Execution 取得进展所需的上下文。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Workflow Task 执行](/tasks#Workflow-任务-执行)

当 Worker 拿起 Workflow Task 并使用它来取得执行的进展时，就会发生 Workflow Task 执行。
Workflow Definition。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

#### [Workflow Task 超时](/百科全书/检测-Workflow-失败#Workflow-任务超时)

Workflow Task 超时是 Temporal Server 等待 Worker 启动的最长时间
从 Task Queue 中提取任务后处理 Workflow Task。

<!-- _Tags: [术语](/tags/term), [解释](/tags/explanation), [超时](/tags/timeouts)_ -->

#### [Workflow Type](/Workflow-定义#Workflow-类型)

Workflow Type 是映射到 Workflow Definition 的名称。

<!-- _标签: [术语](/标签/术语), [解释](/标签/解释)_ -->

## 已弃用的术语

#### tctl（_已弃用_）

tctl 是一个命令行工具，可用于与 Temporal 服务交互。它被取代
[Temporal CLI 实用程序](#cli)。
