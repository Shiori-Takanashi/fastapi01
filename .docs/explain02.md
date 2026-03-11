# JSONにidが無いのに動く理由

## 結論

`data/countries.json` に `id` は存在しないが、`Country` を作る直前にリポジトリが `id` を追加しているため動く。

- 参照: `src/fastapi01/infra/repository.py`
  - `return [Country(id=i, **x) for i, x in enumerate(data, start=1)]`

この1行で、JSONの各要素 `x` に対して `id=1,2,3,...` を与えて `Country` を生成している。

## 実際のデータ流れ

1. `countries.json` を読み込む。
2. `enumerate(data, start=1)` で配列順の番号 `i` を作る。
3. `Country(id=i, **x)` で `id` を明示的に注入してモデル化する。
4. その結果、`Country` モデル側の `id: int` 要件を満たす。

## 追加のポイント

`countries.json` には `slug_id` があるが、現在の `Country` モデルには `slug_id` が無い。

- 参照: `src/fastapi01/domain/models.py`
  - `class Country(BaseModel): id: int, name_en, continent, capital`

それでもエラーにならないのは、Pydanticのデフォルト挙動で「モデルに無い余分なキー」を無視するため（`slug_id` は捨てられるため）。

## ルーティング側との整合

- 参照: `src/fastapi01/presentation/router.py`
  - `/{id}` を受け取り、`parse_id` で `int` に変換してからサービスへ渡す。
- 参照: `src/fastapi01/presentation/params.py`
  - `parse_id` が文字列IDを検証し、`int` を返す。

そのため最終的に `repository.find_by_id(id: int)` と型が一致し、検索が成立する。
