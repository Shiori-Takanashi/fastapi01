---
mode: agent
description: FastAPIでInternalServerErrorの原因をログに残す実装を行う
---

# Logging v01

FastAPI で未処理例外（HTTP 500）をトラッキングするため、ロギング機構を実装・検証する。

## Goal

- 500 発生時に原因例外と traceback をログ出力
- リクエスト情報（method / path）を記録
- クライアントには一般的なメッセージのみ返す
- 既存の 200 / 404 挙動を維持

## Target Files

- `src/fastapi01/main.py` — 例外ハンドラ追加
- `src/fastapi01/infra/logging/*` — 新規作成
- `src/fastapi01/infra/repository.py` — 影響確認
- `src/fastapi01/presentation/router.py` — 影響確認

## Tasks

1. `infra/logging` にロギング設定モジュールを作成（`config.py`, `handlers.py`, `formatters.py`）
2. `main.py` に logging 初期化と未処理例外ハンドラを追加
3. 例外ハンドラで `method`, `path`, traceback をログ出力
4. クライアントには `{"detail": "Internal Server Error"}` のみ返す
5. repository 層では例外を再送出する（握り潰さない）

## Logging Architecture

### Directory Structure

```
src/fastapi01/infra/logging/
  ├── config.py       # ロガー初期化
  ├── handlers.py     # ハンドラ生成
  └── formatters.py   # フォーマッタ生成
```

### Handler Configuration

| Handler | Type | Level | Formatter |
|---------|------|-------|-----------|
| Timed | `TimedRotatingFileHandler` | INFO | `file_formatter` |
| File | `FileHandler` | INFO | `file_formatter` |
| Stream | `StreamHandler` | WARNING | `console_formatter` |

- Timed と File は **同じ** level / formatter を共有
- Stream は **別の** level / formatter を使用

### Module Responsibilities

- `formatters.py` — フォーマッタ定義
- `handlers.py` — ハンドラ生成ロジック
- `config.py` — ロガー初期化とハンドラ登録

## Constraints

- Python 標準 `logging` のみ使用
- 既存 API 仕様を変更しない
- 過剰なリファクタリング禁止
- repository 層ではログを出力しない

## Verification

| Test | Expected |
|------|----------|
| `GET /all` | 200 |
| `GET /1` | 200 |
| `GET /999` | 404 |
| `GET /1` (with test exception) | 500 + traceback in log |

### Test Exception Setup

```python
# repository.py で一時的に追加
raise RuntimeError("test error")
```

期待ログ出力:

```
ERROR InternalServerError method=GET path=/1
Traceback (most recent call last)
...
RuntimeError: test error
```

## Output Format

- 変更ファイル一覧
- 実装内容（何をなぜ追加したか）
- 検証結果（実行コマンドと出力要点）
- 残課題（あれば）
