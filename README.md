# `絶対にスベってはいけない宴会`

[![絶対にスベってはいけない宴会](thumb.png)](https://youtu.be/zlKFP9F6Vko)

## 製品概要
### 宴会-Tech

### 背景

宴会、といっても楽しめる人はそう多くなく、

- 折角の飲み会!! でも、部長のオヤジギャグがきつ〜い。。。
- みんなと仲良くワイワイしたいけど、滑ったら嫌だなあ。。。
- ガツガツ飲む感じだったら嫌だなあ。。。
- プライベートな話を詮索されたくない。。。
- 行っても、ぽつーんってなるから行きたくない。。。
- 飲み会に参加しても、話すことがなくただ聞いているだけ

という声は多い。

滑ることやハラスメントが嫌で、自由に楽しめない人がたくさんいる。

また、

- 飲み会をもっと盛り上げたい！
- いまの宴会は時代遅れだ

と宴会をもっと楽しみたいという人も少なからずいる。

宴会への不満は世の中に溢れている。そこで、宴会への不満を解消し、より良い宴会の実行を支援するアイテムの開発を目指した。

### 製品説明（具体的な製品の説明）

1. \乾杯🍻/に合わせてスタート!!
1. 表情から場の空気を識別
1. 場の空気が盛り下がったときは＼デデーン／で場を盛り上げる

### 特長

#### 1. 表情から場の空気を識別

insta360 から全天周画像を取得！
Micrsoft Emotion APIを用いて宴会に参加している人の表情を認識し、各人の盛り上がりを算出します。

#### 2. 場の空気が盛り下がったときは＼デデーン／で場を盛り上げます！

＼遠藤 田中 浜田 OUT／

1. 宴会でスベってしまった人へのフォロー

1. 宴会でハラスメントな発言をした人への警告、ハラスメント被害の防止

\デデーン/によって、宴会の場の幸福を保ちます。

#### 3. クラウド

主要な処理はIBM Node-Red上で行っているので、スマホアプリとしても、居酒屋に設置するデバイスとしても実装できる。


### 解決出来ること

- スベることを恐れて、宴会を楽しめない人の手助け
- ハラスメントの防止
- 若者が慣れ親しんだ体験で飲み会を盛り上げ、新しい宴会スタイルを創生


### 今後の展望

- 手軽に飲み会に設置できるハードウェアとして、Rasberry Piなどを組み合わせたプロトタイプ

- 粗相を画像・音声の両面から認識
  - NEC 物音認識を活用し、グラスが割れた音を識別
  - Yolo と OpenCV を組み合わせて空のコップを判定
  - Speech to Text 系のAPIを用いて、ハラスメントな発言を検出し注意

## 開発内容・開発技術
### 活用した技術
#### API・データ

* NEC 物音認識API
* Microsoft Emotion API
* IBM Text to Speech
* Google CLOUD SPEECH API

#### フレームワーク・ライブラリ・モジュール
* IBM Node-Red (https://node-red-001.au-syd.mybluemix.net/red/)
* OpenCV
* Web Socket

#### デバイス
* insta360 air


### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* すべての作業
