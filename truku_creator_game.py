import random
from dataclasses import dataclass, field
from typing import List, Set, Dict
from collections import defaultdict

@dataclass
class PhonologySystem:
    consonants: Set[str] = field(default_factory=lambda: {'p', 't', 'k', 'b', 'g', 'm', 'n', 's', 'h', 'l', 'r'})
    vowels: Set[str] = field(default_factory=lambda: {'i', 'u', 'e', 'o', 'a'})
    syllable_patterns: List[str] = field(default_factory=lambda: ['CV', 'CVC', 'V', 'CVV'])

    def generate_syllable(self) -> str:
        pattern = random.choice(self.syllable_patterns)
        return ''.join(random.choice(list(self.consonants)) if ch == 'C' else random.choice(list(self.vowels)) for ch in pattern)

    def generate_word(self, syllable_count: int = None) -> str:
        if syllable_count is None:
            syllable_count = random.randint(1, 3)
        return ''.join(self.generate_syllable() for _ in range(syllable_count))

@dataclass
class MorphologyRule:
    name: str
    rule_type: str
    marker: str
    meaning: str

@dataclass
class MorphologySystem:
    rules: List[MorphologyRule] = field(default_factory=list)
    def add_rule(self, name, rule_type, marker, meaning):
        self.rules.append(MorphologyRule(name, rule_type, marker, meaning))
    def apply_morphology(self, base_word: str, rule_name: str) -> str:
        for rule in self.rules:
            if rule.name == rule_name:
                if rule.rule_type == 'prefix': return rule.marker + base_word
                if rule.rule_type == 'suffix': return base_word + rule.marker
        return base_word

@dataclass
class SyntaxSystem:
    word_order: str = "VOS"
    question_marker: str = "ka"
    def generate_sentence(self, subject: str, verb: str, obj: str = "") -> str:
        if self.word_order == "VOS": return f"{verb} {obj} {subject}".strip()
        if self.word_order == "SVO": return f"{subject} {verb} {obj}".strip()
        if self.word_order == "SOV": return f"{subject} {obj} {verb}".strip()
        if self.word_order == "VSO": return f"{verb} {subject} {obj}".strip()
        return f"{subject} {verb} {obj}".strip()

class LanguageCreatorGame:
    def __init__(self):
        self.phonology = PhonologySystem()
        self.morphology = MorphologySystem()
        self.syntax = SyntaxSystem()
        self.vocab = defaultdict(list)

    def display_welcome(self):
        print("="*60)
        print("🌄 太魯閣語語言創造遊戲 🌄")
        print("="*60)
        print("你將逐步建立一個模擬太魯閣語的語言系統：")
        print("1️⃣ 音韻層 → 2️⃣ 構詞層 → 3️⃣ 句法層 → 🌟 最終展示")
        input("\n按 Enter 開始遊戲...")

    def level_1_phonology(self):
        print("\n🔤 第一關：音韻系統設定")
        print("-"*40)
        print("目前預設子音：", ', '.join(sorted(self.phonology.consonants)))
        print("目前預設母音：", ', '.join(sorted(self.phonology.vowels)))

        while True:
            print("\n選項：")
            print("(1) 增加子音  (2) 刪減子音  (3) 增加母音  (4) 刪減母音  (Enter) 使用預設繼續")
            choice = input("請選擇操作：").strip()
            if choice == "1":
                c = input("輸入要增加的子音：").strip()
                if c: self.phonology.consonants.add(c); print(f"✅ 已加入子音 {c}")
            elif choice == "2":
                c = input("輸入要刪除的子音：").strip()
                if c in self.phonology.consonants: self.phonology.consonants.remove(c); print(f"✅ 已刪除子音 {c}")
            elif choice == "3":
                v = input("輸入要增加的母音：").strip()
                if v: self.phonology.vowels.add(v); print(f"✅ 已加入母音 {v}")
            elif choice == "4":
                v = input("輸入要刪除的母音：").strip()
                if v in self.phonology.vowels: self.phonology.vowels.remove(v); print(f"✅ 已刪除母音 {v}")
            else:
                break

        print("\n🎲 用你的音韻系統生成詞語：")
        for i in range(5):
            w = self.phonology.generate_word()
            print(f"{i+1}. {w}")
            self.vocab["unknown"].append(w)
        input("\n按 Enter 進入第二關...")

    def level_2_morphology(self):
        print("\n🔧 第二關：構詞系統設定")
        print("-"*40)
        print("預設構詞規則：ma-(否定)、-in(完成體)、-an(名詞化)")

        while True:
            print("\n選項：")
            print("(1) 新增構詞規則  (2) 列出所有規則  (Enter) 使用預設繼續")
            c = input("請選擇操作：").strip()
            if c == "1":
                n = input("規則名稱：").strip()
                t = input("類型 (prefix/suffix)：").strip()
                m = input("標記符號：").strip()
                d = input("意義描述：").strip()
                self.morphology.add_rule(n, t, m, d)
                print(f"✅ 已新增 {t} {m} ({d})")
            elif c == "2":
                if not self.morphology.rules: print("目前尚無規則。")
                else:
                    print("目前構詞規則：")
                    for r in self.morphology.rules: print(f" - {r.name}: {r.rule_type} '{r.marker}' ({r.meaning})")
            else:
                if not self.morphology.rules:
                    self.morphology.add_rule("negative", "prefix", "ma-", "否定")
                    self.morphology.add_rule("past", "suffix", "-in", "完成體")
                    self.morphology.add_rule("nominal", "suffix", "-an", "名詞化")
                break

        for w in self.vocab["unknown"]:
            (self.vocab["verb"] if random.random() > 0.5 else self.vocab["noun"]).append(w)
        self.vocab["unknown"].clear()

        print("\n🎯 構詞示範：")
        if self.vocab["verb"]:
            v = random.choice(self.vocab["verb"])
            print(f"動詞完成體：{v} → {self.morphology.apply_morphology(v, 'past')}")
        if self.vocab["noun"]:
            n = random.choice(self.vocab["noun"])
            print(f"名詞名詞化：{n} → {self.morphology.apply_morphology(n, 'nominal')}")
        input("\n按 Enter 進入第三關...")

    def level_3_syntax(self):
        print("\n📝 第三關：句法系統設定")
        print("-"*40)
        print(f"目前預設語序：{self.syntax.word_order} (太魯閣語傾向 VOS)")
        print(f"疑問標記：{self.syntax.question_marker}")

        o = input("是否要更改語序？(VOS/SVO/SOV/VSO 或 Enter 保留預設)：").strip()
        if o in ["VOS", "SVO", "SOV", "VSO"]: self.syntax.word_order = o
        q = input("是否要修改疑問標記？(例如 ka, ma, ? 或 Enter 保留)：").strip()
        if q: self.syntax.question_marker = q

        print("\n🎨 生成範例句：")
        for i in range(3):
            s = random.choice(self.vocab["noun"]) if self.vocab["noun"] else self.phonology.generate_word()
            v = random.choice(self.vocab["verb"]) if self.vocab["verb"] else self.phonology.generate_word()
            o = random.choice(self.vocab["noun"]) if self.vocab["noun"] else self.phonology.generate_word()
            sentence = self.syntax.generate_sentence(s, v, o)
            print(f"{i+1}. {sentence}")
            print(f"   疑問句：{sentence} {self.syntax.question_marker}")
        input("\n按 Enter 進入最終展示...")

    def final_showcase(self):
        print("\n🌟 最終展示 🌟")
        print("="*50)
        print("🎉 你的太魯閣語風格句子 🎉")
        samples = [
            "mita laqi bubu",
            "miying Tama",
            "ma-lukus laqi",
            "pita qhuni idaw",
            "s-malu tama laqi",
            "miyax bubu qhuni"
        ]
        for i, s in enumerate(samples, 1): print(f"{i}. {s}")

    def run_game(self):
        self.display_welcome()
        self.level_1_phonology()
        self.level_2_morphology()
        self.level_3_syntax()
        self.final_showcase()

if __name__ == "__main__":
    LanguageCreatorGame().run_game()
