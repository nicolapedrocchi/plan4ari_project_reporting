---
title: MPPI software ecosystem
type: tool
updated: 2026-10-01
---

# MPPI software ecosystem

| Tool | Language / HW | Scope | Source |
|---|---|---|---|
| MPPI-Generic | CUDA C++, header-only | MPPI, Tube-MPPI, RMPPI; plug-in dynamics/costs | [[sources/vlahov2024mppigeneric]] |
| Nav2 MPPI controller | C++ (xtensor, CPU) | ROS 2 AMR local controller | [[sources/macenski2023nav2survey]] |
| STORM | PyTorch, GPU | 7-DoF arm joint-space MPPI | [[sources/bhardwaj2021storm]] |
| cuRobo | CUDA/PyTorch | arm motion generation (IK, planning, trajopt) | [[sources/sundaralingam2023curobo]] |
| m3p2i-aip (IsaacGym MPPI) | Python, Isaac Gym | simulator-in-the-loop MPPI, M3P2I | [[sources/pezzato2025isaacmppi]], [[sources/zhang2024m3p2i]] |
| Isaac Gym | GPU physics | rollouts | [[sources/makoviychuk2021isaacgym]] |
| MuJoCo MPC (MJPC) | C++ | predictive sampling, iLQG | [[sources/howell2022predictivesampling]] |
| JAX + MuJoCo-MJX | Python/JAX | massively parallel sampling MPC | [[sources/dierking2026parallelsbmpc]] |
| FPGA MPPI | HW design | embedded low-power | [[sources/desai2026fpgampi]] |
| VAMP | C++/Python, CPU SIMD (AVX2/Neon) | vectorised sampling-based planning, ~40 µs median (Panda) | [[sources/thomason2024vamp]] |
| acados | C, code-gen | gradient NMPC (Core IPC candidate) | [[sources/verschueren2022acados]] |

**Gap.** None targets deterministic timing and safety-rated interfaces of industrial controllers (gap #5 in [[comparisons/plan4ari-gap-analysis]]).
_Repository URLs are not recorded here yet: add them when verified (see wiki-ingest skill)._
