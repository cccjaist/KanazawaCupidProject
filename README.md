# KanazawaCupidProject

## 初めてインストールする人向け

1. pythonの最新バージョン(3.1系)をインストールする([リンク](https://www.python.org/downloads/))<br/>
   インストール時に「Add Python 3.X to PATH」にチェックを入れて「Install Now」をクリックする

![image](https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/1e80a7dc-77f9-49d0-8d7a-b9b76783d414)


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

1. GitHubの「<>Code」ボタン、「Download ZIP」ボタンを順にクリックしてプログラムを自分のフォルダにダウンロードする。<br/>
	 ダウンロードしたら、zipファイルを解凍して、「KanazawaCupidProject-main」フォルダを開く。

<img width="300" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/1b183ab9-5b86-42f0-b4eb-3f7b2130b426">

2. コマンドプロンプトを開き、ダウンロードしたファイルがある階層に移動する。方法は2つあるので、好きな方を選ぶこと。<br/>
1つ目は、「KanazawaCupidProject-main」フォルダで右クリックし、「ターミナルを開く」をクリックする方法である。

<img width="650" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/8136c4ec-6977-4312-95d6-1696a3b12d06">

---

2つ目の方法では、まず「KanazawaCupidProject-main」のフォルダを開き、上のアドレスバーを右クリックしてパスをコピーする。

<img width="650" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/f0e0ce2a-d21a-4aba-ac67-524824a2906a">

その後コマンドプロンプトに、以下のコマンドを入力する。

```
cd {ここにさっきコピーしたパスを張り付ける}
```

<img width="650" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/453b1969-c32a-49be-8b51-0ac429c6cbb3">


3. ダウンロードしたファイルの中に`.env`という名前のファイルを作成用意する。用意する方法は2種類ある。

**3.1 サークルメンバー向け**

[Googleドライブのリンク](https://drive.google.com/file/d/1kGPLj9V1mLSZLxXrRYHga9ZhQUWcnlMS/view?usp=sharing)にアクセスして、ダウンロードする。<br/>
**注意：ダウンロードするとき、なぜかファイル名が「.env」から「env」に勝手に書き換わってしまうことがある！必ず「.env」という名前で保存すること。**

<img width="650" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/300e1327-38b0-4a47-bf08-a159be84d555">

<img width="650" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/1f8a2eb5-125e-4e19-a9e8-6fc02a143129">

ダウンロードした「.env」ファイルを、「KanazawaCupidProject-main」の中へ移動させる。

<img width="650" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/7cbfb820-7fbd-4598-aff6-2cf26a6df4b7">

**3.2 サークル以外のメンバー向け**

<img width="650" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/bf250f4e-39ad-4749-9381-e6fec3235616">

<img width="650" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/e2dacd60-edf5-43fd-8877-5d937f143ec0">

4. 3で作った`.env`の中身を、以下の内容にして保存する。但し{}の中身は調べて書き換えること。
	 ChatGPTのAPI Keyは、公式ページから生成可能([リンク](https://platform.openai.com/account/api-keys))。

```
OPENAI_API_KEY={chatGPTのAPIKey}
OPENAI_ORGANIZATION={chatGPTのOrganization Key}
```

<img width="650" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/e896dab8-4f42-4fe7-acd9-d24b08460f29">


### 起動方法

1. VOICE VOXを起動しておく。

2. [一度インストールしたことがある人向け](https://github.com/cccjaist/KanazawaCupidProject#%E4%B8%80%E5%BA%A6%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%97%E3%81%9F%E3%81%93%E3%81%A8%E3%81%8C%E3%81%82%E3%82%8B%E4%BA%BA%E5%90%91%E3%81%91)の2の方法と同じ方法で、コマンドプロンプトを開き、ダウンロードしたファイルがある階層に移動する。

3. 2で開いたコマンドプロンプトに、以下のコマンドを入力する。

```
pipenv run start
```

### アプリの使い方

<img width="437" alt="image" src="https://github.com/cccjaist/KanazawaCupidProject/assets/24668340/43b5ad1a-d5c8-4444-81ea-b687b56be042">


#### 起動時：プロンプトの決定

アプリを起動すると、コマンドプロンプトに以下のような表示が出る。
使いたいプロンプトの番号を入力してエンターキーを押すと、アプリが起動する。

```
----------------------------
You can use these characters.
0 : ずんだもん
1 : ねこえもん
2 : シャロル
3 : シマ
4 : こうしろ じょうじ
(略)
Input the character number>>
```

#### 入力方法

マイクに向かって話しかけるか、「会話内容」にテキストを打ち込んで「会話を追加」ボタンを押すことで、入力が行える。</br>
アプリ内の「音声入力」をOFFにすると、音声入力が行われなくなる。

#### ChatGPTへ質問する方法

ChatGPTへの質問は、問いかけを行う場合と反論を行わせる場合の2つの種類がある。

##### 問いかける場合

「君はどう思う？」ボタンを入力することでChatGPTへ意見を聞くことができる。</br>
アプリ内の表情が横を向いているときは、通信処理を行っている最中である。通信処理の最中は、問いかける形のボタンを押すことはできない。<br/>
通信処理が終了すると、その返信を声に出して話してくれる。<br/>
質問内容が不適切でchatGPTから長い返答が返ってきた場合や、パソコンのスペックが足りず動作に時間がかかる場合は、エラーメッセージを話す。<br/>
会話の返答は、画面上部にあるテキストボックスの中に表示される。

##### 反論させたい場合

「反論して！」ボタンを入力することでChatGPTへ反論がないか聞くことができる。</br>
アプリ内の表情が横を向いているときは、通信処理を行っている最中である。<br/>
通信処理の最中は、問いかける形のボタンを押すことはできない。<br/>
通信処理が終了すると、その返信を声に出して話してくれる。<br/>
質問内容が不適切でchatGPTから長い返答が返ってきた場合や、パソコンのスペックが足りず動作に時間がかかる場合は、エラーメッセージを話す。<br/>
会話の返答は、画面上部にあるテキストボックスの中に表示される。

#### 定期的な話題提供

7分ごとにアラームが鳴ると、会話上部にあるテキストボックスに話題の提供が行われる。内容はランダム。

#### ログの閲覧

「logs」フォルダの中にはアプリのエラー、これまでの会話内容、chatGPTからの返答が記載されているログがある。

##### error_logs

アプリで発生したエラーに関するログが記載されている。ファイル名は`error_(アプリを起動した時間)yyyy_mm_dd_HH_MM.log`である。

##### message_logs

会話内容(音声入力またはテキスト入力された文章)のログが記載されている。ファイル名は`message_(アプリを起動した時間)yyyy_mm_dd_HH_MM.log`である。</br>
`message_(アプリを起動した時間)yyyy_mm_dd_HH_MM.log`がある場合もあるが、これはアプリが異常終了した場合、本来消去されるはずだったファイルが残ってしまっている状態である。<br/>
tmpファイルの中身を同時刻の`.log`ファイルに書き加えてから消去することをお勧めする。

##### response_logs

chatGPTからの返答ログが記載されている。ファイル名は`response_(アプリを起動した時間)yyyy_mm_dd_HH_MM.log`である。

### 起動を終了する方法

アプリ内の「会話を終了する」ボタンをクリックする。<br/>
「×を押してアプリを終了してください」との表示が出るので、アプリを閉じる。

## クレジット提供

アプリ開発に当たり、多くの素材を利用させていただきました。感謝します。

- [ずんだもん立ち絵素材改](https://seiga.nicovideo.jp/seiga/im11148236) 作者：坂本アヒル様
- [東北ずん子立ち絵素材ver1.1.2](https://seiga.nicovideo.jp/seiga/im10886085?ref=pc_watch_contentstree_parent) 作者：こーすけさんたまりあ様
- [メイド服の少女](https://nanamiyuki.com/archives/6461) 作者：七三ゆき様
- [立ち小夜/SAYO素材](https://seiga.nicovideo.jp/seiga/im11095609) 作者：akihiyo様
- [フリー男性立ち絵素材 サラリーマン風男性](https://booth.pm/ja/items/3252647) 作者：RAIKO様
- [魔王魂 ワンポイント23](https://maou.audio/se_onepoint23/)

