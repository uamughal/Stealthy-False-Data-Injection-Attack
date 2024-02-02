# Stealthy False Data Injection Attack on Unmanned Aerial Vehicles

**This code provides how to inject the stealthy measurements into the system without being detected by the anomaly detector.**

Unmanned aerial vehicles (UAVs) are widely used for military and civilian applications. Despite their wide adoption, they are vulnerable to cyber-attacks, which could lead to serious consequences that cause the UAVs to crash or be directed to undesired locations. In this context, several works have investigated false data injection (FDI) attacks. However, existing studies often assume that the attacker knows all the system and control parameters, which may not always be the case. In this paper, we propose a strategy for stealthy FDI attacks that does not require full knowledge of the system and control parameters. This approach eavesdrops and injects false commands and data into two main communication channels, namely, the feedback channel (from the UAV to the ground controller) and the forward channel (from the ground controller to the UAV). The attacker incorporates two separate Kalman filters that process inputs from both channels and subsequently generate an estimate of the UAV’s current state. Then, stealthy false data and commands are injected while ensuring UAV’s stability. We tested the proposed attack in simulation and validated it through experiments on an actual UAV. Our experimental results demonstrate that the proposed FDI attack causes the UAV to deviate from its original path while remaining stealthy. We also demonstrate that our attack causes a large deviation in the UAV’s path compared to other attacks that assume full knowledge of the system parameters. Through this study, we aim to shed some light that helps to develop robust defense mechanisms against such attacks.

**This work is published in IEEE Conference on Communications and Network Security (CNS), 2023, Orlando, FL, USA**

# Real-time Attacking on an actual drone system.
If you require a real-time attack implementation on an actual drone system, which misleads the drone to the wrong destination without being detected. This code involves Kalman filtering and controller manipulations. This code will be provided on request. Please reach out to us using your academic email and indicate the intention that the code will be used for academic research and development purposes. We would be very happy to provide it.**

**The code in this repository provides the simulation and light version.**

# Citing this work
If you are using our implementation, you are encouraged to cite [our paper](https://ieeexplore.ieee.org/abstract/document/10289001).
``` 

@inproceedings{mughal2023stealthy,
  title={Stealthy False Data Injection Attack on Unmanned Aerial Vehicles with Partial Knowledge},
  author={Mughal, Umair Ahmad and Ismail, Muhammad and Rizvi, Syed Ali Asad},
  booktitle={2023 IEEE Conference on Communications and Network Security (CNS)},
  pages={1--9},
  year={2023},
  organization={IEEE}
}

``` 
