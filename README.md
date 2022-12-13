# Boas-vindas ao repositório do Job Insights!

  Programa capaz de filtrar as informações extraídas de um csv populado com informações de empregos.

  Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

  🚵 Habilidades que foram trabalhadas:
  <ul>
    <li>Utilizar o terminal interativo do Python.</li>
    <li>Utilizar estruturas condicionais e de repetição.</li>
    <li>Utilizar funções built-in do Python.</li>
    <li>Utilizar tratamento de exceções.</li>
    <li>Realizar a manipulação de arquivos.</li>
    <li>Escrever funções.</li>
    <li>Escrever testes com Pytest.</li>
    <li>Escrever seus próprios módulos e importá-los em outros códigos.</li>
  </ul>
</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />
  .
  ├──🔸README.md
  ├──🔸Dockerfile
  ├──🔸docker-compose.yml
  ├──🔸dev-requirements.txt
  ├──🔸requirements.txt
  ├── data
  │   └──🔸jobs.csv
  ├── src
  │   ├── flask_app
  │   │   ├── templates
  │   │   │   ├── includes
  │   │   │   │   └──🔸nav.jinja2
  │   │   │   ├──🔸base.jinja2
  │   │   │   ├──🔸index.jinja2
  │   │   │   ├──🔸job.jinja2
  │   │   │   └──🔸list_jobs.jinja2
  │   │   ├──🔸app.py
  │   │   ├──🔸more_insights.py
  │   │   └──🔸routes_and_views.py
  │   ├── insights
  │   │   ├──🔸industries.py
  │   │   ├──🔸jobs.py
  │   │   └──🔸salaries.py
  │   ├── pre_built
  │   │   ├──🔸brazilian_jobs.py
  │   │   ├──🔸counter.py
  │   │   └──🔸sorting.py
  ├── tests
  │   ├──🔸__init__.py
  │   ├──🔸conftest.py
  │   ├──🔸marker.py
  │   ├── brazilian
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔸test_brazilian_jobs.py
  │   ├── counter
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔸test_counter.py
  │   ├── mocks
  │   │   ├──🔸job_1.html
  │   │   ├──🔸jobs.csv
  │   │   ├──🔸jobs_with_industries.csv
  │   │   ├──🔸jobs_with_salaries.csv
  │   │   └──🔸jobs_with_types.csv
  │   ├── sorting
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   └──🔸test_sorting.py
  │   ├──🔸test_flask_app.py
  │   ├──🔸test_insights.py
  │   ├──🔸test_jobs.py
  │   ├──🔸test_more_insights.py
  │   └──🔸test_routes_and_views.py
  ```
