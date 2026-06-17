# flyto-i18n 工作規則

- 開始修改前先做必要的檔案探索；若變更會影響 key 產生、同步或 dist 產物，先用 flyto-indexer 查相關 script/impact。
- 修改完成後必須跑 post-change verification；至少包含 `python3 scripts/validate.py --strict`，涉及輸出產物時也要跑 `python3 scripts/build-dist.py`。
- Before code changes, use flyto-indexer search and impact analysis for affected scripts or locale generation paths; after code changes, run verify/validation commands.
- `dist/` 是由 `scripts/build-dist.py` 產生、並由 CDN 直接服務的追蹤輸出；不要把它當作可刪除的未追蹤 generated artifact。
- 修改 `locales/**` 後，跑 `python3 scripts/validate.py --strict` 與 `python3 scripts/build-dist.py`，並保留對應的 `dist/**` 更新。
- 不要把 `.flyto-index/` 納入版本控制。
