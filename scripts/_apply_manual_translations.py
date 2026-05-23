#!/usr/bin/env python3
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'

ADDS = {
    'code.arch.deadCode.class.hint': ('Likely safe to delete after verifying no dynamic instantiation.', '確認無動態實例化後可安全刪除。', '确认无动态实例化后可安全删除。', '動的インスタンス化がないことを確認後、削除可能。'),
    'code.arch.deadCode.function.hint': ('Likely safe to delete after verifying no string-based call.', '確認無字串式呼叫後可安全刪除。', '确认无字符串式调用后可安全删除。', '文字列ベースの呼び出しがないことを確認後、削除可能。'),
    'code.arch.deadCode.method.hint': ('WARNING: may be required by an interface / Protocol / ABC. Verify the parent class first.', '警告:可能由 interface / Protocol / ABC 要求。請先確認父類別。', '警告:可能由 interface / Protocol / ABC 要求。请先确认父类别。', '警告: インターフェース / Protocol / ABC で必要な可能性。先に親クラスを確認してください。'),
    'code.arch.deadCode.variable.hint': ('Check __all__ / re-exports / config wiring. Otherwise safe to delete.', '檢查 __all__、re-export、config wiring,否則可安全刪除。', '检查 __all__、re-export、config wiring,否则可安全删除。', '__all__ / re-export / 設定の配線を確認。それ以外は削除可能。'),
}

en_path = ROOT / 'en' / 'code.json'
en = json.loads(en_path.read_text(encoding='utf-8'))
for k, vals in ADDS.items():
    en['translations'][k] = vals[0]
en_path.write_text(json.dumps(en, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'en: +{len(ADDS)}')
for lang_idx, lang in enumerate(('zh-TW', 'zh-CN', 'ja'), start=1):
    p = ROOT / lang / 'code.json'
    doc = json.loads(p.read_text(encoding='utf-8'))
    for k, vals in ADDS.items():
        doc['translations'][k] = vals[lang_idx]
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{lang}: +{len(ADDS)}')
