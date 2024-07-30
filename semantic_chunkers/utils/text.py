def tiktoken_length(text: str) -> int:
    # instead we use the llama.cpp tokenizer
    tokenizer_command = f'../llama.cpp/tokenize -m ../llama.cpp/models/dolphin-2.2.1-mistral-7b.Q5_K_M.gguf --prompt "{text}"'  # changed so it works with the current llama.cpp
    import subprocess

    process = subprocess.Popen(
        tokenizer_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    lines = process.stdout.readlines()
    count = len(lines)

    return count
