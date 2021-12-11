# 2020 KAKAO BLIND RECRUITMENT _ 문자열압축
import sys

def solution(s):
    answer = 0
    k = s
    
    sub_key = 1000
    for s in range(1,len(k)):
        n = s
        k_list = [k[i*n:(i+1)*n] for i in range ((len(k)*n)//n)]
        while '' in k_list:
            k_list.remove('')
        s_list = []
        cnt = 1

        for i in range(len(k_list)-1):

            if (k_list[i] == k_list[i+1]):
                cnt += 1
                
                if(i == len(k_list)-2):
                    s_list.append(cnt)
                    s_list.append(k_list[i])
                
            elif (k_list[i] != k_list[i+1]):
                
                if(cnt == 1):
                    s_list.append(k_list[i])
                    
                elif(cnt != 1):   
                    s_list.append(cnt)
                    s_list.append(k_list[i])
                    cnt = 1
                    
        if(k_list[len(k_list)-1] != k_list[len(k_list)-2]):
            s_list.append(k_list[len(k_list)-1])
            
        

        s_cnt = 0
        for x in range(len(s_list)):
            s_str = str(s_list[x])
            s_cnt += len(s_str)
            
        if(sub_key > s_cnt):
            sub_key = s_cnt
    if(len(k) == 1):
        sub_key = 1
    answer = sub_key
    
    return answer

s = sys.stdin.readline().rstrip('\n')
print(solution(s))