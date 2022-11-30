class Plantation:
    def __init__(self, size: int):
        self.size = size
        self.plants = {}
        self.workers = []

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value: int):
        if value < 0:
            raise ValueError("Size must be positive number!")
        self.__size = value

    def hire_worker(self, worker: str):
        if worker in self.workers:
            raise ValueError("Worker already hired!")

        self.workers.append(worker)
        return f"{worker} successfully hired."

    def __len__(self):
        count_of_plants = 0
        for plants_planted in self.plants.values():
            count_of_plants += len(plants_planted)
        return count_of_plants

    def planting(self, worker: str, plant: str):
        if worker not in self.workers:
            raise ValueError(f"Worker with name {worker} is not hired!")

        elif len(self) >= self.size:
            raise ValueError("The plantation is full!")
        if worker in self.plants.keys():
            self.plants[worker].append(plant)
            return f"{worker} planted {plant}."
        self.plants[worker] = [plant]
        return f"{worker} planted it's first {plant}."

    def __str__(self):
        result = [f"Plantation size: {self.size}"]
        result.append(f'{", ".join(self.workers)}')
        for worker, plants in self.plants.items():
            result.append(f"{worker} planted: {', '.join(plants)}")
        return '\n'.join(result)

    def __repr__(self):
        result = ''
        result += f'Size: {self.size}\n'
        result += f'Workers: {", ".join(self.workers)}'
        return result
