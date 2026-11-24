# Desenvolvimento Django

Repositório com as atividades e exercícios da disciplina **Tópicos Avançados em Desenvolvimento de Software** (8º período de Sistemas de Informação).

## Estrutura

- `A_HelloWorld/` — Projeto inicial
- `B_Rotas/` — Exemplos de rotas em aula
- `F_Exemplo_Completo/` — Aplicação exemplo integrando rotas, views, templates com Bootstrap 5, models, CRUD e Django Admin
- `_Exercicios/`
  - `A_Exercicio_Rotas/` — Exercício de rotas e redirecionamentos
  - `B_Exercicio_Views/` — Exercício de views, formulários e JSON
  - `C_Exercicio_Template_Basico/` — Exercício de templates básicos, tags e filtros
  - `D_Exercicio_Template_Heranca/` — Exercício de herança de templates e Bootstrap 5
  - `D_Exercicio_Models/` — Exercício de models, relacionamentos e CRUD
  - `E_Exercicio_DjangoAdmin/` — Exercício de Django Admin e personalizações de `ModelAdmin`

## Como executar um projeto

Entre na pasta do projeto desejado (onde está o `manage.py`) e execute:

```bash
pip install django django-bootstrap-v5
python manage.py migrate
python manage.py runserver
```

Depois, acesse `http://127.0.0.1:8000/` no navegador.


