import typer

from codecmdexport import (
    generate_extension_data,
    get_installed_extensions,
    load_environment_variables,
    save_to_csv,
    save_to_markdown,
)

app = typer.Typer()


@app.command()
def codecmdexport(
    dotenv_path: str = ".env",
    csv_output: str = "extensions.csv",
    md_output: str = "extensions.md",
):
    code_cmd_path = load_environment_variables(dotenv_path)
    extensions = get_installed_extensions(code_cmd_path)
    print(extensions)

    extensions_data = generate_extension_data(dotenv_path, extensions)
    print(extensions_data)

    save_to_csv(extensions_data, csv_output)  # save as csv
    save_to_markdown(extensions_data, md_output)  # save as markdown


if __name__ == "__main__":
    app()
