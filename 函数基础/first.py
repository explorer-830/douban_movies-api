def out_line():
    print("jbbbbbb")
out_line()
def SanJiaoarea(l,h):
    area=1/2*(l*h)
    return area
print(SanJiaoarea(2,3))
def count_aeiou(s):
    """

    :param s:
    :return:
    """
    num=0
    L="aeiou"
    for w in s:
        if w in L:
            num+=1
    print(f"有{num}个元音字母")
count_aeiou("qyuwgfruywtgqw")
SNA=[2,6,4,9,3,2,8,9,]
print(max(SNA))