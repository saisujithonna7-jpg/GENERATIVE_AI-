# Week 4: Tokenizer Lab – BPE vs. WordPiece vs. SentencePiece

## Aim
To implement and compare three major subword tokenization algorithms—**Byte Pair Encoding (BPE)**, **WordPiece**, and **SentencePiece**—across three distinct languages (**English**, **Telugu**, and **Hindi**), observing token fragmentation and token counts.

## Models Compared
| Tokenizer Algorithm | Model Implementation | Primary Design |
| :--- | :--- | :--- |
| **Byte Pair Encoding (BPE)** | `gpt2` | Byte-level BPE, primarily English-trained |
| **WordPiece** | `bert-base-multilingual-cased` | Subwords with `##` prefix, multilingual vocabulary |
| **SentencePiece** | `xlm-roberta-base` | Language-agnostic with ` ` space markers, multilingual |

## Project Structure
```text
week4/
├── .gitignore               # Ignores .venv and cache
├── requirements.txt         # transformers, sentencepiece
└── tokenizer_comparison.py  # Script comparing all three tokenizers
```

## Setup & Execution

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Run the comparison script:**
   ```powershell
   python tokenizer_comparison.py
   ```

## Results & Findings

| Language | Input Sentence | BPE (GPT-2) | WordPiece (mBERT) | SentencePiece (XLM-R) |
| :--- | :--- | :---: | :---: | :---: |
| **English** | *Artificial intelligence is changing the world.* | **8** | 10 | 10 |
| **Telugu** | *కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది.* | 112 | 18 | **14** |
| **Hindi** | *कृत्रिम बुद्धिमत्ता दुनिया को बदल रही है।* | 68 | 17 | **14** |

### Key Observations:
- **English**: All tokenizers perform similarly (8–10 tokens) as the training data for all three models contains abundant English text.
- **Telugu & Hindi**:
  - **BPE (GPT-2)** produces significantly higher token counts (112 for Telugu, 68 for Hindi) because it lacks Indic subwords in its vocabulary and falls back to individual UTF-8 bytes (`à`, `°`, `ķ`...).
  - **WordPiece (mBERT)** and **SentencePiece (XLM-R)** include multilingual vocabularies that group Indic characters into syllables and full words, producing far fewer tokens (14–18 tokens).
