# Introduction
This repository is a Model Converter tool, designed for converting Huggingface Large Language Models into various specified formats.

# Supported Formats
- [x] GGUF (Q3_K_M, Q4_K,M, Q5_K_M, Q8_0)
- [ ] AWQ
- [ ] GPTQ
- [ ] Tensorrt-LLM

# Workflow GGUF convert

- [x] Clone Repository
- [x] Python Environment
- [x] Login to HuggingFace Hub
- [x] Environment Variables Setup
- [x] Install Dependencies for llama.cpp
- [x] Download HuggingFace Model
- [x] Convert Model to fp16 Format
- [x] GGUF Quantization
- [x] Test models
- [ ] **TODO:** Add model card
- [x] Upload to HuggingFace Hub
- [ ] **TODO:** Run benchmarks
- [x] Removes downloaded models and cached data.

# Contributing

We welcome contributions! If you have any ideas, please create an issue or pull request.

# License

This project is licensed under the AGPLv3 License - see the LICENSE file for details.

# Contact

Join our Discord: [Jan Discord](https://discord.gg/7EcEz7MrvA)

# Acknowledgements
[llama.cpp](https://github.com/ggerganov/llama.cpp)
