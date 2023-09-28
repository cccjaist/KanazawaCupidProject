# KanazawaCupidProject

## 準備
1. pythonをインストール
2. pipenvをインストール
```
pip install pipenv
pipenv install
```
4. main.pyと同じ階層に`.env`ファイルを作成し、以下の内容を記述する。
```
OPENAI_API_KEY={chatGPTのAPIKey}
OPENAI_ORGANIZATION={chatGPTのOrganization Key}
```
5. VOICE VOXをダウンロードし、立ち上げておく。

### 起動方法
```
pipenv run start
```
