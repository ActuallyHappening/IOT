def mask(**k):
  print(k)

def test1(**k):
    mask(a=1, **k)

test1(a=2)