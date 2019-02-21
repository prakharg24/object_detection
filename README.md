*The repository contains work done in course 'Special Topics in AI' under Prof Chetan Arora.*

*--- Work in Progress ---*

-------

## Authors and Contribution
Prakhar Ganesh and Sagar Goyal

## Copyright

Copyright © 2018 by Prakhar Ganesh

All rights reserved. No part of this work may be reproduced, distributed, or transmitted in any form or by any means, without the prior written permission of the owner. For permission requests, write to the owner.

## Clone Repository

The following repository contains submodule(s). Clone the repo using the following command.
```
git clone --recurse-submodules https://github.com/prakharg24/object_detection.git
```

Alternatively, first clone the repo, and then initialize every submodule seperately
```
git clone https://github.com/prakharg24/object_detection.git
git submodule update --init --recursive <submodule1_name>
git submodule update --init --recursive <submodule2_name>
...
```

## Contents

* [Authors and Contribution](#authors-and-contribution)
* [Copyright](#copyright)
* [Clone Repository](#clone-repository)
* [Submodules](#submodules)
* [Problem Statement](#problem-statement)
* [Dataset](#dataset)
* [Results](#results)
* [References](#references)

## Submodules

The work done here is solely possible due to the following repositories. I have cloned these repositories, cleaned them and created my own submodules, however the majority of code is from the original repo.

### [keras-frcnn](https://github.com/prakharg24/keras-frcnn)
* Keras implementation of Faster R-CNN for object detection
* Known issues with keras version >=2.2.2
* keras version==2.1.6 and tensorflow version==1.8.0 recommended for smooth working

## Problem Statement

The task is to create an object detection system which classifies the object and returns a set of bounding box coordinates. This repository includes experimentation with different publicly available pretrained pipelines and some modifications made by us on top of it.

The submodule setup and modifications done here are generalised for any object detection problem statement. The experimentation results are for the following [dataset](https://drive.google.com/file/d/1SU5SE13_rRwHHRga0Kb86-D3wU91u7rp/view?usp=sharing). Find the exact problem statement for the same attached [here](https://github.com/prakharg24/object_detection/blob/master/Assignment.pdf).


## Dataset

### Preparing Dataset

## Results

### Download Pretrained Weights

Use the following weights to get the results specified above

| S.No | Dataset | Number of Epochs | Model Name | Weight File |
| ---- | ------- | ---------------- | ---------- | ----------- |
| 1    | [Cow/Dog Dataset]() | xx | Faster R-CNN | [Download](Somelinl) |
| 2    | [Pascal VOC]() | xx | Faster R-CNN | [Download](dsad) |
| 3    | Pascal VOC + Cow/Dog Dataset | xx | Faster R-CNN | [Download](d) |

## References