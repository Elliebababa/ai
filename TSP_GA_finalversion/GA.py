# -*- coding: utf-8 -*-

import random
from Life import Life

class GA(object):
      """遗传算法类"""
      def __init__(self, aCrossRate, aMutationRage, aLifeCount, aGeneLenght, distance, lives,aMatchFun = lambda life : 1):
            self.croessRate = aCrossRate
            self.mutationRate = aMutationRage
            self.lifeCount = aLifeCount
            self.geneLenght = aGeneLenght
            self.matchFun = aMatchFun                 # 适配函数
            self.lives = lives                          # 种群
            self.best = None                         # 保存这一代中最好的个体
            self.generation = 1
            self.maxGen = 100
            self.crossCount = 0
            self.bounds = 0.0                         # 适配值之和，用于选择是计算概率
            self.distance = distance
            self.initPopulation()


      def initPopulation(self):
            '''
            """初始化种群"""
            self.lives = []
            gene = [i+1 for i in range(self.geneLenght)]
            life = Life(gene)
            self.lives.append(life)
            for i in range(self.lifeCount):
                  gene = [ x+1 for x in range(self.geneLenght) ] 
                  random.shuffle(gene)
                  life = Life(gene)     #个体
                  self.lives.append(life)
            '''
            self.best = self.lives[0]
            self.best.score = self.calscore(self.best.gene)
            #print(self.best.gene,self.best.score)
            self.judge()

      
      def judge(self):
            """评估，计算每一个个体的适配值"""
            self.bounds = 0.0
            for life in self.lives:
                  if life.score == -1:
                        life.score = self.calscore(life.gene)
                  self.bounds += life.score
            self.lives.sort()
            #print(1/self.best.score,self.lives[0].score,1/self.lives[1].score,1/self.lives[self.lifeCount-1].score)
            if self.best.score < self.lives[0].score:
                  self.best = self.lives[0]
      

      def cross(self, parent1, parent2):
            """交叉""" #随机生成交换点，有上下限index1和index2
            #两点交叉
            index1 = random.randint(0, self.geneLenght - 1) 
            index2 = random.randint(index1, self.geneLenght - 1)
            tempGene = parent2.gene[index1:index2]   # 交叉的基因片段
            newGene = []
            p1len = 0
            for g in parent1.gene:
                  if p1len == index1:
                        newGene.extend(tempGene)     # 插入基因片段
                        p1len += 1
                  if g not in tempGene:
                        newGene.append(g)
                        p1len += 1
            self.crossCount += 1
            return newGene


      def  mutation(self, gene):
            """突变"""#变异的时候不能只是改变基因序列中的某一位的值（这会导致一个城市经过两次），应该随机交换两个位置的值
            index1 = random.randint(0, self.geneLenght - 1)
            index2 = random.randint(0, self.geneLenght - 1)

            newGene = gene[:]       # 产生一个新的基因序列，以免变异的时候影响父种群
            tmp = newGene[index1:index2]
            tmp.reverse()
            newGene[index1:index2] = tmp
            #newGene[index1], newGene[index2] = newGene[index2], newGene[index1]
            return newGene


      def getOne(self):
            """选择一个个体"""
            r = random.uniform(0, self.bounds)

            for life in self.lives:
                  r -= life.score
                  if r <= 0:
                        return life
            
            raise Exception("选择错误", self.bounds)


      def newChild(self):
            """产生新后的"""
            #迭代10次，取后代和p1中最好的作为新生代
            parent1 = self.getOne()
            parent2 = self.getOne()
            gene = self.cross(parent1, parent2)
            newKid = Life(gene)
                  #print(i,' succeed in creating newKid')
            newKid.score = self.calscore(newKid.gene)
            bestLife = newKid
            for i in range(10):
                  rate = random.random()
                  # 按概率交叉
                  if rate < self.croessRate:
                        # 交叉
                        gene = self.cross(parent1, parent2)
                  else:
                        gene = bestLife.gene

                  # 按概率突变
                  rate = random.random()
                  if rate < self.mutationRate:
                        gene = self.mutation(gene)
                  #取后代最好的放到新的generation
                  newKid = Life(gene)
                  #print(i,' succeed in creating newKid')
                  newKid.score = self.calscore(newKid.gene)
                  #print(i ,newKid.score)

                  if bestLife.score < newKid.score:
                        bestLife = newKid

            return bestLife

      def calscore(self,t):
            totalDis = 0
            for i in range(len(t) - 1):
                  totalDis += self.distance[t[i]][t[i+1]]
            totalDis += self.distance[t[-1]][t[0]]
            #print(len(t),'  totalDis',totalDis)
            return 1/totalDis


      def next(self):
            """产生下一代"""
            #print('self.best to be append:',self.best.gene)
            self.judge()
            newLives = self.lives[0:self.lifeCount//3]
            #newLives.append(self.best)            #把最好的个体加入下一代
            while len(newLives) < self.lifeCount:
                  newC = self.newChild()
                  newLives.append(newC)
                  #print(newC.score,self.best.score)
                  if newC.score > self.best.score:
                        self.best = newC
            self.lives = newLives
            self.generation += 1
            #print(self.generation,self.best.score)
            
