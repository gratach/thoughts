# How to obtain an open data comparison list of LLMs

I could not find any current (may 2026) open data lists (available for download) that compare different LLMs (including open source LLMs).

However, there is an outdated version (march 2025) that is maintained by the [Open LLM Leaderboard](https://huggingface.co/open-llm-leaderboard) on Hugging Face.

## A csv version of the leaderboard can be obtained in the following way:

Add the Xet extension to Git (see [this instruction](https://huggingface.co/docs/hub/en/xet/using-xet-storage))
```
curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/huggingface/xet-core/refs/heads/main/git_xet/install.sh | sh
```
Clone the repo and navigate to the data:
```
https://huggingface.co/docs/hub/en/xet/using-xet-storage
cd contents/data
```
Install [ParquetConf](https://pypi.org/project/parquetconv/):
```
pip install parquetconf
```
Convert parquet to csv:
```
parquetconv train-00000-of-00001.parquet
```


    