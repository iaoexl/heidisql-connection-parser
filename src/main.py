#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import sys

# 合并读取配置文件的函数
def read_lines(file_path, keyword):
    try:
        with open(file_path, encoding="utf-8") as f:
            return [r.strip() for r in f.readlines() if keyword in r]
    except FileNotFoundError:
        print(f"错误：未找到配置文件 {file_path}")
        return []
    except Exception as e:
        print(f"错误：读取配置文件时发生错误 - {e}")
        return []

# 合并提取信息的函数
def extract_info(lines):
    return [re.split("<\|\|\|>", r)[-1] for r in lines]

def heidipass(code):
    """
    解密HeidiSQL加密密码
    :param code: 加密密码
    :return: 解密后的密码
    """
    ascii_part = code[:-1]
    d = int(code[-1])
    decode = lambda x: chr(int(x, 16) - d)
    password = ''.join(map(decode, re.findall("\w{2}", ascii_part)))
    return password

NET_TYPE_MAP = {
    '0': "MariaDB or MySQL (TCP/IP)",
    '1': "MariaDB or MySQL (named pipe)",
    '2': "MariaDB or MySQL (SSH tunnel)",
    '3': "Microsoft SQL sesrver (named pipe)",
    '4': "Microsoft SQL sesrver (TCP/IP)",
    '5': "Microsoft SQL sesrver (SPX/IPX)",
    '6': "Microsoft SQL sesrver (Banyan VINES)",
    '7': "Microsoft SQL sesrver (Windows RPC)",
    '8': "PostgreSQL (TCP/IP)",
    '9': "PostgreSQL (SSH tunnel)",
    '10': "SQLite",
    '11': "ProxySQL Admin (Experimental)",
    '12': "Interbase (TCP/IP, experimental)",
    '13': "Interbase (Local, experimental)",
    '14': "Firebird (TCP/IP, experimental)",
    '15': "Firebird (Local, experimental)",
    '16': "MySQL on RDS",
    '17': "SQLite (Encrypted)"
}

if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)
    settings_file = os.path.join(application_path, "heidisql_settings.cfg")
    # 提取各项信息
    passwords = extract_info(read_lines(settings_file, "\\Password<"))
    hosts = extract_info(read_lines(settings_file, "\Host<"))
    ports = extract_info(read_lines(settings_file, "\Port<"))
    users = extract_info(read_lines(settings_file, "\\User<"))
    net_types = extract_info(read_lines(settings_file, "\\NetType<"))
    #print('提取到的网络类型列表:', net_types)
    net_type_ids = [NET_TYPE_MAP.get(net_type, 'read_error') for net_type in net_types]

    # 检查是否有信息为空
    if not all([passwords, hosts, ports, users, net_type_ids]):
        print("错误：部分数据库连接信息为空或未获取到，请检查配置文件。")
    else:
        # 按NetType分组
        grouped_info = {}
        for host, port, user, password_encoded, net_type_id in zip(hosts, ports, users, passwords, net_type_ids):
            host = host if host else "read_error"
            port = port if port else "read_error"
            user = user if user else "read_error"
            password = heidipass(password_encoded) if password_encoded else "read_error"
            if net_type_id not in grouped_info:
                grouped_info[net_type_id] = []
            grouped_info[net_type_id].append((host, port, user, password))

        # 按组输出结果
        print("The database connection information is as follows:")
        log_file_path = os.path.join(application_path, "heidisql_acc.log")
        with open(log_file_path, 'w', encoding='utf-8') as log_file:
            log_file.write("The database connection information is as follows:\n")
            for net_type_id, connections in grouped_info.items():
                print(f"Database Type: {net_type_id}")
                log_file.write(f"Database Type: {net_type_id}\n")
                print("{:<20} {:<20} {:<20} {:<20}".format("Host", "Port", "User", "Password"))
                log_file.write("{:<20} {:<20} {:<20} {:<20}\n".format("Host", "Port", "User", "Password"))
                for host, port, user, password in connections:
                    print("{:<20} {:<20} {:<20} {:<20}".format(host, port, user, password))
                    log_file.write("{:<20} {:<20} {:<20} {:<20}\n".format(host, port, user, password))
                print()
                log_file.write("\n")
input('Press "Enter" to end the program.')
