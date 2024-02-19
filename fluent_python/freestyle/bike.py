class Bike:
    
    def __init__(self, name:str ,type: str, size: str, price: float, year:int):
        self.name = name
        self.type = type
        self.size = size
        self.price = price
        self.year = year
    
    def __repr__(self) -> str:
        return f"Bike(name={self.name!r}, type={self.type!r}, size={self.size!r}, price={self.price}, year={self.year})"

    def __str__(self) -> str:
        return f"{self.name}"
    
    def __len__(self) -> int:
        size = dict(S=1, M=2, L=3)
        return size[self.size]
    set
    def __bool__(self) -> bool:
        return False

if __name__ == "__main__":
    metrix = Bike(name="Metrix", type="city-bike", size="M", price=569.90, year=2023)