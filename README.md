# Microgrid DRL Optimizer
Este proyecto implementa un agente de Deep Reinforcement Learning (DRL) para optimizar el despacho de energía en una microred.

## Objetivos
* **Negocio:** Minimizar el costo de importación de energía y maximizar el uso de generación solar local.
* **Machine Learning:** Modelar el problema como un MDP (Markov Decision Process) y resolverlo usando algoritmos de DRL.

## Formulación Inicial del Entorno (MDP)
* **State Space:** Hora del día, Estado de Carga de la Batería (SoC), Generación Solar actual, Demanda actual, Precio actual de la energía.
* **Action Space:** Continuo [-1, 1]. (-1 = descargar batería al máximo, 1 = cargar batería al máximo, 0 = mantener).
* **Reward Function:** Penalización equivalente al costo de la energía comprada a la red principal, más una penalización si se violan las restricciones operativas de la batería.
