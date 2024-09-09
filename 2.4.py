x1 = input("Coordonnée en x du premier point : ")
y1 = input("Coordonnée en y du premier point : ")
x2 = input("Coordonnée en x du deuxième point : ")
y2 = input("Coordonnée en y du deuxième point : ")
distance = (((int(x2)-int(x1))**2)+((int(y2)-int(y1))**2))**0.5
print(f"La distance entre le premier et le deuxième point est {distance}")