for x in range(0, 200):
    for y in range(0, 3103):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 400:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
