# docker立ち上げ方法(WSL2)

## インストール

マニュアルそのまま実行。docker desktopとかは不要

``` bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt update
sudo apt install -y docker-ce docker-compose-plugin
```

その後、面倒なsudoをdokcerコマンド実行時に省略するため、以下のコマンドを実行
```
sudo usermod -aG $(whoami) docker 
```

## 開始

以下でdemonを動かす形にしてからdockerのコンテナ実行をする
> sudo service docker start
> docker run (コンテナ名)

demonが動いているか確認するには以下コマンド実行
> sudo service docker status

## トラブルシューティング

以下のログでdockerの実行ログが見れるので、こちらからerror情報を探る
>  cat /var/log/docker.log

## dockerのdemonが起動しない(WSL2)

WSL2のバグでネットワークコントローラが動作しない問題がある模様
[詳細](https://blog.ecbeing.tech/entry/2021/09/07/150000)

その関係で「sudo service docker start」を実行してもdaemonが起動しない問題がある

対応策として、以下コマンドを実行
> sudo update-alternatives --config iptables

設定どうするか聞かれるので1を選択

``` bash
$ sudo update-alternatives --config iptables
There are 2 choices for the alternative iptables (providing /usr/sbin/iptables).

  Selection    Path                       Priority   Status
------------------------------------------------------------
* 0            /usr/sbin/iptables-nft      20        auto mode
  1            /usr/sbin/iptables-legacy   10        manual mode
  2            /usr/sbin/iptables-nft      20        manual mode

Press <enter> to keep the current choice[*], or type selection number: 1
update-alternatives: using /usr/sbin/iptables-legacy to provide /usr/sbin/iptables (iptables) in manual mode
```