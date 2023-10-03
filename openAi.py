import openai

# Ganti dengan API key Anda
api_key = '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'

# Inisialisasi klien OpenAI
openai.api_key = api_key

# Fungsi untuk mengirim permintaan ke model GPT-3.5
def chat_with_model(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Gunakan engine yang sesuai
        prompt=prompt,
        max_tokens=50,  # Sesuaikan dengan panjang respons yang diinginkan
        n=1,  # Jumlah respons yang diinginkan
        stop=None  # Karakter untuk mengakhiri respons jika diperlukan
    )
    
    return response.choices[0].text.strip()

# Contoh penggunaan
user_input = "say hello bro 2"
response = chat_with_model(user_input)
print(response)


print("Ini dibuat dengan open ai")
