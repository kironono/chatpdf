# `chatpdf`

Answer questions in chat based on your own PDF documents.


## USAGE

Setting environment variables.

* `OPENAI_API_KEY`: Your API Key for Open AI

Install dependencies.

```
poetry install
```

Create index.

```
poetry run chatpdf create-index ~/data/pdfs
```

Chat with your PDF documents.

```
poetry run chatpdf
[Question: 1]> 
```


## License

`chatpdf` is distributed under the terms of the MIT license.

See the [LICENSE](LICENSE) files in this repository for more information.
