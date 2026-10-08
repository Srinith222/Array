class Array:
    def __init__(self):
        self._data = []

    def append(self, value):
        self._data.append(value)
        return self

    def insert(self, index, value):
        if index < 0 or index > len(self._data):
            raise IndexError("Index out of range")
        self._data.insert(index, value)
        return self

    def remove(self, value):
        if value not in self._data:
            raise ValueError(f"{value} not found in array")
        self._data.remove(value)
        return self

    def search(self, value):
        try:
            return self._data.index(value)
        except ValueError:
            return -1

    def sort(self):
        self._data.sort()
        return self

    def reverse(self):
        self._data.reverse()
        return self

    def size(self):
        return len(self._data)

    def get(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return f"Array({self._data})"


if __name__ == "__main__":
    arr = Array()
    arr.append(5)
    arr.append(10)
    arr.append(7)
    arr.insert(1, 15)

    print("Array:", arr)
    print("Size:", arr.size())
    print("Search for 10:", arr.search(10))

    arr.sort()
    print("Sorted:", arr)

    arr.reverse()
    print("Reversed:", arr)

    print("Item at index 2:", arr.get(2))
