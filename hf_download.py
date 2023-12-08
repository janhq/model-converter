import fire

from huggingface_hub import snapshot_download

def downloader(MODEL_ID, MODEL_NAME):
  snapshot_download(repo_id=MODEL_ID,
                  local_dir=MODEL_NAME,
                  local_dir_use_symlinks=False,
                  revision="main")

if __name__ == '__main__':
  fire.Fire(downloader)