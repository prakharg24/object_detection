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



Alternatively,
```
git clone https://github.com/prakharg24/object_detection.git
```
and then do the following for each submodule seperately
```
git submodule update --init --recursive <submodule_name>
```

# Contents

* [Authors and Contribution](#authors-and-contribution)
* [Copyright](#copyright)
* [Clone Repository](#clone-repository)
* [Submodules](#submodules)
* [Problem Statement](#problem-statement)
* [Getting Familiar with the Code](#getting-familiar-with-the-code)
* [Files Included](#files-included)
* [Dataset](#dataset)
* [Results](#results)
* [Replicating Our Results](#replicating-our-results)

## Submodules

### [keras-frcnn](https://github.com/kbardool/keras-frcnn/tree/59e12699aea69fa9e15c7ec74694e43087d02240)
* Known issues with keras version >=2.2.2
* keras version=2.1.6 and tensorflow version=1.8.0 recommended for smooth working

## Problem Statement

The task is to create an object detection system which classifies the object and return a set of bounding box coordinates. The possible object labels are : cow/dog. The repository includes experimentation with different publicly available pretrained pipeline and some modifications made by us on top of it.

Please find the exact problem statement attached [here](https://github.com/prakharg24/object_detection/blob/master/Assignment.pdf)