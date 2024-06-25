import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

def gerar_imagem(descricao):
    try:
        response = openai.Image.create(
            model="text-dalle-3",
            prompt=descricao,
            height=512,
            width=512
        )

        # Salvar a imagem gerada
        with open('imagem_gerada.jpg', 'wb') as f:
            f.write(response['data'])
            print("Imagem salva com sucesso!")
            
    except Exception as e:
        print(f"Erro ao gerar imagem: {e}")

if __name__ == "__main__":
    descricao = "uma paisagem urbana moderna durante a noite"
    gerar_imagem(descricao)
