# これはなに

とあるサーバーで動かすBotです。

## 必要なもの

- PostgreSQL
- Python

## どうやったら動かせる？

### 開発時点

```shell
docker-compose up -d postgresql twitter-download twitter-chat
```

twitter-downloadとtwitter-chatはただのスクリプト実行用のサービスなので、runで動かしてもよい
例：

```shell
docker-compose run -rm twitter-download
```

## 必要ライブラリなど

以下がDockerで構築する際に使用するファイルなのでそこ見てね

- [require.txt][1]
- [Dockerfile][2]

物理マシン、VMで動かす場合は元イメージのDockerfileをみて構築すればいいよ。

## 申請など

twitter APIを使用しているので、twitterアプリケーション作成の申請をしてくださいな。

[Twitter API 登録 (アカウント申請方法) から承認されるまでの手順まとめ　※2018年9月時点の情報][3]

## 感謝

[discord\.pyのBot Commands Frameworkを用いたBot開発 \- Qiita][4]

[1]:./docker-python/require.txt
[2]:./docker-python/Dockerfile
[3]:https://qiita.com/kngsym2018/items/2524d21455aac111cdee
[4]:https://qiita.com/Lazialize/items/81f1430d9cd57fbd82fb