*shapes, regions = open('input.txt').read().strip().split('\n\n')

sizes = [shape.count('#') for shape in shapes]

regions = [
    list(map(int, region.replace(':','').replace('x',' ').split()))
        for region in regions.split('\n')
]

print( sum(w*h >= sum([x*y for x,y in zip(ns,sizes)]) for w,h,*ns in regions) )
