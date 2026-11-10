# python05bis 評価 予想質疑応答

Module 06 の評価シート(= python05bis と同内容)と Module 08 の実際の評価者とのやりとりから、
評価で聞かれそうな質問とその回答例をまとめた日本語ドキュメント。

---

## 事前チェック

評価官は最初に以下を確認する:
- Git リポジトリが受験者本人のものか
- 悪意あるエイリアスが仕込まれてないか
- プロジェクト構造が subject と一致してるか

→ 対策: 最初に `ls` と `cat ~/.zshrc` 等でクリーンな状態を見せる。

---

## Part 1: アランビック(import の基礎)

### Q1-1. `import X` と `from X import Y` の違いは?

A.
- `import X`: モジュール X 全体を読み込み、`X.name` でアクセス
- `from X import Y`: X の中の Y だけを直接取り込む(`Y` でアクセス可)
- 内部的にはどちらも `X/__init__.py` を実行する点は同じ

### Q1-2. `import alchemy` した時、`alchemy.create_earth()` が失敗するのはなぜ?

A.
- `import alchemy` は `alchemy/__init__.py` を実行するだけ
- `__init__.py` は `create_air` だけを re-export してる
- `create_earth` は `alchemy/elements.py` に**実在する**が、`__init__.py` が公開してないので `alchemy` パッケージの属性としては見えない
- `alchemy.elements.create_earth` または `from alchemy.elements import create_earth` なら到達可能

### Q1-3. `__init__.py` の役割は?

A.
- ディレクトリを**パッケージ**として扱わせるための「印」
- `import X` した時に**最初に実行**されるコード
- 外部に公開する API のコントロール(ゲートキーパー)
- 空でもパッケージとして機能する

### Q1-4. モジュールとパッケージの違いは?

A.
- モジュール = `.py` ファイル 1個
- パッケージ = `__init__.py` を含むディレクトリ(中にモジュールやサブパッケージが入る)
- 両方 `import` で読み込める「名前空間」だが構造が違う

### Q1-5. `__all__` の役割は?

A.
- `from X import *` した時に取り込まれる名前のリスト
- 公開 API の宣言としても機能(「これが外向きに見せたい関数」の明示)
- flake8 F401(未使用 import)を抑制する副次効果
- アクセス制御ではない(`from X import create_earth` は `__all__` と無関係に動く)

---

## Part 2: 蒸留(potions.py の import 設計)

### Q2-1. `potions.py` から外部の `elements.py` を import するときの書き方は?

A.
```python
from elements import create_fire, create_water
```
- root 直下の `elements.py` は**どのパッケージにも属さない**トップレベルモジュール
- 相対 import (`..elements`) では到達できない(パッケージ外のため)
- 絶対 import 一択

### Q2-2. `potions.py` が内外両方の `elements.py` を使い分けられる理由は?

A.
- 書き方で区別する:
  - `from elements import ...` → root の `elements.py`
  - `from alchemy.elements import ...` → `alchemy/` 内の `elements.py`
- Python は import 文の**文字列から解釈**するので、同名でも別モジュールとして扱える
- 実行時に `sys.modules` にそれぞれ別キーで登録される

### Q2-3. なぜ `ft_distillation_0.py` は root から実行する必要がある?

A.
- `potions.py` の `from elements import ...` は root 直下の `elements.py` を探す
- Python は実行時に「スクリプトのあるディレクトリ」を `sys.path[0]` に入れる
- `alchemy/` から `python3 potions.py` 直接実行すると、`sys.path[0]` が `alchemy/` になり `alchemy/elements.py` を拾ってしまう
- root から `python3 ft_distillation_0.py` が正解

### Q2-4. なぜ `alchemy/__init__.py` に `potions` を re-export する(する場合)?

A.
- 評価シートの指示: 「`alchemy` モジュールの `__init__.py` が更新され、ポーションが公開されている」
- 外部から `alchemy.healing_potion()` の形で呼べるようにするため
- 公開 API を `__init__.py` で一元管理する設計

---

## Part 3: 大いなる変成(絶対 vs 相対 import)

### Q3-1. 絶対 import と相対 import の違いは?

A.
- 絶対: フルパス表記 `from alchemy.elements import X`
- 相対: `.`/`..` を使って現在位置から相対 `from .elements import X` / `from ..elements import X`
- `.` = 同じパッケージ、`..` = 親パッケージ

### Q3-2. いつ絶対を使い、いつ相対を使う?

A.
- **絶対の使い所**:
  - パッケージ**外**を参照する時(必須、相対では届かない)
  - プロジェクト全体で公開する API
  - サブモジュール間の距離が遠い時(`....foo` より `alchemy.foo` の方が読みやすい)
- **相対の使い所**:
  - 同じパッケージ内の密結合な部品を結ぶ時
  - パッケージ名変更の耐性が欲しい時
- **PEP 8 公式見解**: デフォルトは絶対。相対は「絶対だと冗長すぎる複雑なレイアウト」で使う

### Q3-3. なぜ `recipes.py` では両方使った?

A.
- subject の必須条件: 「絶対1つ以上 + 相対1つ以上」
- `from elements import create_fire` → root 直下は絶対一択(必須の絶対)
- `from ..potions import strength_potion` → 親パッケージ内、密結合として相対を選択
- `from alchemy.elements import create_air` → 絶対で出所明示

### Q3-4. `from ..potions import ...` の `..` は何を意味する?

A.
- 「**親パッケージ**」を指す
- `recipes.py` は `alchemy/transmutation/` にあるので、`..` は `alchemy/` を指す
- `..potions` = `alchemy/potions.py`
- ファイルシステムの階層ではなく**パッケージ階層**で動く

### Q3-5. `recipes.py` を直接実行したらエラー、なぜ?

A.
- 相対 import (`from ..potions import ...`) を含むから
- `python3 recipes.py` だと Python は `recipes.py` をトップレベルスクリプトと解釈
- トップレベルスクリプトには「親パッケージ」が存在しない → `..` が解決できない
- 正しくは `ft_transmutation_0.py` 経由で root から実行

---

## Part 4: 爆発を避けよ(循環依存)

### Q4-1. 循環依存とは?

A.
- 2つ以上のモジュールが互いを import で要求し合う状態
- A が B を import し、B も A を import する
- Python の import 評価順によっては `ImportError` で爆発する

### Q4-2. なぜ闇ペアは爆発するが、光ペアは動く?

A.
- **闇**: 両ファイルのトップで相互 import(素朴な設計)
  1. `dark_spellbook` 読み込み開始
  2. L1 で `dark_validator` を要求
  3. `dark_validator` L1 で `dark_spellbook` から属性を取ろうとする
  4. その属性はまだ定義されていない(初期化途中)→ `ImportError`
- **光**: 依存を一方向化 or 定数を別出し(設計判断)
  - 同じテーマでも設計1つで結果が真逆になる

### Q4-3. 循環依存を壊す方法は複数あるが、どれを選びましたか? また代替案は?

A.(方法B を採用した場合)
- **採用: 方法B(片方向依存化)**
  - `light_validator.py` に許可リスト `MAGIC` と `validate_ingredients()` を置く
  - `light_spellbook.py` は validator から両方を import するのみ
  - 依存の向きが spellbook → validator の一方向になり循環を回避
- **代替案1: 関数内 import(方法A)**
  - トップじゃなく関数の中で import する
  - import タイミングをずらすことで評価時には両方の読み込みが完了してる状態に
  - メリット: 最小変更
  - デメリット: 「実行時 import」の設計臭、関数呼び出しごとに評価(キャッシュ有)
- **代替案2: 第3のモジュール導入(方法C)**
  - `light_constants.py` に許可リストだけ切り出す
  - 両者がそこを参照 → 依存の向きが自然(両者 → constants)
  - メリット: DRY、拡張性◎
  - デメリット: ファイル追加、subject に明記されてない

### Q4-4(⚠️重要). 「ingredients は spellbook に定義されるべき」との評価項目に対して

A.(評価シートに「ingredients should be in spellbook, not in validator」とある場合)
- **方法B は validator 側に定数を置くため、この項目に抵触する可能性あり**
- 想定される評価官の指摘:
  > 「許可リストは spellbook の責務では?」
- 弁論の選択肢:
  1. **論理で説明**: 「循環依存回避の設計判断。責務分離より依存グラフ単純化を優先」
  2. **方法C に切り替え**: `light_constants.py` を追加、両者が参照
  3. **方法A に切り替え**: 関数内 import で spellbook に定数を戻す

**安全策**: 評価前に方法C に切り替えておく(定数モジュール追加で、subject には違反しない)

### Q4-5. 「Earth, Wind & Fire」で「Fantasy」が記録できることを確認

A.
```python
light_spell_record("Fantasy", "Earth, wind and fire")
# → "Spell recorded: Fantasy (Earth, wind and fire - VALID)"
```
- 判定: `"earth"` と `"fire"` が許可リストに含まれる(1つでも含まれれば VALID)
- "wind" は許可リストに無いが、他の2つで VALID 確定

### Q4-6. 闇が「光のコピペ+名前変更」ではいけない理由は?

A.
- 課題の目的は「素朴な設計(両方向 import)が壊れること」のデモ
- 光と同じ片方向依存の構造にすると闇も動いてしまう → 課題の意図を達成しない
- 設計判断1つの違いで結果が真逆になることを示すのがポイント

### Q4-7. 例外をキャッチすべきか?

A.
- subject は「キャッチしてもしなくても良い(教育目的)」
- 現状は**キャッチしない**選択
  - トレースバックそのままが「爆発」のデモとして分かりやすい
  - 評価者に「循環依存で死んだ」が一目で伝わる
- try/except で囲むなら `ImportError` を捕まえてメッセージ出してから落とす

---

## Code Quality(コード品質)

### Q5-1. Python 3.10 以上で書かれているか?

A.
```bash
python3 --version   # 3.10 以上であることを確認
```
- `list[str]` などの組み込み型注釈(3.9+)を使用
- `match/case` は未使用(必須ではないが 3.10+ 機能)

### Q5-2. flake8 クリアか?

A.
```bash
flake8 elements.py alchemy/ ex0/*.py ex1/oracle.py ft_*.py
# exit 0
```
- 唯一の E402(ft_kaboom_1.py L6)は `# noqa: E402` で意図明示
- 理由: 3つの print を import より先に実行させる subject 要件のため、意図的に慣習を破っている

### Q5-3. mypy --strict 通るか?

A.
```bash
mypy --strict ft_*.py elements.py alchemy/
```
- 例外: `ft_alembic_1.py` の `attr-defined` エラー
- これは**subject が明示的に意図している**エラー:
  - `alchemy/__init__.py` が `create_earth` を re-export してない
  - mypy がそれを静的に検出するのは正しい挙動
  - `# type: ignore` で隠すのは逆効果(評価者に「なぜ隠した?」と疑われる)

### Q5-4. 型注釈は全関数についてるか?

A. 全関数に引数・戻り値の型注釈を付けてる:
```python
def create_fire() -> str:
def light_spell_record(spell_name: str, ingredients: str) -> str:
def check() -> bool:
```

### Q5-5. docstring は必要か?

A. このモジュールでは必須ではない(評価シート明記)。簡潔な関数名で意図が伝わるので省略。

---

## 深掘り質問(Module 08 スタイル)

Module 08 の実際の評価者とのやりとりを見ると、**概念の本質を問う**深掘り質問が多い。python05bis でも同様のスタイルが予想される。

### Q6-1. パッケージとは具体的に何?

A.
- `__init__.py` を持つディレクトリ
- モジュールの入れ物であり、それ自体もモジュールとして振る舞う
- `import X` で読み込める「名前空間」の単位
- Python 3.3+ には `__init__.py` 無しの「namespace package」もあるが、慣習的には `__init__.py` あり

### Q6-2. import 文は Python 内部で何をしている?

A.
```
import X の内部処理:
1. sys.modules に X があるかチェック(キャッシュ済みなら再利用)
2. 無ければ X.py または X/__init__.py を探す
3. 見つかったファイルをパース → バイトコード化 → 実行
4. 実行結果のモジュールオブジェクトを sys.modules["X"] に登録
5. 呼び出し元のローカル名前空間に X を bind
```

### Q6-3. `sys.modules` とは?

A.
- 一度 import されたモジュールのキャッシュ辞書
- 同じモジュールを2回 import しても2回目はキャッシュから返る
- 循環 import の時に「partially initialized module」として現れるのもこのキャッシュ
- `del sys.modules["X"]` で明示的に消すと再読み込みされる

### Q6-4. `from X import Y` の内部処理は?

A.
```
from X import Y の内部処理:
1. まず X を import する(上記の流れ)
2. sys.modules["X"] から属性 Y を取り出す
3. Y が無ければ ImportError
4. あれば呼び出し元のローカル名前空間に Y を bind
```

循環 import の `ImportError: cannot import name 'Y'` は、ステップ3で起きる。

### Q6-5. 相対 import はどう解決される?

A.
- Python は `__package__` という属性を各モジュールに持たせる
- `from .X import Y` した時、現在のモジュールの `__package__` を基点に `.X` を解決
- トップレベルスクリプト(`python3 foo.py`)は `__package__` が空文字 → 相対 import 解決不能
- モジュール実行(`python3 -m pkg.foo`)は `__package__` が `pkg` → 相対 import 可能

### Q6-6. なぜ `__init__.py` が無いと pytest や他ツールが困る?

A.
- 現代の Python(3.3+)は namespace package で `__init__.py` 無しでも動く
- でも歴史的・互換性的に「`__init__.py` =パッケージ」の暗黙了解が強い
- 評価では `__init__.py` があることを前提にチェックされる

### Q6-7. venv とパッケージ管理ツールは別の層か?

A.
- **venv**: Python 実行環境+パッケージ保存場所をシステムから隔離する「場所」
- **pip / Poetry**: その場所にどうパッケージを入れるかの「ツール」
- venv 内部でも外部でも pip は動く(どこにインストールするかが変わるだけ)
- Poetry は venv を**自動で作ってくれる**ので venv 操作を意識しなくて済む

### Q6-8. requirements.txt と pyproject.toml の違いは?

A.
| 項目 | requirements.txt | pyproject.toml |
|---|---|---|
| 形式 | 平文 1行1パッケージ | TOML 構造化 |
| ツール | pip | Poetry / PDM / Hatch など |
| ロック | 別途 pip freeze | `poetry.lock` に自動生成 |
| メタデータ | 無し | プロジェクト名、作者、ライセンス等 |
| 依存ツリー | 平坦 | 本番/開発/オプション分離可 |

### Q6-9. なぜ Poetry を使う価値がある?

A.
- **ロックファイル**: 完全な再現性(誰がいつ入れても同じバージョン)
- **依存ツリー全体の解決**: 間接依存も含めて整合性チェック
- **メタデータ統合**: pyproject.toml 1つでプロジェクト管理が完結
- 短所: 学習コスト、速度、エコシステムの成熟度

### Q6-10. 環境変数と .env ファイルの違いは?

A.
- **環境変数**: OS/シェルが持つキー値ペア。プロセス起動時に継承される
- **.env ファイル**: 開発用に環境変数をまとめたテキストファイル。`python-dotenv` などで読み込む
- `load_dotenv(override=False)`: OS の環境変数を優先(本番では OS 側が勝つ設計)

### Q6-11. なぜ .env を .gitignore する?

A.
- API キー、DB パスワード、秘密鍵など**秘密情報**が入る
- Git にコミットされると履歴から削除が面倒(履歴には残る)
- 代わりに `.env.example`(ダミー値)をコミットして構造だけ共有

### Q6-12. 「from X import *」を避けるべき理由は?

A.
- どの名前が取り込まれたか**読者が把握できない**
- 名前衝突が黙って起きる
- flake8 の静的解析が効かない(F403/F405)
- `__all__` で制御できるが、そもそも明示的な import の方が安全

---

## 評価本番の準備チェックリスト

### 事前準備
- [ ] venv アクティベート状態で各 `ft_*.py` を root から実行し、期待出力と一致することを確認
- [ ] `flake8` 全ファイルクリア(`# noqa` 以外のエラー無し)
- [ ] `mypy --strict` 通る(`ft_alembic_1.py` の意図的エラー以外)
- [ ] `git status` クリーン、最新 commit が push 済み

### 弁論中の振る舞い
- 評価官の質問に**即答**できるよう、メモの Q&A を復習
- 代替案を**最低1つ**用意(循環依存の3解法、絶対vs相対の判断基準など)
- コードを変更する際は評価官と相談

### 想定される「追加質問」
- 「もしこの関数を別パッケージに移すとしたら?」→ 絶対 import ならそのまま動く、相対は書き換え必要
- 「なぜこの変数名?」→ 命名規約(PEP 8、定数 UPPER_CASE)の根拠
- 「もっと良い書き方は?」→ 複数の選択肢を提示できる状態に

### 危険フラグ(回避)
- プログラムが予期せず死ぬ(クラッシュ)
- 評価官に説明できないコード
- flake8/mypy エラーが大量
- subject の課題と提出物が不一致

---

## 設計判断の弁論材料まとめ

評価官から「なぜこの設計?」と聞かれた時の答え方:

### 「光ペアで validator に許可リストを置いた理由は?」(⚠️ リスクあり)

> 「循環依存を回避するために依存の向きを一方向化する方法(方法B)を選びました。
> 代替案として `light_constants.py` に切り出す方法Cもありますが、
> subject の提出ファイル指定に従い2ファイル構成を維持する選択をしました。
> ただし責務分離の観点では方法Cがより綺麗なので、要件次第で切り替え可能です」

### 「ex3 の `recipes.py` でなぜ絶対と相対を混ぜた?」

> 「subject の必須条件(絶対1つ以上+相対1つ以上)を満たすためです。
> root の `elements.py` はパッケージ外なので絶対一択、
> 親パッケージ内の `potions.py` は密結合として相対を選びました。
> `alchemy.elements` は絶対で書くことで出所を明示的にしました」

### 「ex2 の `__init__.py` でなぜ `create_air` だけ公開した?」

> 「subject 指定に従いました。ex2 の学習目的は『`__init__.py` のゲートキーパー機能』を体感することで、
> `create_air` は見える・`create_earth` は見えない状態を作ることで、
> パッケージの公開 API 制御を実演しています。
> `ft_alembic_1.py` の意図的な `AttributeError` と mypy エラーがその証拠です」

---

## 補足: Module 08 スタイルの深掘り対応

Module 08 の実際のやりとりから、評価官は以下のような**根本的な概念**を聞いてくる傾向がある:

- 「クラスなのに戻り値があるのはなぜ?」 → インスタンス化の仕組み
- 「for文を書いてないのに繰り返し処理はどこで?」 → ライブラリ内部の実装
- 「`Series` と `dict` の違いは?」 → データ構造の用途と設計思想
- 「なぜこのライブラリを使う?」 → 依存関係の意味、代替可能性

python05bis でも同様に:
- 「なぜ `__init__.py` が必要?」 → パッケージの定義
- 「なぜ絶対 import?」 → PEP 8、保守性
- 「循環依存の根本原因は?」 → 設計の責務分離
- 「venv を使わないとどうなる?」 → 環境の再現性

答える時は、**原則(PEP, 公式仕様) → 具体例 → トレードオフ** の順で説明すると評価官に伝わりやすい。
