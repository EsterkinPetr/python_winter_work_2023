import re
def grz(ssim):
    res = re.findall(r'\b[ABEKMHOPCTYX]\d\d\d[ABEKMHOPCTYX]{2}1?78\b', ssim)
    print(*res)
    return
grz('A672CB78 A123BC78 X666XX178 A001AA78 B777BW178 JK555CC178')