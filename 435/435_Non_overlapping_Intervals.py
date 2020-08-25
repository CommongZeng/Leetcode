class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) < 2:
            return 0

        self.intervals = []
        self.adj = {}
        self.d_count = {}
        for i in intervals:
            if self.d_count.get(self.getIntervalHash(i)) is None:
                self.d_count[self.getIntervalHash(i)] = 1
                self.intervals.append(i)
            else:
                self.d_count[self.getIntervalHash(i)] += 1
        self.count = sum(self.d_count.values()) - len(self.d_count.values())
        for i in self.intervals:
            self.adj[self.getIntervalHash(i)] = self.getOverlapIntervals(i, self.intervals)
        # print self.adj
        self.d = {}
        self.count += self.removeIntervalRecursive(self.adj)
        return self.count

    def removeIntervalRecursive(self, adj):
        # print 'adj =', adj
        if self.d.get(self.getAdjHash(adj)) is not None:
            return self.d.get(self.getAdjHash(adj))
        if self.isAllGood(adj):
            # print 'all good.'
            self.d[self.getAdjHash(adj)] = 0
            return 0
        max_adj_count = max([len(item[1]) for item in adj.items()])
        max_adj_intervals = []
        for item in adj.items():
            if len(item[1]) == max_adj_count:
                max_adj_intervals.append(self.getIntervalFromHash(item[0]))
        # print 'max_adj =', max_adj
        if len(max_adj_intervals) == 1:
            adj_tmp = self.removeInteval(adj, max_adj_intervals[0])
            res = 1 + self.removeIntervalRecursive(adj_tmp)
            self.d[self.getAdjHash(adj)] = res
            return res
        list_count = []
        for inteval_to_remove in max_adj_intervals:
            # print 'remove:', inteval_to_remove
            adj_tmp = self.removeInteval(adj, inteval_to_remove)
            count_res = self.removeIntervalRecursive(adj_tmp)
            # print 'count_res =', count_res
            list_count.append(1 + count_res)
            if count_res == 0:
                break
        # print 'list_count =', list_count
        # print 'returning', 1 + min(list_count)
        self.d[self.getAdjHash(adj)] = min(list_count)
        return min(list_count)

    def getOverlapIntervals(self, i, intervals):
        overlap_intervals = []
        for j in intervals:
            if self.isOverlap(i, j):
                overlap_intervals.append(j)
        return overlap_intervals

    def isOverlap(self, a, b):
        return a[1] > b[0] and a[0] < b[1] and (a[0] != b[0] or a[1] != b[1])

    def getIntervalHash(self, a):
        return '[' + str(a[0]) + ',' + str(a[1]) + ']'

    def getIntervalFromHash(self, h):
        return [int(s) for s in h.strip('[]').split(',')]

    def getAdjHash(self, adj):
        s = ''
        for item in sorted(adj.items(), key=lambda x:x[0]):
            if len(item[1]) > 0:
                s += self.getIntervalHash(item[0]) + ','
        return s

    def isAllGood(self, adj):
        for v in adj.values():
            if len(v) > 0:
                return False
        return True

    def removeInteval(self, adj_in, i):
        from copy import deepcopy
        adj = deepcopy(adj_in)
        adj.pop(self.getIntervalHash(i))
        for v in adj.values():
            if i in v:
                v.remove(i)
        return adj

test = Solution()
print test.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) # 1
print test.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) # 2
print test.eraseOverlapIntervals([[1,2],[2,3]]) # 0
print test.eraseOverlapIntervals([[1,2]]) # 0
print test.eraseOverlapIntervals([]) # 0
print test.eraseOverlapIntervals([[1,2],[1,2],[1,2],[1,4],[1,4],[1,4]]) # 5
print test.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]) # 2
print test.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]) # 2
print test.eraseOverlapIntervals([[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]) # 4
print test.eraseOverlapIntervals(
    [[-100,-87],[-99,-44],[-98,-19],[-97,-33],[-96,-60],[-95,-17],[-94,-44],[-93,-9],[-92,-63],[-91,-76],[-90,-44],[-89,-18],[-88,10],[-87,-39],[-86,7],[-85,-76],[-84,-51],[-83,-48],[-82,-36],[-81,-63],[-80,-71],[-79,-4],[-78,-63],[-77,-14],[-76,-10],[-75,-36],[-74,31],[-73,11],[-72,-50],[-71,-30],[-70,33],[-69,-37],[-68,-50],[-67,6],[-66,-50],[-65,-26],[-64,21],[-63,-8],[-62,23],[-61,-34],[-60,13],[-59,19],[-58,41],[-57,-15],[-56,35],[-55,-4],[-54,-20],[-53,44],[-52,48],[-51,12],[-50,-43],[-49,10],[-48,-34],[-47,3],[-46,28],[-45,51],[-44,-14],[-43,59],[-42,-6],[-41,-32],[-40,-12],[-39,33],[-38,17],[-37,-7],[-36,-29],[-35,24],[-34,49],[-33,-19],[-32,2],[-31,8],[-30,74],[-29,58],[-28,13],[-27,-8],[-26,45],[-25,-5],[-24,45],[-23,19],[-22,9],[-21,54],[-20,1],[-19,81],[-18,17],[-17,-10],[-16,7],[-15,86],[-14,-3],[-13,-3],[-12,45],[-11,93],[-10,84],[-9,20],[-8,3],[-7,81],[-6,52],[-5,67],[-4,18],[-3,40],[-2,42],[-1,49],[0,7],[1,104],[2,79],[3,37],[4,47],[5,69],[6,89],[7,110],[8,108],[9,19],[10,25],[11,48],[12,63],[13,94],[14,55],[15,119],[16,64],[17,122],[18,92],[19,37],[20,86],[21,84],[22,122],[23,37],[24,125],[25,99],[26,45],[27,63],[28,40],[29,97],[30,78],[31,102],[32,120],[33,91],[34,107],[35,62],[36,137],[37,55],[38,115],[39,46],[40,136],[41,78],[42,86],[43,106],[44,66],[45,141],[46,92],[47,132],[48,89],[49,61],[50,128],[51,155],[52,153],[53,78],[54,114],[55,84],[56,151],[57,123],[58,69],[59,91],[60,89],[61,73],[62,81],[63,139],[64,108],[65,165],[66,92],[67,117],[68,140],[69,109],[70,102],[71,171],[72,141],[73,117],[74,124],[75,171],[76,132],[77,142],[78,107],[79,132],[80,171],[81,104],[82,160],[83,128],[84,137],[85,176],[86,188],[87,178],[88,117],[89,115],[90,140],[91,165],[92,133],[93,114],[94,125],[95,135],[96,144],[97,114],[98,183],[99,157]]
) # 187
print test.eraseOverlapIntervals(
    [[-100,-98],[-99,-97],[-98,-96],[-97,-95],[-96,-94],[-95,-93],[-94,-92],[-93,-91],[-92,-90],[-91,-89],[-90,-88],[-89,-87],[-88,-86],[-87,-85],[-86,-84],[-85,-83],[-84,-82],[-83,-81],[-82,-80],[-81,-79],[-80,-78],[-79,-77],[-78,-76],[-77,-75],[-76,-74],[-75,-73],[-74,-72],[-73,-71],[-72,-70],[-71,-69],[-70,-68],[-69,-67],[-68,-66],[-67,-65],[-66,-64],[-65,-63],[-64,-62],[-63,-61],[-62,-60],[-61,-59],[-60,-58],[-59,-57],[-58,-56],[-57,-55],[-56,-54],[-55,-53],[-54,-52],[-53,-51],[-52,-50],[-51,-49],[-50,-48],[-49,-47],[-48,-46],[-47,-45],[-46,-44],[-45,-43],[-44,-42],[-43,-41],[-42,-40],[-41,-39],[-40,-38],[-39,-37],[-38,-36],[-37,-35],[-36,-34],[-35,-33],[-34,-32],[-33,-31],[-32,-30],[-31,-29],[-30,-28],[-29,-27],[-28,-26],[-27,-25],[-26,-24],[-25,-23],[-24,-22],[-23,-21],[-22,-20],[-21,-19],[-20,-18],[-19,-17],[-18,-16],[-17,-15],[-16,-14],[-15,-13],[-14,-12],[-13,-11],[-12,-10],[-11,-9],[-10,-8],[-9,-7],[-8,-6],[-7,-5],[-6,-4],[-5,-3],[-4,-2],[-3,-1],[-2,0],[-1,1],[0,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13],[12,14],[13,15],[14,16],[15,17],[16,18],[17,19],[18,20],[19,21],[20,22],[21,23],[22,24],[23,25],[24,26],[25,27],[26,28],[27,29],[28,30],[29,31],[30,32],[31,33],[32,34],[33,35],[34,36],[35,37],[36,38],[37,39],[38,40],[39,41],[40,42],[41,43],[42,44],[43,45],[44,46],[45,47],[46,48],[47,49],[48,50],[49,51],[50,52],[51,53],[52,54],[53,55],[54,56],[55,57],[56,58],[57,59],[58,60],[59,61],[60,62],[61,63],[62,64],[63,65],[64,66],[65,67],[66,68],[67,69],[68,70],[69,71],[70,72],[71,73],[72,74],[73,75],[74,76],[75,77],[76,78],[77,79],[78,80],[79,81],[80,82],[81,83],[82,84],[83,85],[84,86],[85,87],[86,88],[87,89],[88,90],[89,91],[90,92],[91,93],[92,94],[93,95],[94,96],[95,97],[96,98],[97,99],[98,100],[99,101]]
) # 100