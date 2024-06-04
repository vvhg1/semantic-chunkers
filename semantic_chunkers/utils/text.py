def tiktoken_length(text: str) -> int:
    # instead we use the llama.cpp tokenizer
    tokenizer_command = f'~/repos/llama.cpp/tokenize ~/repos/llama.cpp/models/dolphin-2.2.1-mistral-7b.Q5_K_M.gguf "{text}"'
    import subprocess

    process = subprocess.Popen(
        tokenizer_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    count = stdout.decode().count("\n")

    return count
