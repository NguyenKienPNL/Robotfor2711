class calc_mode:
    def __init__(self, request):
        self.arr = request.rstrip().split()
    def check_opr(self, arr):
        opr = ['+', '-', '*', '/']
        flag = True
        for i in arr:
            if flag and i.isdigit() == False:
                return False
            elif flag == False and i not in opr:
                return False
            if flag == True:
                flag = False
            else:
                flag = True
        if arr[-1].isdigit() == False:
            return False
        return True
    def calc_first(self, arr):
        opr = ['/', '*']
        for i in range(len(arr)):
            if arr[i] in opr:
                a = round(float(arr[i-1]), 2)
                b = round(float(arr[i+1]), 2)
                if arr[i] == '*':
                    res = a * b
                else:
                    res = a/b
                arr[i] = str(res)
                arr.pop(i+1)
                arr.pop(i-1)
                return arr
        return arr
    def calc(self, arr):
        res = 0
        while '*' in arr or '/' in arr:
            arr = self.calc_first(arr)
        is_add = True
        for i in arr:
            if i == '+':
                is_add = True
            elif i == '-':
                is_add = False
            else:
                if is_add:
                    res += float(i)
                else:
                    res -= float(i)
        return round(res, 2)