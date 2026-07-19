import csv

def parse_csv(filepath):
    """解析CSV，返回标准数据字典"""
    data = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            data.append([float(x) for x in row])
    
    return {
        'timestamp': [r[0] for r in data],
        'lat': [r[1] for r in data],
        'lon': [r[2] for r in data],
        'alt': [r[3] for r in data],
        'roll': [r[4] for r in data],
        'pitch': [r[5] for r in data],
        'yaw': [r[6] for r in data],
        'voltage': [r[7] for r in data],
        'current': [r[8] for r in data]
    }