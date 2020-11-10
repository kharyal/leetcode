class tree:
    def __init__(self, arr):
        self.arr = arr
        self.segment_tree = [0]*(4*len(arr))
        self.build(0, len(arr)-1, 0)

    def build(self,l,r, ind):
        if l==r:
            self.segment_tree[ind] = (self.arr[l], l,l)
            return
        m = (l+r)//2
        self.build(l, m, 2*ind+1)
        self.build(m+1, r, 2*ind+2)
        self.segment_tree[ind] = (self.segment_tree[2*ind +1][0] + self.segment_tree[2*ind +2][0], l,r)
    
    def query(self, l, r, ind):
        # print(l, r, ind)
        if self.segment_tree[ind][1] == l and self.segment_tree[ind][2] == r:
            return self.segment_tree[ind][0]
        
        elif self.segment_tree[ind][1]>r or self.segment_tree[ind][2]<l:
            return 0
        
        elif (self.segment_tree[ind][1]<=l and self.segment_tree[ind][2]>=l) or (self.segment_tree[ind][1]<=r and self.segment_tree[ind][2]>=r):
            mid = (self.segment_tree[ind][1]+self.segment_tree[ind][2])//2 
            return self.query(l, min(mid,r), 2*ind+1) + self.query(max(mid+1, l), r, 2*ind+2)

t = tree([1,2,3,4,5,6])
print(t.query(0,5,0))