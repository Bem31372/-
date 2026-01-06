width = int(input('กว้าง'))
hight = int(input('ยาว'))

def area (width,hight):
    reg = width*hight
    tri = (1/2)*width*hight
    print(f'reg = {reg} and tri = {tri}')
    return(reg,tri)

area_rec , area_tri = area(width,hight)
print(f"พื้นที่สีเหลี่ยม:{area_rec}")
print(f"พื้นที่สามเหลี่ยม:{area_tri}")

