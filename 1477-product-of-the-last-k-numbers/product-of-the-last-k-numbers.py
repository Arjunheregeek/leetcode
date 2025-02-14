class ProductOfNumbers:

    def __init__(self):
        self.ls = []
    
    def add(self, num: int) -> None:
        if num == 0:
            self.ls.clear()  # Reset on zero
        else:
            if self.ls:
                self.ls.append(self.ls[-1] * num)  # Multiply with last product
            else:
                self.ls.append(num)  # Start fresh if list is empty
    
    def getProduct(self, k: int) -> int:
        if k > len(self.ls):  
            return 0  # If k is larger than the available products
        
        if k == len(self.ls):
            return self.ls[-1]
        
        return self.ls[-1] // self.ls[-k-1]