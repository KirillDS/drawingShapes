def bigbox3(symbol, width, height, space):
    if len(symbol) != 1:
        raise Exception('Symbol: Symbol should be One String Character Long.')
    if len(space) != 1:
        raise Exception('Space: Space should be One String Character Long.')
    if width < 8:
        raise Exception('Width: Width should be Greater than 8.')
    if height < 8:
        raise Exception('Height: Height should be Greater than 8.')
    print(symbol * width)
    for u in range(height - 2):
        print(symbol +(space*(width - 2))+ symbol)
    print(symbol * width)
for symbol, width, height, space in (('E',10,10,'-'),('JJ',8,8,'o'),('K',4,9,'l'),('4',9,3,'k'),('9',9,9,'ii')):
    try:
        bigbox3(symbol, width, height, space)
    except Exception as bb3:
        print('An Exception was raised at '+str(bb3))
#
