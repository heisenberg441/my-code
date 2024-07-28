class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d=set(cards)
        if len(d)==len(cards):
            return -1
        else:
            d={}
            minn=len(cards)
            for i in range(len(cards)):
                if cards[i] in d:
                    minn=min(minn,i-d[cards[i]]+1)
                    
                d[cards[i]]=i
            return minn