def bouncingBall(h,bounce,window):
    count = -1
    if 0 < bounce < 1:
        while h > window >0:
            count += 2
            h *= bounce
    return count

if __name__ == '__main__':
    r = bouncingBall(30,0.66,1.5)
    print(r)
