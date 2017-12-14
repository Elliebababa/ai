# -*- encoding: utf-8 -*-


SCORE_NONE = -1

class Life(object):
      """个体类"""
      def __init__(self, aGene = None):
            self.gene = aGene
            self.score = SCORE_NONE

      def __lt__(self,other):#相同的值则先生成的优先
          return self.score > other.score

