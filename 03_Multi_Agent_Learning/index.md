# 多智能体学习 / Multi-Agent Learning

## 主题介绍 / Topic Introduction

多智能体学习是人工智能领域的重要分支，研究多个智能体在共享环境中的交互、协作与竞争。这一领域结合了博弈论、强化学习、分布式系统等多个学科，旨在理解和设计能够在复杂多智能体环境中有效学习和决策的系统。多智能体强化学习(MARL)作为核心技术，为解决现实世界中的复杂协作问题提供了重要的理论基础和实践方法。

Multi-agent learning is an important branch of artificial intelligence that studies the interaction, cooperation, and competition of multiple agents in shared environments. This field combines game theory, reinforcement learning, distributed systems, and other disciplines, aiming to understand and design systems that can effectively learn and make decisions in complex multi-agent environments. Multi-agent reinforcement learning (MARL) serves as a core technology, providing important theoretical foundations and practical methods for solving complex cooperation problems in the real world.

## 推荐学习路径 / Recommended Learning Path

### 🏗️ 基础理论 / Foundational Theory

1. 博弈论基础 / Game theory foundations
2. 单智能体强化学习 / Single-agent reinforcement learning
3. 分布式系统概念 / Distributed systems concepts

### 🧠 核心概念 / Core Concepts

1. 多智能体强化学习算法 / Multi-agent reinforcement learning algorithms
2. 协调与合作机制 / Coordination and cooperation mechanisms
3. 通信与信息共享 / Communication and information sharing

### 🚀 前沿应用 / Advanced Applications

1. 多机器人协作 / Multi-robot collaboration
2. 自动驾驶车辆协调 / Autonomous vehicle coordination
3. 分布式资源管理 / Distributed resource management

## 精选资料 / Curated Resources

### ⭐ 经典精选 / Canonical Picks

- Multiagent Systems (Shoham & Leyton-Brown) — 多智能体系统经典教材。/ Classic textbook. [查看 View](../_library/Multiagent_Systems_Shoham_Leyton_Brown.pdf)
- QMIX Monotonic Value Function Factorisation — MARL 代表性算法。/ Representative MARL algorithm. [查看 View](../_library/QMIX_Monotonic_Value_Function_Factorisation_for_Deep_Multi-Agent_Reinforcement_Learning.pdf)
- Counterfactual Multi-Agent Policy Gradients — COMA 算法。/ COMA algorithm. [查看 View](../_library/Counterfactual_Multi-Agent_Policy_Gradients.pdf)

### 📚 经典教材 / Classic Textbooks

 
#### Multi-Agent Reinforcement Learning Foundations

**作者/Authors**: Michael L. Littman, Liviu Panait, Jakob Foerster, et al.  
**年份/Year**: 2024  
**标签/Tags**: `多智能体强化学习` `协调` `博弈论` `MARL` `Coordination` `Game Theory`

本书系统梳理了多智能体强化学习的基础理论与算法，包括 centralized critic、self-play、自组织合作等机制；讨论多智能体环境中的学习挑战（如非平稳性、部分可观察性、通信约束）与对应方法，涵盖从独立学习到联合学习的多种思路。

This book systematically outlines the foundations and algorithms of multi-agent reinforcement learning, including centralized critic, self-play, and emergent cooperation mechanisms. It explores learning challenges in multi-agent environments such as non-stationarity, partial observability, and communication constraints, providing corresponding solutions.

**推荐读者/Recommended For**: 已具备强化学习基础、关注多智能体协作和博弈建模的学习者和研究者。/ For readers with RL foundations, interested in multi-agent coordination, game-theoretic modeling, and scalable learning.

**链接/Link**: [../_library/Multi-Agent_Reinforcement_Learning_Foundations.pdf](../_library/Multi-Agent_Reinforcement_Learning_Foundations.pdf)

---

### 📄 更多资料 / More Resources

- The StarCraft Multi-Agent Challenge — SC2 多智能体挑战。/ SMAC benchmark. [查看 View](../_library/The_StarCraft_Multi-Agent_Challenge.pdf)
- The Hanabi Challenge — Hanabi 协作挑战。/ Hanabi benchmark. [查看 View](../_library/The_Hanabi_Challenge_A_New_Frontier_for_AI_Research.pdf)
- The Surprising Effectiveness of PPO in Cooperative, Multi-Agent Games — 多智能体协作中 PPO 的有效性。/ PPO in cooperative MARL. [查看 View](../_library/The_Surprising_Effectiveness_of_PPO_in_Cooperative,_Multi-Agent_Games.pdf)
- Counterfactual Multi-Agent Policy Gradients — COMA 算法。/ COMA algorithm. [查看 View](../_library/Counterfactual_Multi-Agent_Policy_Gradients.pdf)
- Value-Decomposition Networks For Cooperative Multi-Agent Learning — VDN。/ Value decomposition. [查看 View](../_library/Value-Decomposition_Networks_For_Cooperative_Multi-Agent_Learning.pdf)
- QMIX Monotonic Value Function Factorisation — QMIX。/ Monotonic value factorization. [查看 View](../_library/QMIX_Monotonic_Value_Function_Factorisation_for_Deep_Multi-Agent_Reinforcement_Learning.pdf)

#### 📚 经典教材（已收录） / Classic Textbooks (Collected)

- Algorithmic Game Theory — 算法博弈论重要文集。/ Influential compendium. [PDF](../_library/Algorithmic_Game_Theory.pdf)
- Multiagent Systems: A Modern Approach to Distributed AI — 多智能体系统经典教材（文集）。/ Classic textbook. [PDF](../_library/Multiagent_Systems_A_Modern_Approach_To_Distributed_Artificial_Intelligence_Gerhard_Weiss.pdf)
- Distributed Control of Robotic Networks — 图论/一致性/分布式控制基础。/ Foundations in distributed control. [PDF](../_library/DCRN_Bullocortesmartinez_10mar09.pdf)


## 相关主题 / Related Topics

- **00 世界模型与具身智能 / World Models & Embodied AI** → [../00_World_Models_and_Embodied_AI/](../00_World_Models_and_Embodied_AI/) — 具身协作与控制 / embodied coordination and control
- **01 深度学习 / Deep Learning** → [../01_Deep_Learning/](../01_Deep_Learning/) — 表达与通信建模 / representation and communication modeling
- **02 强化学习 / Reinforcement Learning** → [../02_Reinforcement_Learning/](../02_Reinforcement_Learning/) — 策略优化与博弈框架 / policy optimization and game-theoretic frameworks
- **04 AI 基础理论 / AI Foundations** → [../04_AI_Foundations/](../04_AI_Foundations/) — 博弈/优化/概率工具 / game theory, optimization, probability
- **05 LLMs 与 Transformers / LLMs & Transformers** → [../05_LLMs_and_Transformers/](../05_LLMs_and_Transformers/) — 多智能体通信与语言建模 / communication and language modeling
- **06 训练动态与泛化 / Training Dynamics and Generalization** → [../06_Training_Dynamics_and_Generalization/](../06_Training_Dynamics_and_Generalization/) — 非平稳性与泛化 / non-stationarity and generalization
- **08 计算机视觉 / Computer Vision** → [../08_Computer_Vision/](../08_Computer_Vision/) — 多视协作与感知 / multi-view and perception
- **97 科研写作与投稿 / Research Writing and Publishing** → [../97_Research_Writing_and_Publishing/](../97_Research_Writing_and_Publishing/) — 论文写作 / writing
- **LLMs 与 Transformers** / LLMs & Transformers → [../05_LLMs_and_Transformers/](../05_LLMs_and_Transformers/)

## 学习建议 / Study Recommendations

### 对于初学者 / For Beginners

建议先掌握单智能体强化学习的基础知识，然后学习博弈论的基本概念，再进入多智能体学习领域。

It is recommended to first master the fundamentals of single-agent reinforcement learning, then learn basic concepts of game theory, before entering the field of multi-agent learning.

### 对于进阶学习者 / For Advanced Learners

深入研究具体的MARL算法实现，关注最新的研究进展，特别是深度学习在多智能体系统中的应用。重点学习协调机制和通信策略的设计。

Study specific MARL algorithm implementations in depth, pay attention to the latest research developments, especially the application of deep learning in multi-agent systems. Focus on coordination mechanisms and communication strategy design.

---

最后更新 / Last Updated: 2025年9月22日 / September 22, 2025
