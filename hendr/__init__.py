import os
import datetime
import base64
import io
from PIL import Image


def render(template, body_renders, page_title=""):
    body = "\n".join([str(render) for render in body_renders])
    tmp = template.replace("<title>Title</title>", f"<title>{page_title}</title>")
    return tmp.replace("<body>", f"<body>{body}")


def save(html, path):
    with open(path, "w+", encoding="utf-8") as output:
        output.write(html)


def read_standard_template(name):
    d = os.path.dirname(__file__)
    td = os.path.join(d, "template")
    t = os.path.join(td, f"{name}.html")

    with open(t, "r", encoding="utf-8") as f:
        return f.read()


class TableRowRender:
    def __init__(self, column_renders, css_classes):
        self.css_classes = css_classes
        self.column_renders = column_renders

    def __str__(self):
        id = f"row-{AutoId.id()}"
        # <div class="{str(self.css_classes)}" id="{id}" onclick="toggleBorderWidth('{id}')">
        return f"""
        <div class="{str(self.css_classes)}" id="{id}")">
            {self.columns()}                
        </div>
        """

    def columns(self):
        return "\n".join([str(column_render) for column_render in self.column_renders])


class ColumnRender:
    def __init__(self, text, css_classes, css_style):
        self.text = text
        self.css_classes = css_classes
        self.css_style = css_style

    def __str__(self):
        if self.css_classes != "" or self.css_classes != None:
            return f"<span class=\"{self.css_classes}\", style=\"display:inline-block; vertical-align: middle; word-break: break-all; {self.css_style}\"> {str(self.text)} </span>"
        else:
            return f"<span style=\"display:inline-block; vertical-align: middle; word-break: break-all; {self.css_style}\"> {str(self.text)} </span>"


class SpacerRender:
    def __init__(self, height="50px"):
        self.height = height

    def __str__(self):
        return f"<div style=\"margin-top: {self.height};\"></div>"


class ToolTipRender:
    def __init__(self, text_render, tip_render, css_classes="", css_style=""):
        self.text_render = text_render
        self.tip_render = tip_render
        self.css_classes = css_classes
        self.css_style = css_style

    def __str__(self):
        id = f"tooltip-{datetime.datetime.now().timestamp()}-autoId{AutoId.id()}"
        return f"""
            <wow-tooltip class="tooltip">
                <div class="tooltip-label" aria-describedby="{id}" data-tooltip-placeholder>
                    {str(self.text_render)}
                </div>
                <div class="tooltip-dropdown" data-tooltip-dropdown>
                    <div role="tooltip" id="{id}" class="tooltip-dropdown-content {self.css_classes}" style="{self.css_style}">
                        {str(self.tip_render)}
                    </div>
                </div>
            </wow-tooltip>
        """


class TextBoxRender:
    def __init__(self, text, css_classes=""):
        self.text = text
        self.css_classes = css_classes

    def __str__(self):
        return f"<div class=\"box {self.css_classes}\">{self.text}</div>"


class AutoId:
    _id = 0

    @staticmethod
    def id():
        AutoId._id += 1
        return AutoId._id


class PanelContent:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class TopPanelContent:
    def __init__(self, major, minors):
        self.major = major
        self.minors = minors


class TopPanelRender:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f"""
        <div class="top-panel">
            {self.render_major()}
            {self.render_minors()}
        </div>
        """

    def render_major(self):
        left = "\n".join([str(render) for render in self.content.major.left])
        right = "\n".join([str(render) for render in self.content.major.right])

        return f"""
            <div class="major">
                <div style="float: left">{left}</div>
                <div style="float: right;padding-right: 7px">{right}</div>
            </div>
        """

    def render_minors(self):
        r = ""
        for minor in self.content.minors:
            left = "\n".join([str(render) for render in minor.left])
            right = "\n".join([str(render) for render in minor.right])
            r += f"""
            <div class="minor">
                <div style="float: left">{left}</div>
                <div style="float: right;padding-right: 7px">{right}</div>
            </div>
            """
        return r


class BottomPanelRender:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return f"""
        <div class="bottom-panel">
            {self.render_content()}
        </div>
        """

    def render_content(self):
        return "\n".join([str(render) for render in self.content])


class Container:
    def __init__(self, items, joiner=" "):
        self.items = items
        self.joiner = joiner

    def __str__(self):
        return f"{self.joiner}".join([str(item) for item in self.items])