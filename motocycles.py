motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

# motocycles[0] = 'ducati'
# print(motocycles)

motocycles.append('ducati')
print(motocycles)

motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')
print(motocycles)

motocycles.insert(0, 'ducati')
print(motocycles)

del motocycles[0]
print(motocycles)

poped_motocycle = motocycles.pop()
print(motocycles)
print(poped_motocycle)

motocycles.remove('honda')
print(motocycles)
