# 1-й способ (скучный)
lst_s_dev = []


def rasshifrovka(n, i=0, j=1):
    lst = [div for div in range(1, n)]
    while i < n - 2:
        while j < n - 1:
            if n % (lst[i] + lst[j]) == 0:
                lst_s_dev.append(lst[i])
                lst_s_dev.append(lst[j])
            j += 1
        i += 1
        j = i + 1
    return "".join([str(i) for i in lst_s_dev])


for i in range(3, 21):
    print(f'{i}-{rasshifrovka(i)}')
    lst_s_dev.clear()

# 2-й способ. Для души. С рекурсией и классом
class Rashifrovka:
    def __init__(self, n):
        self.n = n
        self.lst_s_dev = []

    def __lst_s_dev(self, n, lst):
        if len(lst) == 1 or len(lst) == 0:
            return self.lst_s_dev
        else:
            for i in range(1, len(lst)):
                if n % (lst[0] + lst[i]) == 0:
                    self.lst_s_dev.append(lst[0])
                    self.lst_s_dev.append(lst[i])
            return self.__lst_s_dev(n, lst[1:len(lst)-1])
        
    def __obnulenie(self):
        self.lst_s_dev.clear()

    def _get_one_rshifrovk(self, m):
        lst = [div for div in range(1, m)]
        res = self.__lst_s_dev(m, lst)
        return ''.join([str(i) for i in res])
    
    def get_all_rshifrovk(self):
        for i in range(3, self.n+1):
            s = self._get_one_rshifrovk(i)
            print(f'{i}-{s}')
            self.__obnulenie()

tak = Rashifrovka(20)
# print(tak._get_one_rshifrovk(15))
# tak.get_all_rshifrovk()
