
import pandas as pd
import os
sql_template = "UPDATE table SET {columns} WHERE column_name = '{building_name}' and city_id = {city};"

'''
 读取excel文件 将标题和对应的数据组装成 Update sql 并按照城市输出到文件
'''
def append_building_sql():

    # 读取Excel文件
    excel_file_path = '/Users/telltao/Downloads/taoNew1.xlsx'

    df = pd.read_excel(excel_file_path)

    # 数据库字段与Excel列的映射关系
    column_mapping = {
        '楼层-变更后': 'floor_total',
        '入住率-变更后': 'occupancy_rate',
        '入住规模-变更后': 'occupancy_scale',
        '楼栋数-变更后': 'building_total'
    }

    city_mapping = {
        '北京': 4,
        '上海': 5,
        '广州': 6,
        '深圳': 7,
        '杭州': 8,
        '成都': 9,
        '佛山': 71,
    }

    # 处理每个城市的数据
    for city_name, city_code in city_mapping.items():
        city_output = []  # 用于存储当前城市的SQL语句
        # python 读取excel 输出的格式是字典式的 例如: row = ('城市','北京') ('楼盘名称','国贸大厦') ....
        for index, row in df.iterrows():
            if pd.notna(row['楼盘名称']) and row['城市'] == city_name:
                columns_values = []
                # 这里的 col = excel的表头 : 城市, 楼盘名称
                for col in df.columns:
                    if pd.notna(row[col]) and col in column_mapping:
                        if col in ['楼层-变更后', '入住规模-变更后']:
                            value = str(int(row[col])) # 保持整数
                        else:
                            value = str(row[col])
                        # 在这里找到 column_mapping字典中  楼盘名称对应的value 然后拼接 f 是格式化
                        columns_values.append(f"{column_mapping[col]} = '{value}'")
                # 将得到的数据格式化到提供的模板里 columns=',  是将
                sql_query = sql_template.format(columns=', '.join(columns_values), building_name=row['楼盘名称'],
                                                city=city_code)
                city_output.append(sql_query)

        # 将当前城市的SQL语句写入文本文件
        with open(f"{city_name}_output.txt", "w") as file:
            for query in city_output:
                file.write(query + "\n")


if __name__ == '__main__':
    append_building_sql()
    current_working_directory = os.getcwd()
    print("当前工作目录：", current_working_directory)
