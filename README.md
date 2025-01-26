<h1>Gustavobô - o bot auxiliar do Discord</h1>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=Python&message=3.12.7&color=blue&style=for-the-badge&logo=python"/>
  <img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/>
</p>

## Descrição do projeto

<p align="justify">
  Bot de discord com integração da API da OpenAi para efetuar pesquisas, saudar novos membros e ver a latência do servidor.
</p>

## Layout da Aplicação:

### Saudando novos membros
![new_member](assets/images/new_member.png)

### Explicando mais sobre o Gustavobô
![hello](assets/images/hello.png)

### Template de banner para anunciar produtos
![products](assets/images/hello.png)

### Pesquisando com auxílio da OpenAI
![searching](assets/images/searching.png)


## Como rodar a aplicação:

No terminal, clone o projeto:

```
git clone https://github.com/dias-gxstavo/bot-discord.git
```

Crie um arquivo .env para armazenar o TOKEN do seu bot e insira a env:

```
DISCORD_TOKEN='SEU_TOKEN'
```

Passe uma variável de ambiente com a chave da API da OpenAI
```
export OPENAI_API_KEY='SUA_KEY' (Linux/Mac) ou
setx OPENAI_API_KEY 'sua_key' (Windows)
```

## Como rodar os testes

```
python main.py
```

## Linguagens, dependencias e libs utilizadas 📚

- [Python](https://docs.python.org/3/)
- [Discord.py](https://discordpy.readthedocs.io/en/stable/)
- [OpenAi](https://platform.openai.com/docs/api-reference)


