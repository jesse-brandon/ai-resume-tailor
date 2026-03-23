import pdfkit
from jinja2 import Environment, FileSystemLoader


def render_pdf(data):

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("resume.html")

    html = template.render(data)

    output_path = "resume.pdf"

    pdfkit.from_string(html, output_path)

    return output_path
