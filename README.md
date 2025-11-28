# Ansible
## Ansibleの前提条件（制御ノードと対象ノード）
### 💻 制御ノード (Control Node) の前提条件

Ansibleを実行するノードです。

| OS | 必須条件 | 補足事項 |
| :--- | :--- | :--- |
| **Linux / macOS** | **Python 3.8 以降** | Ansible CoreはPythonで書かれているため、実行にはPythonが必要です。 |
| | **pip** | Ansibleパッケージをインストールするために必要です。 |
| | **OpenSSH クライアント** | Linux/macOSが標準で搭載しているSSHクライアント（`ssh`コマンド）が必要です。これが**リモート接続の主要な手段**となります。 |
| **Windows** | **非サポート** | Windowsは**制御ノードとして正式にはサポートされていません**。Ansibleを実行するためには、Linux環境（WSLを含む）またはmacOSを使用する必要があります。 |

> 💡 **ポイント**: Ansibleは対象ノードにエージェントをインストールする必要がないため、制御ノードに必要なのは、Ansible本体、Python、そして接続手段（SSH）だけです。

## 🎯 対象ノード (Managed Node) の前提条件

Ansibleによって構成管理されるノードです。

| OS | 必須条件 | 接続方式 |
| :--- | :--- | :--- |
| **Linux / macOS** | **Python 3.5 以降** | モジュール（Ansibleの作業単位）を実行するために必須です。 |
| | **OpenSSH サーバー** | 制御ノードからの接続を受け付けるためのSSHサーバーが必要です。 |
| | **sftp または scp** | ファイル転送のために必要です（通常SSHサーバーに含まれています）。 |
| **Windows** | **PowerShell 3.0 以降** | モジュールの実行環境としてPowerShellが必要です。 |
| | **Python は不要** | Windowsノードでは、AnsibleはWS-Management (WinRM) 接続を通じてPowerShellスクリプトを実行するため、**Pythonは必須ではありません**。 |
| | **WinRM サービス** | **WS-Management (WinRM)** サービスが実行され、Ansible制御ノードからの接続を受け付けるように構成されている必要があります。これが**リモート接続の主要な手段**となります。 |

> 💡 **Windowsに関する補足**: Windowsを対象ノードとする場合、Linux/macOSのようなSSH接続ではなく、**WinRM**接続が推奨されます。WinRMの適切な設定はLinuxのSSH設定よりも複雑になる傾向があるため、Ansibleの公式ドキュメントにある「Setting up a Windows Host」を参照して設定を行う必要があります。

## install
* python
    ```
    ubuntu@ip-172-31-46-156:~/ansible$ python3 -m venv venv
    ubuntu@ip-172-31-46-156:~/ansible$ source venv/bin/activate
    (venv) ubuntu@ip-172-31-46-156:~/ansible$ python --version
    Python 3.13.8
    ```

* ansible
    ```
    (venv) ubuntu@ip-172-31-46-156:~/ansible/step1$ pip install ansible
    Collecting ansible
    Using cached ansible-13.0.0-py3-none-any.whl.metadata (8.1 kB)
    ・・・
    ```

    ```
    (venv) ubuntu@ip-172-31-46-156:~/ansible/step1$ ansible --version
    ansible [core 2.20.0]
    config file = None
    configured module search path = ['/home/ubuntu/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
    ansible python module location = /home/ubuntu/ansible/venv/lib/python3.13/site-packages/ansible
    ansible collection location = /home/ubuntu/.ansible/collections:/usr/share/ansible/collections
    executable location = /home/ubuntu/ansible/venv/bin/ansible
    python version = 3.13.8 (main, Oct  8 2025, 08:53:25) [GCC 13.3.0] (/home/ubuntu/ansible/venv/bin/python3)
    jinja version = 3.1.6
    pyyaml version = 6.0.3 (with libyaml v0.2.5)
    ```

## inventory.ini
* simple (localhost only)
    ```
    # inventory.ini
    [all]
    localhost ansible_connection=local

    [all:vars]
    ansible_python_interpreter=/usr/bin/python
    ```

## run builtin commands
1. ping
    ```
    (venv) ubuntu@ip-172-31-46-156:~/ansible/step1$ ansible all -i inventory.ini -m ansible.builtin.ping
    localhost | SUCCESS => {
        "changed": false,
        "ping": "pong"
    }    
    ```
