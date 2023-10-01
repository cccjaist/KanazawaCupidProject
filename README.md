# KanazawaCupidProject

## 初めてインストールする人向け

1. pythonをインストール([リンク](https://www.python.org/downloads/))<br/>
	 最新バージョン(3.1系)をダウンロード<br/>
   インストール時に「Add Python 3.X to PATH」にチェックを入れて「Install Now」をクリックする
  
2. pipenvをインストール<br/>
	 コマンドプロンプトを起動し、以下のコマンドを入力する

```
pip install pipenv
```

3. Visual Studio installerをインストールする([リンク](https://visualstudio.microsoft.com/ja/downloads/))<br />
	 インストーラを起動し、「Desktop development with C++」をクリックしてダウンロードする

<img width="650" alt="vs2022-installer-workloads" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/07c36018-34b6-4b84-b098-b42ea87dc644">

4. VOICE VOXをインストールする([リンク](https://voicevox.hiroshiba.jp/)

## 一度インストールしたことがある人向け

1. 「<>Code」ボタン、「Download ZIP」ボタンを順にクリックしてプログラムを自分のフォルダにダウンロードする。<br/>
	 ダウンロードしたら、展開してフォルダを開く。

<img width="300" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/1b183ab9-5b86-42f0-b4eb-3f7b2130b426">

2. コマンドプロンプトを開き、ダウンロードしたファイルがある階層に移動する。
	 まず「KanazawaCupidProject」のフォルダを開き、上のバーからパスをコピーする。
	 そしてコマンドプロンプトに、以下のコマンドを入力する。

```
cd {コピーしたパスを張り付ける}
```

<img width="650" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/5eccc2d6-304a-407c-9be9-a0327198ced4">
<img width="650" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/4c529b9c-4af7-478c-83d9-62c8b793dc0d">

3. ダウンロードしたファイルの中に'.env'という名前のファイルを作成する。そして以下の内容を保存する。
	 ChatGPTのAPI Keyは、公式ページからDL可能です。もしくは@makabi_bmkに聞いてください。

```
OPENAI_API_KEY={chatGPTのAPIKey}
OPENAI_ORGANIZATION={chatGPTのOrganization Key}
```

### 起動方法

1. VOICE VOXを起動しておく。

2. コマンドプロンプトを開き、ダウンロードしたファイルがある階層に移動する。
	 まず「KanazawaCupidProject」のフォルダを開き、上のバーからパスをコピーする。
	 そしてコマンドプロンプトに、以下のコマンドを入力する。

```
cd {コピーしたパスを張り付ける}
```

<img width="650" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/5eccc2d6-304a-407c-9be9-a0327198ced4">
<img width="650" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/4c529b9c-4af7-478c-83d9-62c8b793dc0d">

3. 2で開いたコマンドプロンプトに、以下のコマンドを入力する。

```
pipenv run start
```
