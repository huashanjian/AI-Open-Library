# 强化学习 / Reinforcement Learning

## 主题介绍 / Topic Introduction

强化学习是机器学习的重要分支，研究智能体如何在环境中通过试错学习最优策略。它结合了动态规划、蒙特卡洛方法和时序差分学习等技术，为解决序贯决策问题提供了强有力的工具。强化学习在游戏AI、机器人控制、自动驾驶等领域都有重要应用，也是多智能体系统和具身智能的重要理论基础。

Reinforcement learning is an important branch of machine learning that studies how agents learn optimal policies through trial and error in environments. It combines techniques such as dynamic programming, Monte Carlo methods, and temporal difference learning, providing powerful tools for solving sequential decision problems. Reinforcement learning has important applications in game AI, robot control, autonomous driving, and serves as an important theoretical foundation for multi-agent systems and embodied intelligence.

## 推荐学习路径 / Recommended Learning Path

### 🏗️ 基础理论 / Foundational Theory

1. 马尔可夫决策过程 / Markov decision processes
2. 动态规划方法 / Dynamic programming methods
3. 蒙特卡洛方法 / Monte Carlo methods

### 🧠 核心概念 / Core Concepts

1. 时序差分学习 / Temporal difference learning
2. 策略梯度方法 / Policy gradient methods
3. 值函数近似 / Value function approximation

### 🚀 前沿应用 / Advanced Applications

1. 深度强化学习 / Deep reinforcement learning
2. 多智能体强化学习 / Multi-agent reinforcement learning
3. 层次化强化学习 / Hierarchical reinforcement learning

## 精选资料 / Curated Resources

### 📌 经典精选 / Canonical Picks

- Playing Atari with Deep Reinforcement Learning — 深度 Q 网络开山之作，奠定深度RL基础。/ DQN seminal paper laying the foundation of deep RL. [查看 View](../_library/Playing_Atari_with_Deep_Reinforcement_Learning.pdf)
- Proximal Policy Optimization Algorithms — 简单稳定的策略梯度基线。/ A simple and stable policy-gradient baseline. [查看 View](../_library/Proximal_Policy_Optimization_Algorithms.pdf)
- Soft Actor-Critic Algorithms and Applications — 最大熵RL，连续控制表现强劲且稳健。/ Max-entropy RL with strong, robust continuous-control performance. [查看 View](../_library/Soft_Actor-Critic_Algorithms_and_Applications.pdf)
- Model-based Reinforcement Learning: A Survey — 模型式RL全景综述与研究地图。/ A panoramic survey of model-based RL. [查看 View](../_library/Model-based_Reinforcement_Learning_A_Survey.pdf)

### 📚 相关资料 / Related Materials

本主题的资料分散在相关主题文件夹中，请参考：

The materials for this topic are distributed across related topic folders, please refer to:

#### 欠驱动机器人控制中的强化学习 / RL in Underactuated Robot Control

强化学习在机器人控制中的应用，特别是欠驱动系统的控制策略学习。

Applications of reinforcement learning in robot control, especially control strategy learning for underactuated systems.

**参考资料/Reference**: [世界模型与具身智能](../00_World_Models_and_Embodied_AI/) - Underactuated Robotics

#### 多智能体强化学习 / Multi-Agent Reinforcement Learning

多个智能体在共享环境中的学习与协作，包括竞争与合作策略。

Learning and collaboration of multiple agents in shared environments, including competitive and cooperative strategies.

**参考资料/Reference**: [多智能体学习](../03_Multi_Agent_Learning/) - Multi-Agent RL Foundations

---

### 📄 更多资料 / More Resources

- Playing Atari with Deep Reinforcement Learning — 深度 Q 网络开山之作。/ DQN seminal paper. [查看 View](../_library/Playing_Atari_with_Deep_Reinforcement_Learning.pdf)
- Proximal Policy Optimization Algorithms — PPO 论文。/ PPO paper. [查看 View](../_library/Proximal_Policy_Optimization_Algorithms.pdf)
- Soft Actor-Critic Algorithms and Applications — SAC 论文。/ SAC paper. [查看 View](../_library/Soft_Actor-Critic_Algorithms_and_Applications.pdf)
- The Surprising Effectiveness of PPO in Cooperative, Multi-Agent Games — 多智能体环境下 PPO 的有效性。/ PPO in MARL. [查看 View](../_library/The_Surprising_Effectiveness_of_PPO_in_Cooperative,_Multi-Agent_Games.pdf)
- Value-Decomposition Networks For Cooperative Multi-Agent Learning — VDN。/ VDN for cooperative MARL. [查看 View](../_library/Value-Decomposition_Networks_For_Cooperative_Multi-Agent_Learning.pdf)
- QMIX Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning — QMIX。/ QMIX for MARL. [查看 View](../_library/QMIX_Monotonic_Value_Function_Factorisation_for_Deep_Multi-Agent_Reinforcement_Learning.pdf)
- Decision Transformer Reinforcement Learning via Sequence Modeling — 决策 Transformer。/ Decision Transformer. [查看 View](../_library/Decision_Transformer_Reinforcement_Learning_via_Sequence_Modeling.pdf)
- Model-based Reinforcement Learning A Survey — 模型化强化学习综述。/ Survey on MBRL. [查看 View](../_library/Model-based_Reinforcement_Learning_A_Survey.pdf)

#### 📚 经典教材 / Classic Textbooks

- Dynamic Programming and Optimal Control — Bertsekas 经典两卷本。/ Two-volume DP classic. [PDF](../_library/Dynamic_Programming_And_Optimal_Control_2014.pdf)
- Reinforcement Learning and Optimal Control — Bertsekas RL 与最优控制。/ RL and optimal control. [PDF](../_library/Reinforcement_Learning_Bertsekas_Draft.pdf)
- Markov Decision Processes: Discrete Stochastic Dynamic Programming — Puterman MDP 专著。/ Puterman's MDP classic. [PDF](../_library/Markov_Decision_Process.pdf)


## 相关主题 / Related Topics

- **00 世界模型与具身智能 / World Models & Embodied AI** → [../00_World_Models_and_Embodied_AI/](../00_World_Models_and_Embodied_AI/) — 物理/控制与策略学习 / control and policy learning
- **01 深度学习 / Deep Learning** → [../01_Deep_Learning/](../01_Deep_Learning/) — 表达能力与函数逼近 / representation and approximation
- **03 多智能体学习 / Multi-Agent Learning** → [../03_Multi_Agent_Learning/](../03_Multi_Agent_Learning/) — 协作/博弈/部分可观测 / cooperation, games, partial observability
- **04 AI 基础理论 / AI Foundations** → [../04_AI_Foundations/](../04_AI_Foundations/) — 概率/优化/决策理论 / probability, optimization, decision theory
- **05 LLMs 与 Transformers / LLMs & Transformers** → [../05_LLMs_and_Transformers/](../05_LLMs_and_Transformers/) — 序列决策与建模借鉴 / inspirations for sequential modeling
- **06 训练动态与泛化 / Training Dynamics and Generalization** → [../06_Training_Dynamics_and_Generalization/](../06_Training_Dynamics_and_Generalization/) — 训练行为与稳定性 / training behavior and stability
- **08 计算机视觉 / Computer Vision** → [../08_Computer_Vision/](../08_Computer_Vision/) — 视觉强化学习与感知耦合 / vision-RL coupling

## 学习建议 / Study Recommendations

### 对于初学者 / For Beginners

建议从马尔可夫决策过程的数学基础开始，理解强化学习的核心概念，然后学习基本的算法如Q-learning。

Start with the mathematical foundations of Markov decision processes, understand core concepts of reinforcement learning, then learn basic algorithms like Q-learning.

### 对于进阶学习者 / For Advanced Learners

深入学习深度强化学习算法，探索在具体应用领域（如机器人控制、多智能体系统）中的实践方法。

Study deep reinforcement learning algorithms in depth, explore practical methods in specific application domains such as robot control and multi-agent systems.

---

最后更新 / Last Updated: 2025年9月22日 / September 22, 2025
