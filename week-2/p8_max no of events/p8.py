
def maxEvents(e): #-&gt; int:
    lo = min(e[0] for e in events)
    hi = max(e[1] for e in events)
    seen = [0] * (hi - lo + 1)
    for s, t in sorted(events, key=lambda e:e[1]):
      for i in range(s, t + 1):
        if seen[i - lo]: continue
        seen[i - lo] = 1
        break
    return sum(seen)
a=[[1,2],[2,3],[3,4],[1,2]]
print(maxEvents(a))