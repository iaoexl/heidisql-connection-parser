# HeidiSQL 连接配置解析工具(heidisql‑config‑decoder)

>  ⚠️ **法律免责声明**
>  
>  本工具**仅限解析你自己从 HeidiSQL 导出的配置文件**，仅用于找回自己遗忘的数据库连接密码。
>  
>  未经授权获取他人数据库账号密码属于违法行为，全部安全与法律责任由使用者自行承担。
> 
> [main.py](src/main.py)  脚本在Windows环境中运行、测试，适配 [python-3.10](https://www.python.org/ftp/python/3.10.0/python-3.10.0rc2-amd64.exe) 程序。
> 

## 代码来源说明
> 本项目脚本基于互联网开源社区、公开论坛公开的代码片段进行整理、修复与改造。
> 
> 仅做技术学习演示使用，不代表原作者立场。

## 📋项目简介
Python脚本，解析 HeidiSQL 导出的配置文件 `heidisql_settings.cfg`，解密软件加密保存的数据库密码，输出连接信息。
> ⚠️脚本**不会自动读取注册表或程序内存，必须手动导出cfg配置文件**。

### ✅支持解析的连接类型
- MariaDB / MySQL（TCP、命名管道、SSH隧道）
- Microsoft SQL Server
- PostgreSQL（TCP、SSH隧道）
- SQLite / SQLite(Encrypted)
- Firebird、Interbase、ProxySQL Admin、MySQL‑RDS

脚本输出内容：连接类型、Host、Port、User、解密后Password；同时自动输出明文结果到本地日志文件。

### ⚠️版本与系统限制
- 脚本本身无平台限制，但 `heidisql_settings.cfg` 只能由 Windows 端 HeidiSQL 导出。
- 依赖 HeidiSQL 原有加密算法；如果后续版本更新加密逻辑，解密将会失效。
- 字段读取失败时会标记为 `read_error`。

## 🧰环境依赖
> 仅使用Python标准库，无需安装第三方依赖
```bash
# 直接运行，不需要pip安装包
python src/main.py
```

## 打包为可执行程序
> 安装 `pyinstaller`

``` bash
pip install pywin32
pip install pyinstaller
```

> 参数函数

- -F 表示生成单个可执行文件
	
- -w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！
	
- -p 表示你自己自定义需要加载的类路径，一般情况下用不到
	
- -i 表示可执行文件的图标

> 打包举例

``` bash
# 打包为 exe 可执行文件
	pyinstaller -F main.py
# 加载 logo
	pyinstaller -F -i `icon\logo.ico` main.py
# 完整打包案例
	pyinstaller -F --clean --noconfirm --hidden-import=heidisql‑config‑decoder --name heidisql‑config‑decoder main.py
```

## notepad++ 运行python脚本
```bash
cmd /k cd /d "$(CURRENT_DIRECTORY)" & python "$(FULL_CURRENT_PATH)" & echo. & pause & exit
```