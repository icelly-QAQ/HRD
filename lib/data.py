# 有关数据存放

def read_map(path:str, map_x, map_y):
    '''
    读取地图文件。

    参数：
    path: 文件路径

    返回：
    地图列表:list, 分数:int
    '''
    lib = open(path)
    map_list = []
    map_temp = lib.readlines()  # 逐行读取数据

    marks = 0
    if len(map_temp) > ((map_x * map_y) * 2):  # 获取此存档中的分数
        marks = int(map_temp[-1])

    for i in range(map_x * map_y):  # 处理存储时生成的 \n
        map_list.append(int(map_temp[i].replace("\n", "")) - int(map_temp[(map_x * map_y) + i].replace("\n", "")))
    map_temp = []  # 清空临时列表
    for i in range(0, map_y):  # 切片列表
        map_temp.append(map_list[:map_x])
        del map_list[:map_x]
    lib.close()
    return map_temp, marks

def create_map(x: int, y: int) -> list:
    """
    创建指定行数和列数的地图，最后一个数值固定为0。
    
    参数：
    x: 地图的行数。
    y: 地图的列数。
    
    返回值：
    创建的地图，表示为二维列表。
    """
    map_data = []
    number = 1
    
    for i in range(x):
        row = []
        for j in range(y):
            if i == x - 1 and j == y - 1:
                row.append(0)
            else:
                row.append(number)
                number += 1
        map_data.append(row)
    
    return map_data

def map_size(map_list: list) -> tuple:
    """
    获取地图的长宽。
    
    参数：
    map_list: 地图，表示为二维列表。
    
    返回值：
    地图的行数和列数，以元组形式返回 (x, y)。
    """
    x = len(map_list)
    y = len(map_list[0]) if x > 0 else 0
    
    return x, y