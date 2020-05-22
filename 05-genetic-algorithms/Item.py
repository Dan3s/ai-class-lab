from KnapsackGenetic import KnapsackGenetic

class Item:
  def __init__(self, value, weight):
    self.value = value
    self.weight = weight

params = {
    "mutation_percentage": 0.8,
    "select_top": 0.2,
    "generation_size": 20,
    "fit_threshold": 1.0,
    "max_generations": 1000,
    "max_weight": 19,
    "max_per_item": 1,
    "items": [Item(4, 12), Item(2, 2), Item(2, 1), Item(1, 1), Item(10,4)]
}

knapsack = KnapsackGenetic(params)
#print (params["items"])
knapsack.run()