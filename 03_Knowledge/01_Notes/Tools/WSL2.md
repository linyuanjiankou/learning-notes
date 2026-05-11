之前在研究配置Docker的时候，下载了WSL 2，这里列举一些可能会用到的交互指令。
#### 常规操作：
- `wsl`: 进入默认Linux系统
- `exit`: 退出Linux进入Windows终端
- `wsl -l -v`: 在Windows终端中查看已下载的发行版和对应状态
- `wsl -d 系统名称(Ubuntu)`: 直接进入某一个系统
- `wsl --set-default 系统名称(Debian)`: 将某一个系统设置为默认
- `wsl --install 系统名称`: 安装其他系统
- `wsl --list --online`: 查看可在WSL上安装的发行版列表
#### 更改存储位置：
- `Get-ChildItem "HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss" -Recurse`: 查看虚拟磁盘的物理位置
- `wsl --shutdown`: 关闭所有WSL实例
- `wsl --export Ubuntu D:\path\backup\ubuntu-backup.tar`: 将指定发行版导出为tar包（以Ubuntu为例，提前新建文件夹并替换掉`D:\path\backup`）
- `wsl --unregister Ubuntu`: 注销原有的发行版
- `wsl --import Ubuntu D:\new\wsl\location D:\path\backup\ubuntu-backup.tar --version 2`: 在新位置重新导入原来的发行版（将 D:\new\wsl\location 替换为你希望存放新系统文件的目标文件夹，D:\path\backup\ubuntu-backup.tar 替换为刚才备份文件的实际路径）
#### 其他：
- `wsl --help`: 查找命令

### 常见命令速查
### 1.安装与基础设置

|命令|说明|
|---|---|
|wsl --install|安装 WSL 和默认的 Linux 发行版（通常是 Ubuntu）|
|wsl --list --online|查看可安装的 Linux 发行版列表|
|wsl --install -d <发行版名称>|安装指定的 Linux 发行版（例如：-d Ubuntu-22.04）|
|wsl --set-default-version 2|设置新安装的发行版默认使用 WSL 2|
|wsl --update|手动更新 WSL 内核|
|wsl --version|查看 WSL 版本信息|

### 2.发行版管理

|命令|说明|
|---|---|
|wsl -l -v 或 wsl --list --verbose|列出所有已安装的发行版及其状态、WSL 版本|
|wsl -t <发行版> 或 wsl --terminate <发行版>|终止指定发行版的运行|
|wsl --shutdown|立即终止所有正在运行的发行版和 WSL 2 虚拟机|
|wsl --set-version <发行版> 2|将指定发行版转换为 WSL 2|
|wsl --set-default <发行版>|设置默认使用的发行版|
|wsl --unregister <发行版>|注销并删除指定发行版（会清空该发行版的所有数据）|

### 3.运行与交互

|命令|说明|
|---|---|
|wsl 或 wsl ~|启动默认发行版，并进入 Linux 家目录|
|wsl -d <发行版>|启动指定的发行版|
|wsl -u <用户名> 或 wsl --user <用户名>|以指定用户身份运行|
|wsl --cd <目录>|指定启动时的工作目录（Windows 路径或 Linux 路径）|
|wsl --exec <命令>|执行单个 Linux 命令并退出（例如：wsl --exec ls -la）|
|wsl -e <命令>|同上，--exec 的简写|

### 4.导入/导出与备份

|命令|说明|
|---|---|
|wsl --export <发行版> <文件名.tar>|将发行版导出为 tar 文件（备份）|
|wsl --import <新发行版> <安装目录> <文件名.tar>|从 tar 文件导入新的发行版|
|wsl --import-in-place <发行版> <文件名.vhdx>|从 VHDX 文件直接导入（WSL 2 专用）|

### 5.文件互访

|位置/命令|说明|
|---|---|
|\\wsl.localhost\<发行版> 或 \\wsl$\<发行版>|在 Windows 资源管理器中访问 Linux 文件（网络路径）|
|explorer.exe .|在 Linux 终端中打开当前目录到 Windows 资源管理器|
|/mnt/c/|在 Linux 中访问 Windows C 盘（其他盘符同理）|

### 6.其他命令

| 命令           | 说明                         |
| ------------ | -------------------------- |
| wsl --status | 查看 WSL 的全局状态（默认版本、内核版本等）   |
| wsl --help   | 查看所有可用命令的帮助信息              |
| wsl --system | （仅 WSL 2）启动一个专用的“系统分发”用于调试 |