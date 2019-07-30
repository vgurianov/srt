# resacher_instruments module
This module contains classes to measurement and data processing.  
Description:
  - class *Table* is model of detector and data recorder
  - class *DataProcessing* is processor of data.  
  
## Class *Table*
Description: class *Table* is a data recorder
Bases: object  
Parameters:	None

### Attributes: 
    - obtG = []
    - obt = []
    - obx = []
    - localT = []
    - particleT = []

### Operations:  
*fixIt(self,tG, tt, xx, locT, prtT)*
Description: Operation write data about time and location
Parameters:
- tG
- tt
- xx
- locT
- prtT
Return: None

*detect(self, tG, c)*  
Description: Operation write data about intaraction
Parameters:
- tG
- c
Return: None
