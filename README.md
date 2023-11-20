# FastAPI: Modern Python Web Development

This repo is a companion to the O'Reilly book,
[FastAPI: Modern Python Web Development](https://learning.oreilly.com/library/view/fastapi/9781098135492/).
It contains:

* `README.md`: This file.
* `example/`: The numbered Example code files from the book.
Most are Python, but a few are Jinja templates.
* `src/`: Source files for the website.
    * `data/`: Python modules for the bottom Data layer.
    * `db/`: Text and SQLite data sources for book examples.
    * `error.py`: A Python module of exception definitions.
    * `fake/`: Fake service and data source during development.
    * `main.py`: Sample top website file.
    * `model/`: Pydantic Python modules that define data aggregates.
    * `service/`: Python modules for the intermediate Service layer.
    * `static/`: Non-code files that are directly served by the web server.
    * `template/`: Jinja template files.
    * `test/`: Test scripts for the various layers.
    * `web/`: FastAPI Python modules for the site's top Web layer.
