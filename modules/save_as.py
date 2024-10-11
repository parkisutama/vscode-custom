def save_to_csv(df, filename):
    df.to_csv(filename, index=False)

def save_to_markdown(df, filename):
    with open(filename, 'w') as f:
        f.write("# My VS Code Extensions\n\n")
        for index, row in df.iterrows():
            f.write(f"- [{row['extension name']}]({row['url']})\n")
            