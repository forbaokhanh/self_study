class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        depth = 1
        cost = 0
        outside_cost = 0
        for y in nestedList:
            outside_cost += self.calc_cost(y, depth, cost)
        return outside_cost
            
    def calc_cost(self, nestedInteger, depth, cost):
        if nestedInteger.isInteger():
            print nestedInteger.getInteger()
            print "depth" + str(depth)
            cost += nestedInteger.getInteger()*depth
            print "Cost " + str(cost)
            return cost
        else:
            outside_cost = 0
            nIntegerList = nestedInteger.getList()
            for x in nIntegerList:
                outside_cost += self.calc_cost(x, depth + 1, cost)
                print "Big cost " + str(outside_cost)
            return outside_cost


class NestedInteger(object):
    def __init__(self, integer, data):
        self.integer = integer
        self.data = data

    def isInteger(self):
        return self.integer

    def getInteger(self):
        return self.data

    def getList(self):
        return self.data
if __name__ == '__main__':
    s = Solution()
    two = NestedInteger(True, 2)
    one = NestedInteger(True, 1)
    oneone = NestedInteger(True, 1)
    oneoneone = NestedInteger(True, 1)
    oneoneoneone = NestedInteger(True, 1)
    groupone = NestedInteger(False, [one, oneone])
    grouptwo = NestedInteger(False, [oneoneone, oneoneoneone])
    final = [groupone, two, grouptwo]
    print s.depthSum(final)