# HeidiSQL 连接配置解析工具（heidisql-connection-parser）

>  ⚠️ **法律免责声明**
>  
>  本工具**仅限解析你自己从 HeidiSQL 导出的配置文件**，仅用于找回自己遗忘的数据库连接密码。
>  
>  未经授权获取他人数据库账号密码属于违法行为，全部安全与法律责任由使用者自行承担。

## 代码来源说明
> 本项目脚本基于互联网开源社区、公开论坛公开的代码片段进行整理、修复与改造。
> 
> 仅做技术学习演示使用，不代表原作者立场。
> 
> [main.py](src/main.py)  脚本在Windows环境中运行、测试，适配 [python-3.10](https://www.python.org/ftp/python/3.10.0/python-3.10.0rc2-amd64.exe) 程序。

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

## notepad++ 运行python脚本
```bash
cmd /k cd /d "$(CURRENT_DIRECTORY)" & python "$(FULL_CURRENT_PATH)" & echo. & pause & exit
```

## 代码推送与镜像同步说明

本项目的代码推送流程如下：

```text
本地代码 → AtomGit → 自动镜像同步 → 腾讯云 CNB / GitHub / Gitee
```

## 你可以在这些地方找到我 (Find Me Here)

<p align="center">
  <a href="https://gitcode.com/techtest/heidisql-connection-parser.git" target="_blank" rel="noopener">
    <img src="images/6e5e33151cf7d4b69bc75e984af332d9.png" width="18" height="18" alt="GitCode">&nbsp;GitCode
  </a>
  <span style="color: #999;">&nbsp;/&nbsp;</span>
  <a href="https://atomgit.com/techtest/heidisql-connection-parser.git" target="_blank" rel="noopener">&nbsp;AtomGit
  </a>
  &nbsp;&nbsp;
  <a href="https://cnb.cool/iaoexl/techtest/heidisql-connection-parser.git" target="_blank" rel="noopener">
    <img src="images/204dc4444f152572ee9977c2ee15b1e4.png" width="18" height="18" alt="腾讯云 CNB">&nbsp;腾讯云 CNB
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/iaoexl/heidisql-connection-parser.git" target="_blank" rel="noopener">
    <img src="images/c31718c62908f5248d95dff0fe0c96f7.png" width="18" height="18" alt="GitHub">&nbsp;GitHub
  </a>
  &nbsp;&nbsp;
  <a href="https://gitee.com/techtest/heidisql-connection-parser.git" target="_blank" rel="noopener">
    <img src="images/2765d9743c9a0ddfdf7a9bd9df4cab82.png" width="18" height="18" alt="Gitee">&nbsp;Gitee
  </a>
</p>

<!--
## 支持这个项目（Support This Project）

如果这个项目对你有帮助，欢迎[赞助支持](SPONSOR.md)。
-->