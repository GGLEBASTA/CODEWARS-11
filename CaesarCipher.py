class CaesarCipher:
    """Класс обрабатывает строку из латинских букв,сдвигая
    кааждую из них на заданный промежуток shift"""
    """Посторонние символы без изменений заносятся в обработанную строку"""
    def __init__(self, shift): #метод хранит в себе лат.алфавит(нижний регистр) и промежуток сдвига
        self.alpha = [chr(x) for x in range(97, 123)]
        self.dl_alpha = len(self.alpha)
        self.shift = shift


    def encode(self, st): #метод для обработки строки и сдвига каждой буквы вперёд на заданный shift
        self.st = st #обрабатываемая строка
        list_of_new = [] #список для занесения уже обработанных букв и символов
        for i in self.st:
            if(i.lower() not in self.alpha): #если не буква,то сразу заносим
                list_of_new.append(i)
            else:
                index_ = self.alpha.index(i.lower()) #получаем индекс обрабатываемой буквы в лат.алфавите
                if(index_ + self.shift <= self.dl_alpha - 1): #если сдвиг-shift не вышел за границы списка лат.алфавита
                    new_elem = list_of_new.append(self.alpha[index_+self.shift])
                elif(index_ + self.shift > self.dl_alpha - 1): #если сдвиг-shift вышел за пределы списка лат.алфавита
                    new_elem = list_of_new.append(self.alpha[((index_+self.shift) - (self.dl_alpha-1) - 1)])

        list_of_new = [i.upper() for i in list_of_new] #все буквы в верхний регистр
        list_of_new = ''.join(list_of_new) #преобразовываем в строку
        return list_of_new


    def decode(self, st): #метод обратный первому - сдвигает буквы назад (алгоритм тот же,что и в encode)
        self.st = st
        list_of_new2 = []
        for i in self.st:
            if (i.lower() not in self.alpha):
                list_of_new2.append(i)
            else:
                index_ = self.alpha.index(i.lower())
                if(index_-self.shift < 0):
                    new_elem2 = list_of_new2.append(self.alpha[(self.dl_alpha)+(index_ - self.shift)])
                elif(index_-self.shift >= 0):
                    new_elem2 = list_of_new2.append(self.alpha[index_ - self.shift])

        list_of_new2 = [x.upper() for x in list_of_new2]
        list_of_new2 = ''.join(list_of_new2)
        return list_of_new2


m = CaesarCipher(5)
print(m.decode('BFKKQJX'))
