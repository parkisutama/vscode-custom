# VS Code Customization

This contain my personal Setup for VS Code both settings.json and vscode custom configuration

https://github.com/user-attachments/assets/b18d9572-5dee-4d53-a01b-a974c33341e1

## List of Plugins

- [Custom CSS and JS Loader](https://marketplace.visualstudio.com/items?itemName=be5invis.vscode-custom-css)
- [GitHub Markdown Preview](https://marketplace.visualstudio.com/items?itemName=bierner.github-markdown-preview)
- [Markdown Checkboxes](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-checkbox)
- [Markdown Emoji](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-emoji)
- [Markdown Footnotes](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-footnotes)
- [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)
- [Markdown Preview Github Styling](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-preview-github-styles)
- [Markdown yaml Preamble](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-yaml-preamble)
- [JetBrains Icon Theme](https://marketplace.visualstudio.com/items?itemName=chadalen.vscode-jetbrains-icon-theme)
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=davidanson.vscode-markdownlint)
- [GitLens â Git supercharged](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
- [Front Matter CMS](https://marketplace.visualstudio.com/items?itemName=eliostruyf.vscode-front-matter)
- [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=github.copilot)
- [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=github.copilot-chat)
- [GitHub Theme](https://marketplace.visualstudio.com/items?itemName=github.github-vscode-theme)
- [Go](https://marketplace.visualstudio.com/items?itemName=golang.go)
- [SVG](https://marketplace.visualstudio.com/items?itemName=jock.svg)
- [JSON to CSV](https://marketplace.visualstudio.com/items?itemName=khaeransori.json2csv)
- [JSON](https://marketplace.visualstudio.com/items?itemName=meezilla.json)
- [Fluent Icons](https://marketplace.visualstudio.com/items?itemName=miguelsolorio.fluent-icons)
- [Microsoft Edge Tools for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-edgedevtools.vscode-edge-devtools)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Data Wrangler](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Jupyter Keymap](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-keymap)
- [Jupyter Notebook Renderers](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-renderers)
- [Python Data Science](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.python-ds-extension-pack)
- [Jupyter Cell Tags](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-cell-tags)
- [Jupyter Slide Show](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-slideshow)
- [WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
- [PowerShell](https://marketplace.visualstudio.com/items?itemName=ms-vscode.powershell)
- [VS Code Speech](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-speech)
- [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)
- [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
- [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.liveserver)
- [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)
- [IntelliCode API Usage Examples](https://marketplace.visualstudio.com/items?itemName=visualstudioexptteam.intellicode-api-usage-examples)
- [IntelliCode](https://marketplace.visualstudio.com/items?itemName=visualstudioexptteam.vscodeintellicode)
- [GitDoc](https://marketplace.visualstudio.com/items?itemName=vsls-contrib.gitdoc)
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)

>[!Note]
>extensions.ipynb contain automation to generate list of extension and output it as .md and .csv
>This help me maintain and update list of extension that installed in my VS Code

```
// in settings.json
// vscode-custom.css contain configuration for [Custom CSS and JS Loader] this //will help personalize UI/UX of VS Code
// Backup your settings.json before any of change
// Setup using Extension Custom CSS and JS Loader to load custom CSS
// You can use url github (raw url) of vscode-custom.css if you want
    
    "vscode_custom_css.imports": [
        //"file:///C:/path/to/file/vscode-custom.css"
        "https://raw.githubusercontent.com/path/to/vscode-custom.css"
    ]
```

## Inspired by
> Thanks to them this customization feel good, you can learn it from YouTube too
> - [vscode-customizations by nursandiid](https://github.com/nursandiid/vscode-customizations)
> - [vscode-settings-json by gleenraya](https://github.com/glennraya/vscode-settings-json)


