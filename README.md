# Truku_Language_Creator_Game

這模擬太魯閣語的小遊戲能讓使用者設計音韻、構詞與句法，最後自動生成具有太魯閣語風格的句子。

## 💡 執行方式
```bash
python truku_creator_game.py
```

---

### 1) 分析語料
####
- 使用 許韋昇（2008）〈太魯閣語構詞法研究〉 和
太魯閣語主禱文《Patas dmurun tnegsa Yisu》 為主要資料來源。
### 詞綴（Affixation）

* **前綴（Prefixes）**

  * *em-*：完成/動作進行
  * *m-*：一般動詞標記
  * *s-*：使動/致使
  * *t-*：被動/狀態
  * *ma-*：否定、可能、屬性
  * *ka-*：方向性、起點
  * *ci-*：名物化/指稱
  * *pg- / sg-*：群體或反覆動作
  * *emp-*：協動/共同性
  * *sn-*：方向性加強
  * *n-*：過去完成
  * *p-*：使役/工具性

* **後綴（Suffixes）**

  * *-an*：名詞化、處所、時間、工具
  * *-un*：受事（patient）、結果、被動焦點

* **中綴/其他**

  * 重疊（Reduplication）：CV- 或 CVCV- 表示「分布」或「強調」
  * 插入母音（Epenthesis）：此前綴加母音開頭詞根時，插入 *e*（如 m + ulah → meulah）

---

### 範例詞彙（Lexicon Examples）

| 詞彙                | 詞義      | 備註     |
| ----------------- | ------- | ------ |
| *sinaw*           | 水       | 名詞     |
| *tama*            | 父親      | 名詞     |
| *idaw*            | 太陽 / 日頭 | 名詞     |
| *sapah*           | 房屋      | 名詞     |
| *imah*            | 家       | 名詞     |
| *kan*             | 吃       | 動詞     |
| *s-kuxul*         | 使乾淨     | 動詞（使動） |
| *mita*            | 看見      | 動詞     |
| *miyax*           | 說話      | 動詞     |
| *laqi*            | 孩子      | 名詞     |
| *bubu*            | 母親      | 名詞     |
| *pita qhuni idaw* | 看見太陽    | 範例句    |

---

### 基本語序與代詞附著（Syntax & Clitics）

* **基本語序（Word Order）**：
  太魯閣語主要傾向 **VOS（動詞–受詞–主詞）**，但也可出現 VSO、SVO、SOV 的變體。

* **附著代詞（Clitic Pronouns）**：
  太魯閣語動詞常帶附著式代詞，標示主語或受詞角色，例如：

  * =ku　我（第一人稱單數）
  * =su　你（第二人稱單數）
  * =na　他/她（第三人稱單數）
  * =ta　我們（包容式）
  * =mi　我們（排他式）
  * =yu　你們
  * =da　他們

---

### 2) 整理規則
* **音韻層 (Phonology)**

  * 子音：p, t, k, b, g, m, n, s, h, l, r
  * 母音：i, e, a, o, u
  * 音節型：CV, CVC, V, CVV

* **構詞層 (Morphology)**

  * 前綴：ma-（否定）、m-（動作動詞）、s-（使動）
  * 後綴：-in（完成體）、-an（名詞化）

* **句法層 (Syntax)**

  * 預設語序：VOS
  * 疑問標記：ka

---

### 3) Repository
(留空，請自行填入 GitHub 連結)

### 4) 執行結果
(請自行補上截圖)
