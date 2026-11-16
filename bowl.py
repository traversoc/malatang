class Bowl:
    def __init__(self):
        self.items = []

    def add(self, name, weight):
        self.items.append({"name": name, "weight": weight})

    def total_weight(self):
        return sum(item["weight"] for item in self.items)
