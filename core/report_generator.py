# report_generator.py
import os

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Security Scan Report</title>

    <!-- Marked.js -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

    <!-- Highlight.js -->
    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>

    <style>
        body {{
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f7f7f7;
        }}
        h1 {{
            text-align: center;
            margin-bottom: 30px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
        }}
        th, td {{
            border: 1px solid #ccc;
            padding: 12px;
            vertical-align: top;
        }}
        th {{
            background-color: #eee;
            text-transform: uppercase;
        }}
        pre {{
            background: #1e1e1e;
            color: #eee;
            padding: 12px;
            overflow-x: auto;
            border-radius: 6px;
        }}
    </style>
</head>

<body>

<h1>Security Analysis Report</h1>

<table>
    <tr>
        <th>Filename</th>
        <th>Language</th>
        <th>Vulnerability</th>
        <th>Exploit</th>
        <th>Mitigation</th>
    </tr>
    {rows}
</table>

<script>
document.querySelectorAll('.md-block').forEach(block => {{
    const raw = block.textContent;
    const html = marked.parse(raw);
    block.innerHTML = html;
}});

document.querySelectorAll('pre code').forEach((el) => {{
    hljs.highlightElement(el);
}});
</script>

</body>
</html>
"""


def generate_row(result):
    return f"""
    <tr>
        <td>{result['file']}</td>
        <td>{result['language']}</td>
        <td><div class="md-block">{result['analysis']['vulnerability']}</div></td>
        <td><div class="md-block">{result['analysis']['exploit']}</div></td>
        <td><div class="md-block">{result['analysis']['mitigation']}</div></td>
    </tr>
    """

def generate_report(results, output_file="report/security_report.html"):
    rows_html = "".join(generate_row(r) for r in results)
    final_html = HTML_TEMPLATE.format(rows=rows_html)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"[+] Syntax-highlighted HTML report generated: {output_file}")
