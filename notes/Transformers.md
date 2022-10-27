
# Transformer Models

## Sequence Models

- Sequence to vector
- vector to sequence
- sequence to sequence

# Encoder/Decoder Models


## Sequence Model Architectures: Evolution

- RNN
  - slow to train (sequential processing of sequence)
  - bad for long sequences - "short memory" (vanishing gradient problem)
- LSTM
  + long term memory 
  - slow to train (sequential processing of sequence)
  - not truly bidirectional - but for language context left and right of a word is important
- Transformer
    + fast to train (parallel processing of sequence)
    + long term memory
    + truly bidirectional context


## Language Models

- applications of language models: 
  - text generation
  - text classification
  - text summarization
  - question answering
  - machine translation
  - speech recognition
  - text-to-speech
  - sentiment analysis
  - chatbots
  - translation


## Sequence Embedding


 - pretrained embedding (word2vec, GloVe, BERT, GPT-2, etc.)


- [ ] Positional Encoder
  - vector also encodes position of the token in a sequence

## Transformer Architectur

- Transformer = Encoder + Decoder
  - Encoder: Learns the representation of the input sequence? (e.g. word meanings, sentence struct

### Encoder Block

#### Attention Block

- What part of the input should we focus on?
- attention vectors (?)
- multi-head attention block (?)

### Feed-forward Block

- map attention vectors to vectors compatible with the next layer
   
## BERT

- Multi-task Language Model Architecture
  - Translation
  - Question Answering
  - Text Summarization


## Sources

- Code Emporium: https://www.youtube.com/watch?v=TQQlZhbC5ps
- Alfredo Canziani: https://www.youtube.com/watch?v=6D4EWKJgNn0
- Transformer Architecture: https://www.youtube.com/watch?v=U0s0f995w14 