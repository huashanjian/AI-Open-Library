# 世界模型与具身智能 / World Models and Embodied AI

## 主题介绍 / Topic Introduction

世界模型与具身智能是人工智能领域的前沿方向，探讨智能体如何在物理环境中感知、理解并与世界交互。这一领域结合了认知科学、机器人学、深度学习等多个学科，致力于构建能够理解世界运作规律并在其中有效行动的智能系统。欠驱动机器人学是其中的重要分支，研究如何在控制输入少于系统自由度的情况下实现有效控制。

World models and embodied AI represent cutting-edge directions in artificial intelligence, exploring how intelligent agents perceive, understand, and interact with the physical world. This field combines cognitive science, robotics, deep learning, and other disciplines to build intelligent systems that can understand how the world works and act effectively within it. Underactuated robotics is an important branch that studies how to achieve effective control when control inputs are fewer than system degrees of freedom.

## 推荐学习路径 / Recommended Learning Path

### 🏗️ 基础理论 / Foundational Theory

1. 机器人学数学基础 / Mathematical foundations of robotics
2. 动力学与控制理论 / Dynamics and control theory  
3. 欠驱动系统分析 / Underactuated systems analysis

### 🧠 核心概念 / Core Concepts

1. 世界模型构建方法 / World model construction methods
2. 物理仿真与建模 / Physics simulation and modeling
3. 被动动力学利用 / Passive dynamics exploitation

### 🚀 前沿应用 / Advanced Applications

1. 类人机器人步态控制 / Humanoid robot gait control
2. 灵巧操作与抓取 / Dexterous manipulation and grasping
3. 飞行器与移动机器人 / Aircraft and mobile robotics

## 精选资料 / Curated Resources

### ⭐ 经典精选 / Canonical Picks

- Underactuated Robotics — 欠驱动机器人学经典教材，具身智能与控制的基础。/ Classic textbook on underactuated robotics and control foundations. [查看 View](../_library/Underactuated_Robotics_Russ_Tedrake.pdf)
- World Models — 世界模型里程碑论文，提出“想象-计划-控制”范式。/ Landmark paper introducing generative world models for control. [查看 View](../_library/World_Models.pdf)

### 📚 经典教材 / Classic Textbooks

#### Underactuated Robotics

**作者/Author**: Russ Tedrake (MIT OpenCourseWare)  
**年份/Year**: 2024  
**标签/Tags**: `机器人学` `动力学` `欠驱动` `Robotics` `Dynamics` `Underactuation`

该教材深入介绍了欠驱动机器人系统的建模与控制策略，涵盖倒立摆、LQR等关键系统，配套有MIT开源课程资源。本书从基本的动力学原理出发，系统介绍了如何分析和控制欠驱动系统，包括摆系统、行走机器人、飞行器等实例。教材结合了严谨的数学推导和丰富的仿真实验，是理解具身智能中物理约束和动力学的重要参考。

This textbook introduces modeling and control strategies for underactuated robotic systems, including inverted pendulum and LQR, and is complemented by MIT's open course materials. Starting from basic dynamics principles, it systematically covers how to analyze and control underactuated systems with examples including pendulum systems, walking robots, and aircraft.

**推荐读者/Recommended For**: 机器人学习初学者、具身智能研究者、对动力系统控制建模感兴趣的工程专业学生。/ Beginner roboticists, embodied AI researchers, and engineering students interested in control and dynamical modeling.

**链接/Link**: [../_library/Underactuated_Robotics_Russ_Tedrake.pdf](../_library/Underactuated_Robotics_Russ_Tedrake.pdf)

### 📄 更多资源 / More Resources

- World Models — 探索以生成模型为核心的控制与规划范式。/ Pioneering framework using generative models for control and planning. [查看 View](../_library/World_Models.pdf)
- Mastering Diverse Domains through World Models — 使用世界模型在多样场景中泛化。/ Generalization across domains via world models. [查看 View](../_library/Mastering_Diverse_Domains_through_World_Models.pdf)
- Mastering Atari with Discrete World Models — 基于离散世界模型征服 Atari。/ Discrete world models for Atari mastery. [查看 View](../_library/Mastering_Atari_with_Discrete_World_Models.pdf)
- Dream to Control: Learning Behaviors by Latent Imagination — 通过潜在想象实现控制策略学习。/ Learn control via latent imagination. [查看 View](../_library/Dream_to_Control_Learning_Behaviors_by_Latent_Imagination.pdf)
- Learning Latent Dynamics for Planning from Pixels — 从像素学习潜在动力学以用于规划。/ Learn latent dynamics for pixel-based planning. [查看 View](../_library/Learning_Latent_Dynamics_for_Planning_from_Pixels.pdf)
- What Does it Mean for a Neural Network to Learn a World Model — 讨论“何为世界模型”。/ On what it means to learn a world model. [查看 View](../_library/What_Does_it_Mean_for_a_Neural_Network_to_Learn_a_World_Model.pdf)
- World Knowledge from AI Image Generation for Robot Control — 通过图像生成获得可用于控制的世界知识。/ Extract world knowledge for robot control from AI image generation. [查看 View](../_library/World_Knowledge_from_AI_Image_Generation_for_Robot_Control.pdf)

#### 📚 经典教材（交叉）/ Classic Textbooks (Cross-Topic)

- Probabilistic Robotics — 机器人概率方法与 SLAM。/ Probabilistic methods and SLAM. [PDF](../_library/Thrun_Et_Al_2005_Probabilistic_Robotics.pdf)
- Planning Algorithms — 运动规划/最优/采样等综述式教材。/ Comprehensive text on planning. [PDF](../_library/Planning_Algorithms.pdf)
- Modern Robotics: Mechanics, Planning, and Control — 机器人学力学、规划与控制。/ Mechanics, planning, control. [PDF](../_library/Modern_Robotics.pdf)
- Robot Modeling and Control — 机器人建模与控制经典。/ Classic text on robot modeling/control. [PDF](../_library/Robot_Modeling_And_Control_Compress.pdf)
- State Estimation for Robotics — 状态估计与图优化。/ State estimation and graph optimization. [PDF](../_library/State_Estimation_FOR_Robotics.pdf)
- Feedback Systems — 控制与反馈系统基础。/ Control and feedback foundations. [PDF](../_library/Astrom_Feedback_2006.pdf)
 

---

## 相关主题 / Related Topics

- **强化学习** / Reinforcement Learning → [../02_Reinforcement_Learning/](../02_Reinforcement_Learning/)
- **多智能体学习** / Multi-Agent Learning → [../03_Multi_Agent_Learning/](../03_Multi_Agent_Learning/)
- **深度学习** / Deep Learning → [../01_Deep_Learning/](../01_Deep_Learning/)

## 学习建议 / Study Recommendations

### 对于初学者 / For Beginners

建议先掌握基本的物理和数学基础，然后从简单的机械系统开始学习，逐步理解动力学原理。

Start with basic physics and mathematics, then learn from simple mechanical systems to gradually understand dynamics principles.

### 对于进阶学习者 / For Advanced Learners

深入研究具体的控制算法实现，结合仿真环境进行实践，探索如何将理论应用于实际机器人系统。

Study specific control algorithm implementations in depth, practice with simulation environments, and explore how to apply theory to real robotic systems.

---

最后更新 / Last Updated: 2025年9月23日 / September 23, 2025
