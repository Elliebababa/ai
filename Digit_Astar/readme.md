A description of the program.
The program adopts Astar algorithm to solve the eight digit problem and then apply the same evaluation function to solve the nine digit problem.
Both of the two problems use two different evaluation functions to solve the problems.
Evaluation function one (h1) calculates the sum of the distance of the digits from its current grid to its final grid.
Evaluation function two (h2) calculates the number of the mis-placed digits.
In order to compare the efficiency of the two algorithm better, the program displays related variables of two evaluation functions,
and use two thread to run the two function at concurrently to have a look at the speed difference between them.

ps. the cantor algorithm and the priority queue are used to improve the program.

A description of the UI.
The left hand side shows some related variables of the two evaluation functions, including #nodes in open list, #total nodes, the value of the least node.
(Thus it will always be zero at the end of the search.)
In the middle of the panel, the process of the search is exhibited.
The right hand side includes, from top to bottom, the buttons controlling start and end, the radio buttons choosing the eight/nine digit problem,
the initial state and the final state of the problem, as well as the best path to solve the problem.

------------------------------
文件说明：
DigitWrapper--程序运行的主文件
DigitUI.py--程序界面文件
EightDigit--实现八数码问题的文件
NineDigit--实现九数码问题的文件
cantor.py--实现康托展开的文件

运行说明：
运行DigitWrapper.py


程序说明：
程序采用A*算法解决八数码问题，然后用相同的评估函数解决九数码问题。
两个问题分别采用了两种不同的评估函数求解问题。
评估函数1（h1）为计算每个错位数码到其正确位置距离的总和。
评估函数2（h2）为计算错位数码的个数。
为了能更好的将两个算法的效率进行比较，程序中将两种评估函数搜索过程相关的变量展现出来，
并利用了两个线程同时运行两个算法以比较算法的速度。

程序细节：
open表节点排序采用了优先级队列，按照节点的评估值+深度进行排序。
表的存储采用了康托展开将数码序列转化为对应的编码再用哈希列表进行存储，加快了搜索的速度。

程序的界面说明：
界面的左侧分别显示h1和h2两个评估函数的搜索效果。
显示的值有OPEN表的结点数，总拓展的结点数，及当前最小结点的评估函数值（到达终点后即为0）。
界面中间的面板把搜索的过程展现了出来。
界面右侧从上往下分别是控制起止、选择问题的按钮，搜索的始末状态，以及最终得到的路径。
