def check_coupon(entered_code,correct_code,current_date,expiration_date):
    if len(entered_code) != len(correct_code):
        return False
    else:
        for i in range(len(entered_code)):
            if entered_code[i] != correct_code[i]:
                return False

    
