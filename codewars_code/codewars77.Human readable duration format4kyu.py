# Human readable duration format
def zero_one(n):
    if n <= 1:
        return ''
    if n >1:
        return 's'

def format_duration(seconds):
    # divmod()
    answer = ''
    year,last = divmod(seconds,31536000)
    day,last = divmod(last,86400)
    hour,last = divmod(last,3600)
    minute,second = divmod(last,60)
    li = [year,day,hour,minute,second]
    count = 5 - li.count(0)
    #s_year,s_day_,s_hour,s_minute,s_second = zero_one(year),zero_one(day),zero_one(hour),zero_one(minute),zero_one(second)
    s_year = str(year)+' year'+zero_one(year)
    s_day = str(day)+' day'+zero_one(day)
    s_hour = str(hour)+' hour'+zero_one(hour)
    s_minute = str(minute)+' minute'+zero_one(minute)
    s_second = str(second)+' second'+zero_one(second)
    result = [s_year,s_day,s_hour,s_minute,s_second]
    
            
            
    if count == 0:
        return 'now'
    elif count == 1:
        for i in result:
            if i.startswith('0')==False:
                answer += i
    elif count == 2:
        index = 0
        for i in result:
            if i.startswith('0')==False:
                if index == 0:
                    answer = i+' and '
                    index+=1
                else:
                    answer += i
    elif count == 3:
        index = 0
        for i in result:
            if i.startswith('0')==False:
                if index ==0:
                    answer = i+', '
                    index+=1
                elif index ==1:
                    answer += i+' and '
                    index+=1
                else:
                    answer += i
    elif count ==4:
        index = 0
        for i in result:
            if i.startswith('0')==False:
                if index ==0 or index==1:
                    answer += i+', '
                    index+=1
                elif index ==2:
                    answer += i+' and '
                    index+=1
                else:
                    answer += i
    else:
        index = 0
        for i in result:
            if i.startswith('0')==False:
                if index ==0 or index==1 or index ==2:
                    answer += i+', '
                    index+=1
                elif index ==3:
                    answer += i+' and '
                    index+=1
                else:
                    answer += i
    return answer



if __name__ == '__main__':
    r = format_duration(3662)
    print(r)

