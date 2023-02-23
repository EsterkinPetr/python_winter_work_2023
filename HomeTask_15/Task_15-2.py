import re
def grz(ssim):
    res = re.findall(r'[ABEKMHOPCTYX]\d\d\d[ABEKMHOPCTYX]{2}1?78', ssim)
    print(*res)
    return
grz('dgvA672CB78A123BC78X666XnbchbcX178 A001AA278 B777BW178 JK555CC17812nb78h')