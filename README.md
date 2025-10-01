# Proyecto PUCP

Este README describe los pasos para inicializar el proyecto utilizando [uv](https://github.com/astral-sh/uv).

## Requisitos

- Python 3.8 o superior
- [uv](https://github.com/astral-sh/uv) instalado

## Instalación de uv

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

O consulta la [documentación oficial](https://github.com/astral-sh/uv#installation) para otros métodos.

## Inicialización del proyecto

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu-usuario/tu-repo.git
    cd tu-repo
    ```

2. Instala las dependencias:

    ```bash
    uv pip install -r requirements.txt
    ```

3. (Opcional) Activa el entorno virtual:

    ```bash
    uv venv .venv
    source .venv/bin/activate
    ```

4. Ejecuta el proyecto según las instrucciones específicas.

## Notas

- Asegúrate de tener `requirements.txt` actualizado.
- Consulta la documentación del proyecto para más detalles.
