# The Codex — パッケージ、環境、錬金術師のツールチェーン

**概要:** 密閉された実験室を構築し、試薬を補充し、秘密を守り、そして自分の秘薬を本物のPythonパッケージに整理する。仮想環境、依存関係管理、環境を介した設定、そしてパッケージの初期化から循環依存まで、あらゆるインポートの謎を扱う。

**バージョン:** 1.0

---

## 目次

- 第I章: はじめに — 2ページ
- 第II章: AI に関する指示 — 3ページ
- 第III章: 一般的な指示 — 5ページ
- 第IV章: 演習0: 密閉された実験室 — 7ページ
- 第V章: 演習1: 預言者 (The Oracle) — 11ページ
- 第VI章: 演習2: アランビック (蒸留器) — 14ページ
- 第VII章: 演習3: 蒸留と変成 — 16ページ
- 第VIII章: 演習4: 爆発を避けよ — 19ページ
- 第IX章: 提出に関する指示 — 22ページ

---

## 第I章: はじめに

錬金術師の実験室へようこそ、若き弟子よ!

中世の錬金術師は卑金属を金に変えようとしていた。今日、Pythonの錬金術師として、あなたは散らばったコードを整理された再利用可能な魔法の秘薬に変える方法を学ぶ。古代の錬金術師が魔術書を章や節に整理していたように、Pythonコードもモジュールやパッケージに整理されなければならない。

しかし、どんな錬金術師も魔術書から始めはしない。まず実験室そのもの、つまり外界から密閉された作業空間が必要だ。失敗した実験がその壁の外のものを汚染しないようにするためだ。次に、外から持ち込む試薬、そして秘密を誰でも読めるページから守るための印章が来る。

そうして初めて秘薬を書くことができる。そしてそこから本当の謎が始まる:

- `__init__.py` の使い方 — 単純なフォルダを魔法のパッケージに変換するゲートウェイ
- パッケージが何を公開し、何を隠すかを正確に選ぶこと
- 遠くのモジュールから遠くのモジュールのコードを呼び出すこと
- 絶対インポートと相対インポートの管理
- 循環依存を避けること

このコーデックスでは、密閉された作業空間、試薬の供給、秘密の印章、そして最後に魔術書そのものを順に構築する。

> 💡 **ヒント:** これらのツールが**どのように動くか**を理解することに集中せよ。動かすことだけではなく。真の錬金術師は変成プロセスのすべてのステップを理解する!

---

## 第II章: AI に関する指示

### ● コンテキスト

学習の過程で、AIは多くの異なるタスクを支援できる。AIツールの能力とそれらがどのように作業を支援できるかを探る時間をとること。ただし、常に慎重にアプローチし、結果を批判的に評価すること。コード、ドキュメント、アイデア、技術的な説明のいずれであっても、質問が適切に組み立てられていたか、生成された内容が正確であるかを完全に確信することはできない。仲間はミスや盲点を避けるための貴重なリソースだ。

### ● 主なメッセージ

- 繰り返しや面倒なタスクを減らすためにAIを使う
- 将来のキャリアに役立つプロンプト作成スキル(コーディング・非コーディングの両方)を発展させる
- AIシステムの仕組みを学び、一般的なリスク、バイアス、倫理的な問題を予測・回避する
- 仲間と協力して技術スキルとパワースキルの両方を構築し続ける
- 完全に理解し責任を負えるAI生成コンテンツのみ使用する

### ● 学習者のルール

- AIツールを探求し、倫理的に使用し、潜在的なバイアスを減らすためにそれらの動作を理解する時間をとる
- プロンプトする前に問題を熟考する — これはより明確で、より詳細で、より関連性のあるプロンプトを正確な語彙で書くのに役立つ
- AIが生成したものを体系的に確認、レビュー、質問、テストする習慣を身につける
- 常に仲間のレビューを求める — 自分の検証だけに頼らない

### ● フェーズの成果

- 汎用および特定ドメインのプロンプトスキルの両方を発展させる
- AIツールの効果的な使用で生産性を向上させる
- 計算的思考、問題解決、適応性、協調性を強化し続ける

### ● コメントと例

- 試験、評価など、真の理解を示す必要がある状況に定期的に遭遇する。準備を整え、技術的・対人的スキルの両方を構築し続けること
- 自分の推論を説明し仲間と議論することで、理解のギャップが明らかになることが多い。ピアラーニングを優先すること
- AIツールは特定のコンテキストを欠くことが多く、汎用的な回答を出す傾向がある。同じ環境を共有する仲間はより関連性の高い正確な洞察を提供できる
- AIは最も可能性の高い回答を生成する傾向があるのに対し、仲間は代替の視点や貴重なニュアンスを提供できる。品質チェックポイントとして頼ること

#### ✓ 良い例
AIに「ソート関数をどうテストする?」と聞く。アイデアをいくつかもらう。試してみて、結果を仲間とレビューする。一緒にアプローチを洗練する。

#### ✗ 悪い例
AIに関数全体を書かせ、プロジェクトにコピペする。ピアレビューで、何をするのか、なぜそうなるのか説明できない。信頼を失い、プロジェクトを落とす。

#### ✓ 良い例
AIを使ってパーサーの設計を手伝ってもらう。次に仲間とロジックを辿る。2つのバグを見つけ、より良く、よりきれいに、完全に理解した状態で書き直す。

#### ✗ 悪い例
Copilotにプロジェクトの重要部分を生成させる。コンパイルはできるが、パイプの扱い方を説明できない。評価中に正当化できず、プロジェクトを落とす。

---

## 第III章: 一般的な指示

- プロジェクトは **Python 3.10 以降** で書くこと
- **flake8** コーディング規約に従うこと
- すべてのコードには包括的な型アノテーションを含めること。**mypy** で確認すること
- 標準クラスとコレクション(int, str, list, dict など)とそのメソッドはすべて使用可能
- `eval()` と `exec()` を除き、すべての組み込み関数は使用可能
- 各演習は独自の許可されたインポートを宣言する。それらを尊重すること — それは演習の一部だ
- このプロジェクトのどこでも `sys.path` を変更することは禁止

> ⚠️ 演習0と1は外部ライブラリをインストールして使用する。それが教えることだからだ。演習2〜4は逆で、許可されるインポートは自分で作成したモジュールとファイルのみ。各演習のヘッダーを読むこと。

> ℹ️ 演習2〜4では、すべての関数はシンプルで文字列を返すものにすべき。複雑なロジックではなく、インポートの概念に集中すること。

このプロジェクトは5つの演習にまたがる1つの実験室を構築する。演習0と1はそれぞれ独自のフォルダに自己完結している。演習2、3、4はリポジトリのルートに1つのパッケージツリーを成長させ、それぞれ前のものに積み重ねていく。プロジェクトの最後、ファイルツリーはこうなるはず:

```
.
|-- ex0
|   |-- construct.py
|   |-- loading.py
|   |-- pyproject.toml
|   `-- requirements.txt
|-- ex1
|   |-- .env.example
|   |-- .gitignore
|   |-- oracle.py
|   `-- requirements.txt
|-- alchemy
|   |-- __init__.py
|   |-- elements.py
|   |-- potions.py
|   |-- transmutation
|   |   |-- __init__.py
|   |   `-- recipes.py
|   `-- grimoire
|       |-- __init__.py
|       |-- dark_spellbook.py
|       |-- dark_validator.py
|       |-- light_spellbook.py
|       `-- light_validator.py
|-- elements.py
|-- ft_alembic_0.py
|-- ft_alembic_1.py
|-- ft_distillation_0.py
|-- ft_transmutation_0.py
|-- ft_kaboom_0.py
`-- ft_kaboom_1.py
```

---

## 第IV章: 演習0: 密閉された実験室

| | |
|---|---|
| **演習0** | ex0 |
| **ディレクトリ:** | ex0/ |
| **提出ファイル:** | construct.py, loading.py, requirements.txt, pyproject.toml |
| **許可:** | os, sys, site, importlib, pandas, numpy |

> ❓ 「外界が到達できない部屋でなければ、実験室とは何だろうか?」

弟子が何かを混ぜることを許される前に、実験室を密閉しなければならない。失敗した実験が実験そのものだけを台無しにする隔離された空間だ。Pythonでは、その密閉された部屋が**仮想環境**だ。密閉されたら、弟子は所有する他のすべてを汚染することなく、ついに外界から試薬を持ち込むことができる。それが**依存関係管理**だ。

この最初の演習は、どちらか単独では役に立たないため、その準備の両方の半分をカバーする。

### パート1: 部屋を密閉する

`ex0/construct.py` というプログラムを作成し、次のことを行う:

- 仮想環境内で実行されているかどうかを検出する
- 現在のPython環境の情報を表示する
- 仮想環境が検出されない場合、作成と有効化の手順を提供する
- グローバルと仮想環境のパッケージの場所の違いを示す

> ℹ️ プログラムは仮想環境の内外両方で動作し、それぞれの場合に明らかに異なる出力を生成する必要がある。

仮想環境外でのテスト:
```
$> python3 ex0/construct.py
# 仮想環境が検出されず、指示を提供する
```

仮想環境の作成とテスト:
```
$> python3 -m venv lab_env
$> source lab_env/bin/activate
(lab_env) $> python3 ex0/construct.py
# 仮想環境を検出し、詳細を表示する
```

> ⚠️ 仮想環境をリポジトリに提出しないこと。必要に応じてレビュー中に新しいものを作成できる必要がある。

**期待される出力(密閉された実験室の外):**
```
$> python3 ex0/construct.py
LABORATORY STATUS: You are working in the open

Current Python: /usr/bin/python3.11
Virtual Environment: None detected

WARNING: You are in the global environment!
Every reagent you install here leaks into the whole system.

To seal the laboratory, run:
python3 -m venv lab_env
source lab_env/bin/activate  # On Unix
lab_env\Scripts\activate     # On Windows

Then run this program again.
```

**そして密閉された実験室の中:**
```
$> python3 ex0/construct.py
LABORATORY STATUS: The laboratory is sealed

Current Python: /path/to/lab_env/bin/python
Virtual Environment: lab_env
Environment Path: /path/to/lab_env

SUCCESS: You are working in an isolated environment!
Safe to install reagents without affecting
the global system.

Reagent installation path:
/path/to/lab_env/lib/python3.11/site-packages
```

### パート2: 試薬を補充する

> 🗺️ 「試薬が必要だ。たくさんの試薬が。」

空のままでは密閉された実験室は役に立たない。今度は試薬を持ち込み、他の錬金術師があなたの実験室を正確に再現できるように適切に宣言する。これは2回、取引の2つのツール、**pip** と **Poetry** で行う。

`ex0/loading.py` というプログラムを作成し、次のことを行う:

- `ex0/requirements.txt`(pip用)と `ex0/pyproject.toml`(Poetry用)の両方に、いくつかの外部**試薬**(pandasやnumpyなどのライブラリ)を宣言する
- 宣言された各試薬をインポートし、インストールされているバージョンを報告する
- 出力で、pipとPoetryの依存関係管理の違いを示す

> ⚠️ プログラムはどの試薬が利用可能かを検出し、1つが欠けている場合、pipとPoetryの両方のインストールコマンドを含む役立つメッセージを表示する必要がある。クラッシュしてはならない。

試薬がインストールされていない状態でのテスト:
```
$> python3 ex0/loading.py
# 欠落した依存関係と、pipおよびPoetryのインストール手順を表示するはず
```

pipでのインストール:
```
$> pip install -r ex0/requirements.txt
$> python3 ex0/loading.py
# インストールされた試薬のバージョンを一覧表示するはず
```

Poetryでのインストール:
```
$> poetry install
$> poetry run python ex0/loading.py
# Poetry環境内で同じバージョンを一覧表示するはず
```

**期待される挙動:**
```
$> python3 ex0/loading.py
REAGENT STATUS: Loading reagents...

Checking dependencies:
[OK] pandas (2.1.0) - Data manipulation ready
[OK] numpy (1.25.0) - Numerical computation ready

pip vs Poetry:
  requirements.txt declares what to install; pip resolves it at install time.
  pyproject.toml declares the same constraints, and Poetry pins the resolved
  versions in poetry.lock so every install is identical.

All reagents present and accounted for.
```

> ❓ 仮想環境は実際には何を隔離し、何を隔離しないのか? そして、単純な `requirements.txt` の代わりにPoetryを選ぶ理由は何か?

---

## 第V章: 演習1: 預言者 (The Oracle)

| | |
|---|---|
| **演習1** | ex1 |
| **ディレクトリ:** | ex1/ |
| **提出ファイル:** | oracle.py, requirements.txt, .env.example, .gitignore |
| **許可:** | os, sys, python-dotenv, ファイル操作 |

> 💡 「汝自身を知れ。」そしてさらに重要なことに:あなたの魔術書が決して声に出して言うべきでないことを知れ。

預言者はすべてを知っている。預言者は実験室全体の設定を読むことができるからだ。現実の世界では、プログラムは機密知識へのアクセスを必要とする:データベース認証情報、APIキー、エンドポイント。魔術書のページに書かれると、その知識は不注意な `git push` 一回で他のすべての人に知られてしまう。

**環境変数**と `.env` ファイルに基づく設定システムを構築し、秘密は実験室の隣に住み、秘薬の中には決して存在しないようにする。

> ℹ️ `.env` ファイルから環境変数を読み込むために python-dotenv ライブラリを使用すること。目標は独自のパーサーを書くことではなく、`.env` ファイルが設定にどのように使用されるかを学ぶことだ。

### ミッション

`ex1/oracle.py` というプログラムを作成し、次のことを行う:

- 環境変数から設定を読み込む
- 開発設定に `.env` ファイルを使用する
- 開発と本番の設定で異なる動作をする
- クラッシュせずに欠落した設定を適切に処理する

> ℹ️ 開発/本番の違いの示し方は自由だが、プログラムをテストするときに出力で見えるようにする必要がある。

### 設定

プログラムは次の設定変数を処理する:
- `MATRIX_MODE` - "development" または "production"
- `DATABASE_URL` - データストレージへの接続文字列
- `API_KEY` - 外部サービスのシークレットキー
- `LOG_LEVEL` - ログの詳細度
- `ZION_ENDPOINT` - リモートネットワークのURL

> ⚠️ 本物のシークレットをバージョン管理にコミットしないこと! `.env` ファイルは `ex1/.gitignore` にリストされている必要があり、その理由を説明できなければならない。

設定なしでのテスト:
```
$> python3 ex1/oracle.py
# デフォルト値を表示し、欠落した設定について警告するはず
```

`.env` ファイルの使用:
```
$> cp ex1/.env.example ex1/.env
$> # ex1/.env をあなたの値で編集
$> python3 ex1/oracle.py
# .env ファイルから設定を読み込むはず
```

環境経由での上書き:
```
$> MATRIX_MODE=production API_KEY=secret123 python3 ex1/oracle.py
# .env ファイルよりも環境変数を優先するはず
```

**期待される出力の例:**
```
$> python3 ex1/oracle.py
ORACLE STATUS: Consulting the configuration...

Configuration loaded:
Mode: development
Database: Connected to local instance
API Access: Authenticated
Log Level: DEBUG
Remote Network: Online

Configuration security check:
[OK] No hardcoded secrets detected
[OK] .env file properly ignored by git
[OK] Production overrides available

The Oracle sees all configurations.
```

> ❓ 環境変数は、ソースコード内の定数よりも、シークレットの場所として優れているのはなぜか? それでも安全ではないのは何か?

---

## 第VI章: 演習2: アランビック (蒸留器)

| | |
|---|---|
| **演習2** | alembic |
| **提出ファイル:** | elements.py, alchemy/__init__.py, alchemy/elements.py, ft_alembic_0.py, ft_alembic_1.py |
| **許可:** | 組み込み、標準型、このプロジェクトで作成するモジュールのみ |

実験室は密閉され、補充され、設定された。秘薬を書く時が来た。

すべての錬金術師はアランビックのシンプルな材料から始まる。しかし、ある材料は手近にあり、他の材料は戸棚の奥深くにある。この演習は、各材料に到達する `import` メカニズムと、パッケージが外界に何を見せるかを決定するゲートウェイに関するものだ。

まず、実験室アーキテクチャのコンポーネントを構築する。

**elements.py**(リポジトリのルート)に含める:
- `create_fire()` 関数 — 文字列 "Fire element created" を返すだけ
- `create_water()` 関数 — 文字列 "Water element created" を返すだけ

**alchemy/elements.py** に含める:
- `create_earth()` 関数 — 文字列 "Earth element created" を返すだけ
- `create_air()` 関数 — 文字列 "Air element created" を返すだけ

**alchemy/\_\_init\_\_.py** に含める:
- `alchemy` パッケージインターフェースを介して `create_air` を公開するために必要なもの、そして `create_earth` を公開するものは**何もない**。`ft_alembic_1.py` を参照

次に、アーキテクチャを2つのスクリプトでテストする。それぞれが別の方法で要素に到達する:

- `ft_alembic_0.py` は `import ...` 構造を使ってルートの `elements.py` にアクセスし、fireを作成する
- `ft_alembic_1.py` は `import alchemy` を使ってパッケージインターフェースを通り、airを作成する。次に同じインターフェースを通じて `create_earth()` を呼び出す。`alchemy/elements.py` がその関数を定義しているにもかかわらず、これは**失敗**しなければならない。例外をキャッチしてもしなくてもよい、これは教育目的のためだけ。mypy エラーがここで出るのは意図したもの。

> ℹ️ `__init__.py` ファイルで flake8 または mypy エラーに直面することがある。その場合はいつもの慣習に従うこと。

**例:**
```
$> python3 ft_alembic_0.py
=== Alembic 0 ===
Using: 'import ...' structure to access elements.py
Testing create_fire: Fire element created

$> python3 ft_alembic_1.py
=== Alembic 1 ===
Accessing the alchemy module using 'import alchemy'
Testing create_air: Air element created
Now show that not all functions can be reached
This will raise an exception!
Testing the hidden create_earth: Traceback (most recent call last):
  File "/tmp/Python/module-05-bis/ft_alembic_1.py", line 12, in <module>
    print(f"{alchemy.create_earth()}")
             ^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'alchemy' has no attribute 'create_earth'. Did you mean: 'create_air'?
```

> ❓ `alchemy/elements.py` は `create_earth` を定義しているのに、`ft_alembic_1.py` は `import alchemy` 経由でそれに到達できない。何も隠されず、プライベートにもされていない。では、`__init__.py` は正確に何を変えたのか?

---

## 第VII章: 演習3: 蒸留と変成

| | |
|---|---|
| **演習3** | transmutation |
| **提出ファイル:** | alchemy/potions.py, alchemy/transmutation/ をパッケージとして, ft_distillation_0.py, ft_transmutation_0.py |
| **許可:** | 組み込み、標準型、このプロジェクトで作成するモジュールのみ |

ネストしたインポートの技を習得:遠くのファイルから遠くのコードを召喚し、モジュールを越えてサブパッケージに降りる。

### 蒸留

新しいコンポーネントで実験室アーキテクチャを改良する。

**alchemy/potions.py** に含める:
- `healing_potion()` 関数 — 文字列 "Healing potion brewed with '[created earth element]' and '[created air element]'" を返す
- `strength_potion()` 関数 — 文字列 "Strength potion brewed with '[created fire element]' and '[created water element]'" を返す
- 4つの基本要素に到達するために必要な他のすべてのもの。2つはパッケージの外に住んでいることに注意

これらの新しい秘薬を1つのスクリプトでチェック:
- `ft_distillation_0.py` は `from ... import ...` 構造を使って `alchemy/potions.py` に直接アクセスし、ヒーリングポーションとストレングスポーションの両方を醸造する

**例:**
```
$> python3 ft_distillation_0.py
=== Distillation 0 ===
Direct access to alchemy/potions.py
Testing strength_potion: Strength potion brewed with 'Fire element created' and 'Water element created'
Testing healing_potion: Healing potion brewed with 'Earth element created' and 'Air element created'
```

### 偉大なる変成

サブパッケージへとさらに1レベル深く進み、絶対インポートと相対インポートの古代の議論に決着をつける。

**alchemy/transmutation/recipes.py** に含める:
- `lead_to_gold()` 関数 — 文字列 "Recipe transmuting Lead to Gold: brew '[created air]' and '[created strength potion]' mixed with '[created fire]'" を返す
- 少なくとも1つの絶対インポートと1つの相対インポート

そのレシピに到達する1つのスクリプトを作成:
- `ft_transmutation_0.py` は `import ...` 構造を使って `alchemy/transmutation/recipes.py` に直接アクセスし、鉛を金に変成する

**例:**
```
$> python3 ft_transmutation_0.py
=== Transmutation 0 ===
Using file alchemy/transmutation/recipes.py directly
Testing lead to gold: Recipe transmuting Lead to Gold: brew 'Air element created' and 'Strength potion
    brewed with 'Fire element created' and 'Water element created'' mixed with 'Fire element created'
```

> ❓ 錬金術師はいつ絶対的な経路を使い、いつ相対的なものを使うべきか?

---

## 第VIII章: 演習4: 爆発を避けよ

| | |
|---|---|
| **演習4** | grimoire |
| **提出ファイル:** | alchemy/grimoire/ をパッケージとして, ft_kaboom_0.py, ft_kaboom_1.py |
| **許可:** | 組み込み、標準型、このプロジェクトで作成するモジュールのみ |

最後の謎、そして実験室を破壊するもの:**循環依存**。2つのモジュールが無限ループで互いを召喚しようとするときに発生する。

同じ機能を2回書く:1回は動作するように、もう1回は爆発するように。重要な点は、両者の違いは単一の設計上の決定であり、構文の1行ではないことだ。

### 存続する光の魔術書

**alchemy/grimoire/light_spellbook.py** に含める:
- `light_spell_allowed_ingredients()` 関数 — 光魔法に許可された材料のリストを返す: "earth"、"air"、"fire"、"water"
- `light_spell_record(spell_name: str, ingredients: str)` 関数 — 呪文が記録されたか拒否されたかを示す文字列を返す。その決定は以下のバリデータから来る

**alchemy/grimoire/light_validator.py** に含める:
- `validate_ingredients(ingredients: str)` 関数 — 材料と "VALID" または "INVALID" キーワードを含む文字列を返す。材料は、呪文書で許可されている材料の少なくとも1つを含む場合に有効(大文字小文字を区別しない)

問題の形に注目:呪文書は決定するためにバリデータを必要とし、バリデータは何が許可されているかを知るために呪文書を必要とする。それぞれのファイルがもう一方を必要とする。爆発を防ぐ方法はいくつかある。1つを選び、評価中に代替案を説明できるようにする。

### 存続しない闇の魔術書

次に `dark_spellbook.py` と `dark_validator.py` を闇の対応物として書く。`dark_` プレフィックス付きの関数名と、闇の材料: "bats"、"frogs"、"arsenic"、"eyeball"。

今回は、相互依存を素朴な方法で、両方のファイルの先頭に書き、壊れたままにする。このペアは失敗のデモンストレーションなので、本当に失敗しなければならない。

> ⚠️ 光のファイルをコピーして関数名を変更しないこと。インポートサイクルが変更対象であるように、闇のペアを意図的に書くこと。そのコントラストが演習全体だ。

最後に、いくつかの呪文をテスト:
- `ft_kaboom_0.py` は `grimoire` パッケージにアクセスし、光の呪文を記録する(完璧に)
- `ft_kaboom_1.py` は `dark_spellbook.py` に直接到達し、闇の呪文を記録しようとする。これは失敗し、例外を発生させなければならない。これは実験室が爆発したことを示す。例外をキャッチしてもしなくてもよい、これは教育目的のためだけ

**例:**
```
$> python3 ft_kaboom_0.py
=== Kaboom 0 ===
Using grimoire module directly
Testing record light spell: Spell recorded: Fantasy (Earth, wind and fire - VALID)

$> python3 ft_kaboom_1.py
=== Kaboom 1 ===
Access to alchemy/grimoire/dark_spellbook.py directly
Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION
Traceback (most recent call last):
  File "/tmp/Python/module-05-bis/ft_kaboom_1.py", line 7, in <module>
    from alchemy.grimoire.dark_spellbook import dark_spell_record
  File "/tmp/Python/module-05-bis/alchemy/grimoire/dark_spellbook.py", line 2, in <module>
    from .dark_validator import validate_ingredients
  File "/tmp/Python/module-05-bis/alchemy/grimoire/dark_validator.py", line 2, in <module>
    from .dark_spellbook import dark_spell_allowed_ingredients
ImportError: cannot import name 'dark_spell_allowed_ingredients' from partially initialized module '
    alchemy.grimoire.dark_spellbook' (most likely due to a circular import) (/tmp/Python/module-05-bis/
    alchemy/grimoire/dark_spellbook.py)
```

> ❓ どちらの魔術書も互いを必要とする2つのファイルを記述している。なぜ片方だけが爆発するのか?

---

## 第IX章: 提出に関する指示

いつものように、Gitリポジトリに課題を提出する。防衛中はリポジトリ内の作業のみが評価される。

Gitリポジトリのルートに期待されるファイルツリーを配置し、仮想環境や `.env` ファイルを提出しないこと。

> ℹ️ 評価中、新しい実験室をゼロから密閉するように求められたり、インポートメカニズムを説明したり、パッケージが公開するものを変更したり、循環依存を壊したり修復したりするように求められる場合がある。実装だけでなく、謎を理解していることを確認すること。
